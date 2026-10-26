from sqlalchemy import Column,Integer,Text
from database import Base

class PlannerTable(Base):
    __tablename__ = "cognizant_qa"
    id = Column(Integer,primary_key = True, index = True)
    question = Column(Text,nullable = False)
    answer = Column(Text,nullable=False)