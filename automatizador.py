#!python3
#encoding: utf-8
import pyautogui as py
from tkinter import Tk, Label, Button, Entry, Frame, BOTTOM, LEFT, END, INSERT, Radiobutton, StringVar
from time import sleep

# Autor: RENAN SANTANA DESIDÉRIO
# Skyrim belongs to the Nords!   \o/

class App:

	def __init__(self, master):

		# Array vazio para armazenar os comandos:
		self.dados = []
		# Array para armazenar os frames pro RESET funcionar:
		self.frames = {}
		self.contador = 0

		master.title("Automatizador")
		master.resizable(0,0)
		# Frames Principais ------------------------------------------------------------------
		frameTitle = Frame(master)
		frameTitle.pack()

		framePlay = Frame(master)
		framePlay.pack(side=BOTTOM, fill='x')

		frameInsert = Frame(master)
		frameInsert.pack(side=BOTTOM, fill='x')

		# Label que vai dando 'instruções' ao usuário enquanto ele mexe no bagulho
		# Este também é o Widget que atualmente define o tamanho da janela:
		self.info = Label(frameTitle, text="Clique para adicionar um comando", width=40)
		self.info.pack()

		# Widgets ----------------------------------------------------------------------------
		self.buttonClick = Button(frameInsert, text="Clicar", command= self.addClick, width=8)
		self.buttonWait = Button(frameInsert, text="Esperar", command=self.addTime, width=8)
		self.buttonKey = Button(frameInsert, text="Press. Tecla", command=self.addKey, width=8)
		self.buttonText = Button(frameInsert, text="Digit. Texto", command=self.addText, width=8)
		# ------------------------------------------------------------------------------------
		self.buttonPlay = Button(framePlay, text="Play  =>", command=self.play)
		self.buttonReset = Button(framePlay, text="Reset", command=self.reset)
		self.buttonPlay.bind('<Return>', self.play)
		# Packs ------------------------------------------------------------------------------
		self.buttonClick.pack(side=LEFT, expand=True, fill='x')
		self.buttonWait.pack(side=LEFT, expand=True, fill='x')
		self.buttonKey.pack(side=LEFT, expand=True, fill='x')
		self.buttonText.pack(side=LEFT, expand=True, fill='x')

		self.buttonPlay.pack(fill='x')
		self.buttonReset.pack(fill='x')

