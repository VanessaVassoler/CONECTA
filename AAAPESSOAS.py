from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import tkinter as tk
import sqlite3
import pandas as pd



menuinicial = Tk()
menuinicial.iconbitmap('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico')
menuinicial.title('Cadastro de Pessoas - Casa de Apoio Betânia')
menuinicial.geometry("425x600")
enquadramento = Frame(menuinicial, bg='#f5f5ce')
menuinicial.configure(background='#8C1A14')
enquadramento.place(relx=0.035, rely=0.025, relwidth=0.93, relheight=0.95)



#Criando DB
conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\CAB Pessoas.db')

#Criando cursor
c = conn.cursor()

#Criar tabela

c.execute('CREATE TABLE IF NOT EXISTS Pessoas( nome TEXT, end TEXT, cidade TEXT, rg_cpf INTEGER,data_nasc TEXT, data_in TEXT, data_des TEXT, pac TEXT, resp TEXT, obs1 VARCHAR(250), obs2 VARCHAR(250))')
    
def fecharpopup_exportar():
    popup_exportar.destroy()


def fecharpopup_atualizar():
    popup_atualizar.destroy()

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


def exportar():
    try:
        conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\CAB Pessoas.db')
        c = conn.cursor()
        c.execute("SELECT * from Pessoas")
        data = pd.read_sql_query('select * from Pessoas', conn)
        data.to_excel('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Pessoas.xlsx')
        conn.commit()
        conn.close()
        global popup_exportar
        popup_exportar = Tk()
        menuinicial.iconbitmap(('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico'))
        enquadramento_exportar = Frame(popup_exportar, bg='#f5f5ce')
        enquadramento_exportar.place(relx=0.035, rely=0.03, relwidth=0.93, relheight=0.94)
        popup_exportar.iconbitmap('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico')
        popup_exportar.title('   ')
        popup_exportar.geometry("260x100")
        popup_exportar.configure(background='#8C1A14')
        popup_exportar_label = Label(enquadramento_exportar, bg='#f5f5ce', text="Banco de Dados exportado com sucesso.", pady=10, padx=10)
        popup_exportar_label.grid(row=0,column=0)
        popup_exportar_btn = Button(enquadramento_exportar, text="OK", command=fecharpopup_exportar)
        popup_exportar_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=20)
    
    except:
        global popup_erro4
        popup_erro4 = Tk()
        popup_erro4.title("ERRO")
        popup_erro4.geometry("370x120")
        popup_erro4.iconbitmap(('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico'))
        enquadramento_popup_erro4 = Frame(popup_erro4, bg='#f5f5ce')
        enquadramento_popup_erro4.place(relx=0.035, rely=0.03, relwidth=0.93, relheight=0.94)
        popup_erro4.configure(background='#8C1A14')
        popup_erro4_label = Label(enquadramento_popup_erro4, bg='#f5f5ce', text="Não foi possível exportar. Verifique se o arquivo Pessoas.xlsx \n está fechado, reinicie o programa e tente novamente.", pady=20, padx=10)
        popup_erro4_label.grid(row=0,column=0)
        popup_erro4_btn = Button(enquadramento_popup_erro4, text="OK", command=fecharpopup_erro4, bg='white')
        popup_erro4_btn.grid(row=2, column=0, pady=10, padx=10, ipadx=20)

    
