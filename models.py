from sqlalchemy import Column, Integer, String, Float, ForeignKey, Index
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class State(Base):
    __tablename__ = "States"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    abbreviation = Column(String(255))
    population = Column(Integer)
    capital = Column(String(255))
    area = Column(Float)

    counties = relationship("County", back_populates="state", cascade="all, delete-orphan")
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

class County(Base):
    __tablename__ = "Counties"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    population = Column(Integer)
    area = Column(Float)
    state_name = Column(String(255))
    state_id = Column(Integer, ForeignKey("States.id"))

    state = relationship("State", back_populates="counties")
    cities = relationship("City", back_populates="county", cascade="all, delete-orphan")

class City(Base):
    __tablename__ = "Cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    population = Column(Integer)
    area = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    state_name = Column(String(255))
    state_id = Column(Integer, ForeignKey("States.id"))
    county_name = Column(String(255))
    county_id = Column(Integer, ForeignKey("Counties.id"))

    county = relationship("County", back_populates="cities")
