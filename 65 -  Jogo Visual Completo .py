import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title ("65 -  Jogo Visual Completo ")
root.geometry ("550x750")
root.resizable(False, False)
root.config(bg = "white")

jogador_atual ="X"
def alterar_jogada(botaos):

    global jogador_atual
    if botaos["text"] != "":
        return

    botaos.config(text = jogador_atual)
    if verificar_vencedor(botoes):
        Pontuação()
        return

    else:
      verificar_empate(botoes)
    
    jogador_atual = "O" if jogador_atual == "X" else "X"
    
def verificar_vencedor(botoes):
    for i in range(3):
        if botoes[i][0]["text"] == botoes[i][1]["text"] == botoes[i][2]["text"] != "":
            messagebox.showinfo("Vitória!", f"Jogador {botoes[i][0]['text']} venceu!")
            return True
    
        if botoes[0][i]["text"] == botoes[1][i]["text"] == botoes[2][i]["text"] != "":
           messagebox.showinfo("Vitória!", f"Jogador {botoes[0][i]['text']} venceu!")
           return True

    if botoes[0][0]["text"] == botoes[1][1]["text"] == botoes[2][2]["text"] != "":
        messagebox.showinfo("Vitória!", f"Jogador {botoes[0][0]['text']} venceu!")
        
        return True

    if botoes[0][2]["text"] == botoes[1][1]["text"] == botoes[2][0]["text"] != "":
        messagebox.showinfo("Vitória!", f"Jogador {botoes[0][2]['text']} venceu!")
       
        return True
        
def verificar_empate(botoes):
    for i in botoes:
        for botao in i:
            if botao["text"] == "":
                return  
    messagebox.showinfo("Empate!", "O jogo terminou empatado!")

placar_X = 0
placar_O = 0
def Pontuação ():
        global  placar_O, placar_X
        
        if jogador_atual == "X":
             placar_X += 1

        else:
            placar_O += 1

        placar_X1.config(text = f"Jogador X: {placar_X}")
        placar_O1.config(text = f"Jogador O: {placar_O}")

def limpar(botoes):
  global jogador_atual

  for i in botoes:
        for botao in i:
          botao.config(text = "") 

  jogador_atual ="X"

def zerar():

    global placar_X, placar_O
    if placar_X >= 0 and placar_O >= 0:
       placar_O = 0
       placar_X = 0
        
       placar_X1.config(text = f"Jogador X: {placar_X}")
       placar_O1.config(text = f"Jogador O: {placar_O}")

def credito ():
       messagebox.showinfo("Obrigado por jogar!!!", "Feito por :João Victor")


Placar_Pontuação = tk.Frame(root, bg = "blue", width=300, height = 200, )
Placar_Pontuação.grid(row = 0, column = 2, padx = 50, pady = 10, sticky = "n",)

placar_X1 = tk.Label(Placar_Pontuação, text = f"Jogador X: {placar_X}",font = ("arial",15), width=18, fg = "green",bg = "white")
placar_X1.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "n", )

placar_O1 = tk.Label(Placar_Pontuação, text = f"Jogador O: {placar_O}",font = ("arial",15), width=18, fg = "blue",bg = "white" )
placar_O1.grid(row = 0, column = 2, padx = 10, pady = 10, sticky = "n", )



Quad_jogda = tk.Frame(root, width=20, height = 20,bg = "yellow")
Quad_jogda.grid(row = 1, column = 2, padx = 10, pady = 10, sticky = "n", )

sete_b = tk.Button(Quad_jogda, text = "",font= ("arial", 15),fg = "blue", width=15, height=7, bg ="white", command=lambda: alterar_jogada(sete_b ))
sete_b.grid(row = 2, column = 1, padx = 0, pady = 0, sticky = "W" )


oito_b = tk.Button(Quad_jogda, text = "",font= ("arial", 15),fg = "blue", width=15, height=7, bg ="white",command=lambda: alterar_jogada(oito_b))
oito_b.grid(row = 2, column = 2, padx = 2, pady = 2, sticky = "W")


nove_b = tk.Button(Quad_jogda, text = "",font= ("arial", 15),fg = "blue", width=15,height=7,bg ="white",command = lambda: alterar_jogada(nove_b))
nove_b.grid(row = 2, column = 3, padx = 2, pady = 2, sticky = "W" )


seis_b = tk.Button(Quad_jogda, text = "",font= ("arial", 15),fg = "blue", width=15,height=7, bg ="white",command =lambda: alterar_jogada(seis_b))
seis_b.grid(row = 3, column = 1, padx = 2, pady = 2, sticky = "W")


cinco_b = tk.Button(Quad_jogda, text = "",font= ("arial", 15),fg = "blue", width=15,height=7, bg ="white",command = lambda: alterar_jogada(cinco_b))
cinco_b.grid(row = 3, column = 2, padx = 2, pady = 2, sticky = "W")


quatro_b = tk.Button(Quad_jogda, text = "",font= ("arial", 15),fg = "blue", width=15,height=7,bg ="white",command = lambda: alterar_jogada(quatro_b))
quatro_b.grid(row = 3, column = 3, padx = 2, pady = 2, sticky = "W" )

tres_b = tk.Button(Quad_jogda, text = "",font= ("arial", 15),fg = "blue", width=15,height=7,bg ="white",command = lambda:alterar_jogada(tres_b))
tres_b.grid(row = 4, column = 1, padx = 0 , pady = 0, sticky = "W" )


dois_b = tk.Button(Quad_jogda, text = "",font= ("arial", 15),fg = "blue", width=15,height=7,bg ="white",command=lambda: alterar_jogada(dois_b) )
dois_b.grid(row = 4, column = 2, padx =2, pady = 2, sticky = "W")


um_b = tk.Button(Quad_jogda, text = "",font= ("arial", 15),fg = "blue", width=15,height=7, bg ="white",command=lambda: alterar_jogada(um_b))
um_b.grid(row = 4, column = 3, padx = 2, pady = 2, sticky = "W")




funcoes = tk.Frame(root, width=20, height = 20, bg = "blue")
funcoes.grid(row = 2, column = 2, padx = 10, pady = 10, sticky = "n", )

zerar_placar = tk.Button(funcoes, text = "Zerar Placar",font = ("arial",12), width=17, fg = "green",bg ="white",command=zerar)
zerar_placar.grid(row = 0, column = 1, padx = 0, pady = 0, sticky = "W", )

creditos = tk.Button(funcoes, text = "Créditos",font = ("arial",12), width=17, fg = "blue",bg ="white", command= credito)
creditos.grid(row = 0, column = 3, padx = 0, pady = 0, sticky = "W" )

reiniciar = tk.Button(funcoes, text = "Reiniciar Partida",font = ("arial",12), width=17, fg = "red",bg ="white", command= lambda:limpar(botoes))
reiniciar.grid(row = 1, column = 2, padx = 0, pady = 0, sticky = "W", )

botoes= [[sete_b,oito_b,nove_b],[seis_b, cinco_b, quatro_b], [tres_b, dois_b, um_b]]

root.mainloop()













