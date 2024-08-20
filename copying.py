def copyFtoS_data():
    with open('dataFirstVariant.csv', 'r', encoding = 'utf-8') as f:
        dataFirst = f.readlines()
        dataFirst_list = []
        j = 0
        for i in range(len(dataFirst)):
            if dataFirst[i] == '\n' or i == len(dataFirst) - 1:
                dataFirst_list.append(''.join(dataFirst[j:i+1]))
                j = i+1
        
    print('Доступные записи:')
    for idx, record in enumerate(dataFirst_list, 1):
        print(f"{idx}. {record.strip()}")
    
    line = int(input('Введите номер записи для копирования: '))
    if 1 <= line <= len(dataFirst_list):
        select_line = dataFirst_list[line - 1].strip().split('\n')
    else:
        print("Неверный номер записи. Попробуйте снова.")
    
    with open('dataSecondVariant.csv', 'a', encoding='utf-8') as f:
            f.write(';'.join(select_line) + '\n\n')
    print('Запись успешно скопирована.')

def copyStoF_data():
    with open('dataSecondVariant.csv', 'r', encoding = 'utf-8') as f:
        dataSecond = f.readlines()
    
    print('Доступные записи:')
    for idx, record in enumerate(dataSecond, 1):
        print(f"{idx}. {record.strip()}")
    
    line = int(input('Введите номер записи для копирования: '))
    if 1 <= line <= len(dataSecond):
        select_line = dataSecond[line - 1].strip().split(';')
    else:
        print("Неверный номер записи. Попробуйте снова.")
    
    with open('dataFirstVariant.csv', 'a', encoding='utf-8') as f:
        for item in select_line:
            f.write(item + '\n')
        f.write('\n')
    print('Запись успешно скопирована.')