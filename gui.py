from tkinter import *
from tkinter import messagebox
from collections import OrderedDict 
import math

class Application(Frame):
        def __init__(self, master=None):
            super().__init__(master)


class Application_2(Frame):
        def __init__(self, master=None):
            super().__init__(master)
            #self.pack()

root = Tk()
root.title('Client')

# create all of the main containers
top_frame = Frame(root, bg='gray', width=800, height=50, pady=3,borderwidth=1)
ctr_frame = Frame(root, bg='orange', width=800, height=50, pady=3,borderwidth=1)
btm_frame = Frame(root, bg='red', width=450, height=45, pady=3)

# layout all of the main containers
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="nsew")
ctr_frame.grid(row=1, sticky="new")
btm_frame.grid(row=2, sticky="sew")

#top
top_left = Frame(top_frame, bg='blue', width=100, height=190, borderwidth=10,padx=3, pady=3)
top_left2 = Frame(top_frame, bg='brown', width=100, height=190, borderwidth=10, padx=3, pady=3)
top_mid = Frame(top_frame, bg='grey', width=100, height=190, padx=3, pady=3)
top_right = Frame(top_frame, bg='black', width=100, height=190, padx=3, pady=3, borderwidth=1)

top_left.grid(row=0, column=0, sticky="nsw")
top_left2.grid(row=0, column=1, sticky="nsw")
top_mid.grid(row=0, column=2, sticky="nsew")
top_right.grid(row=0, column=9, sticky="ne")

#center
var_client = StringVar()
var_client.set("")
label_client = Label( ctr_frame, textvariable=var_client)
label_client.config(width=200)
label_client.config(font=("Courier", 50))
label_client.pack()

for x in range(10):
    Grid.columnconfigure(btm_frame, x, weight=1)

for y in range(5):
    Grid.rowconfigure(btm_frame, y, weight=1)

# Rimuove un elemento da un dizionario
# d: dizionario
# k: chaive da rimuovere
def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

contatore = 1 
#Asse x/y giglia pulsanti
x = 0
y = 0

numeroCorrente = 1 #numeroCorrente mostrato sul tabellone
#listaOrdini = {} #dizionario contenente gli ordni
listaOrdini = OrderedDict() 
btnID = {} #dizionario contenente gli identificatori dei pulsanti nella griglia

sor = "" # stringa ordinata contenente gli ordini
s = sor # stringa mostrata sul tabellone

limite = 999 #limite contatore

#aggiungi pulsante
#id: button id
def addButton(id):
    btn = Button(btm_frame,text=id, height = 5, width = 5, activebackground='#3E4149')
    btn['command'] = lambda idx=id, binst=btn: click(idx, binst)
    btn.grid(column=(id-1)%10, row=int(math.floor((id-1)/10)), sticky="nwe")

    btnID[str(id)] = (id,btn) #aggiungi l'id del pulsante inserito nella lista

# funzione che inserisce un'ordine alla pressione del pulsantes
def insertOrderByButton():
    global x
    global y
    global contatore
    global numeroCorrente
    global listaOrdini
    global s
    global sor
    global btnID

    print(listaOrdini)
    print(contatore)

    if (len(listaOrdini)+1>limite):
        messagebox.showinfo( "Attenzione!", "La coda degli ordini è piena!")
    else: # la coda non è piena -> almeno un numero libero

        if (str(contatore) in listaOrdini):
            #se il numero inserito è già presente cerca il primo numero libero
            while str(contatore) in listaOrdini:
                contatore +=1
                numeroCorrente +=1
                print(contatore)

        if not(str(contatore) in listaOrdini): #else

            addButton(contatore) # crea un nuovo pulsante da inserire nella griglia

            listaOrdini[str(contatore)] = contatore #aggiungi l'ordine alla lista ordini
            

            rv_listaOrdini = removekey(listaOrdini, str(contatore)) # dizionario senza l'ultimo ordine inserito (??)

            sor = ' - '.join(str(k) for k in sorted(rv_listaOrdini.values())) # lista ordina degli elementi presenti nel dizionario

            if(len(rv_listaOrdini) > 0):
                sor += ' - '
            if(len(rv_listaOrdini) == 1):
                sor = sor[:-2]
            
            s = sor
            print(sorted(rv_listaOrdini.values()))

            numeroCorrente = contatore #aggiorna il numero corrente
            var.set(numeroCorrente) # aggiorna il numero mostrato sul tabellone
            var_client.set(numeroCorrente)
            
            
            contatore +=1
            #resetta il contatore se supera il limite
            if(contatore>limite):
                contatore=1

#rimuove il pulsante specificato dall'id e binst, ed aggiorna la stringa s
def click(idx,binst):
    global s
    global listaOrdini
    global sor
    print("removing")
    print(idx)
    print(binst)
    del listaOrdini[str(idx)]
    sor = ' - '.join(str(k) for k in sorted(listaOrdini.values()))
    sor += ' - '
    s = sor
    binst.destroy()


