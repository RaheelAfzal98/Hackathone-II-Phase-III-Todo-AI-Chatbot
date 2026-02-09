from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from src.models.message import Message


class ConversationBase(SQLModel):
    user_id: str = Field(index=True)
    title: Optional[str] = Field(default=None)


class Conversation(ConversationBase, table=True):
    """
    Represents a single conversation thread between user and AI assistant.
    """
    id: int = Field(primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationships
    messages: list["Message"] = Relationship(back_populates="conversation")


class ConversationCreate(ConversationBase):
    pass


class ConversationRead(ConversationBase):
    id: int
    created_at: datetime
    updated_at: datetime
    messages: list["MessageRead"] = []


# Forward declaration for type checking
if TYPE_CHECKING:
    from src.models.message import MessageRead