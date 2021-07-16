'''
Build a Translator in Python
Author: Amol Ambkar
'''

#import the package
from googletrans import Translator

# Create an instance of Translator to use
translator = Translator()

# translate a spanish text to english text (by default)
translation = translator.translate("Hola Mundo")
print(translation.origin , translation.src ," -->", translation.text, translation.dest)
print(' ')

# Store some text for translation in french language

text = ''' aamchya channel la subscribe kara '''

# detect the language
lang = translator.detect(text)
print(lang)
print(' ')

# Call the translate()
translated = translator.translate(text, dest = 'en')

#print the result
print(translated.text)

'''
if you getting following error
AttributeError: 'NoneType' object has no attribute 'group'

do following :===> 
pip3 uninstall googletrans
pip3 install googletrans==3.1.0a0
'''