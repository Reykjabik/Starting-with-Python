#! python3
''' This program takes an address (whether from the command line or from the clipboard)
    and searches for it automatically in Google Maps.

    NOTE: If known, please add the city at the end, as sometimes Google cannot show you
    a street straight away if it is found on many cities accross the world.

    Example:

    mapIt.py tverskaya 11, Moscow
    
    Original idea and code from Al Sweigart's 'Automate the Boring Stuff with Python'
'''

import webbrowser, sys, pyperclip   # webbrowser: to open browser
                                    # sys: to read command line arguments
                                    # to have access to the clipboard


if len(sys.argv) > 1:                   # if there are arguments in the command line
    address = ' '.join(sys.argv[1:])
else:                                   # otherwise, get the address from the clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
