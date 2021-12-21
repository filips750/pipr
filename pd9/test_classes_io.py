from classes import Database, Person
from classes_io import (
    read_database_from_file,
    write_database_to_file,
    write_ancestors_tree_yaml,
    MalformedCSVError,
    CSVDataError,
)

from datetime import date
from io import StringIO
import pytest



def test_read_database_from_file():
    handle = StringIO(
        "id,name,birth_date,father_id,mother_id\n"
        + "1,Jan Kowalski,1960-06-01,,\n"
        + "2,Anna Wiśniewska,1962-01-06,,\n"
        + "3,Adam Kowalski,1984-03-03,1,2\n"
    )

    database = read_database_from_file(handle)

    assert len(database.people()) == 3

    assert database.get_person_by_id("1").id() == "1"
    assert database.get_person_by_id("1").name() == "Jan Kowalski"
    assert database.get_person_by_id("1").birth_date() == date.fromisoformat(
        "1960-06-01"
    )
    assert database.get_person_by_id("1").father() is None
    assert database.get_person_by_id("1").mother() is None

    assert database.get_person_by_id("2").id() == "2"
    assert database.get_person_by_id("2").name() == "Anna Wiśniewska"
    assert database.get_person_by_id("2").birth_date() == date.fromisoformat(
        "1962-01-06"
    )
    assert database.get_person_by_id("2").father() is None
    assert database.get_person_by_id("2").mother() is None

    assert database.get_person_by_id("3").id() == "3"
    assert database.get_person_by_id("3").name() == "Adam Kowalski"
    assert database.get_person_by_id("3").birth_date() == date.fromisoformat(
        "1984-03-03"
    )
    assert database.get_person_by_id("3").father() is database.get_person_by_id("1")
    assert database.get_person_by_id("3").mother() is database.get_person_by_id("2")


def test_read_database_from_file_invalid_field():
    handle = StringIO(
        "id,names,birth_date,father_id,mother_id\n"
        + "1,Jan Kowalski,1960-06-01,,\n"
        + "2,Anna Wiśniewska,1962-01-06,,\n"
        + "3,Adam Kowalski,1984-03-03,1,2\n"
    )

    with pytest.raises(MalformedCSVError):
        read_database_from_file(handle)


def test_read_database_from_file_invalid_parent_id():
    handle = StringIO(
        "id,name,birth_date,father_id,mother_id\n"
        + "1,Jan Kowalski,1960-06-01,,\n"
        + "2,Anna Wiśniewska,1962-01-06,,\n"
        + "3,Adam Kowalski,1984-03-03,1,4\n"
    )

    with pytest.raises(CSVDataError):
        read_database_from_file(handle)


def test_write_database_to_file():
    handle = StringIO()

    person1 = Person("1", "Jan Kowalski", "1960-06-01")
    person2 = Person("2", "Anna Wiśniewska", "1962-01-06")
    person3 = Person("3", "Adam Kowalski", "1984-03-03", person1, person2)

    write_database_to_file(handle, Database([person1, person2, person3]))
    assert handle.getvalue().splitlines() == [
        "id,name,birth_date,father_id,mother_id",
        "1,Jan Kowalski,1960-06-01,,",
        "2,Anna Wiśniewska,1962-01-06,,",
        "3,Adam Kowalski,1984-03-03,1,2",
        "",
    ]


def test_ancestors_to_yaml():
    data = """id,name,birth_date,father_id,mother_id
1,Jan Kowalski,1960-06-01,,
2,Anna Wiśniewska,1962-01-06,,
3,Adam Kowalski,1984-03-03,1,2
4,Janina Nowak,1980-12-24,,
5,Stefan Kowalski,2004-07-28,3,4
"""
    handle1 = StringIO(data)

    database = read_database_from_file(handle1)
    person = database.get_person_by_id('5')
    print(database.ancestors_tree(person))

    with open('ancestors_tree.yaml', 'w') as handle:
        write_ancestors_tree_yaml(handle, database, person)
