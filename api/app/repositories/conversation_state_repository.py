from database import SessionLocal
from app.models.conversation_state import ConversationState
from datetime import datetime, timedelta

db = SessionLocal()


def get_state(user_id):

    conversation = db.get(ConversationState, user_id)

    if conversation:
        return conversation.state

    return None


def set_state(user_id, state):

    conversation = db.get(ConversationState, user_id)

    if conversation is None:

        conversation = ConversationState(
            user_id=user_id,
            state=state
        )

        db.add(conversation)

    else:

        conversation.state = state

    db.commit()


def clear_state(user_id):

    conversation = db.get(ConversationState, user_id)

    if conversation:

        conversation.state = None
        db.commit()

def is_inactive(user_id: str, hours: int = 2) -> bool:

    conversation = db.get(ConversationState, user_id)

    if conversation is None or conversation.updated_at is None:
        return False

    inactivity_limit = datetime.utcnow() - timedelta(hours=hours)

    return conversation.updated_at < inactivity_limit