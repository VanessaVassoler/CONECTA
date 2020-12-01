from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import tkinter as tk
from PIL import ImageTk,Image
import sqlite3
import pandas as pd

menuinicial = Tk()
menuinicial.title('Doações Casa de Apoio Betânia')
menuinicial.geometry("425x600")
enquadramento = Frame(menuinicial, bg='#f1ecc2')
menuinicial.configure(background='#f6a670')
enquadramento.place(relx=0.035, rely=0.025, relwidth=0.93, relheight=0.95)


# Banco de Dados

#Criando DB
conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\DoaçõesCAB.db')

#Criando cursor
c = conn.cursor()

#Criar tabela

c.execute('CREATE TABLE IF NOT EXISTS doações(p_recebido VARCHAR(100), qnt INTEGER, CPF INTEGER,'\
              'data_entrada TEXT, data_saida TEXT, responsavel TEXT, obs VARCHAR(250))')

def fecharpopup_exportar():
    popup_exportar.destroy()

def fecharpopup_atualizar():
    popup_atualizar.destroy()
#AQUI
def fecharpopup_salvar():
    popup_salvar.destroy()
    
def fecharpopup_erro():
    popup_erro.destroy()

def fecharpopup_erro2():
    popup_erro2.destroy()
 
def fecharpopup_erro3():
    popup_erro3.destroy()

def fecharpopup_erro4():
    popup_erro4.destroy()    
    
def fecharpopup_deletar():
    popup_deletar.destroy()
    
def fecharpopup_confirmacao_delete():
    popup_confirmacao_delete.destroy()
    
def segredo():
    return
    
def exportar():
    try:
        conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\DoaçõesCAB.db')
        c = conn.cursor()
        c.execute("SELECT * from doações")
        data = pd.read_sql_query('select * from doações', conn)
        data.to_excel('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Doações.xlsx')
        conn.commit()
        conn.close()
        global popup_exportar
        popup_exportar = Tk()
        popup_exportar.title("  ")
        popup_exportar.geometry("235x120")
        popup_exportar_label = Label(popup_exportar, text="Bando de Dados exportado com sucesso.", pady=20, padx=10)
        popup_exportar_label.grid(row=0,column=0)
        popup_exportar_btn = Button(popup_exportar, text="OK", command=fecharpopup_exportar)
        popup_exportar_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=20)
        
    except:
        global popup_erro4
        popup_erro4 = Tk()
        popup_erro4.title("ERRO")
        popup_erro4.geometry("345x120")
        popup_erro4_label = Label(popup_erro4, text="Não foi possível exportar. Verifique se o arquivo Doações.xlsx \n está fechado, reinicie o programa e tente novamente.", pady=20, padx=10)
        popup_erro4_label.grid(row=0,column=0)
        popup_erro4_btn = Button(popup_erro4, text="OK", command=fecharpopup_erro4)
        popup_erro4_btn.grid(row=2, column=0, pady=10, padx=10, ipadx=20)

    

def janelaatualizar():
    if selecionardado_entrada.get() != "":
        global editor
        editor = Tk()
        editor.title('Editar dados:')
        editor.geometry("370x250")
        conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\DoaçõesCAB.db')
        c = conn.cursor()
        dados_id = selecionardado_entrada.get()
        c.execute("SELECT * FROM doações  WHERE oid = " + dados_id)
        dados = c.fetchall()
        #Criando Variaveis globais para as caixas de texto:
        global p_recebido_edit
        global qnt_edit
        global CPF_edit
        global data_entrada_edit
        global data_saida_edit
        global responsavel_edit
        global obs_edit
        #Criando caixas de texto edit
        p_recebido_edit = Entry(editor, width=30)
        p_recebido_edit.grid(row=0, column=1, padx=20, pady=(10, 0))
        qnt_edit = Entry(editor, width=30)
        qnt_edit.grid(row=1, column=1, padx=20)
        CPF_edit = Entry(editor, width=30)
        CPF_edit.grid(row=2, column=1, padx=20)
        data_entrada_edit = Entry(editor, width=30)
        data_entrada_edit.grid(row=3, column=1, padx=20)
        data_saida_edit = Entry(editor, width=30)
        data_saida_edit.grid(row=4, column=1, padx=20)
        responsavel_edit = Entry(editor, width=30)
        responsavel_edit.grid(row=5, column=1, padx=20)
        obs_edit = Entry(editor, width=30)
        obs_edit.grid(row=6, column=1, padx=20)      
        #Criando rótulos edit
        p_recebido_label_edit = Label(editor, text = "Produto recebido")
        p_recebido_label_edit.grid(row=0, column=0, pady=(10, 0))
        qnt_label_edit = Label(editor, text = "Quantidade")
        qnt_label_edit.grid(row=1, column=0)
        CPF_label_edit = Label(editor, text = "CPF/CNPJ do doador")
        CPF_label_edit.grid(row=2, column=0)
        data_entrada_label_edit = Label(editor, text = "Data de Recebimento")
        data_entrada_label_edit.grid(row=3, column=0)
        data_saida_label_edit = Label(editor, text = "Data de Saída")
        data_saida_label_edit.grid(row=4, column=0)
        responsavel_label_edit = Label(editor, text = "Respónsável pelo registro")
        responsavel_label_edit.grid(row=5, column=0)
        obs_label_edit = Label(editor, text = "Observações")
        obs_label_edit.grid(row=6, column=0)
        #Loop pelos resultados
        for dado in dados:
                p_recebido_edit.insert(0, dado[0])
                qnt_edit.insert(0, dado[1])
                CPF_edit.insert(0, dado[2])
                data_entrada_edit.insert(0, dado[3])
                data_saida_edit.insert(0, dado[4])
                responsavel_edit.insert(0, dado[5])
                obs_edit.insert(0, dado[6])
                
    #Botao salvar alterações
        salvar_edit_btn = Button(editor, text='Salvar alterações no Banco de Dados', command=atualizar)
        salvar_edit_btn.grid(row=7, column=0, columnspan=2, pady=30, padx = 10, ipadx=60)


