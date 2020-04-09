# Translate file
# I made a file on desktop in english. Read it with py. Store words in list?
# Use module to translate it. Take the string list and combine it.
# Output to file. Done!


from googletrans import Translator

with open('test.txt') as my_file:
    long_string_list = my_file.readlines()
long_string = ''.join(long_string_list)


translator = Translator()


translations = translator.translate(long_string, dest='lv')

with open('translated.txt', mode='w') as my_tl:
    text = my_tl.write(translations.text)

