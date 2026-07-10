import re
import unicodedata

from app.commands.base_command import BaseCommand
from app.services.conversation_state_service import conversation_state_service


def normalize_text(text: str) -> str:
    text = text.lower().strip()

    text = "".join(
        character
        for character in unicodedata.normalize("NFD", text)
        if unicodedata.category(character) != "Mn"
    )

    # Remove pontuações como ?, !, vírgulas etc.
    text = re.sub(r"[^\w\s]", "", text)

    # Remove espaços duplicados
    return " ".join(text.split())


class MenuCommand(BaseCommand):

    price_triggers = {
        "1",
        "preco",
        "precos",
        "valor",
        "valores",
        "planos",
        "quanto custa",
        "ver precos",
        "conhecer precos",
    }

    support_triggers = {
        "2",
        "suporte",
        "ajuda",
        "preciso de ajuda",
        "quero suporte",
        "falar com suporte",
        "estou com problema",
    }

    schedule_triggers = {
        "3",
        "agendar",
        "agendamento",
        "agendar conversa",
        "quero agendar",
        "marcar reuniao",
        "marcar conversa",
        "falar com especialista",
    }

    def can_handle(self, user_id: str, message: str) -> bool:
        normalized_message = normalize_text(message)

        return (
            normalized_message in self.price_triggers
            or normalized_message in self.support_triggers
            or normalized_message in self.schedule_triggers
        )

    def handle(self, user_id: str, message: str) -> str:
        normalized_message = normalize_text(message)

        if normalized_message in self.price_triggers:
            conversation_state_service.set(user_id, "menu")

            return (
                "💎 *Nossos planos*\n\n"
                "🥉 *Plano Básico* — R$ 49,90\n"
                "Ideal para pequenas empresas.\n\n"
                "🥈 *Plano Premium* — R$ 99,90\n"
                "Mais recursos e suporte prioritário.\n\n"
                "💎 *Plano Enterprise*\n"
                "Valor sob consulta.\n\n"
                "❓ Ficou com alguma dúvida sobre os planos ou serviços?\n"
                "Estou à disposição para ajudar."
            )

        if normalized_message in self.support_triggers:
            conversation_state_service.set(user_id, "support")

            return (
                "Certo! Descreva seu problema em uma única mensagem.\n\n"
                "Nossa equipe receberá sua solicitação."
            )

        conversation_state_service.set(user_id, "schedule")

        return (
            "Qual data e horário você deseja para o agendamento?\n\n"
            'Exemplo: "15/07 às 14h".'
        )