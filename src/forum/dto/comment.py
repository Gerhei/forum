from dataclasses import dataclass
from datetime import datetime

from src.forum.models import Comment


@dataclass
class CommentDto:
    text: str
    created_at: datetime
    updated_at: datetime
    user: str

    @classmethod
    def create(cls, comment: Comment) -> 'CommentDto':
        return CommentDto(text=comment.text,
                          created_at=comment.created_at,
                          updated_at=comment.updated_at,
                          user=comment.user.username)
