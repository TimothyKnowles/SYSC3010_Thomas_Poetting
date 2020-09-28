from sense_hat import SenseHat
import sense_hat
import time

s = SenseHat()
s.low_light = True

nothing = (0, 0, 0)
pink = (255, 105, 180)


def letter_T():
    P = pink
    O = nothing
    logo = [
        O, P, P, P, P, P, P, O,
        O, P, P, P, P, P, P, O,
        O, O, O, P, P, O, O, O,
        O, O, O, P, P, O, O, O,
        O, O, O, P, P, O, O, O,
        O, O, O, P, P, O, O, O,
        O, O, O, P, P, O, O, O,
        O, O, O, P, P, O, O, O,
    ]
    return logo


def letter_P():
    P = pink
    O = nothing
    logo = [
        O, O, P, P, P, P, O, O,
        O, O, P, P, P, P, P, O,
        O, O, P, P, O, P, P, O,
        O, O, P, P, O, P, P, O,
        O, O, P, P, P, P, O, O,
        O, O, P, P, O, O, O, O,
        O, O, P, P, O, O, O, O,
        O, O, P, P, O, O, O, O,
    ]
    return logo


images = [letter_T, letter_P]
count = 0

while True:
    for event in s.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                s.set_pixels(images[count % len(images)]())
                count += 1
            if event.direction == "down":
                s.set_pixels(images[count % len(images)]())
                count += 1
            if event.direction == "left":
                s.set_pixels(images[count % len(images)]())
                count += 1
            if event.direction == "right":
                s.set_pixels(images[count % len(images)]())
                count += 1

