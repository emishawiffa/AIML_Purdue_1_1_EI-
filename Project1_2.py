# adventure_game.py
# Text-based adventure game: Travel the world, face challenges, and find the legendary treasure!

def start_game():
    print("Welcome to the Adventure Quest! A legendary treasure awaits.")
    name = input("What is your name, brave explorer? ")
    print(f"\nHello, {name}! Your mission: travel across the world and through dangerous paths to find the treasure.")
    country = input("Choose your country of origin: ")
    city = input(f"Choose a city in {country}: ")
    sports_team = input("Pick your favorite sports team: ")
    print(f"\nYour courage matches the spirit of {sports_team}!")
    print(f"You begin your journey near {city}, {country}.")
    character = {
        "name": name,
        "country": country,
        "city": city,
        "sports_team": sports_team
    }
    first_decision(character)

def first_decision(character):
    print("\nYou stand at the edge of adventure near your chosen city.")
    print("Two paths lie before you:")
    print("1. Enter the Dark Forest")
    print("2. Explore the Mysterious Cave")
    while True:
        choice = input("Choose your path (1 for Forest, 2 for Cave): ")
        if choice == "1":
            forest_path(character)
            break
        elif choice == "2":
            cave_path(character)
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

def forest_path(character):
    print(f"\nThe forest near {character['city']} is dense and full of strange sounds.")
    print("Do you:")
    print("1. Follow the river")
    print("2. Climb a tree to scout ahead")
    while True:
        choice = input("Your choice (1 or 2): ")
        if choice == "1":
            print("You follow the river and spot a map tied to a floating log. It's a clue towards the treasure!")
            challenge_encounter(character)
            break
        elif choice == "2":
            print("You climb a tree, but a wild animal attacks you! Your adventure ends here.")
            end_game(character, False)
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

def cave_path(character):
    print(f"\nThe cave near {character['city']} is dark and echoing.")
    print("Do you:")
    print("1. Light a torch to see inside")
    print("2. Proceed in the dark")
    while True:
        choice = input("Your choice (1 or 2): ")
        if choice == "1":
            print("You light your torch and discover hidden symbols leading you to a secret passage!")
            challenge_encounter(character)
            break
        elif choice == "2":
            print("You proceed in the dark, fall into a pit, and your adventure is over.")
            end_game(character, False)
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

def challenge_encounter(character):
    print("\nA wise old traveler blocks your path and presents a riddle:")
    print('"I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"')
    print("1. Echo")
    print("2. Shadow")
    print("3. River")
    answer = input("Your answer (enter the number): ")
    if answer == "1":
        print("Correct! The traveler steps aside and you journey onward.")
        treasure_chamber(character)
    else:
        print("Incorrect! The traveler shakes his head, and your quest ends here.")
        end_game(character, False)

def treasure_chamber(character):
    print("\nYou reach a hidden chamber deep beneath the land.")
    print(f"The treasure chest is engraved with the symbol of {character['sports_team']} and ancient markers of {character['city']}, {character['country']}.")
    print(f"Congratulations, {character['name']}! You found the legendary treasure of {character['city']}, {character['country']}!")
    end_game(character, True)

def end_game(character, won):
    if won:
        print("\nVICTORY! The world will remember your name!")
    else:
        print("\nGAME OVER. Your quest has ended.")
    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        print("\nRestarting the adventure...\n")
        start_game()
    else:
        print("Thank you for playing Adventure Quest. Farewell!")

if __name__ == "__main__":
    print("Adventure game setup complete. Starting game...\n")
    start_game()