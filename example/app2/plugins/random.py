import random
import string


def make_random(s):
    chars = list(s)
    for idx, char in enumerate(chars):
        if char not in string.punctuation and not char.isspace():
            chars[idx] = random.choice(string.ascii_letters)
    return ''.join(chars)


def setup(app):
    app.register_formatter('random', make_random)
