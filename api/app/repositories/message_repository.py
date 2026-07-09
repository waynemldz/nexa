from database import SessionLocal
from app.models.message import Message

db = SessionLocal()


def save_message(user_id: str, role: str, content: str):

    print("5 - salvando mensagem")
    print("SALVANDO:", user_id, role, content)

    message = Message(
        user_id=user_id,
        role=role,
        content=content
    )

    db.add(message)

    db.commit()


def get_last_messages(user_id: str, limit: int = 10):

    return (
        db.query(Message)
        .filter(Message.user_id == user_id)
        .order_by(Message.id.desc())
        .limit(limit)
        .all()
    )