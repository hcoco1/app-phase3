from sqlalchemy import create_engine, update
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from termcolor import colored
from models import State, County, City
import random
from sqlalchemy.orm.exc import NoResultFound
from geopy.geocoders import Nominatim
import time


Base = declarative_base()
engine = create_engine("sqlite:///geodata.db")

# Drop the tables
Base.metadata.drop_all(engine)

# Recreate the tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()



# Add all provided states using instances of the State class
def add_states(session):
    add_states = [
        State(
            name="Alabama",
            abbreviation="AL",
            population=4903185,
            capital="Montgomery",
            area=52420,
        ),
        State(
            name="Alaska",
            abbreviation="AK",
            population=731545,
            capital="Juneau",
            area=665384,
        ),
        State(
            name="Arizona",
            abbreviation="AZ",
            population=7278717,
            capital="Phoenix",
            area=113990,
        ),
        State(
            name="Arkansas",
            abbreviation="AR",
            population=3017804,
            capital="Little Rock",
            area=53179,
        ),
        State(
            name="California",
            abbreviation="CA",
            population=39538223,
            capital="Sacramento",
            area=163695,
        ),
        State(
            name="Colorado",
            abbreviation="CO",
            population=5773714,
            capital="Denver",
            area=104094,
        ),
        State(
            name="Connecticut",
            abbreviation="CT",
            population=3565287,
            capital="Hartford",
            area=5543,
        ),
        State(
            name="Delaware",
            abbreviation="DE",
            population=989948,
            capital="Dover",
            area=2489,
        ),
        State(
            name="Florida",
            abbreviation="FL",
            population=21538187,
            capital="Tallahassee",
            area=65758,
        ),
        State(
            name="Georgia",
            abbreviation="GA",
            population=10617423,
            capital="Atlanta",
            area=59425,
        ),
        State(
            name="New York",
            abbreviation="NY",
            population=10617423,
            capital="New York",
            area=59425,
        ),
    ]

    session.add_all(add_states)
    session.commit()

