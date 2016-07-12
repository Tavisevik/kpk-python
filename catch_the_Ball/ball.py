import tkinter

def button1_command():
    """
    по стандарту: по пробелу
    :return:
    """
    """
    :return:
    """
    print('Button 1 default command.')

def print_hello(event):
    print('Hello!')
#    print(dir(event))

#    print(event.char)
#    print(event.delta)
#    print(event.height)
#    print(event.keycode)
#    print(event.keysym)
#    print(event.keysym_num)
    print(event.num)
#    print(event.send_event)
#    print(event.serial)
#    print(event.state)
#    print(event.time)
#    print(event.type)
#    print(event.widget)
#    print(event.width)
    print(event.x, event.x)
    print(event.x_root, event.y_root)
    me = event.widget
    # Что можно сделать с me?
    if me== button1:
        print('Hello!')
    elif me == button2:
        print('Yoe press button 2')
    else:
        raise ValueError

def init_main_window():
    """
    Инициализация главного окна
    создание всех виджетов и их упаковка
    :return:
    """
    """
    :return:
    """
    global root, button1, button2, label, text, scale
    root  = tkinter.Tk()

    # вариант 1 - нажатие только левой кнопкой мыши
    # button1 =tkinter.Button(root, text = "Button 1")
    # button1.bind("<Button-1>", print_hello)
    # button1.pack()

    # вариант 2 - нажатие пробела
    #button1 =tkinter.Button(root, text="Button 1", command=button1_command)
    #button1.pack()

    # вариант 3 -  можно нажимать разными кнопками мыши
    button1 =tkinter.Button(root, text="Button 1", command=button1_command)
    button1.bind("<Button>", print_hello)
#    button1.pack()

    button2 =tkinter.Button(root, text = "Button 2")
    button2.bind("<Button>", print_hello)
    button2['text'] = 'Новый текст'
#    button2.pack()

    variable = tkinter.IntVar(0)

    label = tkinter.Label(root, textvariable=variable)
    scale = tkinter.Scale(root,orient=tkinter.HORIZONTAL,length=300,
          from_=0,to=100,tickinterval=10,resolution=5, variable=variable)
    text = tkinter.Entry(root, textvariable=variable)
#    label.pack()
#    scale.pack()
#    text.pack()
    for obj in button1,button2, label,scale,text:
        obj.pack()

    root.mainloop()


init_main_window()