#Da erro mas funciona kjj        
    else:
        global popup_erro2
        popup_erro2 = Tk()
        popup_erro2.title("ERRO")
        popup_erro2.geometry("285x120")
        popup_erro2_label = Label(popup_erro2, text="Nenhum dado foi selecionado. Tente novamente.", pady=20, padx=10)
        popup_erro2_label.grid(row=0,column=0)
        popup_erro2_btn = Button(popup_erro2, text="OK", command=fecharpopup_erro2)
        popup_erro2_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=20)


    
   
def atualizar():
    conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\DoaçõesCAB.db')
    c = conn.cursor()
    dados_id = selecionardado_entrada.get()
    c.execute("""UPDATE doações SET
		p_recebido = :p_recebido,
		qnt = :qnt,
		CPF = :CPF,
		data_entrada = :data_entrada,
		data_saida = :data_saida,
		responsavel = :responsavel,
        obs = :obs
		WHERE oid = :oid""",
		{
		'p_recebido': p_recebido_edit.get(),
		'qnt': qnt_edit.get(),
		'CPF': CPF_edit.get(),
		'data_entrada': data_entrada_edit.get(),
		'data_saida': data_saida_edit.get(),
		'responsavel': responsavel_edit.get(),
        'obs': obs_edit.get(),
		'oid': dados_id
		})
    conn.commit()
    conn.close()
    global popup_atualizar
    popup_atualizar = Tk()
    popup_atualizar.title("   ")
    popup_atualizar.geometry("180x120")
    popup_atualizar_label = Label(popup_atualizar, text="Dado atualizado com sucesso.", pady=20, padx=10)
    popup_atualizar_label.grid(row=0,column=0)
    popup_atualizar_btn = Button(popup_atualizar, text="OK", command=fecharpopup_atualizar)
    popup_atualizar_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=20)
    editor.destroy()        
   
def janelaver():
    global oid
    conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\DoaçõesCAB.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM doações")
    dados = c.fetchall()
    #Criando a janela
    tree = tk.Tk()
    tree.title("Banco do Dados:")
    tree.geometry("1200x600")
    tree_frame=Frame(tree)
    tree_frame.pack(fill=X, pady=20, padx=10)
    tree_scroll=Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scrollx=Scrollbar(tree_frame, orient='horizontal')
    tree_scrollx.pack(side=BOTTOM, fill=X)    
    tree1= ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
    tree1['column'] =("column1", "column2","column3","column4","column5","column6","column7", "column8")
    tree_scroll.config(command=tree1.yview)
    tree_scrollx.config(command=tree1.xview)
    tree1.column("#0", width=0, stretch=NO)
    tree1.column("column1", width=120, anchor=CENTER)
    tree1.column("column2", width=60, anchor=CENTER)
    tree1.column("column3", width=120, anchor=CENTER) 
    tree1.column("column4", width=120, anchor=CENTER)
    tree1.column("column5", width=120, anchor=CENTER)
    tree1.column("column6", width=120, anchor=CENTER)   
    tree1.column("column7", width=200, anchor=CENTER)
    tree1.column("column8", width=50, anchor=CENTER)  
    
    tree1.heading("#0", text="", anchor=W)
    tree1.heading("#1", text="Produto Recebido",)
    tree1.heading("#2", text="Quantidade")
    tree1.heading("#3", text="CPF")
    tree1.heading("#4", text="Data de Entrada")
    tree1.heading("#5", text="Data de Saída")
    tree1.heading("#6", text="Responsável pelo registro")
    tree1.heading("#7", text="OBS")
    tree1.heading("#8", text="ID")
    tree1.pack(fill = X, pady=20, padx=10, ipady=500)
    for dado in dados:
        tree1.insert("", tk.END, values= (str(dado[0]), str(dado[1]), str(dado[2]), str(dado[3]), str(dado[4]),str(dado[5]),str(dado[6]),str(dado[7])))
    conn.commit()
    conn.close()

       