def janelaatualizar():
    if selecionardado_entrada.get() != "":
        global editor
        editor = Tk()
        editor.iconbitmap('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico')
        editor.configure(background='#8C1A14')
        enquadramento_janela_atualizar = Frame(editor, bg='#f5f5ce')
        enquadramento_janela_atualizar.place(relx=0.025, rely=0.03, relwidth=0.95, relheight=0.94)
        editor.title('Editar dados:')
        editor.geometry("380x320")
        conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\CAB Pessoas.db')
        c = conn.cursor()
        dados_id = selecionardado_entrada.get()
        c.execute("SELECT * FROM Pessoas  WHERE oid = " + dados_id)
        dados = c.fetchall()
       
        
        #Criando Variaveis globais para as caixas de texto:
        global nome_edit
        global end_edit
        global cidade_edit
        global rg_cpf_edit
        global data_nasc_edit
        global data_in_edit
        global data_des_edit
        global pac_edit
        global resp_edit
        global obs1_edit
        global obs2_edit

        
        #Criando caixas de texto edit
        nome_edit = Entry(enquadramento_janela_atualizar, width=30)
        nome_edit.grid(row=0, column=1, padx=20, pady=(10, 0))
        end_edit = Entry(enquadramento_janela_atualizar, width=30)
        end_edit.grid(row=1, column=1, padx=20)
        cidade_edit = Entry(enquadramento_janela_atualizar, width=30)
        cidade_edit.grid(row=2, column=1, padx=20)
        rg_cpf_edit = Entry(enquadramento_janela_atualizar, width=30)
        rg_cpf_edit.grid(row=3, column=1, padx=20)
        data_nasc_edit = Entry(enquadramento_janela_atualizar, width=30)
        data_nasc_edit.grid(row=4, column=1, padx=20)
        data_in_edit = Entry(enquadramento_janela_atualizar, width=30)
        data_in_edit.grid(row=5, column=1, padx=20)
        data_des_edit = Entry(enquadramento_janela_atualizar, width=30)
        data_des_edit.grid(row=6, column=1, padx=20)
        pac_edit = Entry(enquadramento_janela_atualizar, width=30)
        pac_edit.grid(row=7, column=1, padx=20)  
        resp_edit = Entry(enquadramento_janela_atualizar, width=30)
        resp_edit.grid(row=8, column=1, padx=20)
        obs1_edit = Entry(enquadramento_janela_atualizar, width=30)
        obs1_edit.grid(row=9, column=1, padx=20)
        obs2_edit = Entry(enquadramento_janela_atualizar, width=30)
        obs2_edit.grid(row=10, column=1, padx=20)     
        
        #Criando rótulos edit
        nome_label_edit = Label(enquadramento_janela_atualizar, text = "Nome:",bg='#f5f5ce')
        nome_label_edit.grid(row=0, column=0, pady=(10, 0), padx=10)
        end_label_edit = Label(enquadramento_janela_atualizar, text = "Endereço",bg='#f5f5ce')
        end_label_edit.grid(row=1, column=0, padx=10)
        cidade_label_edit = Label(enquadramento_janela_atualizar, text = "Cidade",bg='#f5f5ce')
        cidade_label_edit.grid(row=2, column=0, padx=10)
        rg_cpf_label_edit = Label(enquadramento_janela_atualizar, text = "RG ou CPF",bg='#f5f5ce')
        rg_cpf_label_edit.grid(row=3, column=0, padx=10)
        data_nasc_label_edit = Label(enquadramento_janela_atualizar, text = "Data de Nascimento",bg='#f5f5ce')
        data_nasc_label_edit.grid(row=4, column=0, padx=10)
        data_in_label_edit = Label(enquadramento_janela_atualizar, text = "Data de Entrada:",bg='#f5f5ce')
        data_in_label_edit.grid(row=5, column=0)
        data_des_label_edit = Label(enquadramento_janela_atualizar, text = "Data de Desligamento:",bg='#f5f5ce')
        data_des_label_edit.grid(row=6, column=0)
        pac_label_edit = Label(enquadramento_janela_atualizar, text = "Paciente",bg='#f5f5ce')
        pac_label_edit.grid(row=7, column=0)
        resp_label_edit = Label(enquadramento_janela_atualizar, text = "Responsavel",bg='#f5f5ce')
        resp_label_edit.grid(row=8, column=0)
        obs1_label_edit = Label(enquadramento_janela_atualizar, text = "Observações 1",bg='#f5f5ce')
        obs1_label_edit.grid(row=9, column=0)
        obs2_label_edit = Label(enquadramento_janela_atualizar, text = "Observações 2",bg='#f5f5ce')
        obs2_label_edit.grid(row=10, column=0)
    
        #Loop pelos resultados
        for dado in dados:
                nome_edit.insert(0, dado[0])
                end_edit.insert(0, dado[1])
                cidade_edit.insert(0, dado[2])
                rg_cpf_edit.insert(0, dado[3])
                data_nasc_edit.insert(0, dado[4])
                data_in_edit.insert(0, dado[5])
                data_des_edit.insert(0, dado[6])
                pac_edit.insert(0, dado[7])
                resp_edit.insert(0, dado[8])
                obs1_edit.insert(0, dado[9])
                obs2_edit.insert(0, dado[10])
                
    #Botao salvar alterações
        salvar_edit_btn = Button(enquadramento_janela_atualizar, text='Salvar alterações no Banco de Dados', command=atualizar)
        salvar_edit_btn.grid(row=11, column=0, columnspan=2, pady=20, padx = 20, ipadx=30)


      
    else:
        global popup_erro2
        popup_erro2 = Tk()
        popup_erro2.iconbitmap('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico')
        enquadramento_popup_erro2 = Frame(popup_erro2, bg='#f5f5ce')
        enquadramento_popup_erro2.place(relx=0.025, rely=0.03, relwidth=0.95, relheight=0.94)
        popup_erro2.configure(background='#8C1A14')
        popup_erro2.title("ERRO")
        popup_erro2.geometry("300x120")
        popup_erro2_label = Label(enquadramento_popup_erro2, text="Nenhum dado foi selecionado. Tente novamente.", pady=20, padx=10, bg='#f5f5ce')
        popup_erro2_label.grid(row=0,column=0)
        popup_erro2_btn = Button(enquadramento_popup_erro2, text="OK", command=fecharpopup_erro2)
        popup_erro2_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=20)


    
