from tkinter import *
import time
from Text import Words
Words_list = [i+" " for i in Words.split()]
new_Word_list = [Words_list[i] for i in range(0,50//2-12+1)]
new_Word_list2  =[Words_list[i] for i in range(13+1,29)]
new_Word_list3 = [Words_list[i] for i in range(29+1,40+1)]
new_Word_list4  = [Words_list[i] for i in range(40+1,50)]
class TypingGame:
	def __init__(self,color):
		self.color = color
		self.seconds = 60
		root = Tk()
		root.title("Typing Game ")
		root.config(bg=self.color)
		la = Label(root,text="Welcome to Typing Game",font="helvetica 12 bold",bg=self.color)
		la.place(x=0,y=6)
		b1 = Button(root,text="Start Test",command=self.Start_Test)
		b1.place(x=70,y=50)
		root.geometry('200x200')
		root.maxsize(200,200)
		root.mainloop()
	def Start_Test(self):
		win = Tk()
		win.title("Typing Game")
		win.config(bg=self.color)
		win.geometry("672x600")
		win.maxsize(672,600)
		t1 = Label(win,text=new_Word_list,bg=self.color,font="helvetica 10 bold")
		t1.place(x=0,y=0)
		t2 = Label(win,text=new_Word_list2,bg=self.color,font="helvetica 10 bold")
		t2.place(x=0,y=18)
		t3 = Label(win,text=new_Word_list3,bg=self.color,font="helvetica 10 bold")
		t3.place(x=0,y=36)
		t4 = Label(win,text=new_Word_list4,bg=self.color,font="helvetica 10 bold")
		t4.place(x=0,y=54)
		t5 = Label(win,text="Write The Text above inside this box",bg=self.color,font="helvetica 10 bold")
		t5.place(x=180,y=90)
		input_field = Text(win,width=120,height=16)
		input_field.place(x=0,y=138)
		t = Label(win,text="Timer",bg=self.color,font="helvetica 14 bold")
		t.place(x=300,y=424)
		seconds_label = Label(win,text="",bg=self.color,font="helvetica 12 bold")
		seconds_label.place(x=304,y=448)
		def decrement():
				seconds_label.config(text=self.seconds)
				seconds_label.after(1000,decrement)
				self.seconds = self.seconds - 1
				if self.seconds == 0:
					user_Words = input_field.get(1.0,END)
					user_Words = user_Words.split()
					print(len(user_Words)," Words Per Minute ","\n"+"Speed",len(user_Words)/1)
					win.destroy()

		decrement()
		win.mainloop()
Game = TypingGame('light green')