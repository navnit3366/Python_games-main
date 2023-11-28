players_char = ['1', '2', '3']
width = 5
height = 4
table = [['*'] * width for i in range(height)]
 
def draw_field(a: list):
    print("-" * (len(table) * 5 + 1))
    for i in range(len(a)):
        print("|", end="")
        for q in range(len(a[0])):
            print(f" {a[i][q]} |", end="")
        print("\n" + "-" * (len(table) * 5 + 1))
 
print('"Лоскутное одеяло" игра для 3-х игроков')
draw_field(table)
print('Введите координаты хода в через пробел формате: Номер в строке и номер столбца \nШтрафные очки подсчитываются в конце игры')
 
xyv = [[-1, -1], [-1, 0], [-1, 1], \
       [0,  -1],          [0,  1], \
       [1,  -1], [1,  0], [1,  1]  ]
score = [0, 0, 0]
 
 
current_move = 0
while current_move < 20:
        player = current_move % 3
        try:
            x, y = map(int, input(f'Ход игрока {player + 1}: ').split()) 
            # formatted string = f. Тип строк, что улучшает читаемость кода.
        except:
            print('Введите числа в формате: НОМЕР_В_СТРОКЕ НОМЕР_СТОЛБЦА')
            continue
        try:
            if table[y - 1][x - 1] == "*":
                table[y - 1][x - 1] = players_char[player]
            elif table[y - 1][x - 1] != "*":
                print('Поле уже занято')
                current_move -= 1
        except:
            print('Введите числа удовлетворяющие кол-ву строк(1-5) и кол-ву столбцов(1-4)')
            continue
        draw_field(table)
        current_move += 1
 
 
 
for y in range(4):
    for x in range(5):
        for i in range(len(xyv)):
            nx, ny = x + xyv[i][0], y + xyv[i][1]
            if 0 <= nx < 5 and 0 <= ny < 4:
                if table[y][x] == table[ny][nx]:
                    try:
                        score[int(table[y][x]) - 1] += 1
                        print(score)
                    except ValueError:
                        print('Что-то определённо не так(нельзя ставить символы уже на заполненные места)')
                        continue
score = [i // 2 for i in score] #В score штрафые очки удвоены => восстанавливаем баланс дедением на два.
for i in range(len(players_char)):
    print(f'Игрок {i + 1} получил {score[i]} штрафных очков')
 #Рассмотрим все случаи победы
if score[0] < (score[1] and score[2]):
    print(f'Победил 1-ый игрок')
elif score[1] < (score[0] and score[2]):
    print(f'Победил 2-ой игрок')
elif score[2] < (score[0] and score[1]):
    print(f'Победил 3-ий игрок')
elif (score[0] == score[1]) and score[0] < score[2] and score[1] < score[2]:
    print(f'Победили два игрока 1 и 2')
elif (score[1] == score[2]) and score[1] < score[0] and score[2] < score[0]:
    print(f'Победили два игрока 2 и 3 ')
elif (score[0] == score[2]) and score[0] < score[1] and score[2] < score[1]:
    print(f'Победили два игрока 1 и 3')
elif score[0] == score[1] == score[2]:
    print(f'Полная ничья!')
