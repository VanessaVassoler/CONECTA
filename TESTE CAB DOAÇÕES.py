from tkinter import *
from PIL import ImageTk,Image
import sqlite3

janela = Tk()
janela.title('Doações Casa de Apoio Betânia')
janela.geometry("400x600")

#Banco de Dados

#Criando DB
conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\doacao_CAB.db')

#Criando cursor
c = conn.cursor()

#Criar tabela

c.execute('CREATE TABLE IF NOT EXISTS doações2(p_recebido VARCHAR(100), qnt INTEGER, CPF INTEGER,'\
              'data_entrada TEXT, data_saida TEXT, responsavel TEXT, obs VARCHAR(250))')

#Criando função salvar

def salvar():
  
    #conectar no bd
    conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\doacao_CAB.db')
    c = conn.cursor()
    #inserir dados na tabela
    c.execute("INSERT INTO doações2 VALUES (:p_recebido, :qnt, :CPF, :data_entrada, :data_saida, :responsavel, :obs)",
             {
                  'p_recebido': p_recebido.get(),
                  'qnt': qnt.get(),
                  'CPF': CPF.get(),
                  'data_entrada': data_entrada.get(),
                  'data_saida': data_saida.get(),
                  'responsavel': responsavel.get(),
                  'obs': obs.get()
             })
    #limpar caixas
    p_recebido.delete(0, END)
    qnt.delete(0, END)
    CPF.delete(0, END)
    data_entrada.delete(0, END)
    data_saida.delete(0, END)
    responsavel.delete(0, END)
    obs.delete(0, END)
    conn.commit()
    conn.close()

#Criando função Ver
def ver():
        conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\doacao_CAB.db')
        c = conn.cursor()
        c.execute("SELECT *, oid FROM doações2")
        dados = c.fetchall()
        #Loop?
        ver_dados = ''
        for dado in dados:
            ver_dados += "Produto Recebido:  "+ str(dado[0]) + "   " + "Quantidade:   "  + str(dado[1]) + "   " + "CPF/CNPJ do doador:   " + str(dado[2]) + "   " + "Data de entrada:   " + str(dado[3]) + "   " + "Data de saída:   " + str(dado[4]) + "   " + "Responsável pelo registro:   " + str(dado[5]) + "   " + "Observações:   " + "\t" +str(dado[6]) + "   " + "ID:   " + str(dado[7]) + "   "  + "\n"
             
        ver_label = Label(janela, text=ver_dados)
        ver_label.grid(row=9, column=0, columnspan=2)
        conn.commit()
        conn.close()
#Criando caixas de texto

p_recebido = Entry(janela, width=30)
p_recebido.grid(row=0, column=1, padx=20)
qnt = Entry(janela, width=30)
qnt.grid(row=1, column=1, padx=20)
CPF = Entry(janela, width=30)
CPF.grid(row=2, column=1, padx=20)
data_entrada = Entry(janela, width=30)
data_entrada.grid(row=3, column=1, padx=20)
data_saida = Entry(janela, width=30)
data_saida.grid(row=4, column=1, padx=20)
responsavel = Entry(janela, width=30)
responsavel.grid(row=5, column=1, padx=20)
obs = Entry(janela, width=30)
obs.grid(row=6, column=1, padx=20)

#Criando rótulos
p_recebido_label = Label(janela, text = "Produto recebido")
p_recebido_label.grid(row=0, column=0)
qnt_label = Label(janela, text = "Quantidade")
qnt_label.grid(row=1, column=0)
CPF_label = Label(janela, text = "CPF/CNPJ do doador")
CPF_label.grid(row=2, column=0)
data_entrada_label = Label(janela, text = "Data de Recebimento")
data_entrada_label.grid(row=3, column=0)
data_saida_label = Label(janela, text = "Data de Saída")
data_saida_label.grid(row=4, column=0)
responsavel_label = Label(janela, text = "Respónsável pelo registro")
responsavel_label.grid(row=5, column=0)
obs_label = Label(janela, text = "Observações")
obs_label.grid(row=6, column=0)

#Botão para salvar dados
salvar_btn = Button(janela, text='Salvar no Banco de Dados', command=salvar)
salvar_btn.grid(row=7, column=0, columnspan=2, pady=10, padx = 10, ipadx=137)

#Botão para visualização dos dados
ver_btn=Button(janela, text="Visualizar Banco de Dados", command=ver)
ver_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
#Salvar mudanças
conn.commit()

#Desligar conexão
conn.close()

janela.mainloop()
