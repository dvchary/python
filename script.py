import math
import os
import sys

import requests

print(f'[PYTHON VERSION]: {sys.version}')
print(f'[PYTHON PATH]: {sys.executable}')



def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


r = requests.get('https://google.com')
print(r.status_code)
