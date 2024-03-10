# importando tkinter
from tkinter import *
from tkinter import ttk

#cores

cor1 = "#0d0c0d" #preto
cor2 = "#363238" #cinza
cor3 = "#c9bcd1" #branco
cor4 = "#f26680" #red
cor5 = "#3a4dde" #azul
cor6 = "#cfcedb" #cinzinha
cor7 = "#9b6ef5" #roxinho

janela =Tk()
janela.title("Calculadora")
janela.geometry("235x251")
janela.config(bg=cor1)

#frames
frame_tela = Frame(janela, width=235, height=50, bg=cor2)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)



todos_valores = ""

#função
def entrar_valores(Event):
    
    global todos_valores
    
    todos_valores = todos_valores + str(Event)
    
    #valor na tela
    valor_texto.set(todos_valores)

#label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor2, fg=cor3)
app_label.place(x=0,y=0)

#func p/ calculo

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))
    
    #limpar
    
def limpar_tela():
    global todos_valores
    todos_valores=""
    valor_texto.set("")

#button

b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=16, height=2, bg=cor4, relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width=7, height=2, bg=cor7, relief=RAISED, overrelief=RIDGE)
b_2.place(x=176, y=0)
b_3 = Button(frame_corpo, command= lambda: entrar_valores('/'),text="/", width=7, height=2, bg=cor6, fg=cor2, relief=RAISED, overrelief=RIDGE)
b_3.place(x=117, y=0)

b_5 = Button(frame_corpo, command= lambda: entrar_valores('7'), text="7", width=7, height=2, bg=cor6, relief=RAISED, overrelief=RIDGE)
b_5.place(x=0, y=40)
b_6 = Button(frame_corpo, command= lambda: entrar_valores('8'), text="8", width=7, height=2, bg=cor6, relief=RAISED, overrelief=RIDGE)
b_6.place(x=59, y=40)
b_7 = Button(frame_corpo, command= lambda: entrar_valores('9'), text="9", width=7, height=2, bg=cor6, relief=RAISED, overrelief=RIDGE)
b_7.place(x=118, y=40)
b_8 = Button(frame_corpo, command= lambda: entrar_valores('*'), text="*", width=7, height=2, bg=cor7, fg=cor2, relief=RAISED, overrelief=RIDGE)
b_8.place(x=177, y=40)

b_9 = Button(frame_corpo, command= lambda: entrar_valores('4'), text="4", width=7, height=2, bg=cor6, relief=RAISED, overrelief=RIDGE)
b_9.place(x=0, y=80)
b_10 = Button(frame_corpo, command= lambda: entrar_valores('5'), text="5", width=7, height=2, bg=cor6, relief=RAISED, overrelief=RIDGE)
b_10.place(x=59, y=80)
b_11 = Button(frame_corpo, command= lambda: entrar_valores('6'), text="6", width=7, height=2, bg=cor6, relief=RAISED, overrelief=RIDGE)
b_11.place(x=118, y=80)
b_12 = Button(frame_corpo, command= lambda: entrar_valores('-'), text="-", width=7, height=2, bg=cor7, fg=cor2, relief=RAISED, overrelief=RIDGE)
b_12.place(x=177, y=80)

b_13 = Button(frame_corpo, command= lambda: entrar_valores('1'), text="1", width=7, height=2, bg=cor6, relief=RAISED, overrelief=RIDGE)
b_13.place(x=0, y=120)
b_14 = Button(frame_corpo,command= lambda: entrar_valores('2'), text="2", width=7, height=2, bg=cor6, relief=RAISED, overrelief=RIDGE)
b_14.place(x=59, y=120)
b_15 = Button(frame_corpo, command= lambda: entrar_valores('3'), text="3", width=7, height=2, bg=cor6, relief=RAISED, overrelief=RIDGE)
b_15.place(x=118, y=120)
b_16 = Button(frame_corpo, command= lambda: entrar_valores('+'), text="+", width=7, height=2, bg=cor7, fg=cor2, relief=RAISED, overrelief=RIDGE)
b_16.place(x=177, y=120)

b_1 = Button(frame_corpo,command= lambda: entrar_valores('0'), text="0", width=16, height=2, bg=cor6, relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=160)
b_2 = Button(frame_corpo,command= lambda: entrar_valores('.'), text=".", width=7, height=2, bg=cor7, relief=RAISED, overrelief=RIDGE)
b_2.place(x=176, y=160)
b_3 = Button(frame_corpo, command= calcular, text="=", width=7, height=2, bg=cor6, fg=cor2, relief=RAISED, overrelief=RIDGE)
b_3.place(x=117, y=160)

janela.mainloop()