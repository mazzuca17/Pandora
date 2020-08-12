#
# Name : Pandora
# Author: Matías Mazzuca
# 
#

from tkinter import *
from tkinter import filedialog
from pygame import mixer

class music:
	def __init__(self, ventana):
		ventana.geometry("270x270")
		ventana.title("Pandora")
		ventana.config(bg="black", relief="ridge", bd="1")
		

		Open =  Button(ventana, text = "Abrir", width = 15, bg="white", relief = "ridge", bd="1", command = self.B_Open)
		Open.place(x=60, y=60)
		Play = Button(ventana, text = "Reproducir", width = 15, bg="white", relief = "ridge", bd="1", command = self.B_Play)
		Play.place(x=60, y=90)
		Pause = Button(ventana, text = "Pausa", width = 15, bg="white", relief = "ridge", bd="1", command = self.B_Pause)
		Pause.place(x=60, y = 120)
		Stop = Button(ventana, text = "Detener", width = 15, bg="white", relief = "ridge", bd="1", command = self.B_Stop)
		Stop.place(x=60, y=150)

		self.open_music = False
		self.play_music = False

	def B_Open(self):
		self.open_music = filedialog.askopenfilename()
	def B_Play(self):
		if self.open_music:
			mixer.init()
			mixer.music.load(self.open_music)
			mixer.music.set_volume(0.7)
			mixer.music.play()
	def B_Pause(self):
		if self.play_music:
			mixer.music.pause()
			self.play_music = False
		else:
			mixer.music.unpause()
			self.play_music = True
	def B_Stop(self):
		mixer.music.stop()



ventana = Tk()
imagen = PhotoImage(file= "logo.png")
Label(ventana, image = imagen).place(x=60, y = 0)
music(ventana)
ventana.mainloop()