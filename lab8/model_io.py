from model import Person


def read_from_file(file_handle):
    people = []
    file_handle.readline()
    for line in file_handle:
        line = line.rstrip()
        tokens = line.split(',')
        id, name, sex, birth_date = tokens
        person = Person(id, name, sex, birth_date)
        people.append(person)
    return people


def write_to_file(file_handle, people):
    file_handle.write('id,name,sex,birth_date\n')
    for person in people:
        id = person.id()
        name = person.name()
        sex = person.sex()
        birth_date = person.birth_date()
        line = f'{id},{name},{sex},{birth_date}\n'
        file_handle.write(line)
