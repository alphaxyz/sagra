from tkinter import *
from tkinter import messagebox
from collections import OrderedDict 
from PIL import ImageTk, Image #Pillow
import os
import math
import configparser
"""
fnt = {
'headermessage': 40,
'btngrid': 8,
'varclient': 50,
'currentnumberlabel'; 200,
}"""
fnt = {}
def initConf():
    headerMessage_def = 40
    btnGrid_def = 8
    varclient_def = 50
    currentnumberlabel_def = 200
    try:
        file = open('sagra.conf', 'r')
    except IOError:
        file = open('sagra.conf', 'w')
        file.write('[fonts]\n')
        file.write('headermessage = '+str(headerMessage_def)+'\n')
        file.write('btngrid = '+str(btnGrid_def)+'\n')
        file.write('varclient = '+str(varclient_def)+'\n')
        file.write('currentnumberlabel = '+str(currentnumberlabel_def)+'\n')
        file.close()

def confParse():
    global fnt
    
    try:
        file = open('sagra.conf', 'r')
    except IOError:
        print('error')
    config = configparser.ConfigParser()
    config.read('sagra.conf')
    if 'fonts' in config:
        fonts = config['fonts']
        for key in config['fonts']:
            fnt[key] =int(fonts[key])

initConf()
confParse()
print(fnt)

class Application(Frame):
        def __init__(self, master=None):
            super().__init__(master)


class Application_2(Frame):
        def __init__(self, master=None):
            super().__init__(master)
            #self.pack()

class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

root = Tk()
root.title('Client')

def saveConf(x):
    print(x)

# Menu
def create_window():
    global fnt
    window = Toplevel(root)
    e = Entry(window, background="pink",font=("Courier", 28), width=10)
    e.insert(0, fnt['headermessage'])
    e.grid(row=0, column=0, columnspan=3,sticky="nsew")

    e2 = Entry(window, background="pink",font=("Courier", 28), width=10)
    e2.insert(0, fnt['btngrid'])
    e2.grid(row=1, column=0, columnspan=3,sticky="nsew")

    e3 = Entry(window, background="pink",font=("Courier", 28), width=10)
    e3.insert(0, fnt['varclient'])
    e3.grid(row=2, column=0, columnspan=3,sticky="nsew")

    e4 = Entry(window, background="pink",font=("Courier", 28), width=10)
    e4.insert(0, fnt['currentnumberlabel'])
    e4.grid(row=3, column=0, columnspan=3,sticky="nsew")

    b = Button(window, text="Salva", command=saveConf(e.get()))
    b.grid(row=0, column=3, columnspan=3, rowspan=4, sticky="nsew")
    window.mainloop()


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Fonts", command=create_window)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Options", menu=filemenu)
root.config(menu=menubar)

# create all of the main containers
top_frame = Frame(root, bg='gray', width=100, height=20, pady=3,borderwidth=1)
#ctr_frame = Frame(root, bg='orange', width=100, height=50, pady=3,borderwidth=1)
btm_frame = Frame(root, bg='red', width=150, height=45, pady=3)

# layout all of the main containers
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="nsew")
#ctr_frame.grid(row=1, sticky="new")
btm_frame.grid(row=1, sticky="sew")

#top
top_left = Frame(top_frame, bg='blue', width=50, height=20, borderwidth=10,padx=3, pady=3)
top_left2 = Frame(top_frame, bg='blue', width=50, height=20, borderwidth=10, padx=3, pady=3)
top_left3 = Frame(top_frame, bg='brown', width=50, height=20, borderwidth=10, padx=3, pady=3)
top_mid = Frame(top_frame, bg='grey', width=50, height=20, padx=3, pady=3)
top_right = Frame(top_frame, bg='black', width=20, height=20, padx=3, pady=3, borderwidth=1)

top_left.grid(row=0, column=0, sticky="nsw")
top_left2.grid(row=0, column=1, sticky="nsw")
top_left3.grid(row=0, column=2, sticky="nsw")
top_mid.grid(row=0, column=3, sticky="nsew")
top_right.grid(row=0, column=9, sticky="ne")

#center
var_client = StringVar()
var_client.set("")
label_client = Label( top_left2, textvariable=var_client)
label_client.config(width=5)
label_client.config(font=("Courier", fnt['varclient']))
label_client.pack()

for x in range(10):
    Grid.columnconfigure(btm_frame, x, weight=1)

for y in range(10):
    Grid.rowconfigure(btm_frame, y, weight=1)

# Rimuove un elemento da un dizionario
# d: dizionario
# k: chaive da rimuovere
def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

contatore = 0
var_client.set(contatore)
#Asse x/y giglia pulsanti
x = 0
y = 0

