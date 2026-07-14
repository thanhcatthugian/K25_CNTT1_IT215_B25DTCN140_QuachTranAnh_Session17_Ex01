from database import Base

from sqlalchemy import Column,String,Integer

from sqlalchemy.orm import relationship

class Truck(Base):
    __tablename__ = "trucks"

    id = Column(Integer,primary_key=True,autoincrement=True)
    license_plate = Column(String(50),nullable = False)
    association = relationship("Association",back_populates="trucks")