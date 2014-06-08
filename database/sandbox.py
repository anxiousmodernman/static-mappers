from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mssql import BIT, DECIMAL, UNIQUEIDENTIFIER
from sqlalchemy.types import DateTime
from sqlalchemy.orm import relationship


# Define table with declarative base and create it
Base = declarative_base()


class ZoomPosFunc(Base):
    __tablename__ = 'jira_rep_1792_pos_func'
    recordid = Column(Integer)
    email = Column(String())
    match_status = Column(String())
    zoomid = Column(Integer())
    title = Column(String())
    position_function = Column(String())