numeroCorrente = 1 #numeroCorrente mostrato sul tabellone
listaOrdini = OrderedDict() #dizionario ordinato contenente gli ordni
btnID = {} #dizionario contenente gli identificatori dei pulsanti nella griglia

sor = "" # stringa ordinata contenente gli ordini
s = sor # stringa mostrata sul tabellone

limite = 99 #limite contatore

#aggiungi pulsante
#id: button id
def addBtnToGrid(id):
    btn = HoverButton(btm_frame,text=id, height = 3, width = 5, activebackground='#585f72')
    btn['command'] = lambda idx=id, binst=btn: removeBtnFromGrid(idx, binst)
    btn.config(font=("Courier bold", fnt['btngrid']))
    #btn.grid(column=(id-1)%10, row=int(math.floor((id-1)/10)), sticky="nwe")
    btn.grid(column=(id)%10, row=int(math.floor((id)/10)), sticky="nwe")
    btnID[str(id)] = (id,btn) #aggiungi l'id del pulsante inserito nella lista

# funzione che inserisce un'ordine alla pressione del pulsante
def insertOrderByButton():
    global x, y
    global contatore, numeroCorrente
    global listaOrdini, btnID
    global s, sor 

    if (len(listaOrdini)+1>limite):
        messagebox.showinfo( "Attenzione!", "La coda degli ordini è piena!")
    else: # la coda non è piena -> almeno un numero libero
        if (str(contatore) in listaOrdini):
            #se il numero inserito è già presente cerca il primo numero libero
            while str(contatore) in listaOrdini:
                contatore +=1
                numeroCorrente +=1

        if not(str(contatore) in listaOrdini): #else
            addOrder(contatore)
            contatore +=1
            #resetta il contatore se supera il limite
            if(contatore>limite):
                contatore=0

#rimuove il pulsante specificato dall'id e binst, ed aggiorna la stringa s
def removeBtnFromGrid(idx,binst):
    global s, sor, listaOrdini
    del listaOrdini[str(idx)]
    sor = ' - '.join(str(k) for k in sorted(listaOrdini.values()))
    sor += ' - '
    s = sor
    binst.destroy()


# create the widgets for the top frame
#s_button = Button(top_left, text = "Successivo", command = insertOrderByButton,height = 10, width = 30)

def increase():
    global contatore
    contatore+=1
    if(contatore>limite):
                contatore=0
    var_client.set(contatore)

def decrease():
    global contatore
    contatore-=1
    if(contatore<0):
                contatore=limite
    var_client.set(contatore)


def addOrder(number):
    global listaOrdini
    global sor, s
    if (len(listaOrdini)+1>limite):
        messagebox.showinfo( "Attenzione!", "La coda degli ordini è piena!")
    if str(number) in listaOrdini:
            deletemsg(number)
    else:
        numeroCorrente = number
        addBtnToGrid(number) # crea un nuovo pulsante da inserire nella griglia
        listaOrdini[str(number)] = number #aggiungi l'ordine alla lista ordini
        
        rv_listaOrdini = removekey(listaOrdini, str(number)) # dizionario senza l'ultimo ordine inserito (??)

        sor = ' - '.join(str(k) for k in sorted(rv_listaOrdini.values())) # lista ordina degli elementi presenti nel dizionario

        if(len(rv_listaOrdini) > 0):
            sor += ' - '
        if(len(rv_listaOrdini) == 1):
            sor = sor[:-2]
        
        s = sor

        numeroCorrente = number #aggiorna il numero corrente
        currentNumberSV.set(numeroCorrente) # aggiorna il numero mostrato sul tabellone
        

def addOrderBtn():
    global contatore
    addOrder(contatore)
    contatore+=1
    if(contatore>limite):
        contatore=0
    var_client.set(contatore)

# ripristina i valori iniziali
def reset():
    global contatore
    global x, y
    global numeroCorrente
    global listaOrdini
    global btnID
    global sor, s
    result = messagebox.askquestion("ATTENZIONE!","Si vuole davvero ripristinare il sistema?", icon='warning')
    if result == 'yes':
        print("Deleted")
        contatore = 0
        var_client.set(contatore)
        x = 0
        y = 0
        numeroCorrente = 1 #numeroCorrente mostrato sul tabellone
        tempList = listaOrdini.copy()
        for ordine in tempList:
            removeBtnFromGrid(btnID[str(ordine)][0],btnID[str(ordine)][1])
        listaOrdini = OrderedDict()
        btnID = {} #dizionario contenente gli identificatori dei pulsanti nella griglia

        sor = "" # stringa ordinata contenente gli ordini
        s = sor # stringa mostrata sul tabellone
        currentNumberSV.set("")
    else:
        print("did nothing")

