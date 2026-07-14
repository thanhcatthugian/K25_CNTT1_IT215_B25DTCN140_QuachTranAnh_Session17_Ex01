from database import Base

from sqlalchemy import Column, String,Integer,ForeignKey

from sqlalchemy.orm import relationship

class Waybill(Base):
    __tablename__ = "waybills"

    id = Column(Integer,primary_key=True,autoincrement=True)
    tracking_number = Column(String(50),nullable = False)
    shipping_status = Column(String(50),nullable = False)
    package = relationship("Package",back_populates="waybill",uselist=False)
    package_id = Column(Integer,ForeignKey("packages.id"),unique=True,nullable=False)
