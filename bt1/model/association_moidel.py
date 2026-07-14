from database import Base

from sqlalchemy import Column,Integer,ForeignKey,PrimaryKeyConstraint

from sqlalchemy.orm import relationship

class Association(Base):
    __tablename__ = "package_truck"

    packages = relationship("Package",back_populates="association")
    trucks = relationship("Truck",back_populates="association")

    package_id = Column(Integer,ForeignKey("packages.id"))
    truck_id = Column(Integer,ForeignKey("trucks.id"))
    PrimaryKeyConstraint(package_id,truck_id)