#FALTA ACERTAR ATUALIZAR    
def atualizar():
    conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\CAB Pessoas.db')
    c = conn.cursor()
    dados_id = selecionardado_entrada.get()
    c.execute("""UPDATE Pessoas SET
		nome = :nome,
		end = :end,
        cidade= :cidade,
		rg_cpf = :rg_cpf,
		data_nasc = :data_nasc,
        data_in = :data_in,
		data_des = :data_des,
		pac = :pac,
        resp = :resp,
        obs1 = :obs1,
        obs2 = :obs2
		WHERE oid = :oid""",
		{
		'nome':nome_edit.get(),
		'end': end_edit.get(),
        'cidade': cidade_edit.get(),
		'rg_cpf': rg_cpf_edit.get(),
		'data_nasc': data_nasc_edit.get(),
        'data_in':data_in_edit.get(),
		'data_des': data_des_edit.get(),
		'pac': pac_edit.get(),
        'resp': resp_edit.get(),
        'obs1': obs1_edit.get(),
        'obs2': obs2_edit.get(),
        'oid': dados_id
        })
    
    conn.commit()
    conn.close()
    global popup_atualizar
    popup_atualizar = Tk()
    popup_atualizar.iconbitmap('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico')
    popup_atualizar.title("   ")
    popup_atualizar.geometry("190x120")
    popup_atualizar.configure(background='#8C1A14')
    enquadramento_popup_atualizar= Frame(popup_atualizar, bg='#f5f5ce')
    enquadramento_popup_atualizar.place(relx=0.025, rely=0.03, relwidth=0.95, relheight=0.94)
    popup_atualizar_label = Label(enquadramento_popup_atualizar, bg='#f5f5ce', text="Dado atualizado com sucesso.", pady=20, padx=10)
    popup_atualizar_label.grid(row=0,column=0)
    popup_atualizar_btn = Button(enquadramento_popup_atualizar, text="OK", command=fecharpopup_atualizar)
    popup_atualizar_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=20)
    editor.destroy()        
   