counties_to_add = [
    {
        "name": "Orange",
        "population": 1393452,  # As of 2019
        "area": 903,  # Square miles
        "state_name": "Florida",
        "city_name": "Orlando",
    },
    {
        "name": "Seminole",
        "population": 471826,  # As of 2019
        "area": 309,  # Square miles
        "state_name": "Florida",
        "city_name": "Orlando",
    },
    {
        "name": "Lake County",
        "population": 367118,  # As of 2019
        "area": 953,  # Square miles
        "state_name": "Florida",
        "city_name": "Orlando",
    },
    {
        "name": "Osceola",
        "population": 375751,  # As of 2019
        "area": 1325,  # Square miles
        "state_name": "Florida",
        "city_name": "Orlando",
    },
    {
        "name": "Miami Dade",
        "population": 2716940,  # As of 2019
        "area": 1898,  # Square miles
        "state_name": "Florida",
        "city_name": "Miami",
    },
    {
        "name": "Broward",
        "population": 1952778,  # As of 2019
        "area": 1209,  # Square miles
        "state_name": "Florida",
        "city_name": "Fort Lauderdale",
    },
    {
        "name": "Palm Beach",
        "population": 1496770,  # As of 2019
        "area": 1969,  # Square miles
        "state_name": "Florida",
        "city_name": "West Palm Beach",
    },
    {
        "name": "Hillsborough",
        "population": 1471968,  # As of 2019
        "area": 1020,  # Square miles
        "state_name": "Florida",
        "city_name": "Tampa",
    },
    {
        "name": "Pinellas",
        "population": 974996,  # As of 2019
        "area": 274,  # Square miles
        "state_name": "Florida",
        "city_name": "St. Petersburg",
    },
    {
        "name": "Duval",
        "population": 957755,  # As of 2019
        "area": 762,  # Square miles
        "state_name": "Florida",
        "city_name": "Jacksonville",
    },
    {
        "name": "Lee",
        "population": 770577,  # As of 2019
        "area": 785,  # Square miles
        "state_name": "Florida",
        "city_name": "Fort Myers",
    },
    {
        "name": "Polk",
        "population": 724777,  # As of 2019
        "area": 1798,  # Square miles
        "state_name": "Florida",
        "city_name": "Lakeland",
    },
    {
        "name": "Kings (Brooklyn)",
        "population": 2559903,  # As of 2019
        "area": 69,  # Square miles
        "state_name": "New York",
        "city_name": "Brooklyn",
    },
    {
        "name": "Queens",
        "population": 2253858,  # As of 2019
        "area": 108,  # Square miles
        "state_name": "New York",
        "city_name": "Queens",
    },
    {
        "name": "New York (Manhattan)",
        "population": 1628706,  # As of 2019
        "area": 22.7,  # Square miles
        "state_name": "New York",
        "city_name": "Manhattan",
    },
    {
        "name": "Suffolk",
        "population": 1476601,  # As of 2019
        "area": 912,  # Square miles
        "state_name": "New York",
        "city_name": "Riverhead",
    },
    {
        "name": "Bronx",
        "population": 1472654,  # As of 2019
        "area": 42,  # Square miles
        "state_name": "New York",
        "city_name": "The Bronx",
    },
    {
        "name": "Nassau",
        "population": 1356924,  # As of 2019
        "area": 285,  # Square miles
        "state_name": "New York",
        "city_name": "Mineola",
    },
    {
        "name": "Westchester",
        "population": 967506,  # As of 2019
        "area": 432,  # Square miles
        "state_name": "New York",
        "city_name": "White Plains",
    },
    {
        "name": "Erie",
        "population": 918702,  # As of 2019
        "area": 1044,  # Square miles
        "state_name": "New York",
        "city_name": "Buffalo",
    },
    {
        "name": "Monroe",
        "population": 741770,  # As of 2019
        "area": 657,  # Square miles
        "state_name": "New York",
        "city_name": "Rochester",
    },
    {
        "name": "Richmond (Staten Island)",
        "population": 476143,  # As of 2019
        "area": 57,  # Square miles
        "state_name": "New York",
        "city_name": "Staten Island",
    },
]
def add_counties(session, state_name):
    state = session.query(State).filter_by(name=state_name).first()

    if state:
           for county_data in counties_to_add:
            if county_data["state_name"] == state_name:  # Only add counties for the specified state
                try:
                    # Create a new county and associate it with the state
                    new_county = County(
                        name=county_data["name"],
                        population=county_data["population"],
                        area=county_data["area"],
                        state_name=county_data["state_name"],
                        state=state,
                    )

                    # Add the new county to the session
                    session.add(new_county)
                    # Commit the session to persist the change to the database
                    session.commit()
                except SQLAlchemyError as e:
                    session.rollback()
                    print(f"Error adding county {county_data['name']}: {e}")
    else:
        print(f"State {state_name} not found!")

    # Find the existing state and county by their names


