#currently 1dollar = 83rs
#so u just have to multiply the given USD by 83 to get INR

def convert(dollar):
    converted = dollar*83
    print(f"{dollar} USD = {converted} INR")
    return converted


convert(40)
    