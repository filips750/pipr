import datetime
import json


class InvalidPersonError(Exception):
    pass


class MalformedPersonData(Exception):
    pass


class NoPersonWithSuchId(Exception):
    pass


class JsonDataError(Exception):
    pass


class Person:
    def __init__(self, id, name, birth_date, father=None, mother=None):
        self._id = id
        self._name = name
        self._birthdate = birth_date
        self._children = []
        self.set_mother(mother)
        self.set_father(father)

    def set_mother(self, mother):
        if mother:
            self._mother = mother
            mother.add_kid(self)
        else:
            self._mother = None

    def set_father(self, father):
        if father:
            self._father = father
            father.add_kid(self)
        else:
            self._father = None

    def add_kid(self, kid):
        self._children.append(kid)

    def id(self):
        return self._id

    def name(self):
        return self._name

    def birth_date(self):
        return datetime.date.fromisoformat(self._birthdate)

    def children(self):
        return self._children

    def father(self):
        return self._father

    def mother(self):
        return self._mother

    def oldest_sibling(self):
        if self.mother() is None and self.father() is None:
            return None
        oldest_sibling = None
        oldest_date = self.birth_date()
        for child in self.mother().children():
            temp_birthdate = child.birth_date()
            if oldest_date > temp_birthdate:
                oldest_sibling = child
                oldest_date = child.birth_date()
        for child in self.father().children():
            if oldest_date > child.birth_date():
                oldest_sibling = child
                oldest_date = child.birth_date()
        return oldest_sibling


class Database:
    def __init__(self, people=None):
        if people:
            self._people = people
        else:
            self._people = []

    def people(self):
        return self._people

    def add_person(self, person_to_add):
        self._people.append(person_to_add)

    def get_person_by_id(self, id):
        if id is None or id == '':
            return None
        for person in self._people:
            if person.id() == id:
                return person
        raise NoPersonWithSuchId()

    def ancestors_tree(self, person):
        tree = {}
        tree["id"] = person._id
        tree["name"] = person._name
        tree["birth_date"] = person._birthdate
        if person._father:
            tree["father"] = self.ancestors_tree(person._father)
        if person._mother:
            tree["mother"] = self.ancestors_tree(person._mother)
        return tree

    def read_from_json(self, file_handle):
        data = json.load(file_handle)
        try:
            for item in data:
                try:
                    id = item['id']
                    name = item['name']
                    birth_date = item['birth_date']
                    father_id = item['father_id']
                    mother_id = item['mother_id']
                except Exception as e:
                    raise JsonDataError from e
                person = Person(id, name, birth_date, self.get_person_by_id(father_id), self.get_person_by_id(mother_id))
                self._people.append(person)
        except KeyError:
            raise MalformedPersonData()
        return self
