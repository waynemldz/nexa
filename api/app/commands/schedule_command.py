import re

from app.commands.base_command import BaseCommand
from app.services.conversation_state_service import conversation_state_service


class ScheduleCommand(BaseCommand):

    def can_handle(self, user_id: str, message: str) -> bool:
        return conversation_state_service.get(user_id) == "schedule"

    def handle(self, user_id: str, message: str) -> str:

        if self.is_availability_question(message):
            return (
                "🕐 Nosso horário de atendimento é de segunda a sexta-feira, "
                "das 8h às 18h.\n\n"
                "Qual data e horário você prefere?"
            )

        schedule = self.normalize_schedule_request(message)

        conversation_state_service.clear(user_id)

        return (
            f"📅 Recebemos sua solicitação de agendamento para *{schedule}*.\n\n"
            "Nossa equipe entrará em contato em breve para confirmar a disponibilidade."
        )

    def normalize_schedule_request(self, message: str) -> str:

        text = message.strip()

        prefixes = [
            r"^podemos agendar\s+",
            r"^quero agendar\s+",
            r"^teria para\s+",
            r"^gostaria de agendar\s+",
            r"^agendar\s+",
            r"^teria como\s+",
            r"^tem como marcar\s+",
            r"^marcar para\s+",
            r"^marcar\s+",
            r"^pode ser\s+",
            r"^teria na\s+",
        ]

        for prefix in prefixes:
            text = re.sub(prefix, "", text, flags=re.IGNORECASE)

        text = re.sub(r"\s+para mim$", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s+por favor$", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s+pra mim$", "", text, flags=re.IGNORECASE)
        text = re.sub(r"\s+por gentileza$", "", text, flags=re.IGNORECASE)

        text = text.rstrip(".,?!")

        return text

    def is_availability_question(self, message: str) -> bool:
        normalized_message = message.lower().strip()

        availability_terms = {
            "horario",
            "horários",
            "horarios",
            "disponivel",
            "disponível",
            "disponibilidade",
        }

        return any(
            term in normalized_message
            for term in availability_terms
        )