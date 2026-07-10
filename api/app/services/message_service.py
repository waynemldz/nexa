from app.commands.command_dispatcher import CommandDispatcher
from app.services.ai_service import ask_ai


dispatcher = CommandDispatcher()


def process_message(user_id: str, message: str):

    response = dispatcher.dispatch(user_id, message)


    if response:
        return response

    from app.services.conversation_state_service import conversation_state_service
    if conversation_state_service.get(user_id) == "human":
     return (
        "Você já está aguardando atendimento humano.\n"
        "Em instantes um atendente responderá sua mensagem."
    )
    
    return ask_ai(user_id, message)