from sqlalchemy import Column, Integer, String, Boolean, func, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(15), nullable=False)
    surname = Column(String(15), nullable=False)
    email = Column(String(15), nullable=False)
    phone = Column(String(15), nullable=False)
    birthday = Column(DateTime, nullable=False)
    info = Column(String(150), nullable=True)
