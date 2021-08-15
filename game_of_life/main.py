from board import Board

def main():
    user_rows = int(input('HOW MANY ROWS FOR LIFE ??'))
    user_columns = int(input('HOW MANY COLUMNS FOR LIFE ?? '))
    game_of_life_board=Board(user_rows,user_columns)
    game_of_life_board.draw_board()
    user_action =''
    while user_action !='q':
        user_action=input('ENTER(RETURN) TO GIVE LIFE ANOTHER CHANCE//q to QUIT  :')
        if user_action=='':
            game_of_life_board.update_board()
            game_of_life_board.draw_board()
main()

