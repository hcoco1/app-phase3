from sqlalchemy import create_engine, update
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from termcolor import colored
from models import State, County, City
import random
from sqlalchemy.orm.exc import NoResultFound
from geopy.geocoders import Nominatim
from geopy import exc
import time
from data_config import cities_to_add, counties_to_add, states_to_add, facilities_to_add


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
    
def add_counties(session):
    session.add_all(counties_to_add)
    session.commit()
    
def add_cities(session):
    session.add_all(cities_to_add)
    session.commit()
    
def add_facilities(session):
    session.add_all(facilities_to_add)
    session.commit()
    
    
def add_single_state(session, name, population=0, area=0):
    existing_state = session.query(State).filter_by(name=name).first()
    if existing_state:
        print(colored(f"State {name} already exists!", "yellow"))
        return

    try:
        new_state = State(name=name, population=population, area=area)
        session.add(new_state)
        session.commit()
        print(f"State {name} added successfully!")
    except SQLAlchemyError as e:
        session.rollback()
        print(colored(f"Error adding state {name}: {e} Try again!", "red"))




def add_counties1(session, state_name):
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
        print(colored(f"State {state_name} not found! Add {state_name} to the States table and try to add the county again", "yellow"))
        
def add_single_county(session, name, state_name, population=0, area=0):
    existing_county = session.query(County).filter_by(name=name).first()
    if existing_county:
        print(colored(f"County {name} already exists in state {state_name}!", "yellow"))
        return

    state = session.query(State).filter_by(name=state_name).first()
    if not state:
        print(colored(f"State {state_name} not found! Add {state_name} to the States table and try to add the county again", "yellow"))
        return

    try:
        new_county = County(name=name, population=population, area=area, state_name=state_name, state=state)
        session.add(new_county)
        session.commit()
        print(f"County {name} added successfully!")
    except SQLAlchemyError as e:
        session.rollback()
        print(colored(f"Error adding county {name}: {e}", "red"))

 

# 


def add_cities1(session):
    # Loop through cities data
    for city_data in cities_to_add:
        # Query for the state based on the state_name in city_data
        state = session.query(State).filter_by(name=city_data["state_name"]).first()
        if not state:
            print(colored(f"State {city_data['state_name']} not found! Add {city_data['state_name']} and try to add the cities again ", "red"))
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
            
def add_single_city(session, name, state_name, county_name, population=0, area=0, latitude=0, longitude=0):
    existing_city = session.query(City).filter_by(name=name, state_name=state_name, county_name=county_name).first()
    if existing_city:
        print(colored(f"City {name} already exists in county {county_name} of state {state_name}!", "yellow"))
        return

    state = session.query(State).filter_by(name=state_name).first()
    county = session.query(County).filter_by(name=county_name).first()

    if not state:
        print(colored(f"State {state_name} not found! Add {state_name} to the States table and try to add the city again", "yellow"))
        return

    if not county:
        print(colored(f"County {county_name} not found! Add {county_name} to the Counties table and try again!", "red"))
        return

    try:
        new_city = City(name=name, population=population, area=area, latitude=latitude, longitude=longitude, state_name=state_name, state=state, county_name=county_name, county=county)
        session.add(new_city)
        session.commit()
        print(f"City {name} added successfully!")
    except SQLAlchemyError as e:
        session.rollback()
        print(colored(f"Error adding city {name}: {e}", "red"))




# UPDATE

def update_state_attribute(state_name, attribute, new_value):
    state_to_update = session.query(State).filter_by(name=state_name).first()
    if state_to_update:
        setattr(state_to_update, attribute, new_value)
        session.commit()
    else:
        print(colored(f"State {state_name} not found! Add {state_name} to the States table", "yellow"))


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


user_agent_name = "GeoApp v1.0 (hcoco1@hotmail.com.com)"
geolocator = Nominatim(user_agent=user_agent_name)


def update_city_coordinates():
    # Fetch all cities with latitude and longitude values equal to 0
    cities_to_update = (
        session.query(City).filter((City.latitude == 0) & (City.longitude == 0)).all()
    )

    for city in cities_to_update:
        try:
            location = geolocator.geocode(f"{city.name}")
            if location:
                city.latitude = location.latitude
                city.longitude = location.longitude
                print(
                    f"Updated coordinates for {city.name}: {city.latitude}, {city.longitude}"
                )
                session.commit()
            time.sleep(1)  # Delay for 1 second between requests
        except exc.GeocoderServiceError:
            print(f"Service error when geocoding {city.name}. Skipping...")
            continue
        except exc.GeocoderUnavailable:
            print(f"Geocoding service unavailable for {city.name}. Skipping...")
            continue
