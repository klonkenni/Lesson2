
def calculator(string):
    string = string.replace(" ", "")
    parts = string.split("+")

    for plus in range(len(parts)):
        if "-" in parts[plus]:
            parts[plus] = parts[plus].split("-")


    print(parts)


if __name__ == "__main__":
    calculator("10 + 2 * 3 - 4  + 1 / 2")

