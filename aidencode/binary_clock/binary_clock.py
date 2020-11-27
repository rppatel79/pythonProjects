from sense_hat import SenseHat

sense = SenseHat()


def decimal_to_binary(n):
    """Function to convert Decimal number to Binary number string"""
    return bin(n).replace("0b", "")


def pad_for_led(n):
    """pads the LHS with 0s"""
    return str(n).zfill(8)

def update_sense_hat(rowId, rowValues, colour):
    """update the sense hate
    Keyword arguments:
    rowId - an integer between 0 < and >8
    rowValues - a string of length of 8.  The values are either 0 or 1
    colours -- an array 3 number representing RBG colours
        """
    for colIdx in range(0, len(rowValues)):
        x = colour if rowValues[colIdx] == "1" else (0, 0, 0)
        sense.set_pixel(colIdx, rowId, x)


def start():
    from datetime import datetime

    clear_colour = (0, 0, 0)
    for rowId in range(0, 8):
        update_sense_hat(rowId, '00000000', clear_colour)

    while True:
        now = datetime.now()

        print("-------------------------------------------")
        print("now =", now)
        print("-------------------------------------------")

        print("month 0=", pad_for_led(decimal_to_binary(now.month)))
        print("day 1=", pad_for_led(decimal_to_binary(now.day)))
        print("hour 2=", pad_for_led(decimal_to_binary(now.hour if now.hour <= 12 else now.hour - 12)))
        print("minute 3=", pad_for_led(decimal_to_binary(now.minute)))
        print("seconds 4=", pad_for_led(decimal_to_binary(now.second)))
        print("microsecond 4=", pad_for_led(decimal_to_binary(int((now.microsecond / 10 ** 6) * 255))))
        print("am/pm 6=", pad_for_led((0 if now.hour < 12 else 1)))

        print("-------------------------------------------")

        # calendar date
        calendar_colour = (0, 0, 255)
        update_sense_hat(0, pad_for_led(decimal_to_binary(now.month)), calendar_colour)
        update_sense_hat(1, pad_for_led(decimal_to_binary(now.day)), calendar_colour)

        # time
        time_colour = (255, 0, 0)
        update_sense_hat(2, pad_for_led(decimal_to_binary(now.hour if now.hour <= 12 else now.hour - 12)), time_colour)
        update_sense_hat(3, pad_for_led(decimal_to_binary(now.minute)), time_colour)
        update_sense_hat(4, pad_for_led(decimal_to_binary(now.second)), time_colour)
        update_sense_hat(5, pad_for_led(decimal_to_binary(int((now.microsecond / 10 ** 6) * 255))), time_colour)
        update_sense_hat(6, pad_for_led((0 if now.hour < 12 else 1)), time_colour)


if __name__ == '__main__':
    start()
