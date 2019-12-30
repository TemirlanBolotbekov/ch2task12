# Нужен синтаксис который выводит индекс буквы F в тексте,самую 1ю и последнюю,если встречается только одна
#выводит одну,если нет то ничего не выводит.

name = (input('Enter your text :'))
name2 = name.count('f')
if name2 > 1:
    print(name.find('f',0))
    print(name.rfind('f',-1))
elif name2 == 1:
    print(name.find('f'))
    