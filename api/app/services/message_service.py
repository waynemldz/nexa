from app.commands.command_dispatcher import CommandDispatcher

dispatcher = CommandDispatcher()


def process_message(user_id: str, message: str):

    response = dispatcher.dispatch(user_id, message)

    if response:
        return response

    return (
        "Desculpe, não entendi sua mensagem.\n\n"
        "Digite 'oi' para iniciar o atendimento."
    )