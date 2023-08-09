from sqlalchemy import create_engine, update
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from termcolor import colored
from models import State, County, City
import random
from sqlalchemy.orm.exc import NoResultFound



Base = declarative_base()
engine = create_engine("sqlite:///geodata.db")

# Drop the tables
Base.metadata.drop_all(engine)

# Recreate the tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def random_population():
    # Generate a random population between 10,000 and 1,000,000
    return random.randint(10_000, 1_000_000)

def random_area():
    # Generate a random area between 100 and 10,000
    return random.randint(100, 10_000)

def random_latitude():
    return random.uniform(24.396308, 49.384358)

def random_longitude():
    return random.uniform(-125.000000, -66.934570)





# Add all provided states using instances of the State class
def add_states(session):
    add_states = [
        State(
            name="Illinois",
            abbreviation="IL",
            population=random_population(),
            capital="Chicago",
            area=random_area(),
        ),
        State(
            name="Texas",
            abbreviation="TX",
            population=random_population(),
            capital="Houston",
            area=random_area(),
        ),
        State(
            name="Alabama",
            abbreviation="AL",
            population=random_population(),
            capital="Birmingham",
            area=random_area(),
        ),
        State(
            name="Indiana",
            abbreviation="IN",
            population=random_population(),
            capital="Crawfordsville",
            area=random_area(),
        ),
        State(
            name="Oklahoma",
            abbreviation="OK",
            population=random_population(),
            capital="Tulsa",
            area=random_area(),
        ),
        State(
            name="Delaware",
            abbreviation="DE",
            population=random_population(),
            capital="Newark",
            area=random_area(),
        ),
        State(
            name="Arizona",
            abbreviation="AZ",
            population=random_population(),
            capital="Gilbert",
            area=random_area(),
        ),
        State(
            name="California",
            abbreviation="CA",
            population=random_population(),
            capital="San Jose",
            area=random_area(),
        ),
        State(
            name="Tennessee",
            abbreviation="TN",
            population=random_population(),
            capital="Nashville",
            area=random_area(),
        ),
        State(
            name="Florida",
            abbreviation="FL",
            population=222222222,
            capital="Lehigh Acres",
            area=random_area(),
        ),
        State(
            name="District of Columbia",
            abbreviation="DC",
            population=random_population(),
            capital="Washington",
            area=random_area(),
        ),
        State(
            name="New Jersey",
            abbreviation="NJ",
            population=random_population(),
            capital="Trenton",
            area=random_area(),
        ),
        State(
            name="Connecticut",
            abbreviation="CT",
            population=random_population(),
            capital="Hartford",
            area=random_area(),
        ),
        State(
            name="Missouri",
            abbreviation="MO",
            population=random_population(),
            capital="Independence",
            area=random_area(),
        ),
        State(
            name="Ohio",
            abbreviation="OH",
            population=random_population(),
            capital="Cincinnati",
            area=random_area(),
        ),
        State(
            name="Nebraska",
            abbreviation="NE",
            population=random_population(),
            capital="Omaha",
            area=random_area(),
        ),
        State(
            name="New York",
            abbreviation="NY",
            population=random_population(),
            capital="Brooklyn",
            area=random_area(),
        ),
        State(
            name="Hawaii",
            abbreviation="HI",
            population=random_population(),
            capital="Honolulu",
            area=random_area(),
        ),
        State(
            name="Minnesota",
            abbreviation="MN",
            population=random_population(),
            capital="Minneapolis",
            area=random_area(),
        ),
        State(
            name="Massachusetts",
            abbreviation="MA",
            population=random_population(),
            capital="Newton",
            area=random_area(),
        ),
        State(
            name="Pennsylvania",
            abbreviation="PA",
            population=random_population(),
            capital="Harrisburg",
            area=random_area(),
        ),
        ]

    session.add_all(add_states)
    session.commit()





def add_counties(session):
    state = session.query(State).filter_by(name="Florida").first()

    if state:
        # List of counties to add
        counties_to_add = [
            {"name": "Orange", "population": 580000, "area": 1920, "state_name":"Florida", "city_name":"Orlando"},
            {"name": "Seminole", "population": 2799000, "area": 5630, "state_name":"Florida", "city_name":"Orlando"},
            {"name": "Lake County", "population": 45716000, "area": 3310, "state_name":"Florida", "city_name":"Orlando"},
            {"name": "Osceola", "population": 716000, "area": 2230, "state_name":"Florida", "city_name":"Orlando"},
            {"name": "Miami Dade", "population": 716000, "area": 2230, "state_name":"Florida", "city_name":"Miami"}
            # Add more counties as needed
        ]

        for county_data in counties_to_add:
            try:
                # Create a new county and associate it with the state
                new_county = County(name=county_data["name"], 
                                    population=random_population(), 
                                    area=random_area(),
                                    state_name=county_data["state_name"], 
                                    state=state,
                                    city_name=county_data["city_name"])

                # Add the new county to the session
                session.add(new_county)
                # Commit the session to persist the change to the database
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                print(colored(f"Error adding county {county_data['name']}: {e}", "red"))
    else:
        print(colored("State not found!", "red"))
        
        

    # Find the existing state and county by their names
def add_cities(session):
    state = session.query(State).filter_by(name="Florida").first()
    if not state:
        print(colored("State not found!", "red"))
        return

    # List of cities to add
    cities_to_add = [
        {"name": "Orlando", "population": 300000, "area": 150, "latitude": 40.7128, "longitude": -74.0060, "state_name":"Florida", "county_name": "Orange"},
        {"name": "Orlando", "population": 300000, "area": 150, "latitude": 40.7128, "longitude": -74.0060, "state_name":"Florida", "county_name": "Seminole"},
        {"name": "Orlando", "population": 300000, "area": 150, "latitude": 40.7128, "longitude": -74.0060, "state_name":"Florida", "county_name": "Lake County"},
        {"name": "Orlando", "population": 300000, "area": 150, "latitude": 40.7128, "longitude": -74.0060, "state_name":"Florida", "county_name": "Osceola"},
        {"name": "Miami", "population": 300000, "area": 150, "latitude": 40.7128, "longitude": -74.0060, "state_name":"Florida", "county_name": "Miami Dade"},
        
        
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
                population=random_population(),
                area=random_area(),
                latitude=random_latitude(),
                longitude=random_longitude(),
                state_name=city_data["state_name"],
                state=state,
                county_name=city_data["county_name"],
                county=county
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





