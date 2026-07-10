from app.commands.command_dispatcher import CommandDispatcher
from app.services.ai_service import ask_ai
from app.services.conversation_state_service import conversation_state_service

dispatcher = CommandDispatcher()


def get_main_menu() -> str:
    return (
        "Olá! Eu sou a Nexa, assistente virtual da Wayne Tech.\n\n"
        "Como posso ajudar?\n"
        "1 - Conhecer serviços e preços\n"
        "2 - Solicitar suporte\n"
        "3 - Agendar uma conversa\n\n"
        'Digite "menu" para voltar ao início.'
    )


def process_message(user_id: str, message: str):

    current_state = conversation_state_service.get(user_id)
    normalized_message = message.lower().strip()

    if current_state == "human":

        if conversation_state_service.is_inactive(user_id, hours=2):
            conversation_state_service.clear(user_id)
            conversation_state_service.set(user_id, "menu")

            return get_main_menu()

        return (
            "Sua solicitação continua em atendimento. ✅\n"
            "Nossa equipe responderá assim que possível."
        )
    
    acknowledgement_messages = {
        "ok",
        "okay",
        "ta bom",
        "tá bom",
        "tudo bem",
        "beleza",
        "entendi",
        "certo",
        "blz",
        "valeu",
        "obrigado",
        "obrigada",
    }

    negative_responses = {
        "nao",
        "não",
        "nao obrigado",
        "não obrigado",
        "nao obrigada",
        "não obrigada",
        "so isso",
        "só isso",
        "somente isso",
        "por enquanto nao",
        "por enquanto não",
    }

    if current_state == "awaiting_more":

        if (
            normalized_message in negative_responses
            or normalized_message in acknowledgement_messages
        ):
            conversation_state_service.clear(user_id)

            return (
                "Tudo certo! 😊\n\n"
                "Conversa encerrada. Quando precisar, é só enviar uma nova mensagem."
            )

    conversation_state_service.set(user_id, "menu")

    if normalized_message in {
        "oi",
        "ola",
        "olá",
        "menu",
        "voltar",
        "voltar ao menu",
        "menu principal",
    }:
        conversation_state_service.set(user_id, "menu")
        return get_main_menu()

    

    if normalized_message in acknowledgement_messages:
        conversation_state_service.set(user_id, "awaiting_more")

        return (
            "Perfeito! 😊\n\n"
            "Posso ajudar em algo mais?"
        )

    if current_state is None:
        conversation_state_service.set(user_id, "menu")
        return get_main_menu()

    response = dispatcher.dispatch(user_id, message)

    if response:
        return response

    return ask_ai(user_id, message)