def janelasalvar():
    #menuinicial.withdraw()
    global janela_salvar
    janela_salvar = Tk()
    janela_salvar.title('Cadastro de Novo Dado')
    janela_salvar.geometry('370x250')
    conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\DoaçõesCAB.db')
    c = conn.cursor()
    global p_recebido
    global qnt
    global CPF
    global data_entrada
    global data_saida
    global responsavel
    global obs
    #criando entradas
    p_recebido = Entry(janela_salvar, width=30)
    p_recebido.grid(row=0, column=1, padx=20, pady=(10, 0))
    qnt = Entry(janela_salvar, width=30)
    qnt.grid(row=1, column=1, padx=20)
    CPF = Entry(janela_salvar, width=30)
    CPF.grid(row=2, column=1, padx=20)
    data_entrada = Entry(janela_salvar, width=30)
    data_entrada.grid(row=3, column=1, padx=20)
    data_saida = Entry(janela_salvar, width=30)
    data_saida.grid(row=4, column=1, padx=20)
    responsavel = Entry(janela_salvar, width=30)
    responsavel.grid(row=5, column=1, padx=20)
    obs = Entry(janela_salvar, width=30)
    obs.grid(row=6, column=1, padx=20)

    #Criando rótulos
    p_recebido_label = Label(janela_salvar, text = "Produto recebido")
    p_recebido_label.grid(row=0, column=0, pady=(10, 0))
    qnt_label = Label(janela_salvar, text = "Quantidade")
    qnt_label.grid(row=1, column=0)
    CPF_label = Label(janela_salvar, text = "CPF/CNPJ do doador")
    CPF_label.grid(row=2, column=0)
    data_entrada_label = Label(janela_salvar, text = "Data de Recebimento")
    data_entrada_label.grid(row=3, column=0)
    data_saida_label = Label(janela_salvar, text = "Data de Saída")
    data_saida_label.grid(row=4, column=0)
    responsavel_label = Label(janela_salvar, text = "Respónsável pelo registro")
    responsavel_label.grid(row=5, column=0)
    obs_label = Label(janela_salvar, text = "Observações")
    obs_label.grid(row=6, column=0)
    #Botão para salvar dados
    salvar_btn = Button(janela_salvar, text='Salvar no Banco de Dados', command = salvar)
    salvar_btn.grid(row=7, column=0, columnspan=2, pady=30, padx = 10, ipadx=100)
    
def salvar():
    if p_recebido.get() != "" and qnt.get() != "":
    #conectar no bd
        conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\DoaçõesCAB.db')
        c = conn.cursor()
    #inserir dados na tabela
        c.execute("INSERT INTO doações VALUES (:p_recebido, :qnt, :CPF, :data_entrada, :data_saida, :responsavel, :obs)",
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
        global popup_salvar
        popup_salvar = Tk()
        popup_salvar.title("   ")
        popup_salvar.geometry("150x120")
        popup_salvar_label = Label(popup_salvar, text="Dado salvo com sucesso.", pady=20, padx=10)
        popup_salvar_label.grid(row=0,column=0)
        popup_salvar_btn = Button(popup_salvar, text="OK", command=fecharpopup_salvar)
        popup_salvar_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=20)
        janela_salvar.destroy()
    
    else:
        global popup_erro3
        popup_erro3 = Tk()
        popup_erro3.title("ERRO")
        popup_erro3.geometry("390x120")
        popup_erro3_label = Label(popup_erro3, text="Alguns campos essenciais não poram preenchidas. Tente novamente.", pady=20, padx=10)
        popup_erro3_label.grid(row=0,column=0)
        popup_erro3_btn = Button(popup_erro3, text="OK", command=fecharpopup_erro3)
        popup_erro3_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=20)


