from app.commands.base_command import BaseCommand
from app.services.conversation_state_service import conversation_state_service


class MenuCommand(BaseCommand):

    def can_handle(self, user_id: str, message: str) -> bool:

        state = conversation_state_service.get(user_id)

        return (
            state == "menu"
            and message.strip() in ["1", "2", "3"]
        )

    def handle(self, user_id: str, message: str) -> str:

        option = message.strip()

        if option == "1":

            conversation_state_service.set(user_id, "prices")

            return "Consultando tabela de preços..."

        if option == "2":

            conversation_state_service.set(user_id, "support")

            return "Descreva seu problema que nossa equipe irá ajudar."

        if option == "3":

            conversation_state_service.set(user_id, "schedule")

            return "Qual data você deseja agendar?"