def add_cities(session):
    state = session.query(State).filter_by(name="Florida").first()
    if not state:
        print(colored("State not found!", "red"))
        return

    # List of cities to add
    cities_to_add = [
        {
            "name": "Orlando",
            "population": 300000,
            "area": 150,
            "latitude": 0,
            "longitude": 0,
            "state_name": "Florida",
            "county_name": "Orange",
        },
        {
            "name": "Orlando",
            "population": 300000,
            "area": 150,
            "latitude": 0,
            "longitude": 0,
            "state_name": "Florida",
            "county_name": "Seminole",
        },
        {
            "name": "Orlando",
            "population": 300000,
            "area": 150,
            "latitude": 0,
            "longitude": 0,
            "state_name": "Florida",
            "county_name": "Lake County",
        },
        {
            "name": "Orlando",
            "population": 300000,
            "area": 150,
            "latitude": 0,
            "longitude": 0,
            "state_name": "Florida",
            "county_name": "Osceola",
        },
        {
            "name": "Miami",
            "population": 300000,
            "area": 150,
            "latitude": 0,
            "longitude": 0,
            "state_name": "Florida",
            "county_name": "Miami Dade",
        },
    ]

    for city_data in cities_to_add:
        county = session.query(County).filter_by(name=city_data["county_name"]).first()
        if not county:
            print(colored(f"County {city_data['county_name']} not found!", "red"))
            continue

        try:
            # Create a new city and associate it with the found state and county
            new_city = City(
                name=city_data["name"],
                population=0,
                area=0,
                latitude=0,
                longitude=0,
                state_name=city_data["state_name"],
                state=state,
                county_name=city_data["county_name"],
                county=county,
            )
            # Add the new city to the session
            session.add(new_city)
            # Commit the session to persist the change to the database
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(colored(f"Error adding city {city_data['name']}: {e}", "red"))


# UPDATE


def update_state_attribute(state_name, attribute, new_value):
    state_to_update = session.query(State).filter_by(name=state_name).first()
    if state_to_update:
        setattr(state_to_update, attribute, new_value)
        session.commit()
    else:
        print(f"State {state_name} not found!")


def update_county_attribute(county_name, attribute, new_value):
    county_to_update = session.query(County).filter_by(name=county_name).first()
    if county_to_update:
        setattr(county_to_update, attribute, new_value)
        session.commit()
    else:
        print(f"County {county_name} not found!")


def update_city_attribute(city_name, attribute, new_value):
    cities_to_update = session.query(City).filter_by(name=city_name).all()
    if cities_to_update:
        for city in cities_to_update:
            setattr(city, attribute, new_value)
        session.commit()
    else:
        print(colored(f"City {city_name} not found!", "red"))


# DELETE


def delete_state_by_name(session, state_name):
    try:
        state = session.query(State).filter_by(name=state_name).first()
        if state:
            session.delete(state)
            session.commit()
            print(f"State {state_name} deleted successfully!")
        else:
            print(f"State {state_name} not found!")
    except SQLAlchemyError as e:
        session.rollback()
        print(colored(f"Error deleting state {state_name}: {e}", "red"))


def delete_county_by_name(session, county_name):
    try:
        county = session.query(County).filter_by(name=county_name).first()
        if county:
            session.delete(county)
            session.commit()
            print(f"County {county_name} deleted successfully!")
        else:
            print(f"County {county_name} not found!")
    except SQLAlchemyError as e:
        session.rollback()
        print(colored(f"Error deleting county {county_name}: {e}", "red"))


def delete_city_by_name(session, city_name):
    try:
        # If there are multiple cities with the same name in different counties, this will delete all of them.
        cities = session.query(City).filter_by(name=city_name).all()
        if cities:
            for city in cities:
                session.delete(city)
            session.commit()
            print(f"City/Cities named {city_name} deleted successfully!")
        else:
            print(f"City {city_name} not found!")
    except SQLAlchemyError as e:
        session.rollback()
        print(colored(f"Error deleting city {city_name}: {e}", "red"))


geolocator = Nominatim(user_agent="YourAppName_Geocoder")


def update_city_coordinates():
    # Fetch all cities with latitude and longitude values equal to 0
    cities_to_update = (
        session.query(City).filter((City.latitude == 0) | (City.longitude == 0)).all()
    )

    for city in cities_to_update:
        try:
            location = geolocator.geocode(f"{city.name}, {city.state_name}")
            if location:
                city.latitude = location.latitude
                city.longitude = location.longitude
                print(
                    f"Updated coordinates for {city.name}: {city.latitude}, {city.longitude}"
                )
                session.commit()
            time.sleep(1)  # Delay for 1 second between requests
        except geopy.exc.GeocoderServiceError:
            print(f"Error geocoding {city.name}. Skipping...")
            continue
