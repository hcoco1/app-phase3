from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

association_table = Table(
    "CityFacilityAssociation",
    Base.metadata,
    Column("city_id", Integer, ForeignKey("Cities.id")),
    Column("facility_id", Integer, ForeignKey("Facilities.id"))
)

class State(Base):
    __tablename__ = "States"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    abbreviation = Column(String(255))
    population = Column(Integer)
    capital = Column(String(255))
    area = Column(Float)
    # ForeignKeys
   

class County(Base):
    __tablename__ = "Counties"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    population = Column(Integer)
    area = Column(Float)
    # ForeignKeys


class City(Base):
    __tablename__ = "Cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    population = Column(Integer)
    area = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    county_name = Column(String(255))

    # ORM relationship
    facilities = relationship("Facilities", secondary=association_table, back_populates="cities")

class Facilities(Base):
    __tablename__ = "Facilities"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    facility_type = Column(String(255))
    
    # ORM relationship
    cities = relationship("City", secondary=association_table, back_populates="facilities")

