# Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.

print("*" * 10, " Старт игры ", "*" * 10)

game_board = list(range(1, 10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token, name):
   valid = False
   while not valid:
      player_answer = input(f"{name}, куда поставим {player_token} ? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(game_board[player_answer-1]) not in "XO"):
            game_board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(game_board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if game_board[each[0]] == game_board[each[1]] == game_board[each[2]]:
          return game_board[each[0]]
   return False

def main(board):
    name_1 = input('Первый игрок, представьтесь: ')
    name_2 = input('Второй игрок, представьтесь: ')
    counter = 0
    win = False
    while not win:
        draw_board(game_board)
        if counter % 2 == 0:
           take_input("X", name_1)
        else:
           take_input("O", name_2)
        counter += 1
        if counter > 4:
           tmp = check_win(game_board)
           if tmp:
                if tmp == "X":
                    print(name_1, "выиграл!")
                else:
                    print(name_2, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(game_board)

main(game_board)

input("Нажмите Enter для выхода!")
