from database import SessionLocal, Usuario

db = SessionLocal()

def get_user_by_id(user_id):
    return db.get(Usuario, user_id)

def save_user(user_id, nome):
    usuario = get_user_by_id(user_id)

    if usuario is None:

        usuario = Usuario(
            user_id=user_id,
            nome=nome
        )
        db.add(usuario)

    else:
        usuario.nome = nome

    db.commit()

    return usuario