def janelaver():
    global oid
    conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\CAB Pessoas.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM Pessoas")
    dados = c.fetchall()
    #Criando a janela
    tree =tk.Tk()
    tree.iconbitmap('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico')
    tree.geometry("1300x600") 
    tree.title("Banco de Dados:")
    tree_frame=Frame(tree, bg='#f5f5ce')
    tree.configure(bg='#8C1A14')
    #tree_frame.pack(fill=X, pady=20, padx=10)
    tree_frame.place(relx=0.005, rely=0.01, relwidth=0.99, relheight=0.98)
    tree_scroll=Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT, fill=Y)    
    tree1= ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
    tree_scrollx=Scrollbar(tree_frame, orient="horizontal")
    tree_scrollx.pack(side=BOTTOM, fill=X)    
    tree1= ttk.Treeview(tree_frame, xscrollcommand=tree_scroll.set)
    tree1['column'] =("column1", "column2","column3","column4","column5","column6","column7", "column8", "column9", "column10", "column11","column12")
    tree_scroll.config(command=tree1.yview)
    tree_scrollx.config(command=tree1.xview)
   
    tree1.column("#0", width=0, stretch=NO)
    tree1.column("column1", width=120,anchor=CENTER)
    tree1.column("column2", width=80, anchor=CENTER)
    tree1.column("column3", width=120, anchor=CENTER) 
    tree1.column("column4", width=100, anchor=CENTER)
    tree1.column("column5", width=100, anchor=CENTER)
    tree1.column("column6", width=100, anchor=CENTER)   
    tree1.column("column7", width=180, anchor=CENTER)
    tree1.column("column8", width=50, anchor=CENTER)
    tree1.column("column9", width=180, anchor=CENTER)
    tree1.column("column10", width=50, anchor=CENTER) 
    tree1.column("column11", width=50, anchor=CENTER)  
    tree1.column("column12", width=50, anchor=CENTER)  
    
    tree1.heading("#0", text="", anchor=W)
    tree1.heading("#1", text="Nome",)
    tree1.heading("#2", text="Endereço")
    tree1.heading("#3", text="Cidade")
    tree1.heading("#4", text="RG/CPF")
    tree1.heading("#5", text="Data de Nascimento")
    tree1.heading("#6", text="Data de Entrada")
    tree1.heading("#7", text="Data de Desligamento")
    tree1.heading("#8", text="Paciente")
    tree1.heading("#9", text="Responsavel pelo Registro")
    tree1.heading("#10", text="Obs1")
    tree1.heading("#11", text="Obs2")
    tree1.heading("#12", text="ID")
    tree1.pack(fill = X, pady=20, padx=10, ipady=500) 
    
    for dado in dados:
        tree1.insert("", tk.END, values= (str(dado[0]), str(dado[1]), str(dado[2]), str(dado[3]), str(dado[4]),str(dado[5]),str(dado[6]),str(dado[7]), str(dado[8]), str(dado[9]), str(dado[10]), str(dado[11])))
    conn.commit()
    conn.close()

       

