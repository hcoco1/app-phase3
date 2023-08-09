#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Importing models and functions from other files
from models import Base
from database_operations import (
    add_states,
    add_counties,
    add_cities,
    update_state_attribute,
    update_county_attribute,
    update_city_attribute,
    delete_state_by_name,
    delete_county_by_name,
    delete_city_by_name,
)
from display import display_states, display_counties, display_cities

if __name__ == "__main__":
    # Database setup
    engine = create_engine("sqlite:///geodata.db")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Add data to the database
        add_states(session)
        add_counties(session)
        add_cities(session)

        update_state_attribute("Florida", "population", 9000000)
        update_county_attribute("Orange", "population", 1650000)
        update_city_attribute("Orlando", "population", 1350000)

        # delete_state_by_name(session, "Florida")
        # delete_county_by_name(session, "Orange")
        delete_city_by_name(session, "Orlando")

        # Display data using prettytable
        display_states(session)
        display_counties(session)
        display_cities(session)

    except SQLAlchemyError as e:
        session.rollback()
        print(f"An error occurred: {e}")

    finally:
        session.close()
