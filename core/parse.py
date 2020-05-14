import re

def parse(intput_string, names, separator=",", end=";"):

    types_re = {
        "float": "^[-+]?([0-9]*[\.,][0-9]+|[0-9]+)$",
        "int": "^[0-9]+$",
        "str": "^[a-zA-Z0-9\.,\? ]*$",
    }

    len_data  = len(names)
    splited_string = [string.strip() for string in intput_string.split(separator)]
    elements = []

    assert len_data == len(splited_string), "The lenght of the string and the data does not match"

    for element, type_ in zip(splited_string, names.values()):
        try:
            elements.append(type_(element))
        except:
            print("Error convirtiendo", element, type_)
            elements.append(None)

    return dict(zip(names, elements))