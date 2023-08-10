import click
from models.base import Session
from models.state import State

@click.command()
def create_tables():
    """Create database tables."""
    from models.base import Base, engine
    Base.metadata.create_all(engine)
    click.echo("Tables created successfully!")

@click.command()
@click.argument('name')
@click.argument('abbreviation')
def add_state(name, abbreviation):
    """Add a new state."""
    session = Session()
    state = State(name=name, abbreviation=abbreviation)
    session.add(state)
    session.commit()
    click.echo(f"State {name} added successfully!")

@click.command()
def list_states():
    """List all states."""
    session = Session()
    states = session.query(State).all()
    for state in states:
        click.echo(state.name)


