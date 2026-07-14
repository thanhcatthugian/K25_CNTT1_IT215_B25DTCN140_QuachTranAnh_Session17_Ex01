from database import Base
from sqlalchemy import Column,String,Integer,Float,ForeignKey
from sqlalchemy.orm import relationship
class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer,primary_key=True,autoincrement=True)
    package_code = Column(String(50),nullable=False,unique=True)
    weight = Column(Float,nullable=False)
    warehouse_id = Column(Integer,ForeignKey("warehouses.id"))
    warehouse = relationship("Warehouse",back_populates="packages")
    waybill = relationship("Waybill",back_populates="package")
    association = relationship("Association",back_populates="packages")