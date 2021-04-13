from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user_table"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def __str__(self) -> str:
        return str({"user": self.username, "password": self.password})

    def to_json(self):
        return {"user": self.username, "password": self.password}

    def get_id(self) -> str:
        return str(self.username)

