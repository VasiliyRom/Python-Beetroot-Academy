name = input('Введіть Ім\'я: ')
name = name.strip(' ')
while True:
    operator = input(f'''{name.capitalize()}, виберіть операцію зі списку наступних:
    Додавання___________________________(1)
    Віднімання__________________________(2)
    Множення____________________________(3)
    Ділення_____________________________(4)
    Ділення націло______________________(5)
    Остача від цілочисельного ділення___(6)
    Піднести число в степінь____________(7)
    Округлити число_____________________(8)
    Знайти квадрат числа________________(9)
    Випадкове число від x до y)_________(10)
    Конвертер валют_____________________(11)
    Вийти з програми____________________(exit)\n''')
    
    if operator == '1':
        x = input('x= ')
        x = x.strip(' ')
        y = input('y= ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x} + {y} = {float(x) + float(y)}')
    
    elif operator == '2':
        x = input('x= ')
        x = x.strip(' ')
        y = input('y= ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x} - {y} = {float(x) - float(y)}')
            
    elif operator == '3':
        x = input('x= ')
        x = x.strip(' ')
        y = input('y= ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x} * {y} = {float(x) * float(y)}')
    
    elif operator == '4':
        x = input('x= ')
        x = x.strip(' ')
        y = input('y= ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            x = float(x)
            y = float(y)
            if y == 0:
                print('На нуль не ділиться') 
            else:
                print(f'{x} / {y} = {x / y}')  
                
    elif operator == '5':
        x = input('x= ')
        x = x.strip(' ')
        y = input('y= ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x} // {y} = {int(x) // int(y)}')       
    
    elif operator == '6':
        x = input('x= ')
        x = x.strip(' ')
        y = input('y= ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x} % {y} = {int(x) % int(y)}')        
   
    elif operator == '7':
        x = input('x= ')
        x = x.strip(' ')
        y = input('В яку степінь: ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x} ^ {y} = {float(x) ** int(y)}')        
    
    elif operator == '8':
        x = input('x= ')
        x = x.strip(' ')
        y = input('кількість знаків після коми: ')
        y = y.strip(' ')        
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'{x}, {y} знаків після коми = {round(float(x), int(y))}')   

    elif operator == '9':
        x = input('x= ')
        if x.isalpha() and y.isalpha():
            print(f'{x} не є числом.')
        else:
            print(f'{x} в квадраті = {int(x) * int(x)}')  
            
    elif operator == '10':
        import random
        x = input('Від: ')
        x = x.strip(' ')
        y = input('До: ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            x = int(x)
            y = int(y)
            com = random.randint(x,y)
            print(com)   
    
    elif operator == '11':
        x = input('Сума: ')
        x = x.strip(' ')
        y = input('Курс: ')
        y = y.strip(' ')
        if x.isalpha() and y.isalpha():
            print(f'{x} або {y} не є числом.')
        else:
            print(f'Отримаєте {float(x) * float(y)}')
            
    elif operator == 'exit' or operator == 'Exit' or operator == 'EXIT' or operator == 'q':
        print(f'До побачення, {name.capitalize()}!')
        break
    else:
        print(f'{operator} - неправильний знак')