def janelasalvar():
    #menuinicial.withdraw()
    global janela_salvar
    janela_salvar = Tk()
    janela_salvar.iconbitmap('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico')
    enquadramento_janela_salvar = Frame(janela_salvar, bg='#f5f5ce')
    enquadramento_janela_salvar.place(relx=0.025, rely=0.03, relwidth=0.95, relheight=0.94)
    janela_salvar.title('Cadastro de Novo Dado:')
    janela_salvar.geometry('420x320')
    janela_salvar.configure(background='#8C1A14')
    conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\CAB Pessoas.db')
    c = conn.cursor()
    global nome
    global end
    global cidade
    global rg_cpf
    global data_nasc
    global data_in
    global data_des
    global pac
    global resp
    global obs1
    global obs2  
    #criando entradas
    nome = Entry(janela_salvar, width=30)
    nome.grid(row=0, column=1, padx=20, pady=(20, 0))
    end = Entry(janela_salvar, width=30)
    end.grid(row=1, column=1, padx=20)
    cidade = Entry(janela_salvar, width=30)
    cidade.grid(row=2, column=1, padx=20)
    rg_cpf = Entry(janela_salvar, width=30)
    rg_cpf.grid(row=3, column=1, padx=20)
    data_nasc = Entry(janela_salvar, width=30)
    data_nasc.grid(row=4, column=1, padx=20)
    data_in = Entry(janela_salvar, width=30)
    data_in.grid(row=5, column=1, padx=20)
    data_des = Entry(janela_salvar, width=30)
    data_des.grid(row=6, column=1, padx=20)
    pac = Entry(janela_salvar, width=30)
    pac.grid(row=7, column=1, padx=20)
    resp = Entry(janela_salvar, width=30)
    resp.grid(row=8, column=1, padx=20)
    obs1 = Entry(janela_salvar, width=30)
    obs1.grid(row=9, column=1, padx=20)
    obs2 = Entry(janela_salvar, width=30)
    obs2.grid(row=10, column=1, padx=20)
    
    #Criando rótulos
    nome_label = Label(janela_salvar, text = "Nome", bg='#f5f5ce')
    nome_label.grid(row=0, column=0, pady=(10, 0), padx=20)
    end_label = Label(janela_salvar, text = "Endereco",bg='#f5f5ce')
    end_label.grid(row=1, column=0, padx=20)
    cidade_label = Label(janela_salvar, text = "Cidade",bg='#f5f5ce')
    cidade_label.grid(row=2, column=0, padx=20)
    rg_cpf_label = Label(janela_salvar, text = "RG ou CPF",bg='#f5f5ce')
    rg_cpf_label.grid(row=3, column=0, padx=20)
    data_nasc_label = Label(janela_salvar, text = "Data de Nascimento",bg='#f5f5ce')
    data_nasc_label.grid(row=4, column=0, padx=20)
    data_in_label = Label(janela_salvar, text = "Data de Entrada",bg='#f5f5ce')
    data_in_label.grid(row=5, column=0, padx=20)
    data_des_label = Label(janela_salvar, text = "Data de Desligamento",bg='#f5f5ce')
    data_des_label.grid(row=6, column=0, padx=20)
    pac_label = Label(janela_salvar, text = "Paciente",bg='#f5f5ce')
    pac_label.grid(row=7, column=0, padx=20)
    resp_label = Label(janela_salvar, text = "Respónsável pelo registro", bg='#f5f5ce')
    resp_label.grid(row=8, column=0, padx=20)
    obs1_label = Label(janela_salvar, text = "Observaçao 1", bg='#f5f5ce')
    obs1_label.grid(row=9, column=0, padx=20)
    obs2_label = Label(janela_salvar, text = "Observaçao 2",bg='#f5f5ce')
    obs2_label.grid(row=10, column=0, padx=20)
    #Botão para salvar dados
    salvar_btn = Button(janela_salvar, text='Salvar no Banco de Dados', command = salvar, bg='white')
    salvar_btn.grid(row=11, column=0, columnspan=2, pady=10, padx = 35, ipadx=100)
    
#Criando função salvar

