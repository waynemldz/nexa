from google import genai

from app.config.settings import settings
from app.repositories.message_repository import (
    save_message,
    get_last_messages
)
from app.services.knowledge_service import get_company_context


client = genai.Client(api_key=settings.GEMINI_API_KEY)


def ask_ai(user_id: str, user_message: str) -> str:

    print("4 - entrou na IA")
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