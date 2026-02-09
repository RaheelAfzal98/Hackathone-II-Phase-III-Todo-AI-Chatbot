from typing import List, Optional
from sqlmodel import Session, select
from src.models.conversation import Conversation, ConversationCreate
from src.models.message import Message


class ConversationService:
    def create_conversation(self, conversation_data: ConversationCreate, db_session: Session) -> Conversation:
        """Create a new conversation."""
        conversation = Conversation(
            user_id=conversation_data.user_id,
            title=conversation_data.title
        )
        db_session.add(conversation)
        db_session.commit()
        db_session.refresh(conversation)
        return conversation

    def get_conversation_by_id(self, conversation_id: int, db_session: Session) -> Optional[Conversation]:
        """Retrieve a conversation by its ID."""
        return db_session.get(Conversation, conversation_id)

    def get_user_conversations(self, user_id: str, db_session: Session) -> List[Conversation]:
        """Retrieve all conversations for a specific user."""
        statement = select(Conversation).where(Conversation.user_id == user_id)
        results = db_session.exec(statement)
        return results.all()

    def update_conversation_title(self, conversation_id: int, title: str, db_session: Session) -> Optional[Conversation]:
        """Update the title of a conversation."""
        conversation = db_session.get(Conversation, conversation_id)
        if conversation:
            conversation.title = title
            conversation.updated_at = conversation.updated_at  # Use current time
            db_session.add(conversation)
            db_session.commit()
            db_session.refresh(conversation)
        return conversation

    def add_message_to_conversation(self, conversation_id: int, message: Message, db_session: Session) -> Optional[Message]:
        """Add a message to a conversation."""
        conversation = db_session.get(Conversation, conversation_id)
        if conversation:
            conversation.updated_at = conversation.updated_at  # Use current time
            db_session.add(message)
            db_session.commit()
            db_session.refresh(message)
            return message
        return None

    def get_conversation_messages(self, conversation_id: int, db_session: Session) -> List[Message]:
        """Retrieve all messages for a specific conversation."""
        conversation = db_session.get(Conversation, conversation_id)
        if conversation:
            return conversation.messages
        return []

    def delete_conversation(self, conversation_id: int, db_session: Session) -> bool:
        """Delete a conversation and its messages."""
        conversation = db_session.get(Conversation, conversation_id)
        if conversation:
            db_session.delete(conversation)
            db_session.commit()
            return True
        return False