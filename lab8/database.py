from model_io import read_from_file, write_to_file


class PersonFileNotFound(FileNotFoundError):
    pass


class PersonPermissionErorr(PermissionError):
    pass


class PersonPathIsADirectoryError(IsADirectoryError):
    pass


class Database:
    def __init__(self):
        self.people = []

    def load_from_file(self, path):
        try:
            with open(path, 'r') as file_handle:
                self._people = read_from_file(file_handle)
        except FileNotFoundError as e:
            raise PersonFileNotFound('Could not open person database')

        except PermissionError as e:
            raise PersonPermissionErorr('You do not have permissions to open database')

        except IsADirectoryError as e:
            raise PersonPathIsADirectoryError('Can only work on files')

    def save_to_file(self, path):
        write_to_file(path, self)
