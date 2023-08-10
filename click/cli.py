import click
from sqlalchemy import create_engine, update
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from models import State, County, City
from cli_database_operations import (
    add_states,
    add_counties,
    add_cities,
    update_state_attribute,
    update_county_attribute,
    update_city_attribute,
    delete_state_by_name,
    delete_county_by_name,
    delete_city_by_name,
    update_city_coordinates,
    session,
    add_single_state,
    add_single_county,
    add_single_city,
)

Base = declarative_base()
engine = create_engine("sqlite:///geodata.db")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


@click.group()
def cli():
    """GeoData Management Tool"""
    pass


@cli.command()
def add_all_states():
    """Add all states from predefined list."""
    add_states(session)
    click.echo("All states added successfully!")


@cli.command()
@click.option("--name", prompt="State Name")
@click.option("--population", type=int, default=0, prompt="Population")
@click.option("--area", type=float, default=0.0, prompt="Area")
def add_state(name, population, area):
    """Add a new state."""
    result = add_single_state(session, name, population, area)
    click.echo(result)
