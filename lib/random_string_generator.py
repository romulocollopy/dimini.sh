import string
import random

LEGAL_CHARS = string.ascii_uppercase + string.digits

def random_string_generator(size=4, chars=LEGAL_CHARS):
   return ''.join(random.choice(chars) for x in range(size))

