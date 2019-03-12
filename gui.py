from tkinter import *
from tkinter import messagebox

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
btm_frame = Frame(root, bg='red', width=450, height=45, pady=3)

# layout all of the main containers
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="nsew")
btm_frame.grid(row=1, sticky="sew")

#top
ctr_left = Frame(top_frame, bg='blue', width=100, height=190,borderwidth=10,padx=3, pady=3)
ctr_mid = Frame(top_frame, bg='grey', width=100, height=190, padx=3, pady=3)
ctr_right = Frame(top_frame, bg='black', width=100, height=190, padx=3, pady=3,borderwidth=1)

ctr_left.grid(row=0, column=0, sticky="nsw")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=9, sticky="ne")


for x in range(10):
    Grid.columnconfigure(btm_frame, x, weight=1)

for y in range(5):
    Grid.rowconfigure(btm_frame, y, weight=1)


def getX(x):
    if(x%10)>0:
        return (x%10)-1
    else: #x%10 == 0
        return 9

def getY(y):
    if (y%10)==0:
        return int((y/10)-1)
    else: #x%10 == 0
        return int(math.floor(y/10))

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

i = 1
x = 0
y = 0
current = 1 #current number set by text
numeri = {}
btnID = {}
sor = ""
s = sor
limite = 999
#sort the string
def helloCallBack():
    global x
    global y
    global i
    global current
    global numeri
    global s
    global sor
    global btnID
    print(numeri)
    print(i)
    if (len(numeri)+1>limite):
        messagebox.showinfo( "Attenzione", "CODA PIENA")
    else:
        if (str(i) in numeri):
            while str(i) in numeri:
                i +=1
                current +=1
                print(i)
        if not(str(i) in numeri):
        #    messagebox.showinfo( "Attenzione", testo + " è già presente nella coda")
        #else:
            btn = Button(btm_frame,text=i, height = 5, width = 5, activebackground='#3E4149')
            
            btn['command'] = lambda idx=i, binst=btn: click(idx, binst)
            current = i
            #btn.grid(column=getX(i), row=getY(i), sticky="nwe")
            btn.grid(column=(i-1)%10, row=int(math.floor((i-1)/10)), sticky="nwe")
            #print("i:{}, x:{}, y:{}".format(i,getX(i),getY(i)))
            
            # if current in numeri:
            #     text.insert(INSERT, "rimosso"+str(current))
            numeri[str(i)] = i
            btnID[str(i)] = (i,btn)
            #print(btnID.values())
            rv_numeri = removekey(numeri, str(i))
            #sor = ' - '.join(numeri.keys())
            #sor = ' - '.join(rv_numeri.keys())
            sor = ' - '.join(str(k) for k in sorted(rv_numeri.values()))
            if(len(rv_numeri) > 0):
                sor += ' - '
            if(len(rv_numeri) == 1):
                sor = sor[:-2]
            
            s = sor
            #print(' '.join(rv_numeri.keys()))
            print(sorted(rv_numeri.values()))
            #print('lung: {}'.format(len(rv_numeri)))
            #text.pack()
            var.set(current)
            label.pack()
            
            i +=1
            if(i>limite):
                i=1
            #B = Button(root, text = str(current), command = helloCallBack)
            #B.place()

def click(idx,binst):
    global s
    global numeri
    global sor
    print("removing")
    print(idx)
    print(binst)
    del numeri[str(idx)]
    #sor = ' - '.join(numeri.keys())
    sor = ' - '.join(str(k) for k in sorted(numeri.values()))
    sor += ' - '
    s = sor
    binst.destroy()


# create the widgets for the top frame
s_button = Button(ctr_left, text = "Successivo", command = helloCallBack,height = 10, width = 30)

entry = Entry(ctr_right, background="pink",font=("Courier", 28))

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
def helloCallBack2():
    global numeri
    global current
    global s
    global sor
    global btnID
    testo = entry.get()
    if testo == '':
        messagebox.showinfo( "Attenzione!", "Inserire un numero")
    num = int(testo)
    if testo in numeri:
        #messagebox.showinfo( "Attenzione!", testo + " è già presente nella coda")
        #btn = Button(btm_frame,text=num, height = 5, width = 5, activebackground='#3E4149')
        deletemsg(num)
    else:
        current = num
        label.pack()
        var.set(current)
        btn = Button(btm_frame,text=num, height = 5, width = 5, activebackground='#3E4149')
    
        btn['command'] = lambda idx=num, binst=btn: click(idx, binst)
        #btn.grid(column=getX(num), row=getY(num), sticky="nwe")
        btn.grid(column=(num-1)%10, row=int(math.floor((num-1)/10)), sticky="nwe")
        #print(num%10)
        numeri[str(num)] = num
        btnID[str(num)] = (num,btn)
        rv_numeri = removekey(numeri, str(num))
        #sor = ' - '.join(numeri.keys())
        #sor = ' - '.join(rv_numeri.keys())
        sor = ' - '.join(str(k) for k in sorted(rv_numeri.values()))

        if(len(rv_numeri) > 0):
            sor += ' - '
        if(len(rv_numeri) == 1):
            sor = sor[:-2]
        #sor += ' - '
        s = sor
        var.set(current)
        print(' '.join(rv_numeri.keys()))
    entry.delete(0, 'end')

def get(event):
    helloCallBack2()

entry.bind('<Return>', get)
m_button = Button(ctr_right, text = "Inserisci", command=helloCallBack2, height = 6, width = 20)

# layout the widgets in the top frame
s_button.grid(row=0, column=1, columnspan=3,sticky="ew")
entry.grid(row=1, column=0, sticky="w", padx=20,)
m_button.grid(row=1, column=1, sticky="w", padx=20)

# create the center widgets

btm_frame.grid_rowconfigure(0, weight=1)
btm_frame.grid_columnconfigure(1, weight=1)


second_win = Toplevel(root)
second_win.geometry('{}x{}'.format(460, 350))
app2 = Application_2(second_win)
second_win.title('Tabellone')
#text = Text(second_win)
#text.config(height=10)
#text.pack()

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

varr1 = StringVar()
varr1.set("Stiamo servendo il numero")
labell1 = Label( top_frame2, textvariable=varr1)
#labell1.config(width=200)
labell1.config(font=("Courier", 50))
labell1.grid(row=1, column=0,sticky="nsew")


###PROBLEMA-------------------------------------------------------------
var = StringVar()
label = Label( cnt_frame2, textvariable = var, relief = RAISED )
label.config(width=200)
label.config(font=("Courier", 200))
label.grid(row=1, column=0,sticky="nsew")
#label.pack()
###PROBLEMA--------------------------------------------------------

varr = StringVar()
varr.set(s)
labell = Label( btm_frame2, textvariable=varr, relief=RAISED )
labell.config(width=200)
labell.config(font=("Courier", 100))
#labell.pack()

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