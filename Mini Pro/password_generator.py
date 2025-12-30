import random
import string

def generate_password(length):
    password = [
        random.choice(string.ascii_letters),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password += random.choices(characters, k=length-3)
    
    random.shuffle(password)
    return ''.join(password)

