field = list(range(1,10)) #создаём поле как список с числами от 1 до 9
def field_playing(field): #создаём переменную и присваиваем ей имя
    print ("-" * 15) #нижняя черта
    for i in range(3): #количество повторений цикла
        print ("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|") #боковые столбцы
        print ("-" * 15)#нижняя черта
def take_input(player_token): #take_input принимает параметры player-token, что в свою очередь ставит нас в известность, что игроки ходят по очереди. take-input делает так, что пустая клеточка становится занятой.
    valid = False #Действительный является ошибочным
    while not valid: #Если не занят
        player_answer = input("Куда поставите " + player_token+"? ") #Ответ игрока
        try: #попытка
            player_answer = int(player_answer) #рассматривание введённого числа со стороны игрока
        except: #исключение
            print ("Некорректный ввод.")
            continue #завершить данный цикл
        if player_answer >= 1 and player_answer <= 9: #Открытие нового цикла
            if (str(field[player_answer-1]) not in "XO"): #что нельзя указывать
                field[player_answer-1] = player_token #Отметить на доске то, что указал игрок
                valid = True #Действительный является открытым к записи и такое возможно записать/применить к нашей доске.
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число 1 - 9 для хода.")
def check_win(field): #Проверка игрового поля
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)) #все возможные комбинации для того, чтоб была засчитана победа
    for each in win_coord: #Для каждого при победе:
        if field[each[0]] == field[each[1]] == field[each[2]]: #Присваиваем что победа любого игрока это победа
            return field[each[0]] #Обнулить поле
    return False #Завершение цикла
def main(field): #ну, как же тут обойтись без логики? Добавляем при помощи main логику.
    counter = 0 #счётчик
    win = False 
    while not win:
        field_playing(field)
        if counter % 2 == 0: #Каждый ирок ходит по-очереди
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            temp = check_win(field)#временная переменная
            if temp:
                print (temp, "выиграл!")
                win = True
                break #завершение цикла
        if counter == 9:#случай ничьи
            print ("Ничья!")
            break #завершение цикла
    field_playing(field) #закрытие
main(field) #завершаем нашу логику. Обязательно надо закрыть.
