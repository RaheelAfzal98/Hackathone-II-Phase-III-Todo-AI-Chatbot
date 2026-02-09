from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import Optional
from src.database.session import get_session
from src.services.conversation_service import ConversationService
from src.services.ai_agent_service import AIAgentService
from src.models.message import Message, MessageCreate
from src.models.conversation import ConversationCreate
from src.auth.dependencies import get_current_user_id
from pydantic import BaseModel
import os


router = APIRouter(tags=["chat"])

# Request/Response models
class ChatRequest(BaseModel):
    message: str
    conversation_id: Optional[int] = None


class ChatResponse(BaseModel):
    conversation_id: int
    response: str
    tool_calls: list = []
    tool_responses: list = []


@router.post("/{user_id}/chat", response_model=ChatResponse)
async def chat_endpoint(
    user_id: str,
    request: ChatRequest,
    db_session: Session = Depends(get_session),
    current_user_id: str = Depends(get_current_user_id)
):
    """
    Process a chat message and return AI response.

    Args:
        user_id: The authenticated user's ID (must match current_user)
        request: Contains the user's message and optional conversation_id

    Returns:
        ChatResponse with conversation_id, AI response, and any tool calls
    """
    # Verify that the user_id in the path matches the authenticated user
    if current_user_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden: User ID mismatch")

    # Initialize services
    conversation_service = ConversationService()
    ai_agent_service = AIAgentService(openrouter_api_key=os.getenv("OPEN_ROUTER_API_KEY"))
    ai_agent_service.initialize_agent_with_tools()  # Initialize with MCP tools

    # Get or create conversation
    conversation = None
    if request.conversation_id:
        conversation = conversation_service.get_conversation_by_id(request.conversation_id, db_session)
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
        if conversation.user_id != user_id:
            raise HTTPException(status_code=403, detail="Access denied: Conversation does not belong to user")
    else:
        # Create new conversation
        conversation_data = ConversationCreate(user_id=user_id)
        conversation = conversation_service.create_conversation(conversation_data, db_session)

    # Create and save user message
    user_message = Message(
        conversation_id=conversation.id,
        sender='user',
        content=request.message,
        tool_calls=None,  # Explicitly set to None for user messages
        tool_responses=None  # Explicitly set to None for user messages
    )
    db_session.add(user_message)
    db_session.commit()

    # Process the message with the AI agent
    result = await ai_agent_service.process_natural_language_request(
        user_input=request.message,
        user_id=user_id,
        conversation_id=conversation.id
    )

    # Create and save AI response message
    ai_message = Message(
        conversation_id=conversation.id,
        sender='assistant',
        content=result["response"],
        tool_calls=result.get("tool_calls") if result.get("tool_calls") else None,
        tool_responses=result.get("tool_responses") if result.get("tool_responses") else None
    )
    db_session.add(ai_message)
    db_session.commit()

    return ChatResponse(
        conversation_id=conversation.id,
        response=result["response"],
        tool_calls=result.get("tool_calls", []),
        tool_responses=result.get("tool_responses", [])
    )


# Endpoint to get conversation history
@router.get("/{user_id}/conversations/{conversation_id}")
def get_conversation(
    user_id: str,
    conversation_id: int,
    db_session: Session = Depends(get_session),
    current_user_id: str = Depends(get_current_user_id)
):
    """
    Retrieve a specific conversation with its messages.
    """
    # Verify user authentication
    if current_user_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden: User ID mismatch")

    conversation_service = ConversationService()
    conversation = conversation_service.get_conversation_by_id(conversation_id, db_session)

    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")

    if conversation.user_id != user_id:
        raise HTTPException(status_code=403, detail="Access denied: Conversation does not belong to user")

    return conversation