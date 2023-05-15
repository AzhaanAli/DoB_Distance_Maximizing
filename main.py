"""
Okay, for context, the inspiration for this project came from my boredom at work.

While carding adults for alcohol, I noticed that there was a huge standard deviation in
the distance my fingers had to travel while typing their date of birth into the keypad.

Quickly, I began to wonder which birthdate(s) would result in my fingers to travel
the MOST distance, and so that is exactly what this program seeks to uncover.

______________________________________________________________________________

COMPONENTS OF THE PROBLEM:

- My keypad at work is organized as follows:
    1  2  3
    4  5  6
    7  8  9
       0

- Dates follow a hard format.
    - Formatted month, day, year, for example like '04132003' representing April 13th, 2003.
    - The month and day are always two-digit numbers. If the number is only a digit, a zero will be added to the front.

- I will define the net distance traveled for a date to be the distance one fingertip must travel to each
  consecutive number in the date from beginning to last.

"""

# Coordinate representation of the numbers on the keypad.
COORDINATES = {
    1: (0, 0),  2: (1, 0),  3: (2, 0),
    4: (0, 1),  5: (1, 1),  6: (2, 1),
    7: (0, 2),  8: (1, 2),  9: (2, 2),
                0: (1, 3),
}


# Takes in two keypad numbers as input, and returns an integer representing the distance squared.
# Taking the square root to get a number representing normal euclidean distance is unnecessary.
# This is because if d_1 > d_2, then d_1^2 > d_2^2, making the squares just as good of a metric.
def distance(a, b):
    a = COORDINATES[int(a)]
    b = COORDINATES[int(b)]

    # Pythagorean formula.
    # distance^2 = (x_1 - x_2)^2 + (y_1 - y_2)^2
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy


# Sums up the distance between numbers in a date.
def date_distance(date):
    d = 0
    for i in range(0, 7):
        d += distance(date[i], date[i + 1])
    return d


# Returns dates with the highest distance value.
def get_best_dates():
    # Keep track of the highest distance as well as the date(s) with that distance.
    best_score = 0
    best_dates = []

    # Permute to all dates.
    for m in range(1, 13):
        for d in range(1, 32):
            for y in range(1940, 2003):

                # Translate m, d, and y into one properly formatted date string and log it's score.
                date = str(m).zfill(2) + str(d).zfill(2) + str(y)
                score = date_distance(date)

                # If a new highest distance is found, clear tracker variables and fill them with the new dates found.
                if score > best_score:
                    best_score = score
                    best_dates = [date]

                # If there's a tie, add the date to the list of current bests.
                elif score == best_score:
                    best_dates.append(date)

    # Return the finished list of best dates.
    return best_dates


# Finally, print all dates of the highest distance.
# These dates ended up to be 10/10/1973 and 10/30/1973!
for date in get_best_dates():
    print(date)
