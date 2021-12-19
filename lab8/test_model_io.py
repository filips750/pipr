from model_io import read_from_file, write_to_file
import pytest


def test_read_from_file():
    read_from_file('lab8/people.txt')


def test_read_from_file_not_exists():
    with pytest.raises(FileNotFoundError):
        read_from_file('nonexistant')


def test_read_from_file_directory():
    with pytest.raises(PersonPathIsADirectoryError):
        read_from_file('/')


def test_read_and_write():
    with open ('lab8/people.txt', 'r') as people_txt:
        people = read_from_file(people_txt)
    with open('people_saved.txt', 'w') as people_saved:
        write_to_file(people_saved, people)


test_read_and_write()
