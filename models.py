from sqlalchemy import Column, Integer, String, Float, ForeignKey, Index
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.schema import UniqueConstraint
from termcolor import colored

Base = declarative_base()


class State(Base):
    __tablename__ = "States"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    abbreviation = Column(String(255))
    population = Column(Integer)
    capital = Column(String(255))
    area = Column(Float)

    __table_args__ = (
        UniqueConstraint("name", name="_state_name_uc"),
        UniqueConstraint("abbreviation", name="_state_abbreviation_uc"),
        Index("idx_abbreviation", "abbreviation"),  # New index on abbreviation column
    )

    # ORM relationships
    counties = relationship("County", back_populates="state")
    cities = relationship("City", backref="state")

    def __repr__(self):
        return colored(
            f"<State(id={self.id}, name={self.name}, abbreviation={self.abbreviation}, population={self.population}, capital={self.capital}, area={self.area})>",
            "blue",
        )


class County(Base):
    __tablename__ = "Counties"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    population = Column(Integer)
    area = Column(Float)
    state_name = Column(String(255))
    state_id = Column(Integer, ForeignKey("States.id"))
    city_name = Column(String(255))
    state = relationship("State", back_populates="counties")

    __table_args__ = (
        UniqueConstraint("name", "state_id", name="_county_state_uc"),
        Index("idx_name", "name"),  # New index on name column
    )

    # ORM relationships
    cities = relationship("City", back_populates="county")

    def __repr__(self):
        return colored(
            f"<County(id={self.id}, name={self.name}, population={self.population}, area={self.area}, state_name={self.state_name} state_id={self.state_id} city_name={self.city_name})>",
            "blue",
        )


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
    county_id = Column(
        Integer, ForeignKey("Counties.id")
    )  # Foreign key to Counties table

    __table_args__ = (
        UniqueConstraint("name", "county_id", "state_id", name="_city_county_state_uc"),
        Index("idx_city_name", "name"),  # New index on name column
    )

    # ORM relationships
    county = relationship("County", back_populates="cities")

    def __repr__(self):
        return colored(
            f"<City(id={self.id}, name={self.name}, population={self.population}, area={self.area}, latitude={self.latitude}, longitude={self.longitude}, state_name={self.state_name} state_id={self.state_id}, county_name={self.county_name} county_id={self.county_id})>",
            "blue",
        )