import random
import string
def generate_random_password(length=18):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage
random_password = generate_random_password()
print(generate_random_password())