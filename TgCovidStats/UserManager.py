from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import QueuePool
import logging

Base = declarative_base()


class User(Base):

    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    selected_region = Column(Integer, default=0)
    selected_province = Column(Integer, default=0)
    send_notifications = Column(Boolean, default=True)


class UserManager:
    def __init__(self, username: str, password: str, database: str):
        engine = create_engine("mysql+pymysql://{USER}:{PASS}@localhost/{DB}?host=localhost?port=3306".format(USER=username, PASS=password, DB=database),poolclass=QueuePool,)
        session_factory = sessionmaker(bind=engine)
        self.Session = scoped_session(session_factory)
        Base.metadata.create_all(engine)

    def get_all_users(self):
        users = []
        session = self.Session()
        try:
            users_query = session.query(User).all()
            for user in users_query:
                users.append(
                    {
                        "id": user.id,
                        "selected_region": user.selected_region,
                        "selected_province": user.selected_province,
                        "send_notifications": user.send_notifications,
                    }
                )
        except Exception as e:
            logging.error("An exception has occurred during query: {}".format(e))
            session.rollback()
            return None
        finally:
            session.close()
            self.Session.remove()
            return users

    def insert_user(self, user_id: int):
        if self.user_exists(user_id):
            return
        session = self.Session()
        try:
            logging.info("Adding user: %d", user_id)
            session.add(User(user_id=user_id))
        except Exception as e:
            logging.error(
                "An exception has occurred during user registration: {}".format(e)
            )
            session.rollback()
        finally:
            session.commit()
            session.close()
            self.Session.remove()

    def user_exists(self, user_id: int):
        return self.get_user(user_id) is not None

    def get_user(self, user_id: int):
        session = self.Session()
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
        except Exception as e:
            logging.error("An error has occurred during user query: {}".format(e))
            session.rollback()
            return None
        finally:
            session.close()
            self.Session.remove()
            return user

    def update_region(self, user_id: int, value: str):
        session = self.Session()
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            user.selected_region = value
        except Exception as e:
            logging.error("An error has occurred during region update: {}".format(e))
            session.rollback()
        finally:
            session.commit()
            session.close()
            self.Session.remove()

    def update_province(self, user_id: int, value: str):
        session = self.Session()
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            user.selected_province = value
        except Exception as e:
            logging.error("An error has occurred during province update: {}".format(e))
            session.rollback()
        finally:
            session.commit()
            session.close()
            self.Session.remove()

    def update_send_notifications(self, user_id: int, value: bool):
        session = self.Session()
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            user.send_notifications = value
        except Exception as e:
            logging.error(
                "An error has occurred during send_notification attribute update: {}".format(
                    e
                )
            )
            session.rollback()
        finally:
            session.commit()
            session.close()
            self.Session.remove()
