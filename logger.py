from data_create import name_data, surname_data, phone_data, adres_data
from copying import copyFtoS_data, copyStoF_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adres = adres_data()
    var = int(input(f"Формат ввода данных\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{adres}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{adres}\n"
    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input('Введите число: '))
        
    if var == 1:
        with open('dataFirstVariant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{adres}\n\n")
    elif var == 2:
        with open('dataSecondVariant.csv', 'a', encoding = 'utf-8') as f:
            f.write(f"{name};{surname};{phone};{adres}\n\n")

def export_data():
    print('Вывожу данные из 1 файла: \n')
    with open('dataFirstVariant.csv', 'r', encoding = 'utf-8') as f:
        dataFirst = f.readlines()
        dataFirst_list = []
        j = 0
        for i in range(len(dataFirst)):
            if dataFirst[i] == '\n' or i == len(dataFirst) - 1:
                dataFirst_list.append(''.join(dataFirst[j:i+1]))
                j = i
        print(''.join(dataFirst_list))        
    
    print('Вывожу данные из 2 файла: \n')
    with open('dataSecondVariant.csv', 'r', encoding = 'utf-8') as f:
        dataSecond = f.readlines()
        print(*dataSecond)
    
def copy_data():
    print('Из какого файла копировать?\n 1 - dataFirstVariant\n 2 - dataSecondVariant')
    sourse = int(input('Введите номер файла: '))
    while sourse != 1 and sourse != 2:
        print('Неверный выбор файла')
        sourse = int(input('Введтие номер файла: '))
            
    if sourse == 1:
        copyFtoS_data()
    elif sourse == 2:
        copyStoF_data()
