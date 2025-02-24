def p(b):
    """This function is essentially meant to displays the contents
    of a 2D grid(or matrix) in a neatly formatted, table-like structure.
    Each row of the grid is joined with " | ", and "----" acts as a row separator."""
    for r in b:
        print(" | ".join(r))
        print("-" * 5)


def c_w(b, p):
    """This function is crucial for detecting if a player wins in the game of Tic-Tac-Toe.
    It uses efficient logic to check for rows, columns, and diagonals where the same player
    symbol (p) appears consecutively. This function is called repeatedly during the game's
    progression to determine if a win condition has been achieved."""
    for i in range(3):
        if all(b[i][j] == p for j in range(3)) or all(b[j][i] == p for j in range(3)):
            return True
    if all(b[i][i] == p for i in range(3)) or all(b[i][2 - i] == p for i in range(3)):
        return True
    return False


def f(b):
    """This function is a utility to check if the game board b is fully occupied (no empty spaces
    " " exist). It's a concise and efficient use of all() function is combined
    with a generator expression."""
    return all(c != " " for r in b for c in r)


def t():
    """This function controls the entire flow of the Tic-Tac-Toe
    game and uses helper functions for boarding printing, checking
    for wins, and determining if the board is full."""
    b = [[" " for _ in range(3)] for _ in range(3)]
    p = ["X", "O"]
    print("Tic-Tac-Toe Game")
    p(b)
    for t in range(9):
        pl = p[t % 2]
        while 1:
            try:
                r, c = map(int, input(f"P {pl}, row col (0-2): ").split())
                if b[r][c] == " ":
                    b[r][c] = pl
                    break
                else:
                    print("Nope. Again.")
            except:
                print("Wrong. 0-2 pls.")
        p(b)
        if c_w(b, pl):
            print(f"P {pl} wins!")
            return
        if f(b):
            print("Draw!")
            return
    print("Draw!")


def method_name():
    t()
    """The t() line calls the function t."""


method_name()
