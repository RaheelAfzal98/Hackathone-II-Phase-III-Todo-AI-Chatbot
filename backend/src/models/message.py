from sqlmodel import SQLModel, Field, Relationship
from pydantic import field_validator
import re
from datetime import datetime
from typing import TYPE_CHECKING, Optional
from sqlalchemy import JSON

if TYPE_CHECKING:
    from src.models.conversation import Conversation


class MessageBase(SQLModel):
    conversation_id: int = Field(foreign_key="conversation.id", index=True)
    sender: str = Field()  # Enum: 'user', 'assistant', 'system'
    content: str = Field(min_length=1)
    tool_calls: Optional[dict] = Field(default=None, sa_type=JSON)
    tool_responses: Optional[dict] = Field(default=None, sa_type=JSON)


class Message(MessageBase, table=True):
    """
    Represents individual messages within a conversation.
    """
    id: int = Field(primary_key=True)
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    # Relationships
    conversation: "Conversation" = Relationship(back_populates="messages")


class MessageCreate(MessageBase):
    pass


class MessageRead(MessageBase):
    id: int
    timestamp: datetime
    conversation: Optional["ConversationRead"] = None


    @field_validator('sender')
    @classmethod
    def validate_sender(cls, v):
        if not re.match(r'^(user|assistant|system)$', v):
            raise ValueError('sender must be one of: user, assistant, system')
        return v

# Forward declaration for type checking
if TYPE_CHECKING:
    from src.models.conversation import ConversationRead