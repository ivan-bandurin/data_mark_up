from tkinter import *
import sys
root = Tk()
root.minsize(width=500, height=400) 

l_1 = Label()
l_1.pack(side=LEFT, pady=15)
l = Label()
l.pack(side=LEFT, pady=15)

# Начало счетчика строк
if int(sys.argv[1]) == 0:
    x = int(sys.argv[1])
else:
    x = int(sys.argv[1]) + 1
# Линия, выведенная на экран
showed_line = []

# Функция get_line получает на вход номер строки файла и вовзращает ее в виде чистой декодированной строки
def get_line(n):
    with open('zakaz.csv', 'rb') as fp:
        for i, line in enumerate(fp):
            if i < n:
                continue
            elif i > n:
                break
            return line[:-3].decode('utf_8')

# Функция обработки нажатия клавиши "Пробел"
# При нажатии клавиши пробел на экран выводится первая строка обрабатываемого набора данных
def bs(event):
    global x
    global showed_line
    l_1.config(text = str(x))
    showed_line = get_line(x)    
    l.config(text = showed_line)

# Функция обработки нажатия клавиши "Стрелка влево" 
# При нажатии клавиши пробел на экран строка помечается как не содержащая персональных данных
def bl(event):
    global x
    global showed_line
    # showed_line = get_line(x)
    res = open('marked.csv', 'a')
    res.write(showed_line.replace(';',':') + ';' + "0" + '\n')
    res.close()    
    x += 1
    showed_line = get_line(x)
    l_1.config(text = str(x))
    l.config(text = showed_line)

# Функция обработки нажатия клавиши "Стрелка вправо" 
# При нажатии клавиши пробел на экран строка помечается как содержащая персональных данных 
def br(event):
    global x
    global showed_line
    # showed_line = get_line(x)
    res = open('marked.csv', 'a')
    res.write(showed_line.replace(';',':') + ';' + "1" + '\n')
    res.close()    
    x += 1
    showed_line = get_line(x)
    l_1.config(text = str(x))
    l.config(text = showed_line)

# Функция вывода номера последней размеченной строки
# При нажатии клавиши N выводится номер последней строки, которой присвоили отметку
# После нажатия клавиши "Пробел" возращается необработанная строка
def bn(event):
    global x
    l_1.config(text = 'Number of last marked string - ' + str(x-1))
    l.config(text = get_line(x-1))

root.bind('<Left>', bl)
root.bind('<Right>', br)
root.bind('<space>', bs)
root.bind('n', bn)

help_text = ('For start press "Space"\n' + 
             'For marking up as data including personal information press "Right"\n' +
             'For marking up as data NOT including personal information press "Left"\n' +
             'For showing number of last marked string press "n"')
l_1.config(text = help_text)


root.mainloop()
 




