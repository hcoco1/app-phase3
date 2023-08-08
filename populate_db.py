#!/usr/bin/env python3

import click
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create SQLite database and connect
engine = create_engine('sqlite:///geodata.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class State(Base):
    __tablename__ = 'states'
    StateID = Column(Integer, primary_key=True)
    StateName = Column(String)
    Abbreviation = Column(String)
    Population = Column(Integer)
    Capital = Column(String)
    Area = Column(Float)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.argument('abbreviation')
@click.argument('population', type=int)
@click.argument('capital')
@click.argument('area', type=float)
def create_state(name, abbreviation, population, capital, area):
    """Create a new state."""
    new_state = State(
        StateName=name,
        Abbreviation=abbreviation,
        Population=population,
        Capital=capital,
        Area=area
    )
    session.add(new_state)
    session.commit()
    click.echo(f'State "{name}" created.')

@cli.command()
def read_states():
    """Read and display all states."""
    states = session.query(State).all()
    for state in states:
        click.echo(f'{state.StateID}: {state.StateName} ({state.Abbreviation})')

@cli.command()
@click.argument('state_id', type=int)
@click.argument('new_name')
def update_state(state_id, new_name):
    """Update a state's name."""
    state = session.query(State).get(state_id)
    if state:
        state.StateName = new_name
        session.commit()
        click.echo(f'State {state_id} updated with new name: {new_name}.')
    else:
        click.echo(f'State with ID {state_id} not found.')

@cli.command()
@click.argument('state_id', type=int)
def delete_state(state_id):
    """Delete a state."""
    state = session.query(State).get(state_id)
    if state:
        session.delete(state)
        session.commit()
        click.echo(f'State {state_id} deleted.')
    else:
        click.echo(f'State with ID {state_id} not found.')

if __name__ == '__main__':
    cli()


