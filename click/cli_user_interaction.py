from termcolor import colored
import pyfiglet
import click
import geodata_logic as logic
import datetime

def save_user_details(username):
    """Save user name and current date to a text file."""
    with open("cli_user_details.txt", "a") as file:
        file.write(f"{username}, {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")


@click.group()
def user_cli():
    """GeoData User Interaction Tool"""
    pass

@user_cli.command()
def interactive():
    # Welcome banner
    banner = pyfiglet.figlet_format("GeoData Tool", font="slant")
    print(colored(banner, "cyan"))
    
        # Ask for user name and save it with the current date
    username = input(colored("Enter your name: ", "green"))
    save_user_details(username)
    
    while True:
        print(colored("\nChoose a CRUD operation:", "red"))
        print(colored("1. Show the DataBase", "yellow"))
        print(colored("2. Add a new State", "yellow"))
        print(colored("3. Add a new City", "yellow"))
        print(colored("4. Add a new County", "yellow"))
        print(colored("5. Update a State", "yellow"))
        print(colored("6. Update a City", "yellow"))
        print(colored("7. Update a County", "yellow"))
        print(colored("8. Delete a State", "yellow"))
        print(colored("9. Delete a County", "yellow"))
        print(colored("10. Delete a City", "yellow"))
        print(colored("11. Exit", "yellow"))

        choice = input(colored("Enter your choice: ", "red"))

        if choice == "1":
            logic.show_all_logic()
        elif choice == "2":
            logic.add_state_logic()
        elif choice == "3":
            logic.add_city_logic()
            logic.update_coordinates_logic()
        elif choice == "4":
            logic.add_county_logic()
        elif choice == "5":
            logic.update_state_logic()
        elif choice == "6":
            logic.update_city_logic()
        elif choice == "7":
            logic.update_county_logic()
        elif choice == "8":
            logic.delete_state_logic()
        elif choice == "9":
            logic.delete_county_logic()
        elif choice == "10":
            logic.delete_city_logic()
        elif choice == "11":
            print(colored("\nThank you for using GeoData Tool!", "cyan"))
            banner = pyfiglet.figlet_format(f"Goodbye {username}", font="slant")
            print(colored(banner, "cyan"))
            break
        else:
            print(colored("Invalid choice. Please try again.", "red"))

# Add the new command to the group
user_cli.add_command(interactive)

if __name__ == "__main__":
    user_cli()
