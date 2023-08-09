from database_operations import session
from models import State, City, County
import datetime


def save_user_details():
    # Ask the user for their name
    user_name = input("Please enter your name (or type 'exit' to quit): ")

    if user_name.lower() == "exit":
        print("Exiting the program. Take alook of our dB before close the terminal!! Goodbye!")
        return

    # Get the current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open a text file in append mode and save the details
    with open("user_details.txt", "a") as file:
        file.write(f"{user_name}, {current_datetime}\n")

    print("Your name and visit's date were saved successfully!")
    

def get_user_query():
    # Ask user for the type of information
    query_type = input("What information do you want? (state, city, county)(or type 'exit' to quit): ").strip().lower()
    
    if query_type.lower() == "exit":
        print("Exiting the program. Take a look of our dB before close the terminal!! Goodbye!")
        return

    # Depending on the user's choice, query the database
    if query_type == "state":
        state_name = input("Enter the name of the state: ").strip()
        state = session.query(State).filter_by(name=state_name).first()
        if state:
            print(f"Details for state {state.name}: Population = {state.population}, Area = {state.area}")
        else:
            print(f"No data found for state: {state_name}")

    elif query_type == "city":
        city_name = input("Enter the name of the city: ").strip()
        city = session.query(City).filter_by(name=city_name).first()
        if city:
            print(f"Details for city {city.name}: Population = {city.population}, Area = {city.area}, State = {city.state_name}, County = {city.county_name}")
        else:
            print(f"No data found for city: {city_name}")

    elif query_type == "county":
        county_name = input("Enter the name of the county: ").strip()
        county = session.query(County).filter_by(name=county_name).first()
        if county:
            print(f"Details for county {county.name}: Population = {county.population}, Area = {county.area}, State = {county.state_name}")
        else:
            print(f"No data found for county: {county_name}")

    else:
        print("Invalid input. Please choose state, city, or county.")