def salvar():
    if nome.get() !=   "" and rg_cpf.get() != "":
        #conectar no bd
        conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\CAB Pessoas.db')
        c = conn.cursor()
        #inserir dados na tabela
        c.execute("INSERT INTO Pessoas VALUES (:nome, :end, :cidade, :rg_cpf, :data_nasc, :data_in, :data_des, :pac, :resp, :obs1, :obs2)",
                     {
                      'nome': nome.get(),
                      'end': end.get(),
                      'cidade': cidade.get(),
                      'rg_cpf': rg_cpf.get(),
                      'data_nasc': data_nasc.get(),
                      'data_in': data_in.get(),
                      'data_des': data_des.get(),
                      'pac': pac.get(),
                      'resp': resp.get(),
                      'obs1': obs1.get(),
                      'obs2': obs2.get()
                      })
        #limpar caixas
        nome.delete(0, END)
        end.delete(0, END)
        cidade.delete(0, END)
        rg_cpf.delete(0, END)
        data_nasc.delete(0, END)
        data_in.delete(0, END)
        data_des.delete(0, END)
        pac.delete(0, END)
        resp.delete(0, END)
        obs1.delete(0, END)
        obs2.delete(0, END)
        conn.commit()
        conn.close()
        global popup_salvar
        popup_salvar = Tk()
        popup_salvar.iconbitmap('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico')
        popup_salvar.geometry("170x120")
        popup_salvar.title('   ')
        enquadramento_popup_salvar = Frame(popup_salvar, bg='#f5f5ce')
        enquadramento_popup_salvar.place(relx=0.035, rely=0.03, relwidth=0.93, relheight=0.94)
        popup_salvar.configure(background='#8C1A14')
        popup_salvar_label = Label(enquadramento_popup_salvar, text="Dado salvo com sucesso.", pady=20, padx=10, bg='#f5f5ce')
        popup_salvar_label.grid(row=0,column=0)
        popup_salvar_btn = Button(enquadramento_popup_salvar, text="OK", command=fecharpopup_salvar, bg='white')
        popup_salvar_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=20)
        janela_salvar.destroy()
    else:
            global popup_erro3
            popup_erro3 = Tk()
            popup_erro3.title('ERRO')
            popup_erro3.geometry('410x120')
            popup_erro3.iconbitmap('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico')
            enquadramento_popup_erro3 = Frame(popup_erro3, bg='#f5f5ce')
            enquadramento_popup_erro3.place(relx=0.025, rely=0.03, relwidth=0.95, relheight=0.94)
            popup_erro3.configure(background='#8C1A14')
            popup_erro3_label = Label(enquadramento_popup_erro3, bg='#f5f5ce', text="Alguns campos essenciais não poram preenchidos. Tente novamente.", pady=20, padx=10)
            popup_erro3_label.grid(row=0,column=0)
            popup_erro3_btn = Button(enquadramento_popup_erro3, text="OK", command=fecharpopup_erro3, bg='white')
            popup_erro3_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=20)
            
def deletar():
    
        conn = sqlite3.connect('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\CAB Pessoas.db')
        c = conn.cursor()
        #deletar
        c.execute("DELETE from Pessoas WHERE oid = " + selecionardado_entrada.get())
        conn.commit()
        conn.close()
        selecionardado_entrada.delete(0,END)
        popup_deletar.destroy()
        global popup_confirmacao_delete
        popup_confirmacao_delete = Tk()
        popup_confirmacao_delete.title('   ')
        popup_confirmacao_delete.geometry('185x100')
        popup_confirmacao_delete.iconbitmap('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico')
        enquadramento_popup_confirmacao_delete = Frame(popup_confirmacao_delete, bg='#f5f5ce')
        enquadramento_popup_confirmacao_delete.place(relx=0.035, rely=0.03, relwidth=0.93, relheight=0.94)
        popup_confirmacao_delete.configure(background='#8C1A14')
        popup_confirmacao_delete_label=Label(enquadramento_popup_confirmacao_delete, text="Dado deletato com sucesso.", bg='#f5f5ce')
        popup_confirmacao_delete_label.grid(row=0, column=0, padx=10, pady=(20,0))
        popup_confirmacao_delete_btn=Button(enquadramento_popup_confirmacao_delete, text="OK", command=fecharpopup_confirmacao_delete, bg='white')
        popup_confirmacao_delete_btn.grid(row=1,column=0, padx=10, pady=20, ipadx=20)
 
        
