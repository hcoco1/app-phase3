from sqlalchemy import Column, Integer, String, Float, ForeignKey, Index
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class State(Base):
    __tablename__ = "States"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    abbreviation = Column(String(255))
    population = Column(Integer)
    capital = Column(String(255))
    area = Column(Float)
    area_in_Km = Column(Float)

    counties = relationship("County", back_populates="state", cascade="all, delete-orphan")
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<State(id={self.id}, name={self.name}, abbreviation={self.abbreviation}, population={self.population}, capital={self.capital}, area={self.area} area_in_Km={self.area_in_Km})>"

class County(Base):
    __tablename__ = "Counties"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    population = Column(Integer)
    area = Column(Float)
    state_name = Column(String(255))
    state_id = Column(Integer, ForeignKey("States.id"))

    state = relationship("State", back_populates="counties")
    cities = relationship("City", back_populates="county", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<County(id={self.id}, name={self.name}, population={self.population}, area={self.area}, state_name={self.state_name})>"

class City(Base):
    __tablename__ = "Cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True)
    population = Column(Integer)
    area = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)
    state_name = Column(String(255))
    state_id = Column(Integer, ForeignKey("States.id"))
    county_name = Column(String(255))
    county_id = Column(Integer, ForeignKey("Counties.id"))
    county = relationship("County", back_populates="cities")

    def __repr__(self):
        return f"<City(id={self.id}, name={self.name}, population={self.population}, area={self.area}, latitude={self.latitude}, longitude={self.longitude}, state_name={self.state_name}, county_name={self.county_name})>"

