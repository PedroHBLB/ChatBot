from tkinter import *
from chatbot import ChatBot
myChatBot = ChatBot()
myChatBot.createModel()

def GeraGUI():

    # Função do Botão Enviar
    def Enviar():
        msg = chatInput.get("1.0", 'end-1c').strip()
        chatInput.delete("0.0", END)

        if(msg != ""):
            # Insere no Log a mensagem do usuário
            chatLog.config(state=NORMAL)
            chatLog.insert(END, "Você: " + msg + "\n")
            chatLog.config(fg="#000000", font=("Verdana", 10))

            # Busca a resposta do Chatbot
            resposta, intencao = myChatBot.chatbot_response(msg)

            # Insere no Log a mensagem do Chatbot
            chatLog.insert(END, "PIPEBot: " + resposta + "\n\n")
            chatLog.config(state=DISABLED)
            chatLog.yview(END)

            if(intencao[0]['intent'] == "Despedida"):
                chatLog.config(state=NORMAL)
                chatLog.insert(END, "*** Diálogo Encerrado ***" + '\n')
                chatLog.config(state=DISABLED)
                chatInput.config(state=DISABLED)



    # Tela Principal
    tela = Tk()
    tela.title("FAPESP - PIPEBot")
    tela.geometry("400x500")
    tela.resizable(width=FALSE, height=FALSE)

    # Log de Mensagens
    chatLog = Text(tela, bd=2, bg="white", height="8", width="50", font="Arial", wrap=WORD)
    chatLog.config(state=DISABLED)

    # Scroll do Log
    chatScroll = Scrollbar(tela, command=chatLog.yview)
    chatLog["yscrollcommand"] = chatScroll.set

    # Botão Enviar
    chatEnviar = Button(tela, font=("Verdana", 10, "bold"), text="Enviar", width="10", height=5,
                        bd=2, bg="#66b2ff", activebackground="#0080ff", fg="#000000", command=Enviar)
    
    # Caixa de envio de mensagem do usuário
    chatInput = Text(tela, bd=2, bg="white", width="29", height="5", font="Arial")

    # Alocação de elementos na tela
    chatLog.place(x=6, y=6, height=386, width=370)
    chatScroll.place(x=376, y=6, height=386)
    chatEnviar.place(x=275, y=401, height=90)
    chatInput.place(x=6, y=401, height=90, width=265)

    chatLog.config(state=NORMAL)
    chatLog.insert(END, "PIPEBot: Olá! Eu sou o PIPEBot e estou aqui para te ajudar com duvidas sobre o PIPE da FAPESP\n\n")
    chatLog.config(fg="#000000", font=("Verdana", 10,))
    chatLog.config(state=DISABLED)

    tela.mainloop()

def main():
    GeraGUI()

main()