from prettytable.colortable import ColorTable, Themes, Theme
from models import State, County, City

# ALL STATES
def display_states(session):
    
    add_states = session.query(State).all()
    # Create a new table
    table = ColorTable(theme=Themes.OCEAN)
    table.align = "l"
    # Set the headers for your table columns
    table.field_names = ["ID", "Name", "Abbreviation", "Population", "Capital", "Area"]
    # Add rows to the table
    for state in add_states:
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
def display_counties(session):
    add_counties = session.query(County).all()

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
    table.field_names = ["ID", "Name", "Population", "Area", "State", "State_ID"]
    # Add rows to the table
    for county in add_counties:
        table.add_row(
            [county.id, county.name, county.population, county.area, county.state_name, county.state_id]
        )
    # Print the title
    print("-" * len("COUNTIES Table"))
    print("COUNTIES Table")
    print("-" * len("COUNTIES Table"))
    # Print the table
    print(table)


# ALL CITIES
def display_cities(session):
    add_cities = session.query(City).all()
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
        "State",
        "State_ID",
        "County",
        "County_ID",
    ]
    # Add rows to the table

    for city in add_cities:
        # print(colored(city, "yellow", "on_magenta"))
        table.add_row(
            [
                city.id,
                city.name,
                city.population,
                city.area,
                city.latitude,
                city.longitude,
                city.state_name,
                city.state_id,
                city.county_name,
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