# create the widgets for the top frame
s_button = Button(top_left, text = "Successivo", command = insertOrderByButton,height = 10, width = 30)

def undoOrder():
    global listaOrdini
    global btnID
    tempList = listaOrdini.copy()
    if len(listaOrdini)>0:
        removedOrder = tempList.popitem()
        
        removed_key = removedOrder[0]
        click(btnID[removed_key][0],btnID[removed_key][1])
    else:
        messagebox.showinfo( "Errore!", "Impossibile annullare, la coda degli ordini è vuota", icon='error')

undo_button = Button(top_left2, text = "Annulla", command = undoOrder,height = 10, width = 30)

entry = Entry(top_right, background="pink",font=("Courier", 28))

#elimina se gia presente
def deletemsg(numero):
    global btnID
    result = messagebox.askquestion("Attenzione!", str(numero) + " è già presente nella coda. Si desidera eliminarlo?", icon='warning')
    if result == 'yes':
        print("Deleted")
        print(btnID[str(numero)])
        click(btnID[str(numero)][0],btnID[str(numero)][1])
    else:
        print("I'm Not Deleted Yet")

#deve essere un numero
def insertOrderByEntry():
    global listaOrdini
    global numeroCorrente
    global s
    global sor
    global btnID
    testo = entry.get()
    if testo == '': #TODO:deve essere un numero
        messagebox.showinfo( "Attenzione!", "Inserire un numero", icon='warning')
    else:
        num = int(testo)
        if testo in listaOrdini:
            deletemsg(num)
        else:
            numeroCorrente = num
            var.set(numeroCorrente)
            var_client.set(numeroCorrente)
            addButton(num)

            listaOrdini[str(num)] = num

            rv_listaOrdini = removekey(listaOrdini, str(num))

            sor = ' - '.join(str(k) for k in sorted(rv_listaOrdini.values()))

            if(len(rv_listaOrdini) > 0):
                sor += ' - '
            if(len(rv_listaOrdini) == 1):
                sor = sor[:-2]

            s = sor
            var.set(numeroCorrente)
            print(' '.join(rv_listaOrdini.keys()))

    entry.delete(0, 'end')

#gestisce la pressione del tasto ENTER
def get(event):
    insertOrderByEntry()

entry.bind('<Return>', get)

m_button = Button(top_right, text = "Inserisci", command=insertOrderByEntry, height = 6, width = 20)

# layout the widgets in the top frame
s_button.grid(row=0, column=0, columnspan=3,sticky="ew")
undo_button.grid(row=0, column=1, columnspan=3,sticky="ew")
entry.grid(row=1, column=0, sticky="w", padx=20,)
m_button.grid(row=1, column=1, sticky="w", padx=20)

# create the center widgets

btm_frame.grid_rowconfigure(0, weight=1)
btm_frame.grid_columnconfigure(1, weight=1)


second_win = Toplevel(root)
second_win.geometry('{}x{}'.format(460, 350))
app2 = Application_2(second_win)
second_win.title('Tabellone')

# create all of the main containers
top_frame2 = Frame(second_win, width=450, height=20, pady=3)
cnt_frame2 = Frame(second_win, bg='black', width=450, height=45, pady=3)
btm_frame2 = Frame(second_win, bg='red', width=450, height=45, pady=3)

# layout all of the main containers
second_win.grid_rowconfigure(1, weight=1)
second_win.grid_columnconfigure(0, weight=1)

top_frame2.grid(row=0, sticky="ns")
cnt_frame2.grid(row=1, sticky="sew")
btm_frame2.grid(row=2, sticky="sew")

headerMessageSV = StringVar()
headerMessageSV.set("Stiamo servendo il numero")
headerMessage = Label( top_frame2, textvariable=headerMessageSV)
headerMessage.config(font=("Courier", 40))
headerMessage.grid(row=1, column=0,sticky="nsew")


###PROBLEMA-------------------------------------------------------------
var = StringVar()
label = Label( cnt_frame2, textvariable = var, relief = RAISED )
label.config(width=200)
label.config(font=("Courier bold", 200))
label.grid(row=1, column=0,sticky="nsew")
label.pack()

###PROBLEMA--------------------------------------------------------

varr = StringVar()
varr.set(s)
labell = Label( btm_frame2, textvariable=varr, relief=RAISED )
labell.config(width=200)
labell.config(font=("Courier", 100))

#permette di far scorrere la lista degli ordini sul tabellone
def task():
    global s
    if len(s)>6:
        s = s[1:] + s[0]
    print(s)
    varr.set(s)
    labell.pack()
    second_win.after(1000, task)  # reschedule event in 2 seconds

second_win.after(2000, task)
root.mainloop()


root.mainloop()