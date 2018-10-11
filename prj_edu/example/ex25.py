import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
#session 을 관리하기 위한 클래스와 세션 생성 클래스를 불러온다.
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# app_teardown_appcontext
# def shutdown_session(exception=None):
#    db_session.remove()

#데이터베이스 초기화 함수
def __init_db():
    Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True )

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email


    def __repr__(self):
        return "<User %r>" % (self.name)