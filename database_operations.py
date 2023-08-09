from sqlalchemy import create_engine, update
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from termcolor import colored
from models import State, County, City
import random
from sqlalchemy.orm.exc import NoResultFound
from geopy.geocoders import Nominatim
import time
from data_config import cities_to_add, counties_to_add, states_to_add


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
    session.add_all(states_to_add)
    session.commit()


def add_counties(session, state_name):
    state = session.query(State).filter_by(name=state_name).first()

    if state:
        for county_data in counties_to_add:
            if (
                county_data["state_name"] == state_name
            ):  # Only add counties for the specified state
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
        
        

# 


def add_cities(session):
    # Loop through cities data
    for city_data in cities_to_add:
        # Query for the state based on the state_name in city_data
        state = session.query(State).filter_by(name=city_data["state_name"]).first()
        if not state:
            print(colored(f"State {city_data['state_name']} not found!", "red"))
            continue

        # Query for the county based on the county_name in city_data
        county = session.query(County).filter_by(name=city_data["county_name"]).first()
        if not county:
            print(colored(f"County {city_data['county_name']} not found!", "red"))
            continue

        try:
            # Create a new city and associate it with the found state and county
            new_city = City(
                name=city_data["name"],
                population=city_data["population"],
                area=city_data["area"],
                latitude=city_data["latitude"],
                longitude=city_data["longitude"],
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
        session.query(City).filter((City.latitude != 0) | (City.longitude != 0)).all()
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
