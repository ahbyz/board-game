"""4*4 board game pc vs user
    Each cell on the board has 4 properties:
    black or white
    tall or short
    square or round
    hollow or solid
"""
import copy
import random

combinations = {"BTSH", "BTSS", "BTRH", "BTRS", "BSSH", "BSSS", "BSRH", "BSRS", "WTSH", "WTSS", "WTRH", "WTRS", "WSSH",
                "WSSS", "WSRH", "WSRS"}
default = ["E", "E", "E", "E"]
row1 = copy.deepcopy(default)
row2 = copy.deepcopy(default)
row3 = copy.deepcopy(default)
row4 = copy.deepcopy(default)
board = [row1, row2, row3, row4]
coordinates = {"0 0", "0 1", "0 2", "0 3", "1 0", "1 1", "1 2", "1 3", "2 0", "2 1", "2 2", "2 3", "3 0", "3 1", "3 2",
               "3 3"}
pieces_on_board = []
occupied_coords = []
available = list(combinations)
free_coords = list(coordinates)

"""
class Pieces:
    def __init__(self):
        self.black = self.tall = self.square = self.hollow = self.x = self.y = 0
        self.word = ""
        self.coord = ""

    def hold_values(self, entry, coords):
        if entry[0] == "B":
            self.black = 1
        else:
            self.black = 0
        if entry[1] == "T":
            self.tall = 1
        else:
            self.tall = 0
        if entry[2] == "S":
            self.square = 1
        else:
            self.square = 0
        if entry[3] == "H":
            self.hollow = 1
        else:
            self.hollow = 0
        self.x = int(coords[0])
        self.y = int(coords[2])
        self.word = entry
        self.coord = coords
"""


def get_piece():
    name = input("Pick a piece: ")
    if name in combinations:
        if name not in pieces_on_board:
            return name
        else:
            print("Piece on the board!")
            return get_piece()
    else:
        print("No such piece!")
        return get_piece()


def get_pc_piece():
    for items in pieces_on_board:
        if items in available:
            available.remove(items)
    return random.choice(available)


def get_pc_coords():
    for item in occupied_coords:
        if item in free_coords:
            free_coords.remove(item)
    return random.choice(free_coords)


def get_coords():
    coords = input("Pick coords: ")
    print("")
    if coords in coordinates:
        if coords not in occupied_coords:
            return coords
        else:
            print("Coords are occupied!")
            return get_coords()
    else:
        print("Coordinate not in index range!")
        return get_coords()


def place_unique_piece(input_piece, input_coords):
    pieces_on_board.append(input_piece)
    occupied_coords.append(input_coords)
    x1 = int(input_coords[0])
    y = int(input_coords[2])
    new = board[x1]
    new[y] = input_piece
    board[x1] = new
    for lines in board:
        print(" ".join(lines))
    print("")


def check_win() -> bool:
    #   check horizontal lines

    for i in range(4):
        if "E" not in board[i]:
            for j in range(4):
                if(
                    (board[i][0][j] == board[i][1][j])
                    & (board[i][1][j] == board[i][2][j])
                    & (board[i][2][j] == board[i][3][j])
                ):
                    return True

    #   check vertical lines

    for j in range(4):
        for i in range(4):
            new = [board[0][j], board[1][j], board[2][j], board[3][j]]
            if "E" not in new:
                if(
                    (board[0][j][i] == board[1][j][i])
                    & (board[1][j][i] == board[2][j][i])
                    & (board[2][j][i] == board[3][j][i])
                ):
                    return True

    #   check diagonal

    for i in range(4):
        new = [board[0][0], board[1][1], board[2][2], board[3][3]]
        if "E" not in new:
            if(
                (board[0][0][i] == board[1][1][i])
                & (board[1][1][i] == board[2][2][i])
                & (board[2][2][i] == board[3][3][i])
            ):
                return True

    #   check reverse diagonal

    for i in range(4):
        new = [board[0][3], board[1][2], board[2][1], board[3][0]]
        if "E" not in new:
            if(
                (board[0][3][i] == board[1][2][i])
                & (board[1][2][i] == board[2][1][i])
                & (board[3][0][i] == board[2][1][i])
            ):
                return True

    return False


while True:
    new_piece = get_piece()
    new_coords = get_coords()
    place_unique_piece(new_piece, new_coords)
    x = check_win()
    if x:
        print("Game won!")
        break
    if ("E" not in row1) and ("E" not in row2) and ("E" not in row3) and ("E" not in row4):
        print("Game over!")
    print("PC's turn:\n")
    pc_piece = get_pc_piece()
    pc_coords = get_pc_coords()
    place_unique_piece(pc_piece, pc_coords)
    x = check_win()
    if x:
        print("Game won!")
        break
    if ("E" not in row1) and ("E" not in row2) and ("E" not in row3) and ("E" not in row4):
        print("Game over!")
