from tkinter import *
root = Tk()
root.minsize(width=500, height=400) 
x = 0
l_1 = Label()
l_1.pack(side=LEFT, pady=15)
l = Label()
l.pack(side=LEFT, pady=15)

def bl(event):
    global x
    with open('zakaz.csv', 'rb') as fp:
        for i, line in enumerate(fp):
            if i < x:
                continue
            elif i > x:
                break
            target = line[:-3].decode('utf_8')
    res = open('marked.csv', 'a')
    res.write(target.replace(';',':') + ';' + "0" + '\n')
    res.close()    
    x += 1
    with open('zakaz.csv', 'rb') as fp:
        for i, line in enumerate(fp):
            if i < x:
                continue
            elif i > x:
                break
            target = line[:-3].decode('utf_8')
    l_1.config(text = str(x))
    l.config(text = target)
 

 
def br(event):
    global x
    with open('zakaz.csv', 'rb') as fp:
        for i, line in enumerate(fp):
            if i < x:
                continue
            elif i > x:
                break
            target = line[:-3].decode('utf_8')
    res = open('marked.csv', 'a')
    res.write(target.replace(';',':') + ';' + "1" + '\n')
    res.close()    
    x += 1
    with open('zakaz.csv', 'rb') as fp:
        for i, line in enumerate(fp):
            if i < x:
                continue
            elif i > x:
                break
            target = line[:-3].decode('utf_8')
    l_1.config(text = str(x))
    l.config(text = target)

def bs(event):
    global x

    l_1.config(text = str(x))
    with open('zakaz.csv', 'rb') as fp:
        for i, line in enumerate(fp):
            if i < x:
                continue
            elif i > x:
                break
            target = line[:-3].decode('utf_8')
    
    l.config(text = target)



root.bind('<Left>', bl)
root.bind('<Right>', br)
root.bind('<space>', bs)

# with open('zakaz.csv', 'rb') as fp:
#     for i, line in enumerate(fp):
#         if i < x:
#             continue
#         elif i > x:
#             break
#         target = line[:-3].decode('utf_8')

# l_1.config(text = x)
# l.config(text = target)

root.mainloop()
 




