from bs4 import BeautifulSoup
import requests


def hex_to_ansi_background(hex_color):
    # Convert hex color to RGB
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)

    # Create ANSI escape code for background color
    ansi_background = f'\033[48;2;{r};{g};{b}m'

    return ansi_background


def getColor(hex_color):
    BACKGROUND_COLOR = hex_to_ansi_background(hex_color)
    RESET = '\033[0m'  # Reset to default color

    # Define the dimensions of the box
    width = 10
    height = 5

    # Print the colored box
    return BACKGROUND_COLOR + " " * 3 + RESET


url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html'
data = requests.get(url).text
soup = BeautifulSoup(data, "html5lib")
table = soup.find('table')

for i, row in enumerate(table.findAll('tr')):
    cols = row.findAll('td')
    color_name = cols[2].string
    color_code = cols[3].text
    color = ''
    if i != 0:
        color = getColor(str(color_code))
    print(f'{color_name:20}{color_code:8}{color:4}')
