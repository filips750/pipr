import csv
from chess_openings_exceptions import(
   MalformedCSVError
)

def opening_name(game, path):
    my_game = game.split(' ')
    max_move_count = 0
    with open(path, 'r') as handle:
        reader = csv.DictReader(handle)
        try:
            for row in reader:
                move_count = 0
                ECOCode = row['ECOCode']
                Name = row['Name']
                OpeningMoves = row['Opening Moves']
                sequence = OpeningMoves.split(' ')
                iterator = 1
                range_for_loop = min(len(sequence), len(my_game))
                for move_number in range(range_for_loop):
                    if sequence[move_number] == my_game[move_number]:
                        move_count += 1
                        if move_count > max_move_count:
                            max_count_sequence_name = ECOCode
                            max_move_count = move_count
            return max_count_sequence_name
        except Exception:
            MalformedCSVError


def main():
    game = '1 d4 Nf6 2 c4 c5 3 d5 e6 4 Nc3 exd5 5 cxd5 d6 6 e4 g6 7 Nf3 Bg7 8 Be2 O-O'
    print(opening_name(game, 'b4thirdexam/chessopenings/chessopen.csv'))


if __name__ == "__main__":
    main()
