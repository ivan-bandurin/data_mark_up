# python3.9
# data_mark_up_script.py - предназначен для простой разметки данных с делением на два класса

from tkinter import *
from tkinter import filedialog as fd
import sys

root = Tk()
root.minsize(width=500, height=400) 

l_1 = Label()
l_1.pack(side=LEFT, pady=15)
l = Label()
l.pack(side=LEFT, pady=15)


showed_line = []
x = 0
source_file = 'z.csv'
marked_file = 'marked.csv'

#устанавливает номер первой строки и выводит ее
def set_counter():
    global x
    global showed_line
    try:
        x = int(counter_input.get())
    except:
        x = 0
    
    l_1.config(text = str(x))
    showed_line = get_line(x)    
    l.config(text = showed_line)

# Функция get_line получает на вход номер строки файла и вовзращает ее в виде чистой декодированной строки
def get_line(n):
    global source_file
    with open(source_file, 'rb') as fp:
        for i, line in enumerate(fp):
            if i == n:
                return line[:-3].decode('utf_8')



# Функция обработки нажатия клавиши "Стрелка влево" 
# При нажатии клавиши пробел на экран строка помечается как 0
def bl(event):
    global marked_file
    global x
    global showed_line
    res = open(marked_file, 'a')
    res.write(showed_line.replace(';',':') + ';' + "0" + '\n')
    res.close()    
    x += 1
    showed_line = get_line(x)
    l_1.config(text = str(x))
    l.config(text = showed_line)

# Функция обработки нажатия клавиши "Стрелка вправо" 
# При нажатии клавиши пробел на экран строка помечается как 1
def br(event):
    global marked_file
    global x
    global showed_line

    res = open(marked_file, 'a')
    res.write(showed_line.replace(';',':') + ';' + "1" + '\n')
    res.close()    
    x += 1
    showed_line = get_line(x)
    l_1.config(text = str(x))
    l.config(text = showed_line)


# Функция вывода номера последней размеченной строки
# После нажатия клавиши "Пробел" возращается необработанная строка
def bn():
    global marked_file
    with open(marked_file, 'r') as f:
        n = 0
        res = ''
        for line in f:
            n += 1
            res = line
    l_1.config(text = 'Number of last marked string - ' + str(n-1))
    l.config(text = line)
    counter_input.delete(first=0, last=END)
    counter_input.insert(END, str(n))

def get_source_file():
    global source_file
    source_file = fd.askopenfilename()

def get_marked_file():
    global marked_file
    marked_file = fd.askopenfilename() 

counter_input = Entry(root, width=5)
counter_button = Button(root, text='set line', command=set_counter)
last_marked = Button(root, text='get last marked string', command=bn)

read_source_file = Button(root, text='open source file', command=get_source_file)
read_marked_file = Button(root, text='read marked file ', command=get_marked_file)

counter_button.place(x=20, y=20)
counter_input.place(x=90, y=23)
last_marked.place(x=20, y=50)
read_source_file.place(x=250, y=20)
read_marked_file.place(x=250, y=50)
root.bind('<Left>', bl)
root.bind('<Right>', br)


help_text = ('For start press "set line"\n' + 
             'For marking up as 1 press "Right"\n' +
             'For marking up as 0 press "Left"\n')
l_1.config(text = help_text)


root.mainloop()
 




