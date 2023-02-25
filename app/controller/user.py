from database.database import Session
from models.user import User

class UserOrm:

    @staticmethod
    def get_all():
        with Session() as session:
            query = session.query(User).all()
            if query:
                return query
            else:
                return 'Não existe nenhum usuário!'
        
    def get(id: int):
        with Session() as session:
            query = session.query(User).filter(User.id == id).first()
            if query:
                return query
            else:
                return 'Não existe nenhum usuário com esse ID!'
    
    def create(name: str, password: str):
        with Session() as session:
            session.expire_on_commit = False
            user = User(nick_name=name, password=password)
            session.add(user)
            session.commit()
            return user
        
    def delete(id: int):
        user = UserOrm.get(id=id)
        if user:
            with Session() as session:
                session.delete(user)
                session.commit()
            return f'Usuário {user} foi deletado!'
        else:
            return 'Não existe nenhum usuário com esse nome!'