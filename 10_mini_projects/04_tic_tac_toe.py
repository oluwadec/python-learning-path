"""04_tic_tac_toe.py - Mini project: a tic-tac-toe game with a winner check."""

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),     # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),     # columns
    (0, 4, 8), (2, 4, 6),                # diagonals
]


def show_board(board: list) -> None:
    for start in (0, 3, 6):
        print(" " + " | ".join(board[start:start + 3]))
        if start < 6:
            print("---+---+---")


def winner(board: list):
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return "Draw" if " " not in board else None


def play(moves: list) -> str:
    """Play a list of board positions (0-8), X first."""
    board = [" "] * 9
    player = "X"
    for position in moves:
        board[position] = player
        result = winner(board)
        if result:
            show_board(board)
            return result
        player = "O" if player == "X" else "X"
    show_board(board)
    return "Game not finished"


if __name__ == "__main__":
    print("Winner:", play([0, 3, 1, 4, 2]))       # X wins the top row
