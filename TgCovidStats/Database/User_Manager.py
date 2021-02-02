from sqlalchemy import create_engine,Column,Integer,String,Boolean
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import QueuePool
import logging

Base = declarative_base()

class User(Base):

    __tablename__ = "user"

    user_id = Column(Integer,primary_key=True)
    selected_region = Column(String(50),default="")
    selected_province = Column(String(50),default="")
    send_notification = Column(Boolean,default=True)

class UserManager:

    def __init__(self,username: str,password: str):
        engine = create_engine("mysql+pymysql://{USER}:{PASS}@localhost/db?host=localhost?port=3306".format(USER=username,PASS=password), poolclass=QueuePool)
        session_factory = sessionmaker(bind=engine)
        self.Session = scoped_session(session_factory)
        Base.metadata.create_all(engine)

    def insert_user(self,user_id: int):
        if self.user_exists(user_id):
            return
        session = self.Session()
        logging.info("Adding user: %d",user_id)
        session.add(User(user_id=user_id))
        session.commit()
        session.close()
    
    def user_exists(self,user_id: int):
        return self.get_user(user_id) is not None

    def get_user(self,user_id: int):
        session = self.Session()
        user = session.query(User).filter(User.user_id==user_id).first()
        session.close()
        return user
    
    def update_region(self,user_id: int,value: str):
        session = self.Session()
        user = session.query(User).filter(User.user_id==user_id).first()
        user.selected_region = value
        session.commit()
        session.close()

    def update_province(self,user_id: int,value: str):
        session = self.Session()
        user = session.query(User).filter(User.user_id==user_id).first()
        user.selected_province = value
        session.commit()
        session.close()
    



