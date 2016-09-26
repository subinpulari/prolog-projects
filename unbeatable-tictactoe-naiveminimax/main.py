from Tkinter import *
from tkFont import *
from subprocess import Popen,PIPE
import tkMessageBox
"""
Board:
	0-0	1-0	2-0
	0-1	1-1	2-1
	0-2	1-2	2-2
______________________________________

	1 	2	3
	4	5	6
	7	8	9
"""
class game_canvas:
	def __init__(self,master):
		self.w = Canvas(master,height=600,width=600,background="black")
		self.w.pack()
		self.board = [[0 for x in range(3)] for y in range(3)]
		"""myfont = Font(size="80")
		t = self.w.create_text(300,300,text="Play",fill="white",activefill="red",font=myfont)
		self.w.tag_bind(t,"<1>",self.start_game)"""
		self.start_game()

	def start_game(self):
		self.clear_canvas()
		self.w.create_line(0,200,600,200,fill="white",width=4)
		self.w.create_line(0,400,600,400,fill="white",width=4)
		self.w.create_line(200,0,200,600,fill="white",width=4)
		self.w.create_line(400,0,400,600,fill="white",width=4)
		self.w.create_line(0,0,600,600,fill="white",width=4)
		self.w.create_line(0,0,0,600,fill="white",width=4)
		self.w.create_line(0,600,600,600,fill="white",width=4)
		self.w.create_line(600,0,600,600,fill="white",width=4)
		self.w.create_rectangle(0, 198, 198, 0, fill="black",activefill="red")
		self.w.create_rectangle(202, 198, 398, 0, fill="black",activefill="red")
		self.w.create_rectangle(402, 198, 598, 0, fill="black",activefill="red")
		self.w.create_rectangle(0,202, 198, 398, fill="black",activefill="red")
		self.w.create_rectangle(202, 202, 398, 398, fill="black",activefill="red")
		self.w.create_rectangle(402, 202, 598, 398, fill="black",activefill="red")
		self.w.create_rectangle(0, 402, 198, 598, fill="black",activefill="red")
		self.w.create_rectangle(202, 402, 398, 598, fill="black",activefill="red")
		self.w.create_rectangle(402, 402, 598, 598, fill="black",activefill="red")
		self.game_loop()
		self.x = PhotoImage(file="x.gif")
		self.o = PhotoImage(file="o.gif")
		self.filled=0

	def drawn(self):
		if self.filled==9:
			return True
		else:
			return False

	def owins(self):
		if (((self.board[0][0]==1)and(self.board[0][1]==1)and(self.board[0][2]==1)) or ((self.board[1][0]==1)and(self.board[1][1]==1)and(self.board[1][2]==1)) or ((self.board[2][0]==1)and(self.board[2][1]==1)and(self.board[2][2]==1)) or ((self.board[0][0]==1)and(self.board[1][0]==1)and(self.board[2][0]==1)) or ((self.board[0][1]==1)and(self.board[1][1]==1)and(self.board[2][1]==1)) or ((self.board[0][2]==1)and(self.board[1][2]==1)and(self.board[2][2]==1)) or ((self.board[0][0]==1)and(self.board[1][1]==1)and(self.board[2][2]==1)) or ((self.board[0][2]==1)and(self.board[1][1]==1)and(self.board[2][0]==1))):
			return True
		else:
			return False

	def xwins(self):
		if (((self.board[0][0]==2)and(self.board[0][1]==2)and(self.board[0][2]==2)) or ((self.board[1][0]==2)and(self.board[1][1]==2)and(self.board[1][2]==2)) or ((self.board[2][0]==2)and(self.board[2][1]==2)and(self.board[2][2]==2)) or ((self.board[0][0]==2)and(self.board[1][0]==2)and(self.board[2][0]==2)) or ((self.board[0][1]==2)and(self.board[1][1]==2)and(self.board[2][1]==2)) or ((self.board[0][2]==2)and(self.board[1][2]==2)and(self.board[2][2]==2)) or ((self.board[0][0]==2)and(self.board[1][1]==2)and(self.board[2][2]==2)) or ((self.board[0][2]==2)and(self.board[1][1]==2)and(self.board[2][0]==2))):
			return True
		else:
			return False

	def get_board_state(self):
		s="["
		start=1;
		for i in range(3):
			for j in range(3):
				if(self.board[i][j]==1):
					if not(start):
						s=s+","
					else:
					 	start=0
					s=s+"o/"+str(i)+"/"+str(j)
				if(self.board[i][j]==2):
					if not(start):
						s=s+","
					else:
					 	start=0
					s=s+"x/"+str(i)+"/"+str(j)
		s=s+"]"
		return s
			

	def check_game_over(self):		
		if self.drawn():
			tkMessageBox.showinfo("Game Over!","IT'S A DRAW!")
			master.destroy()
		if self.owins():
			tkMessageBox.showinfo("Game Over!","YOU WIN!")
			master.destroy()
		if self.xwins():
			tkMessageBox.showinfo("Game Over!","COMPUTER WINS")
			master.destroy()

		

	def handle_game_click(self,e):
		print e.x,e.y
		#on lines, then do nothing
		if(((e.x>=198)and(e.x<=202))or((e.x>=398)and(e.x<=402))or(e.x>=598)):
			return
		if(((e.y>=198)and(e.y<=202))or((e.y>=398)and(e.y<=402))or(e.y>=598)):
			return
		i=e.x/200
		j=e.y/200
		
		if(self.board[i][j]==0):
			self.w.create_image(((2*i)+1)*100,((2*j)+1)*100,image=self.o)
			self.board[i][j]=1
			self.filled+=1

		self.check_game_over()

		print self.get_board_state()

		#get new move and execute
		prolog = Popen(["swipl"],stdin=PIPE,stdout=PIPE)
		result = prolog.communicate("[tictactoe].\nget_next_move("+self.get_board_state()+",x/X/Y,_).\n")[0]
		print "Result=",result
		i=result[result.find("X = ")+4]
		j=result[result.find("Y = ")+4]
		if(i=='Y'):
			i=int(j)
			j=i
		else:
			i=int(i)
			j=int(j)
		self.w.create_image(((2*i)+1)*100,((2*j)+1)*100,image=self.x)
		self.board[i][j]=2
		self.filled+=1

		self.check_game_over()

		

	def game_loop(self):
		self.w.bind("<1>",self.handle_game_click)
		
	

		
			
	def clear_canvas(self):
		self.w.delete("all")
	
	

master = Tk()
master.wm_title("Tic-Tac-Toe")
main = game_canvas(master)

master.mainloop()
master.destroy()

