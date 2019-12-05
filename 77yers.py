import datetime

age = input('Введите свой возраст: ')

while age != "+":
    now = datetime.datetime.now()
    data_now = int(now.year)
    range_data = data_now + 77 - int(age)
    if int(age) < 77:
        print(f"Вам испольнится 77 лет в {range_data} году!")
    elif int(age) == 77:
        print(f"Сейчас {data_now} год, и Вам уже 77 лет!")
    else:
        print(f"Вам было 77 лет в {range_data} году!")
    
    print("Введите другой возраст, либо нажмите клавишу '+'")

    age = input('Введите свой возраст: ')

if age == "+":
    print("Программа завершена!")