# ---------------------------------------------------------------------------------------
	def takePosition(self):		
		# Exibe a posicao atual X e Y do mouse
		pos = py.position()
		pos_x = pos[0]
		pos_y = pos[1]
		# --------------------------------------------
		self.campoX.delete(0, END)
		self.campoY.delete(0, END)
		self.campoX.insert(INSERT, pos_x)
		self.campoY.insert(INSERT, pos_y)
		# Volta o texto inicial de instrução ao usuário
		self.resetInfo()

	def addClick(self, *arg):
		# Adiciona um comando de CLICK
		frameAdicional = self.frameAdicional = Frame(root)
		frameAdicional.pack(fill='x')

		self.label = Label(frameAdicional, text="Position: ", width=10)
		self.campoX = Entry(frameAdicional, width=10)
		self.campoY = Entry(frameAdicional, width=10)
		self.butTake = Button(frameAdicional, text="Save", command=self.takePosition)
		self.label.pack(side=LEFT)
		self.campoX.pack(side=LEFT)
		self.campoY.pack(side=LEFT)
		self.butTake.pack(side=LEFT, fill='x', expand=True)
		self.butTake.focus_force()
		self.salvaFrame(frameAdicional, ('click', (self.campoX, self.campoY)))
		# Atualiza a label de info
		self.info['text'] = "Posicione o mouse na tela e aperte espaço"


	def addTime(self):
		# Adiciona um comando de ESPERA
		frameAdicional = self.frameAdicional = Frame(root)
		frameAdicional.pack(fill='x')

		self.label1 = Label(frameAdicional, text="Wait: ", width=10)
		self.sec = Entry(frameAdicional)
		self.label2 = Label(frameAdicional, text=" seconds")
		self.label1.pack(side=LEFT)
		self.sec.pack(side=LEFT)
		self.label2.pack(side=LEFT)
		self.sec.focus_force()
		self.salvaFrame(frameAdicional, ('time', self.sec))
		# Atualiza a label de info
		self.info['text'] = "Digite o tempo de espera em segundos"

	def addKey(self):
		# Adiciona um comando de PRESSIONAR TECLA
		frameAdicional = self.frameAdicional = Frame(root)
		frameAdicional.pack(fill='x')

		self.valor = StringVar()
		self.label1 = Label(frameAdicional, text="Key: ", width=10)
		# Botao Enter
		self.key1 = Radiobutton(
			frameAdicional,
			indicatoron	= 0,
			text 		= "Enter",
			variable 	= self.valor,
			value 		= 'enter',
			command 	= lambda: self.trocaKey(frameAdicional, self.key1, self.valor.get()))
		# Botao F5
		self.key2 = Radiobutton(
			frameAdicional,
			indicatoron	= 0,
			text 		= "F5",
			variable 	= self.valor,
			value 		= 'f5',
			command 	= lambda: self.trocaKey(frameAdicional, self.key2, self.valor.get()))
		# Botao TAB
		self.key3 = Radiobutton(
			frameAdicional,
			indicatoron	= 0,
			text 		= "TAB",
			variable 	= self.valor,
			value 		= 'tab',
			command 	= lambda: self.trocaKey(frameAdicional, self.key3, self.valor.get()))

		self.label1.pack(side=LEFT)
		self.key1.pack(side=LEFT, expand=True, fill='x')
		self.key2.pack(side=LEFT, expand=True, fill='x')
		self.key3.pack(side=LEFT, expand=True, fill='x')
		# Atualiza a label de info
		self.info['text'] = "Selecione a tecla que será pressionada"

	def trocaKey(self, frame, key, value):
		# Procedimento chamado ao se escolher qual TECLA será pressionada

		# Muda a cor do botão escolhido
		key['bg'] = 'light grey'
		# Desativa todos os botões
		self.key1['state'] = "disabled"
		self.key2['state'] = "disabled"
		self.key3['state'] = "disabled"
		# Chama a função que salva o comando passando a TECLA selecionada
		self.salvaFrame(frame, ('key', value))

	def addText(self):
		# Adiciona um comando de TEXTO
		frameAdicional = self.frameAdicional = Frame(root)
		frameAdicional.pack(fill='x')

		self.label = Label(frameAdicional, text="Text: ", width=10)
		self.text = Entry(frameAdicional)
		self.label.pack(side=LEFT)
		self.text.pack(side=LEFT, expand=True, fill='x')
		self.text.focus_force()
		self.salvaFrame(frameAdicional, ('text', self.text))
		# Atualiza a label de info
		self.info['text'] = "Digite o texto que será digitado"

	def reset(self):
		# Limpa todos os comandos criatos, reseta a porra toda
		try:
			# Limpar todos os frames criados
			self.frameAdicional.destroy()
			for i in self.frames:
				self.frames[i].destroy()
			# Limpar listas:
			self.dados = []
			self.frames = {}
			self.contador = 0
			# Atualiza a label de info
			self.resetInfo()
		except:
			pass

	def salvaFrame(self, frame, campo):
		# Adiciona o frame recém criado ao dicionario, e os campos na lista
		self.contador += 1
		self.frames[self.contador] = frame
		self.dados.append(campo)

	def resetInfo(self):
		# Atualiza a label de info
		self.info['text'] = "Clique para adicionar um comando"

	def play(self, *arg):
		""" Executa a sequencia de macros passada. Verificando primeiro
			a flag sobre o tipo de evento, e depois pegando os valores.
		"""
		for i in self.dados:
			# Verifica a flag para saber qual comando executar:
			if i[0] == 'click':
				try:
					# Clica com o mouse na posição XY da tela
					py.click(int(i[1][0].get()), int(i[1][1].get()))
				except:
					pass

			elif i[0] == 'time':
				# Substitui as vírgulas por pontos
				time = str(i[1].get()).replace(',','.')
				try:
					# Aguarda o tempo digitados
					sleep(float(time))
				except:
					pass

			elif i[0] == 'text':
				try:
					# Digita o que estava no campo
					py.typewrite(str(i[1].get()))
				except:
					pass

			elif i[0] == 'key':
				try:
					# Pressiona a tecla selecionada
					py.typewrite([i[1]])
				except:
					pass

if __name__ == '__main__':
	root = Tk()
	App(root)
	root.mainloop()