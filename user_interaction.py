from database_operations import session
from models import State, City, County
import datetime




def save_user_details():
    # Ask the user for their name
    user_name = input("Please enter your name (or type 'exit' to quit): ")

    if user_name.lower() == "exit":
        print("Exiting the program. Goodbye!")
        return None  # Return None if the user wants to exit

    # Get the current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open a text file in append mode and save the details
    with open("user_details.txt", "a") as file:
        file.write(f"{user_name}, {current_datetime}\n")

    print("Your name was saved successfully in our local storage!")
    return user_name  # Return the captured user_name

    

def get_user_query(session, user_name):

    def check_exit(user_input):
        """Check if the user wants to exit and terminate if so."""
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the program. Goodbye!")
            exit()  # Use exit() to terminate the entire program, or you can use 'return' to exit the function.

    # Ask user for the type of information: state, city, county
    entity_type = input(f" Hey {user_name} would you like to take a look of my dataBase? Type: Yes or type 'exit' to quit: ").strip().lower()
    check_exit(entity_type)


    # Ask user for the type of operation: create, read, update, delete
    operation = input("Which operation do you want to perform? (create, read, update, delete) or type 'exit' to quit: ").strip().lower()
    check_exit(operation)

    if operation == "create":
        # Handle create operation
        # For simplicity, we'll only handle state creation here. You can expand for city and county.
        if entity_type == "state":
            state_name = input("Enter the name of the state to create: ").strip()
            check_exit(state_name)
            # Add other fields like population, area, etc.
            # Create the state in the database
            # session.add(State(name=state_name, ...))
            # session.commit()

    elif operation == "read":
        # Handle read operation
        if entity_type == "state":
            state_name = input("Enter the name of the state to read: ").strip()
            check_exit(state_name)
            state = session.query(State).filter_by(name=state_name).first()
            if state:
                print(f"Details for state {state.name}: Population = {state.population}, Area = {state.area}")
            else:
                print(f"No data found for state: {state_name}")

    elif operation == "update":
        # Handle update operation
        # For simplicity, we'll only handle state update here. You can expand for city and county.
        if entity_type == "state":
            state_name = input("Enter the name of the state to update: ").strip()
            check_exit(state_name)
            # Query the state and update the desired fields
            # state = session.query(State).filter_by(name=state_name).first()
            # if state:
            #     state.population = updated_population
            #     session.commit()

    elif operation == "delete":
        # Handle delete operation
        # For simplicity, we'll only handle state deletion here. You can expand for city and county.
        if entity_type == "state":
            state_name = input("Enter the name of the state to delete: ").strip()
            check_exit(state_name)
            # Query the state and delete it
            # state = session.query(State).filter_by(name=state_name).first()
            # if state:
            #     session.delete(state)
            #     session.commit()

    print("Operation completed.")