add_btn = Button(top_left, text = "Inserisci", command = addOrderBtn,height = 5, width = 20)
plus_btn = Button(top_left, text = "+", command = increase,height = 5, width = 10)
minus_btn = Button(top_left, text = "-", command = decrease,height = 5, width = 10)
#reset_btn = Button(top_left, text = "Reset", command = reset,height = 10, width = 10)
# Annulla ordine
def undoOrder():
    global listaOrdini
    global btnID
    tempList = listaOrdini.copy()
    if len(listaOrdini)>0:
        removedOrder = tempList.popitem()
        
        removed_key = removedOrder[0]
        removeBtnFromGrid(btnID[removed_key][0],btnID[removed_key][1])
    else:
        messagebox.showinfo( "Errore!", "Impossibile annullare, la coda degli ordini è vuota", icon='error')

#undo_button = Button(top_left3, text = "Annulla", command = undoOrder,height = 10, width = 30)
reset_btn = Button(top_left3, text = "Reset", command = reset,height = 5, width = 15)
entry = Entry(top_right, background="pink",font=("Courier", 28), width=10)

#elimina se gia presente
def deletemsg(numero):
    global btnID
    result = messagebox.askquestion("Attenzione!", str(numero) + " è già presente nella coda. Si desidera eliminarlo?", icon='warning')
    if result == 'yes':
        print("Deleted")
        removeBtnFromGrid(btnID[str(numero)][0],btnID[str(numero)][1])
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
            addOrder(num)

    entry.delete(0, 'end')

#gestisce la pressione del tasto ENTER
def get(event):
    insertOrderByEntry()

entry.bind('<Return>', get)

m_button = Button(top_right, text = "Inserisci", command=insertOrderByEntry, height = 5, width = 15)

# layout the widgets in the top frame
#s_button.grid(row=0, column=0, columnspan=3,sticky="ew")
plus_btn.grid(row=0, column=0, columnspan=3,sticky="ew")
minus_btn.grid(row=1, column=0, columnspan=3,sticky="ew")
add_btn.grid(row=0, column=8, columnspan=3, rowspan=2,sticky="ew", padx=5)
reset_btn.grid(row=0, column=1, columnspan=3,sticky="ew")
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
top_frame2 = Frame(second_win, bg='yellow', width=150)
cnt_frame2 = Frame(second_win, pady=100)
cnt_left_frame2 = Frame(second_win, width=78, padx=50, pady=50)
btm_frame2 = Frame(second_win, bg='red', width=150, pady=15)
footer_frame2 = Frame(second_win, width=150, pady=3)

# layout all of the main containers
second_win.grid_rowconfigure(0, weight=1)
second_win.grid_columnconfigure(0, weight=1)

top_frame2.grid(row=0, sticky="n", columnspan=2)
cnt_frame2.grid(row=1, column=0, sticky="nsew")
cnt_left_frame2.grid(row=1, column=1, sticky="ns")
btm_frame2.grid(row=2,column=0, sticky="sew", columnspan=2)
footer_frame2.grid(row=3,column=0, sticky="sew", columnspan=2)

headerMessageSV = StringVar()
headerMessageSV.set("Stiamo servendo il numero")
headerMessage = Label( top_frame2, textvariable=headerMessageSV)
headerMessage.config(font=("Courier", fnt['headermessage']))
headerMessage.grid(row=0, column=0,sticky="new")


###PROBLEMA-------------------------------------------------------------
currentNumberSV = StringVar()
currentNumberLabel = Label( cnt_frame2, textvariable = currentNumberSV )
#currentNumberLabel.config(width=200)
currentNumberLabel.config(font=("Courier bold", currentnumberlabel['currentnumberlabel']))
currentNumberLabel.grid(row=1, column=0,sticky="nswe")
currentNumberLabel.pack()

###PROBLEMA--------------------------------------------------------

bottomSV = StringVar()
bottomSV.set(s)
bottomLabel = Label( btm_frame2, textvariable=bottomSV)
bottomLabel.config(width=200)
bottomLabel.config(font=("Courier", 100))
bottomLabel.grid(sticky="nsew")
bottomLabel.pack()

#logo
img = ImageTk.PhotoImage(Image.open("logo.gif"))
Label(cnt_left_frame2, image=img).grid(sticky="ns") 

#permette di far scorrere la lista degli ordini sul tabellone
def task():
    global s
    if len(s)>6:
        s = s[1:] + s[0]
    bottomSV.set(s)
    
    second_win.after(1000, task)  # reschedule event in 2 seconds

second_win.after(2000, task)
root.mainloop()


root.mainloop()