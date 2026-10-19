"""Script that returns the correct "ohms" given the colors"""

def label(colors):
    """Function that returns the correct "ohms" given the colors"""
    colorlist = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    exponent = 1 * pow(10, colorlist.index(colors[2])) 
    duo = (colorlist.index(colors[0]) * 10) + colorlist.index(colors[1])
    total = exponent * duo
    if total >= 1000000000:
        return str(int(total/1000000000)) + " gigaohms"
    if total >= 1000000:
        return str(int(total/1000000)) + " megaohms"
    if total >= 1000:
        return str(int(total/1000)) + " kiloohms"
    return str(total) + " ohms"
    