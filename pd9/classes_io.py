from classes import Person, Database
import csv
import yaml
import json


class MalformedCSVError(Exception):
    pass


class MalformedPersonData(Exception):
    pass


class CSVDataError(Exception):
    pass


class InvalidPersonError(Exception):
    pass


def read_database_from_file(handle):
    database = Database([])
    reader = csv.DictReader(handle)
    try:
        for row in reader:
            id = row['id']
            name = row['name']
            birth_date = row['birth_date']
            father_id = row['father_id']
            mother_id = row['mother_id']
            try:
                person = Person(id, name, birth_date, database.get_person_by_id(father_id), database.get_person_by_id(mother_id))
                database.add_person(person)
            except Exception:
                raise CSVDataError(row)
    except KeyError as e:
        raise MalformedCSVError(str(e))
    return database


def write_database_to_file(handle, database):
    writer = csv.DictWriter(handle, ['id', 'name', 'birth_date', 'father_id', 'mother_id'])
    handle.write('id,name,birth_date,father_id,mother_id\n')
    for person in database.people():
        id = person.id()
        name = person.name()
        birth_date = person.birth_date()
        father = person.father()
        mother = person.mother()
        if father is None:
            father_id = ''
        else:
            father_id = father.id()
        if mother is None:
            mother_id = ''
        else:
            mother_id = mother.id()
        writer.writerow({
            'id': id,
            'name': name,
            'birth_date': birth_date,
            'father_id': father_id,
            'mother_id': mother_id
        })
    handle.write('\n')


def write_ancestors_tree_yaml(handle, database, person):
    dictionary = database.ancestors_tree(person)
    yaml.dump(dictionary, stream=handle, allow_unicode=True)


def read_from_json(file_handle, database):
    data = json.load(file_handle)
    for item in data:
        try:
            id = item['id']
            name = item['name']
            birth_date = item['birth_date']
            father_id = item['father_id']
            mother_id = item['mother_id']
            person = Person(id, name, birth_date, database.get_person_by_id(father_id), database.get_person_by_id(mother_id))
        except KeyError as e:
            raise MalformedPersonData('Missing key in file') from e
        except Exception as e:
            raise InvalidPersonError from e
        database._people.append(person)
    return database
