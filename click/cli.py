import click
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from cli_display import display_states, display_counties, display_cities

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
engine = create_engine("sqlite:///cli_geodata.db")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


@click.group()
def cli():
    """GeoData Management Tool"""
    pass

# 2. Commands for  ADD States

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

# 3. Commands for ADD Counties

@cli.command()
@click.argument("state_name", required=True)
def add_all_counties(state_name):
    """Add counties for a given state from a predefined list."""
    result = add_counties(session, state_name)
    click.echo(result)

@cli.command()
@click.option("--name", prompt="County Name")
@click.argument("state_name", required=True)
@click.option("--population", type=int, default=0, prompt="Population")
@click.option("--area", type=float, default=0.0, prompt="Area")
def add_county(name, state_name, population, area):
    """Add a single county."""
    result = add_single_county(session, name, state_name, population, area)
    click.echo(result)
    
# 4. Commands for ADD Cities

@cli.command()
def add_all_cities():
    """Add all cities from predefined list."""
    result = add_cities(session)
    click.echo(result)

@cli.command()
@click.option("--name", prompt="City Name")
@click.argument("state_name", required=True)
@click.argument("county_name", required=True)
@click.option("--population", type=int, default=0, prompt="Population")
@click.option("--area", type=float, default=0.0, prompt="Area")
@click.option("--latitude", type=float, default=0.0, prompt="Latitude")
@click.option("--longitude", type=float, default=0.0, prompt="Longitude")
def add_city(name, state_name, county_name, population, area, latitude, longitude):
    """Add a single city."""
    result = add_single_city(session, name, state_name, county_name, population, area, latitude, longitude)
    click.echo(result)

# 5. Update Commands

@cli.command()
@click.argument("state_name", required=True)
@click.argument("attribute", required=True)
@click.argument("new_value", required=True)
def update_state(state_name, attribute, new_value):
    """Update attributes of a state."""
    result = update_state_attribute(state_name, attribute, new_value)
    click.echo(result)
    
@cli.command()
@click.argument("county_name", required=True)
@click.argument("attribute", required=True)
@click.argument("new_value", required=True)
def update_county(county_name, attribute, new_value):
    """Update attributes of a county."""
    result = update_county_attribute(county_name, attribute, new_value)
    click.echo(result)
    
@cli.command()
@click.argument("city_name", required=True)
@click.argument("attribute", required=True)
@click.argument("new_value", required=True)
def update_city(city_name, attribute, new_value):
    """Update attributes of a city."""
    result = update_city_attribute(city_name, attribute, new_value)
    click.echo(result)
    
  # 6. Delete Commands

@cli.command()
@click.argument("state_name", required=True)
def delete_state(state_name):
    """Delete a state by name."""
    result = delete_state_by_name(session, state_name)
    click.echo(result)

@cli.command()
@click.argument("county_name", required=True)
def delete_county(county_name):
    """Delete a county by name."""
    result = delete_county_by_name(session, county_name)
    click.echo(result)

@cli.command()
@click.argument("city_name", required=True)
def delete_city(city_name):
    """Delete a city by name."""
    result = delete_city_by_name(session, city_name)
    click.echo(result)

# Utility commands
@cli.command('update-coordinates')
def update_coordinates():
    """Update coordinates for cities."""
    update_city_coordinates()
    
    
@cli.command()
def show_states():
    """Display all states in a colored Table."""
    display_states(session)

@cli.command()
def show_counties():
    """Display all counties in a colored Table."""
    display_counties(session)

@cli.command()
def show_cities():
    """Display all cities in a colored Table."""
    display_cities(session)

    
    
if __name__ == "__main__":
    cli()



