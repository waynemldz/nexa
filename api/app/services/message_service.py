from app.commands.command_dispatcher import CommandDispatcher
from app.services.ai_service import ask_ai

dispatcher = CommandDispatcher()


def process_message(user_id: str, message: str):

    print("1 - process_message")

    response = dispatcher.dispatch(user_id, message)

    print("2 - dispatcher:", response)

    if response:
        return response

    print("3 - chamando IA")

    return ask_ai(user_id, message)