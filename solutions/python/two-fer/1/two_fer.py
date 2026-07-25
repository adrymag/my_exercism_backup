# def two_fer(name):
def two_fer(*args):
    if not args:
        return "One for you, one for me."
    if len(args) == 0:
        return "One for you, one for me."
    name = args[0]
    if name.strip() == "" or name == None:
        name = "you"
    return "One for " + name + ", one for me."

# def two_fer():
#     return "One for you, one for me."