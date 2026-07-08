from app.commands.base_command import BaseCommand
from app.services.conversation_state_service import conversation_state_service


class PriceCommand(BaseCommand):

    def can_handle(self, user_id: str, message: str) -> bool:
        return conversation_state_service.get(user_id) == "prices"

    def handle(self, user_id: str, message: str) -> str:

        conversation_state_service.clear(user_id)

        return (
            "💰 Tabela de preços\n\n"
            "• Plano Básico - R$ 49,90\n"
            "• Plano Premium - R$ 99,90\n"
            "• Plano Enterprise - Sob consulta"
        )