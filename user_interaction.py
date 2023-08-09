import database_operations
import display
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

    

def get_user_query():
    while True:
        print("\nChoose an operation:")
        print("1. Show the DataBase")
        print("2. Add a new State")
        print("3. Add a new City")
        print("4. Add a new County")
        print("5. Update a State")
        print("6. Update a City")
        print("7. Update a County")
        print("8. Delete a State")
        print("9. Delete a County")
        print("10. Delete a City")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display.display_states(session)
            display.display_counties(session)
            display.display_cities(session)

        elif choice == "2":
            state_name = input("Enter state name: ").strip().lower()
            database_operations.add_single_state(session, state_name.title())

        elif choice == "3":
            state_name = input("Enter the name of the state where the city is located: ").strip().lower()
            county_name = input("Enter the name of the county where the city is located: ").strip().lower()
            name = input("Enter city name: ").strip().lower()
            database_operations.add_single_city(session, name.title(), state_name.title(), county_name.title() )

        elif choice == "4":
            state_name = input("Enter the name of the state where the county is located: ").strip().lower()
            name = input("Enter county name: ").strip().lower()
            database_operations.add_single_county(session,name.title(), state_name.title() )
            
        elif choice == "5":
            state_name = input("Enter the name of the state to modify: ").strip().lower()
            attribute = input("Enter the attribute to modify: ").strip().lower()
            new_value = input("Enter the new value: ").strip().lower()
            database_operations.update_state_attribute(state_name.title(), attribute, new_value)
            
        elif choice == "6":
            city_name = input("Enter the name of the city to modify: ").strip().lower()
            attribute = input("Enter the attribute to modify: ").strip().lower()
            new_value = input("Enter the new value: ").strip().lower()
            database_operations.update_city_attribute(city_name.title(), attribute, new_value)

        elif choice == "7":
            county_name = input("Enter the name of the county to modify: ").strip().lower()
            attribute = input("Enter the attribute to modify: ").strip().lower()
            new_value = input("Enter the new value: ").strip().lower()
            database_operations.update_county_attribute(county_name.title(), attribute, new_value)
            
        elif choice == "8":
            state_name = input("Enter state name to delete: ").strip().lower()
            database_operations.delete_state_by_name(session, state_name.title())
            
        elif choice == "9":
            county_name = input("Enter county name to delete: ").strip().lower()
            database_operations.delete_county_by_name(session, county_name.title())
            
        elif choice == "10":
            city_name = input("Enter city name to delete: ").strip().lower()
            database_operations.delete_city_by_name(session, city_name.title())

        elif choice == "11":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")






