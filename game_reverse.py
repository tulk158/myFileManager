import random


def game_reverse():
    print('Вам нужно загадать число от 1 до 100')
    min_number = 1
    max_number = 100
    result = None

    while result != '=':
        number = random.randint(min_number,max_number)
        print(number)
        result = input('Введите = или < или > \n')
        if result == '>':
            min_number = number + 1
        elif result =='<':
            max_number = number - 1
    print('Победа')


if __name__ == '__main__':
    game_reverse()