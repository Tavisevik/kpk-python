import tkinter
from random import choice, randint
# randint(1, 1000) - достигает от 1 до 100 включительно
# choice(2,5,1) - выбирает из списка

ball_initial_number = 20
ball_minimal_radius = 15
ball_maximal_radius = 40
ball_available_colors = ['green', 'blue', 'red', 'gray', '#FF00FF', '#FFFF00']

def click_ball(event):
    """
    Обработчик событий от мышки для игрового холста
    :param event:мышка указывет
     По клику мышкой нужно удалять тот объект, на который
     А также засчитывать его очки
    :return:
    """
    obj = canvas.find_closest(event.x, event.y)
    #print(dir(obj)) # печатает номер объекта при создании
    #if obj['x']
    #print(canvas.coords(obj)
    x1, y1, x2, y2 = canvas.coords(obj)
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete(obj)
        #FIXME: нужно учесть объект в очках
        create_random_ball()

def move_all_balls(event):
    """
    передвигат все шарики на чуть-чуть
    :return:
    """
    for obj in canvas.find_all():
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        canvas.move(obj, dx, dy)

def create_random_ball():
    """
    создает шарик в случайном месте игрового холста
    шарик не выходит за границу тгрового поля
    :return:
    """
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0, int(canvas['width'])-1-2 * R)
    y = randint(0, int(canvas['width'])-1-2 * R)
    canvas.create_oval(x,y,x+2*R, y+2*R, width=1, fill=random_color())

def random_color():
    """
    :return: случайный цвет из некоторого набора цветов
    """
    return choice(ball_available_colors)

def init_ball_catch_game():
    """
     Создает необхоимое для игры количство шариков,по которым нужно будет кликать

     """
    for i in range(ball_initial_number):
        create_random_ball()


def init_main_window():
    """
    Инициализация главного окна
        :return:
    """
    global root, canvas
    root  = tkinter.Tk()
    canvas = tkinter.Canvas(root, background='white', width=400, height=400)
    canvas.bind('<Button>', click_ball)
    canvas.bind('<Motion>', move_all_balls)
    canvas.pack()

if __name__ == "__main":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
    print("Заходите поиграть еще!")

