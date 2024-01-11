from random import choice
from pyfiglet import Figlet
import sys

# Instancing figlet
figlet = Figlet()
# "Importing" the full list of fonts available in the figlet lib
fonts = figlet.getFonts()

# Checking if there is only the name of the file
if len(sys.argv) == 1:
    # chossing a font randomly from the lib list
    font = choice(fonts)

# Check besides the len, if font inputed by user is valid
elif (len(sys.argv) == 3) and (sys.argv[1] in ['-f', '--font']) and (sys.argv[2] in fonts):
    # choosing a font passed by the user
    font = sys.argv[2]

else:
    sys.exit("Invalid Usage")


# set font
figlet.setFont(font=font)
# Prompting user for text
text = str(input("Input: ")).strip()
# Printing Result
print(figlet.renderText(text))
