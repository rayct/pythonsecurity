import random
import string
from datetime import datetime

def generate_random_password(length=18):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_password_to_file(password):
    with open('/home/ray/Repos/github.com/rayct/pythonsecurity/projects/passwords.txt', 'a') as file:
        timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        file.write(f'{timestamp} - {password}\n')

# Example usage
random_password = generate_random_password()
print(random_password)
save_password_to_file(random_password)