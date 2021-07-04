"""
Author : Amol Ambkar
Program : Create Jokes
"""

import pyjokes

#create a single joke
joke = pyjokes.get_joke(language='en',category='all')

#create list of jokes
joke = pyjokes.get_jokes(language='en',category='all')

for i in range(5):
    print(joke[i])