def deletar():
    
        conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\DoaçõesCAB.db')
        c = conn.cursor()
        #deletar
        c.execute("DELETE from doações WHERE oid = " + selecionardado_entrada.get())
        conn.commit()
        conn.close()
        selecionardado_entrada.delete(0,END)
        popup_deletar.destroy()
        global popup_confirmacao_delete
        popup_confirmacao_delete = Tk()
        popup_confirmacao_delete.title("   ")
        popup_confirmacao_delete.geometry("170x150")
        popup_confirmacao_delete_label=Label(popup_confirmacao_delete, text="Dado deletato com sucesso.")
        popup_confirmacao_delete_label.grid(row=0, column=0, padx=10, pady=20)
        popup_confirmacao_delete_btn=Button(popup_confirmacao_delete, text="OK", command=fecharpopup_confirmacao_delete)
        popup_confirmacao_delete_btn.grid(row=1,column=0, padx=10, pady=20, ipadx=20)

    

def janeladeletar():
    if selecionardado_entrada.get() != "":
        global popup_deletar
        popup_deletar = Tk()
        popup_deletar.title("   ")
        popup_deletar.geometry("200x150")
        popup_deletar_label = Label(popup_deletar, text = "Deseja deletar o cadastro de ID " + selecionardado_entrada.get() + "?")
        popup_deletar_label.grid(row=0, column=0, columnspan=2, pady=20, padx=10)        
        popup_deletar_sim_btn = Button(popup_deletar, text = "Sim", command=deletar)
        popup_deletar_sim_btn.grid(row=1, column=0, pady=20, padx=10, ipadx=20)
        popup_deletar_nao_btn = Button(popup_deletar, text="Não", command=fecharpopup_deletar)
        popup_deletar_nao_btn.grid(row=1, column=1, pady=20, padx=10, ipadx=20)
              
    else:        
        global popup_erro
        popup_erro = Tk()
        popup_erro.title("ERRO")
        popup_erro.geometry("285x120")
        popup_erro_label = Label(popup_erro, text="Nenhum dado foi selecionado. Tente novamente.", pady=20, padx=10)
        popup_erro_label.grid(row=0,column=0)
        popup_erro_btn = Button(popup_erro, text="OK", command=fecharpopup_erro)
        popup_erro_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=20)
        








#Criação entrada e rótulo Selecionar

selecionardado_label = Label(menuinicial, text="Dado Selecionado:", bg='#f1ecc2', anchor=E)
selecionardado_label.place(relx = 0.329, rely = 0.3, anchor=CENTER, width=110, height=30)
#selecionardado_label.grid(row=2, column=0)

selecionardado_entrada = Entry(menuinicial, width=15)
selecionardado_entrada.place(relx = 0.7, rely = 0.3, anchor = CENTER, width=52, height=30)
#selecionardado_entrada.grid(row=2, column=1, pady=20)


#Criando botões
janelasalvar_btn=Button(menuinicial, text="Cadastro de Doação", command=janelasalvar, bg='white')
janelasalvar_btn.place(relx = 0.5, rely = 0.1, anchor = CENTER, width=320, height=30)
#janelasalvar_btn.grid(row=0,column=0, columnspan=2, padx=50, pady=[60,20], ipadx=105)

janelaver_btn=Button(menuinicial, text="Visualizar Bando de Dados", command=janelaver, bg='white')
janelaver_btn.place(relx = 0.5, rely = 0.2, anchor = CENTER, width=320, height=30)
#janelaver_btn.grid(row=1,column=0,columnspan=2, padx=10, pady=20, ipadx=90)

deletardado_btn=Button(menuinicial, text="Deletar Dado Selecionado", command=janeladeletar, bg='white')
deletardado_btn.place(relx = 0.5, rely = 0.4, anchor = CENTER, width=320, height=30)
#deletardado_btn.grid(row=3,column=0,columnspan=2, padx=10, pady=20, ipadx=90)

alterardado_btn=Button(menuinicial, text="Editar Dado Selecionado", command=janelaatualizar, bg='white')
alterardado_btn.place(relx = 0.5, rely = 0.5, anchor = CENTER, width=320, height=30)
#alterardado_btn.grid(row=4,column=0,columnspan=2, padx=10, pady=20, ipadx=95)

exportarexcel_btn=Button(menuinicial, text="Exportar Banco de Dados para o Excel", command=exportar, bg='white')
exportarexcel_btn.place(relx = 0.5, rely = 0.9, anchor = CENTER, width=320, height=30)
#exportarexcel_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=[160,0], ipadx=60)

#segredo=Button(menuinicial, text="SEGREDO", command=segredo)
#segredo.place(x=600,y=500)
conn.commit()
conn.close()
menuinicial.mainloop()


