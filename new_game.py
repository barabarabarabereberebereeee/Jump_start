from tkinter import*
import time
import random
root=Tk()
root.title('Jump')
root.resizable(0,0)
root.wm_attributes("-topmost",1)#первое окно
c=Canvas(root,width=500,height=500,highlightthickness=0,bg='black')#убирает рамку
c.pack()
root.update()
class Ball:
    def __init__(self,c,color,p,s):
        self.c=c
        self.id=c.create_oval(10,10,25,25,fill=color)
        self.c.move(self.id,250,250)
        self.x=random.randint(-5,5)
        self.y=-1
        self.height_ball=self.c.winfo_height()
        self.width_ball = self.c.winfo_width()
        self.p=p
        self.death=False
        self.s=s
    def ball_go(self):
        self.c.move(self.id,self.x,self.y)
        jump_start=self.c.coords(self.id)#coords - это функция, которая взвращает координаты объекта в виде списка(x1 y1 x2 y2)
        if self.ball_paddle(jump_start)==True:
            self.y=-2
        if jump_start[1]<=0:
            self.y=2
        if jump_start[3]>=self.height_ball:
            self.death=True
        if jump_start[2]>=self.width_ball:
            self.x=-2  ##;self.width_ball+=10
        if jump_start[0]<=0:
            self.x=2
    def ball_paddle(self,jump_start):
        wall_p = self.c.coords(self.p.id)
        if jump_start[2]>=wall_p[0] and jump_start[0]<=wall_p[2]:
            if jump_start[3]>=wall_p[1] and jump_start[3]<=wall_p[3]:
                self.s.text()
                return True
        return False
class Paddle:
    def __init__(self, c, color):
        self.c = c
        self.id = c.create_rectangle(0, 0, 100, 10, fill=color)
        self.c.move(self.id, 250, 250)
        self.x = 0
        self.width_ball = self.c.winfo_width()
        self.c.bind_all('<KeyPress-Right>',self.right)
        self.c.bind_all('<KeyPress-Left>', self.left)
    def go(self):
        self.c.move(self.id,self.x,0)
        wall = self.c.coords(self.id)  # coords - это функция, которая взвращает координаты объекта в виде списка(x1 y1 x2 y2)
        if wall[2] >= self.width_ball:
            self.x = -0
        if wall[0] <= 0:
            self.x = 0
    def right(self,e):
        self.x=2
    def left(self,e):
         self.x=-2
class Score:
    def __init__(self,c,color):
        self.score=0
        self.c=c
        self.id=c.create_text(450,10,text=self.score,fill=color)
        self.i = c.create_text(400, 10, text='your score', fill=color)
    def text(self):
        self.score+=100
        self.c.itemconfig(self.id,text=self.score)
class Death:
    def __init__(self,c):
        self.c=c
    def death_plaer(self,color):
        self.y = c.create_text(250, 250, text='YOU LOSE', fill=color)
d = Death(c)
s=Score(c,'white')
p=Paddle(c,'white')
b=Ball(c,'white',p,s)
while True:
    if b.death==False:
        p.go()
        b.ball_go()
    else:
        d.death_plaer('red')
        break

    root.update_idletasks()#обновление всех ожидающих событий
    root.update()#обновление всего остального
    time.sleep(0.01)
root.mainloop()