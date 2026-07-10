from fastapi import APIRouter
from app.services.conversation_state_service import conversation_state_service

from app.repositories.ticket_repository import (
    get_open_ticket,
    close_ticket
)

router = APIRouter(prefix="/admin")


@router.get("/tickets/{user_id}")
def get_ticket(user_id: str):

    ticket = get_open_ticket(user_id)

    if ticket is None:
        return {
            "message": "Nenhum ticket aberto."
        }

    return {
        "id": ticket.id,
        "user_id": ticket.user_id,
        "status": ticket.status
    }


@router.post("/tickets/{user_id}/close")
def finish_ticket(user_id: str):

    ticket = close_ticket(user_id)

    if ticket is None:
        return {
            "message": "Nenhum ticket encontrado."
        }

    return {
        "message": "Ticket encerrado."
    }

@router.post("/reset/{user_id}")
def reset_conversation(user_id: str):

    conversation_state_service.clear(user_id)

    return {
        "message": "Conversa reiniciada."
    }