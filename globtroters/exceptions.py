class WrongColorName(Exception):
    def __init__(self) -> None:
        print("The color isn't on list")


class ColorInConfigIsNotATuple(Exception):
    def __init__(self, color) -> None:
        print(f"{color} must be a tuple")


class NameCannotBeEmpty(Exception):
    def __init__(self) -> None:
        print("Name cannot be empty! Please enter your name")


class ConfigFileError(Exception):
    def __init__(self, wrong_parameter_name) -> None:
        print(f'{wrong_parameter_name} is wrong type')


class MissingArgumentsConfigFile(Exception):
    def __init__(self) -> None:
        print('One or more arguments in config file are missing. Please check if all arguments are correctly')
