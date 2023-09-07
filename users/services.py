import random
import string


def random_key():
    characters = string.ascii_letters + string.digits
    return ''.join(random.sample(characters, 30))
