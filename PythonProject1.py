import random
import string

# Predefined lists of adjectives and nouns
adjectives = ["Assertive","Compassionate","Diligent","Fearless","Humble","Loyal","Outgoing","Passionate","Happy","Wise","Angry","Cool","Brave","Charming"]
nouns = ["Tiger", "Dragon", "Falcon", "Panda", "Phoenix", "Wolf", "Bear", "Knight", "Wizard", "Ninja","Pegasus","Nemesis","Titan","Ironman",]

def generate_username(include_numbers=True, include_special_chars=True, length=None):
    # Randomly select an adjective and a noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    # Combine the adjective and noun
    username = adjective + noun
    
    # Add numbers if required
    if include_numbers:
        username += str(random.randint(10, 99))
    
    # Add special characters if required
    if include_special_chars:
        special_chars = "!@#$%^&*"
        username += random.choice(special_chars)
    
    # Adjust the length if specified
    if length and len(username) > length:
        username = username[:length]
    
    return username

def save_usernames_to_file(usernames, filename="usernames.txt"):
    try:
        with open(filename, "w") as file:
            for username in usernames:
                file.write(username + "\n")
        print(f"Usernames saved to {filename}")
    except Exception as e:
        print(f"Error saving usernames to file: {e}")

def main():
    print("Welcome to the Random Username Generator!")
    
    # Get user preferences
    try:
        include_numbers = input("Include numbers in the username? (yes/no): ").strip().lower() == "yes"
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
        length = input("Set a maximum length for the username (or press Enter to skip): ").strip()
        length = int(length) if length else None
        count = int(input("How many usernames would you like to generate? (e.g., 5): ").strip())
    except ValueError:
        print("Invalid input. Please restart the program and provide valid options.")
        return
    
    # Generate usernames based on preferences
    usernames = [generate_username(include_numbers, include_special_chars, length) for _ in range(count)]
    
    # Display generated usernames
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)
    
    # Save to file option
    save_option = input("\nWould you like to save these usernames to a file? (yes/no): ").strip().lower()
    if save_option == "yes":
        filename = input("Enter the filename to save (default: usernames.txt): ").strip()
        filename = filename if filename else "usernames.txt"
        save_usernames_to_file(usernames, filename)

if __name__ == "__main__":
    main()

