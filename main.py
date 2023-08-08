#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Index
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.schema import UniqueConstraint

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
        return f"<State(id={self.id}, name={self.name}, abbreviation={self.abbreviation}, population={self.population}, capital={self.capital}, area={self.area})>"


class County(Base):
    __tablename__ = "Counties"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    population = Column(Integer)
    area = Column(Float)

    state_id = Column(Integer, ForeignKey("States.id"))
    state = relationship("State", back_populates="counties")

    __table_args__ = (
        UniqueConstraint("name", "state_id", name="_county_state_uc"),
        Index("idx_name", "name"),  # New index on name column
    )

    # ORM relationships
    cities = relationship("City", back_populates="county")

    def __repr__(self):
        return f"<County(id={self.id}, name={self.name}, population={self.population}, area={self.area}, state_id={self.state_id})>"


class City(Base):
    __tablename__ = "Cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    population = Column(Integer)
    area = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)

    state_id = Column(Integer, ForeignKey("States.id"))
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
        return f"<City(id={self.id}, name={self.name}, population={self.population}, area={self.area}, latitude={self.latitude}, longitude={self.longitude}, state_id={self.state_id}, county_id={self.county_id})>"


if __name__ == "__main__":
    # Create an SQLite database and the tables
    engine = create_engine("sqlite:///geodata.db")
    Base.metadata.create_all(engine)
    # Base.metadata.drop_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Add all provided states using instances of the State class
    states_to_add = [
        State(
            name="Illinois",
            abbreviation="IL",
            population=572416,
            capital="Chicago",
            area=74810,
        ),
        State(
            name="Texas",
            abbreviation="TX",
            population=3856813,
            capital="Houston",
            area=261061,
        ),
        State(
            name="Alabama",
            abbreviation="AL",
            population=1400268,
            capital="Birmingham",
            area=62206,
        ),
        State(
            name="Indiana",
            abbreviation="IN",
            population=650597,
            capital="Crawfordsville",
            area=254996,
        ),
        State(
            name="Oklahoma",
            abbreviation="OK",
            population=1743791,
            capital="Tulsa",
            area=204646,
        ),
        State(
            name="Delaware",
            abbreviation="DE",
            population=2432814,
            capital="Newark",
            area=272971,
        ),
        State(
            name="Arizona",
            abbreviation="AZ",
            population=1481513,
            capital="Gilbert",
            area=219024,
        ),
        State(
            name="California",
            abbreviation="CA",
            population=1642739,
            capital="San Jose",
            area=193225,
        ),
        State(
            name="Tennessee",
            abbreviation="TN",
            population=2967424,
            capital="Nashville",
            area=199990,
        ),
        State(
            name="Florida",
            abbreviation="FL",
            population=4615458,
            capital="Lehigh Acres",
            area=78523,
        ),
        State(
            name="District of Columbia",
            abbreviation="DC",
            population=4920035,
            capital="Washington",
            area=248355,
        ),
        State(
            name="New Jersey",
            abbreviation="NJ",
            population=1421164,
            capital="Trenton",
            area=156607,
        ),
        State(
            name="Connecticut",
            abbreviation="CT",
            population=3461452,
            capital="Hartford",
            area=191523,
        ),
        State(
            name="Missouri",
            abbreviation="MO",
            population=3427132,
            capital="Independence",
            area=255529,
        ),
        State(
            name="Ohio",
            abbreviation="OH",
            population=4509421,
            capital="Cincinnati",
            area=83227,
        ),
        State(
            name="Nebraska",
            abbreviation="NE",
            population=2422350,
            capital="Omaha",
            area=96799,
        ),
        State(
            name="New York",
            abbreviation="NY",
            population=2399022,
            capital="Brooklyn",
            area=23004,
        ),
        State(
            name="Hawaii",
            abbreviation="HI",
            population=2741680,
            capital="Honolulu",
            area=108045,
        ),
        State(
            name="Minnesota",
            abbreviation="MN",
            population=2966503,
            capital="Minneapolis",
            area=60602,
        ),
        State(
            name="Massachusetts",
            abbreviation="MA",
            population=4936117,
            capital="Newton",
            area=60788,
        ),
        State(
            name="Pennsylvania",
            abbreviation="PA",
            population=506268,
            capital="Harrisburg",
            area=26013,
        ),
    ]

    session.add_all(states_to_add)
    session.commit()


# 3. ✅ Query all states.

#    all_states = session.query(State).all()
#    for state in all_states:
#        print(colored(state, 'blue'))
#    session.close()


# 4. ✅ Query all students by name.
# 5. ✅ Query all students by name, and order by name.
# 6. ✅ Query all students by name, order by name, descending.
# 7. ✅ Limit student query to 1 result
# 8. ✅ Use the SQLAlchemy func.count function to report how many student entries exist.
# 9. ✅ Filter student query results by name
# 10. ✅ Update the student data for a single column.
# 11. ✅ Delete a student database entry/row.
