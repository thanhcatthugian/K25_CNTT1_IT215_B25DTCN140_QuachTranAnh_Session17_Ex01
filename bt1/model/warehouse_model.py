from database import Base

from sqlalchemy import Column,Integer,String,ForeignKey

from sqlalchemy.orm import relationship

class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer,primary_key=True,autoincrement=True)
    warehouse_name  = Column(String(50),nullable=False)
    location = Column(String(50),nullable=False)
    packages = relationship("Package",back_populates="warehouse")
