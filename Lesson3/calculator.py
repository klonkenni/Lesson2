

def calculator(val):
    val = val.replace(" ", "")
    first_value_is_negative = False

    # Check if the first number is negative
    if val[:1] == "-":
        first_value_is_negative = True
        val = val[1:]

    if "+" in val:
        val = val.split("+")
        if first_value_is_negative:
            val[0] = -float(val[0])
        result = float(val[0])+float(val[1])
        return result

    if "-" in val:
        val = val.split("-")
        if first_value_is_negative:
            val[0] = -float(val[0])
        result = float(val[0])-float(val[1])
        return result

    if "*" in val:
        val = val.split("*")
        if first_value_is_negative:
            val[0] = -float(val[0])
        result = float(val[0])*float(val[1])
        return result

    try:
        if "/" in val:
            val = val.split("/")
            if first_value_is_negative:
                val[0] = -float(val[0])
            result = float(val[0])/float(val[1])
            return result
    except ZeroDivisionError:
        return ("You can't divide by 0")

    return val