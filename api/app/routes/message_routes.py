from fastapi import APIRouter
from pydantic import BaseModel

from app.services.message_service import process_message
from app.services.conversation_state_service import conversation_state_service

router = APIRouter()


class Message(BaseModel):
    user_id: str
    message: str


@router.get("/")
def home():
    return {"message": "API funcionando"}


@router.post("/message")
def receive_message(data: Message):

    response = process_message(
        data.user_id,
        data.message
    )

    current_state = conversation_state_service.get(data.user_id)

    return {
        "response": response,
        "state": current_state
    }

@router.post("/conversation/{user_id}/reset")
def reset_conversation(user_id: str):
    conversation_state_service.clear(user_id)

    return {
        "message": "Conversation reset successfully"
    }