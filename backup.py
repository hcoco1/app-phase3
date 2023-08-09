#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Index
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy.exc import SQLAlchemyError
from termcolor import colored
from prettytable.colortable import ColorTable, Themes, Theme

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

    state_id = Column(Integer, ForeignKey("States.id"))
    state = relationship("State", back_populates="counties")

    __table_args__ = (
        UniqueConstraint("name", "state_id", name="_county_state_uc"),
        Index("idx_name", "name"),  # New index on name column
    )

    # ORM relationships
    cities = relationship("City", back_populates="county")

    def __repr__(self):
        return colored(
            f"<County(id={self.id}, name={self.name}, population={self.population}, area={self.area}, state_id={self.state_id})>",
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
        return colored(
            f"<City(id={self.id}, name={self.name}, population={self.population}, area={self.area}, latitude={self.latitude}, longitude={self.longitude}, state_id={self.state_id}, county_id={self.county_id})>",
            "blue",
        )


if __name__ == "__main__":
    engine = create_engine("sqlite:///geodata.db")

    # Drop the tables
    Base.metadata.drop_all(engine)

    # Recreate the tables
    Base.metadata.create_all(engine)

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

# ADD a county
state = session.query(State).filter_by(name="Florida").first()

if state:
    try:
        # Create a new county and associate it with the state
        new_county = County(name="Orange", population=580000, area=1920, state=state)

        # Add the new county to the session
        session.add(new_county)

        # Commit the session to persist the change to the database
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(colored(f"Error adding county: {e}", "red"))
else:
    print(colored("State not found!", "red"))

    # ADD a city
state = session.query(State).filter_by(name="Florida").first()
county = session.query(County).filter_by(name="Orange").first()

if state and county:
    try:
        # Create a new city and associate it with the found state and county
        new_city = City(
            name="Orlando",
            population=300000,
            area=150,
            latitude=40.7128,
            longitude=-74.0060,
            state=state,
            county=county,
        )

        # Add the new city to the session
        session.add(new_city)

        # Commit the session to persist the change to the database
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        print(colored(f"Error adding city: {e}", "red"))
else:
    print(colored("State or County not found!", "red"))


# ALL STATES
all_states = session.query(State).all()
# Create a new table
table = ColorTable(theme=Themes.OCEAN)
table.align = "l"
# Set the headers for your table columns
table.field_names = ["ID", "Name", "Abbreviation", "Population", "Capital", "Area"]
# Add rows to the table
for state in all_states:
    # print(colored(state, "blue", "on_white"))
    table.add_row(
        [
            state.id,
            state.name,
            state.abbreviation,
            state.population,
            state.capital,
            state.area,
        ]
    )
print("-" * len("STATES Table"))
print("STATES Table")
print("-" * len("STATES Table"))
# Print the table
print(table)


# ALL COUNTIES
all_counties = session.query(County).all()

# Create a new theme instance based on the OCEAN theme and change only the font color
custom_font_color_theme = Theme(
    default_color="93",  # Yellow for font color
    vertical_color=Themes.OCEAN.vertical_color,
    horizontal_color=Themes.OCEAN.horizontal_color,
    junction_color=Themes.OCEAN.junction_color,
)

# Create a new table with the custom font color theme
table = ColorTable(theme=custom_font_color_theme)
table.align = "l"
# Set the headers for your table columns
table.field_names = ["ID", "Name", "Population", "Area", "State_ID"]
# Add rows to the table
for county in all_counties:
    table.add_row(
        [county.id, county.name, county.population, county.area, county.state_id]
    )
# Print the title
print("-" * len("COUNTIES Table"))
print("COUNTIES Table")
print("-" * len("COUNTIES Table"))
# Print the table
print(table)


# ALL CITIES
all_cities = session.query(City).all()
# Create a new theme instance based on the OCEAN theme and change only the font color
custom_font_color_theme = Theme(
    default_color="50",  # Yellow for font color
    vertical_color=Themes.OCEAN.vertical_color,
    horizontal_color=Themes.OCEAN.horizontal_color,
    junction_color=Themes.OCEAN.junction_color,
)
# Create a new table with the custom font color theme
table = ColorTable(theme=custom_font_color_theme)
table.align = "l"
# Set the headers for your table columns
table.field_names = [
    "ID",
    "Name",
    "Population",
    "Area",
    "Latitude",
    "Longitude",
    "State_ID",
    "County_ID",
]
# Add rows to the table

for city in all_cities:
    # print(colored(city, "yellow", "on_magenta"))
    table.add_row(
        [
            city.id,
            city.name,
            city.population,
            city.area,
            city.longitude,
            city.longitude,
            city.state_id,
            city.county_id,
        ]
    )
    # Print the title
print("-" * len("CITY Table"))
print("CITY Table")
print("-" * len("CITY Table"))
# Print the table
print(table)


session.close()

