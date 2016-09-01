"""
Intermediate Exercise
hexadecimal colour code finder
"""
COLOUR_CODES = {"aliceblue": "#f0f8ff", "azure1": "#f0ffff", "black": "#000000", "blue1": "#0000ff", "white": "#000000",
                "cyan1": "#00ffff", "darkgreen": "#006400", "coral": "#ff7f50", "darkorange": "#ff8c00",
                "darkorchid": "#9932cc"}

colour = input("Enter colour: ")
while colour != "":
    print(COLOUR_CODES[colour.lower()])
    colour = input("Enter colour: ")
