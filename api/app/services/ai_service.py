from google import genai

from app.config.settings import settings
from app.repositories.message_repository import (
    save_message,
    get_last_messages
)
from app.services.knowledge_service import get_company_context


client = genai.Client(api_key=settings.GEMINI_API_KEY)


def ask_ai(user_id: str, user_message: str) -> str:

    history = reversed(get_last_messages(user_id))

    company_context = get_company_context()

    prompt = f"""
    Você é Wayne Assistant.

    Você trabalha para a empresa abaixo.

    Informações da empresa:

    {company_context}

    Nunca invente informações.

    Caso algo não esteja descrito acima, diga que um atendente responderá em breve.

    Sempre responda em português do Brasil.
    """

    contents = [prompt]

    for message in history:
        contents.append(
        f"{message.role}: {message.content}"
    )

    contents.append(f"Usuário: {user_message}")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="\n".join(contents)
    )

    answer = response.text

    save_message(
        user_id,
        "Usuário",
        user_message
)

    save_message(
        user_id,
        "Assistente",
        answer
)

    return answer

    prompt = f"""
    Extraia somente a data e o horário da mensagem abaixo.

    Mensagem:
    {message}

    Regras:
    - Remova expressões como "podemos agendar", "quero marcar" e "teria horário".
    - Preserve apenas a data e o horário informados.
    - Não adicione explicações.
    - Não invente informações.
    - Responda em português do Brasil.

    Exemplo:
    Entrada: Podemos agendar sexta-feira às 8?
    Saída: sexta-feira às 8h
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()