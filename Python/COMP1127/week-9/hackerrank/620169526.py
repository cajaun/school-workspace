
def check_colour(rgb):
    red, green, blue = rgb

    return "R" if red > green + blue else "G" if green > red + blue else "B" if blue > red + green else "O"

def chirp_range(db):

    return 1 if db <= 25 else 3 if db > 89 else 2 if 35 <= db <= 77 else None

def bird_type(btype, red, green, blue, db):


    type_lookup = {
        ("SCB", "R", 1): "T1",
        ("LSB", "B", 2): "T2",
        ("HB", "G", 3): "T3"
    }
    color = check_colour((red, green, blue))
    chirp = chirp_range(db)


    if (btype, color, chirp) in type_lookup:
        return type_lookup[(btype, color, chirp)]
    elif (btype, color) in [(key[0], key[1]) for key in type_lookup]:
        return "UD"
    return "Unknown"

def closest_match(newbird, blist):
    newBtype, newRed, newGreen, newBlue, newDb = newbird
    newBirdType = bird_type(newBtype, newRed, newGreen, newBlue, newDb)
    
    closest_bird = None
    closest_difference = float('inf')

    for family, btype, red, green, blue, db in blist:
        dbBirdType = bird_type(btype, red, green, blue, db)

    
        if dbBirdType == newBirdType and dbBirdType != "Unknown":
            return family


        pitch_difference = abs(db - newDb)
        if pitch_difference < closest_difference:
            closest_difference = pitch_difference
            closest_bird = family

    return closest_bird