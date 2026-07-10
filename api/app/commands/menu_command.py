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
                "💰 Tabela de preços\n\n"
                "• Plano Básico - R$ 49,90\n"
                "• Plano Premium - R$ 99,90\n"
                "• Plano Enterprise - Sob consulta\n\n"
                "Você também pode fazer perguntas sobre nossos serviços.\n"
                'Digite "menu" para voltar ao menu principal.'
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