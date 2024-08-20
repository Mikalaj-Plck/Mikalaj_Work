from logger import input_data, export_data, copy_data

def interface():
    print("Бот-справочник. \n 1 - Запись данных \n 2 - Вывод данных \n 3 - Копирование данных")
    command = int(input('Введите число: '))
    
    while command != 1 and command != 2 and command != 3:
        print('Неправильный ввод')
        command = int(input('Введите число: '))
    if command == 1:
        input_data()
    elif command == 2:
        export_data()
    elif command == 3:
        copy_data()