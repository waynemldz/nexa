from app.commands.base_command import BaseCommand
from app.services.conversation_state_service import conversation_state_service
from app.services.ticket_service import ticket_service


class SupportCommand(BaseCommand):

    def can_handle(self, user_id: str, message: str) -> bool:
        return conversation_state_service.get(user_id) == "support"

    def handle(self, user_id: str, message: str) -> str:

        ticket = ticket_service.create(user_id)

        conversation_state_service.set(user_id, "human")

        return (
            "Sua solicitação foi registrada com sucesso! ✅\n\n"
            f"Protocolo: #{ticket.id}\n"
            "Nossa equipe responderá assim que possível.\n\n"
            "Você pode continuar enviando informações nesta conversa."
        )