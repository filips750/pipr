import sys
import argparse
from random import choice, randint
from passwordgenerator_exceptions import LenghtMustBeAnInteger

def pick_words_to_password(path, number_of_words, min_length, max_length):
    all_words_list = []
    choosen_words = []
    end_list = []
    with open(path, 'r') as handle:
        all_words = handle.readlines()
    for line in all_words:
        if line[-1:] == '\n':
            line = line[:-1]
        temp_list = line.split(',')
        for word in temp_list:
            all_words_list.append(word)
    try:
        for word in all_words_list:
            if min_length <= len(word) <= max_length:
                choosen_words.append(word)
        for number in range(number_of_words):
            choosen_word = choice(choosen_words)
            choosen_words.remove(choosen_word)
            end_list.append(choosen_word)
    except(TypeError):
        raise LenghtMustBeAnInteger
    return end_list


def create_password(separator, padding_digits, padding_symbol, padding_symbol_number, words):
    word_part = ''
    word_part = word_part + separator
    symbols = padding_symbol*padding_symbol_number
    first_digits = make_digits(padding_digits)
    last_digits = make_digits(padding_digits)
    for word in words:
        word_part = word_part + word + separator
    return str(symbols + first_digits + word_part + last_digits + symbols)


def create_passwords(separator, padding_digits, padding_symbol, padding_symbol_number, password_number, path, number_of_words, min_length, max_length):
    passwords = []
    for iterator in range(password_number):
        words = pick_words_to_password(path, number_of_words, min_length, max_length)
        passwords.append(create_password(separator, padding_digits, padding_symbol, padding_symbol_number, words))
    return str(passwords)


def make_digits(padding_digits):
    digits_to_return = ''
    for iterator in range(padding_digits):
        digits_to_return = digits_to_return + str(randint(0, 9))
    return str(digits_to_return)




def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('--possible_separators')
    parser.add_argument('--padding_digits')
    parser.add_argument('--padding_symbols_number')
    parser.add_argument('--possible_padding_symbols')
    parser.add_argument('--words_number')
    parser.add_argument('--minimal_word_length')
    parser.add_argument('--maximal_word_length')
    parser.add_argument('--generated_passwords')
    args = parser.parse_args(arguments[1:])
    if args.possible_separators:
        separator = choice(args.possible_separators)
    min_word = args.minimal_word_length
    max_word = args.maximal_word_length
    words_number = args.words_number
    padding_digits = args.padding_digits
    padding_symbol = choice.args.padding_symbol
    padding_symbol_number = args.padding_symbols_number
    password_number = args.generated_passwords
    path = 'words.txt'
    print(create_passwords(separator, padding_digits, padding_symbol, padding_symbol_number, password_number, path, words_number, min_word, max_word))


if __name__ == '__main__':
    main(sys.argv)

