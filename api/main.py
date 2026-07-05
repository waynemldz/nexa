from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal, Usuario

app = FastAPI()
db = SessionLocal()
user_states = {}
user_names = {}

class Message(BaseModel):
    user_id: str
    message:str

@app.get("/")
def home():
    return {"message":"API funcionando"}

@app.post("/message")
def receive_message(data: Message):

    user_id = data.user_id
    print("Usuário:", user_id)

    user_message = data.message.lower().strip()

    if user_message.startswith("meu nome é"):

        nome = data.message[11:].strip()

        usuario = db.get(Usuario, user_id)

        if usuario is None:

            usuario = Usuario(
                user_id=user_id,
                nome=nome
            )

            db.add(usuario)

        else:

            usuario.nome = nome

        db.commit()

        return {
            "response": f"Prazer, {nome}! Vou me lembrar do seu nome."
        }

    current_state = user_states.get(user_id)

    if user_message in [
        "oi",
        "olá",
        "ola",
        "bom dia",
        "boa tarde",
        "opa"
    ]:

        user_states[user_id] = "menu"

        return {
            "response": (
                "Olá! Seja bem-vindo à Assistente Virtual de Whatsapp do Wayne (em fase de desenvolvimento).\n"
                "Digite:\n"
                "1 - Ver preços\n"
                "2 - Suporte\n"
                "3 - Agendamento"
            )
        }

    if current_state == "menu":

        if user_message == "1":

            user_states[user_id] = "precos"

            return {
                "response": "Nosso plano básico custa R$99 por mês."
            }

        elif user_message == "2":

            user_states[user_id] = "suporte"

            return {
                "response": "Descreva seu problema em uma única mensagem."
            }

        elif user_message == "3":

            user_states[user_id] = "agendamento"

            return {
                "response": "Qual horário você deseja?"
            }

    if current_state == "suporte":
        user_states[user_id] = "usuario_teste"
        return {
            "response": (
                f"Entendi seu problema: {data.message}. "
                "Nossa equipe responderá em breve."
            )
        }
    
    if user_message == "qual é meu nome?":

        usuario = db.get(Usuario, user_id)

        if usuario:

            return {
                "response": f"Seu nome é {usuario.nome}."
            }
        
        return {
            "response": "Você ainda não me disse seu nome."
        }

    return {
        "response": "Digite 'oi' para iniciar."
    }