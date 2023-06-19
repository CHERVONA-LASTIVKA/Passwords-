import random
import string

def generate_password(length, complexity):
    if complexity == "weak":
        characters = string.ascii_lowercase
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Please choose from 'weak', 'medium', or 'strong'.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter desired password length: "))
    complexity = input("Enter desired complexity level (weak/medium/strong): ")

    password = generate_password(length, complexity)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