def janeladeletar():
    if selecionardado_entrada.get() != "":
        global popup_deletar
        popup_deletar = Tk()
        popup_deletar.title('   ')
        popup_deletar.iconbitmap('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico')
        popup_deletar.geometry("217x130")
        enquadramento_popup_deletar = Frame(popup_deletar, bg='#f5f5ce')
        enquadramento_popup_deletar.place(relx=0.035, rely=0.03, relwidth=0.93, relheight=0.94)
        popup_deletar.configure(background='#8C1A14')
        popup_deletar_label = Label(enquadramento_popup_deletar,bg ='#f5f5ce', text = "Deseja deletar o cadastro de ID " + selecionardado_entrada.get() + "?")
        popup_deletar_label.grid(row=0, column=0, columnspan=2, pady=20, padx=10)        
        popup_deletar_sim_btn = Button(enquadramento_popup_deletar, text = "Sim", command=deletar, bg='white')
        popup_deletar_sim_btn.grid(row=1, column=0, pady=20, padx=10, ipadx=20)
        popup_deletar_nao_btn = Button(enquadramento_popup_deletar, text="Não", command=fecharpopup_deletar, bg='white')
        popup_deletar_nao_btn.grid(row=1, column=1, pady=20, padx=(0, 10), ipadx=20)
              
    else:        
        global popup_erro
        popup_erro = Tk()
        popup_erro.title("ERRO")
        popup_erro.geometry("300x120")
        popup_erro.iconbitmap('C:\\Users\\Thomas\\Desktop\\THOMAS\\python\\Ícone-PEssoas.ico')
        enquadramento_popup_erro = Frame(popup_erro, bg='#f5f5ce')
        enquadramento_popup_erro.place(relx=0.025, rely=0.03, relwidth=0.95, relheight=0.94)
        popup_erro.configure(background='#8C1A14')
        popup_erro_label = Label(enquadramento_popup_erro, text="Nenhum dado foi selecionado. Tente novamente.", bg='#f5f5ce', pady=20, padx=10)
        popup_erro_label.grid(row=0,column=0)
        popup_erro_btn = Button(enquadramento_popup_erro, text="OK", command=fecharpopup_erro, bg='white')
        popup_erro_btn.grid(row=1, column=0, pady=10, padx=10, ipadx=20)
  
        
#Criação entrada e rótulo Selecionar
selecionardado_label = Label(menuinicial, text="Dado Selecionado:", bg='#f5f5ce', anchor=E)
selecionardado_label.place(relx = 0.329, rely = 0.3, anchor=CENTER, width=110, height=30)


selecionardado_entrada = Entry(menuinicial, width=15)
selecionardado_entrada.place(relx = 0.7, rely = 0.3, anchor = CENTER, width=52, height=30)



#Criando botões
janelasalvar_btn=Button(menuinicial, text="Cadastro de Pessoas", command=janelasalvar, bg='white')
janelasalvar_btn.place(relx=0.5,rely=0.1, anchor=CENTER, width=320, height=30)

janelaver_btn=Button(menuinicial, text="Visualizar Banco de Dados", command=janelaver, bg='white')
janelaver_btn.place(relx=0.5,rely=0.2, anchor=CENTER, width=320, height=30)

deletardado_btn=Button(menuinicial, text="Deletar Dado Selecionado", command=janeladeletar, bg='white')
deletardado_btn.place(relx=0.5,rely=0.6, anchor=CENTER, width=320, height=30)

alterardado_btn=Button(menuinicial, text="Editar Dado Selecionado", command=janelaatualizar, bg='white')
alterardado_btn.place(relx=0.5,rely=0.7, anchor=CENTER, width=320, height=30)

exportarexcel_btn=Button(menuinicial, text="Exportar Banco de Dados para o Excel", command=exportar, bg='white')
exportarexcel_btn.place(relx=0.5, rely=0.9,anchor=CENTER, width=320, height=30)


conn.commit()
conn.close()
menuinicial.mainloop()
