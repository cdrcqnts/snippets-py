def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")


# colorize("Hello", "red")
# colorize(1, "red")

# try:
# except:
def get_value_from_dict(d, key):
    try:
        return d[key]
    except KeyError:
        return None


d = {"name": "Slicky"}

# print(get_value_from_dict(d, "nam"))

# try:
# except:
# else:
# finally:


def get_a_number():
    while True:
        try:
            num = int(input("please enter a number: "))
        except ValueError:
            # try not successful
            print("That's not a number!")
        else:
            # try successful
            print("Good job, you entered a number!")
            break
        finally:
            # runs after try in any case
            print("RUNS NO MATTER WHAT!")


def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Don't divide by zero please.")
    except TypeError as err:
        print("a and b must be of type int or float.")
        print(err)
    else:
        print(f"{a} divided by {b} is {result}")


print(divide(1, 2))
print(divide(1, 0))
