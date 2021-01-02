from tkinter import Tk, Frame, X, Label, RIGHT, Button, StringVar, Entry, CENTER
from threading import Thread
from time import sleep
from math import factorial, sqrt, log, sin, cos, tan, pi

window = Tk()
window.resizable(False, False) 
window.title("Калькулятор")
window.configure(background='#222327')
window.overrideredirect(True)
 
font_very_small=("Montserrat Medium", 7)
font_small=("Montserrat Medium", 15)
font=("Montserrat Medium", 20)
bg="#222327" 
fg="#FFFFFF" 
fgs='#ff7336'  
height=58 
width=58 
border=23 
wind_height=667
wind_width=width*4+border*5
xwin = 0
ywin = 0
positionRight = int(window.winfo_screenwidth()/2 - wind_width/2)
positionDown = int(window.winfo_screenheight()/2 - wind_height/2)
maximised_value=str(width*8+border*8)+"x"+str(667)
window.geometry(str(wind_width)+'x'+str(wind_height)+"+{}+{}".format(positionRight, positionDown))
maxsize=False
true_focus=True

title_bar = Frame(window, bg=bg, height=35, border='0', bd=2)
title_bar.pack(fill=X)
Name = Label(title_bar, text='Калькулятор', border='0',font=("Montserrat Medium", 12), bg=bg, fg=fg)
Name.place(x=10, y=10)
frame=Frame(window, bg=bg)
frame.place(anchor='se', height=height*2+border*2, width=wind_width-border*2, x=wind_width-border, y=wind_height-border*6-height*5)
lablast = Label(text="", anchor='e', justify=RIGHT, bg=bg, fg='#6C6C6C', font=font_small, border='0')
lablast.place(anchor='ne',height=height-border, x=wind_width-border*2, y=wind_height-border*9-height*6) 
lab = Label(text="", anchor='e',  justify=RIGHT, bg=bg, fg=fg, font=("Montserrat Medium", 30), border='0') 
lab.place(anchor='ne',x=wind_width-border*2,y=wind_height-border*7-height*6, height=height) 

def deny_focus(event):
    global true_focus
    true_focus=False
def return_focus(event):
    global true_focus
    true_focus=True
    lab.focus_set()
    

def expand_window():
    global maxsize
    if maxsize==True:
        window.geometry(str(wind_width)+'x'+str(wind_height))
        ex_button.config(text='MORE')
        maxsize=False
    else:
        window.geometry(maximised_value)
        ex_button.config(text='LESS')
        maxsize=True
        title_bar.pack(fill=X)
ex_button = Button(text = "MORE",border='0', bg=bg,fg=fg, font=("Gotham Narrow Book", 10), command=expand_window)
ex_button.place(anchor='ne', x=wind_width- border, y=wind_height-border*6-height*5+1, height=15, width=45)

def hide():
    window.withdraw()
    window.overrideredirect(0)
    window.iconify()

def hide_event(event):
    window.withdraw()
    window.overrideredirect(0)
    window.iconify()

def show_screen(event):
    window.deiconify()
    window.overrideredirect(1)
    
close_button = Button(title_bar, text = "×",border='0', bg=bg,fg=fg, font=("Gotham Narrow Book", 10), command=window.destroy)
close_button.place(x=wind_width-15, y=10, height=15, width=15, anchor='ne')
min_button = Button(title_bar,text = "-",border='0', bg=bg, fg=fg, font=("Gotham Narrow Book", 10), command=hide)
min_button.place(x=wind_width-45, y=10, height=15, width=15, anchor='ne')

def get_pos(event):
    global xwin, ywin
    xwin = window.winfo_x()
    ywin = window.winfo_y()
    ywin-=event.y_root
    xwin-=event.x_root
def move_window(event):
    window.geometry(str(window.winfo_width())+'x'+str(window.winfo_height()) + '+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))

title_bar.bind('<Button-1>', get_pos)
title_bar.bind('<B1-Motion>', move_window)
title_bar.bind("<Map>", show_screen)
Name.bind('<Button-1>', get_pos)
Name.bind('<B1-Motion>', move_window)

l=[]
lastchari=len(l)-1

def zero_check():
    if l!=[]:
        if l[lastchari]!='0': add_digit(l,'0')
        else: error('Число не может начинатся с двух нулей')
    else: add_digit(l,'0') 

def dot_button():
    dot_already_found=False
    if l!=[]:
        for i in l[lastchari]:
            if i=='.':
                dot_already_found=True
        if dot_already_found==False:
            add_digit(l,'.')
        else: error('Нельзя ставить больше чем одной запятой в числе')
    else: error('Пустое уравнение')

def update_lab():
    string=''
    for i in l:
        string+=i
    if lab.winfo_width()>250:
        lab.config(font=font_small)
    elif len(string)<12:
        lab.config(font=("Gotham Narrow Book", 25))
    lab.config(text=string)

def add_digit(l, number):
    if len(l)!=0:
        if len(l)==1 and l[lastchari]=='-':
            l[lastchari]=l[lastchari]+number
        elif l[lastchari]=='-' and l[lastchari-1]=='(':
            l[lastchari]=l[lastchari]+number
        elif l[lastchari]!='0' or number=='.':
            if l[lastchari]=='-' or l[lastchari]=='*' or l[lastchari]=='+' or l[lastchari]=='/'or l[lastchari]=='(' or l[lastchari]==')':
                l.append(number)
            else: l[lastchari]=l[lastchari]+number
        else: error('Число не может начинатся с 2-х нулей')
    else: l.append(number)
    update_lab()
    print(l)

def add_symbol(l,number):
    if l==[] and number=='-' :
        l.append(number)
    else:
        if l!=[]:
            if number=='-' and l[lastchari]!='-' and l[lastchari]!='*' and l[lastchari]!='+' and l[lastchari]!='/':
                l.append(number)
            elif l[lastchari]!='-' and l[lastchari]!='*' and l[lastchari]!='+' and l[lastchari]!='/' and l[lastchari]!='(':
                l.append(number)
            else: error('Двойные символы')
        else: error('Нельзя поставить знак в начало')
    update_lab()
    print(l)

r_sk_counter=0 
l_sk_counter=0
def add_skobka(l,number):
    global r_sk_counter, l_sk_counter
    if number == '(':
        if l!=[]:
            if l[lastchari]!='-' and l[lastchari]!='*' and l[lastchari]!='+' and l[lastchari]!='/' and l[lastchari]!='(':
                l.append('*')
        l_sk_counter+=1
        l.append(number)
    elif number == ')':
        if l!=[]:
            if r_sk_counter<l_sk_counter:
                if l[lastchari]!='-' and l[lastchari]!='*' and l[lastchari]!='+' and l[lastchari]!='/' and l[lastchari]!='(':
                    r_sk_counter+=1
                    l.append(number)
                else: error('Нeльзя правую поставить скобку перед знаком')
            else: error('Лишняя правая скобка')
    update_lab()
    print(l)
def add_chislo(chislo):
    global l
    if round(chislo,7)%1==0:
        answer = round(float(chislo))
    else:
        answer = round(float(chislo),7)
    if l!=[]:
            if l[lastchari]!='-' and l[lastchari]!='*' and l[lastchari]!='+' and l[lastchari]!='/' :
                l.append('+')
                add_digit(l,str(answer))
            else:
                add_digit(l,str(answer))
    else:
        add_digit(l,str(answer))
    update_lab() 
def check_ckobki():
    global r_sk_counter,l_sk_counter
    if l_sk_counter==r_sk_counter: return True
    else: return False
def cancel_button():
    global l, r_sk_counter, l_sk_counter
    if l!=[]:
        if len(l[lastchari])!=1:
            l[lastchari] = l[lastchari][:-1]
        else:
            if l[lastchari]=='(':
                l_sk_counter-=1
            if l[lastchari]==')':
                r_sk_counter-=1
            del l[lastchari]
        print(l)    
        update_lab()
    else: error('Нечего стирать')
def acancel_button():
    global l
    if l!=[]:
        global r_sk_counter, l_sk_counter
        r_sk_counter=0
        l_sk_counter=0
        l.clear()
        lab.config(text=l)
        lablast.config(text='')
    else: 
        error('Нечего стирать')
def error(code):
    print(code)
    x = Thread(target=eeeee, args=(code,))
    x.start()
def eeeee(code):
    error_field.config(text=code)
    sleep(3)
    error_field.config(text='')
    
error_field=Label(text='', fg=fg, bg=bg)
error_field.place(anchor='sw', x=border, y=wind_height-border*6-height*5-1) 
def ravno_button(l):
    divide_by_zero=False
    for i in range(len(l)):
        if l[i]=='/' and l[i+1]=='0':
            divide_by_zero=True
            break
    if divide_by_zero==False:
        if check_ckobki()==False:
            error('Неравное количество парных скобок')
        else:
            last_ex='' 
            for i in l:
                last_ex+=i
            last_ex+='='
            answer = equals(l,'МАССИВ УРАВНЕНИЯ:')
            if answer!=None:
                lablast.config(text=last_ex)
                l[0]=answer
                update_lab()
                last_ex+=answer
                export_lines.append(last_ex)
    else: error('Нельзя делить на ноль')

def equals(l,nazva):
    lastchari=len(l)-1
    lfound=0
    rfound=0 
    print(nazva,l)
    for i in l:
        if i =='(':
            lfound+=1 
        if i ==')':
            rfound+=1
    if l==[] or l[lastchari]=='-' or l[lastchari]=='*' or l[lastchari]=='+' or l[lastchari]=='/' or l[lastchari][-1]=='.' :
        error('Недописанное уравнение')
    else:
        while len(l)!=1:
            lchecked=0
            rchecked=0
            templ=[]
            indexestodel=[]
            startcheck=False
            needs_to_del=False
            try:
                for i in range(len(l)):
                    if l[i]=='(':
                        lchecked+=1
                        if lchecked==1:
                            needs_to_del=True
                            firstskobka_index=i
                            startcheck=True
                            continue
                    if startcheck==True:
                        if l[i]==')':
                            rchecked+=1
                            if rchecked==rfound or rchecked==lchecked:
                                lastskobka_index=i
                                startcheck=False
                                l[firstskobka_index]=equals(templ,'МАССИВ СКОБОК:')
                                templ.clear()
                                for k in range(firstskobka_index, lastskobka_index):
                                    indexestodel.append(k+1)
                            else:
                                templ.append(l[i]) 
                        else:
                            templ.append(l[i])               
            except: pass
            indexestodel.reverse()
            if needs_to_del==True:
                try:
                    needs_to_del=False
                    for k in indexestodel:
                        del l[k]
                    print(nazva,'Массив для просчета',l)
                except: 
                    needs_to_del=False
            try:
                for i in range(len(l)):
                    if l[i]=='*':
                        l[i-1]=str(float(l[i-1])*float(l[i+1]))
                        del l[i]
                        del l[i]
                    if l[i]=='/':
                        l[i-1]=str(float(l[i-1])/float(l[i+1]))
                        del l[i]
                        del l[i]           
            except: pass
            try:
                for i in range(len(l)):
                    if l[i]=='+':
                        l[i-1]=str(float(l[i-1])+float(l[i+1]))
                        del l[i]
                        del l[i]
                    if l[i]=='-':
                        l[i-1]=str(float(l[i-1])-float(l[i+1]))
                        del l[i]
                        del l[i]
            except: pass
        print(nazva,'Решенный массив',l)
        if round(float(l[0]),7)%1==0:
            answer = round(float(l[0]))
        else:
            answer = round(float(l[0]),7)
        print('ОТВЕТ:',str(answer))
        return str(answer)


btn1 = Button(text="1", bg=bg, fg=fg, font=font, border='0', command=lambda: add_digit(l,'1'))
btn2 = Button(text="2", bg=bg, fg=fg, font=font, border='0', command=lambda: add_digit(l,'2'))
btn3 = Button(text="3", bg=bg, fg=fg, font=font, border='0', command=lambda: add_digit(l,'3'))
btn4 = Button(text="4", bg=bg, fg=fg, font=font, border='0', command=lambda: add_digit(l,'4'))
btn5 = Button(text="5", bg=bg, fg=fg, font=font, border='0', command=lambda: add_digit(l,'5'))
btn6 = Button(text="6", bg=bg, fg=fg, font=font, border='0', command=lambda: add_digit(l,'6'))
btn7 = Button(text="7", bg=bg, fg=fg, font=font, border='0', command=lambda: add_digit(l,'7'))
btn8 = Button(text="8", bg=bg, fg=fg, font=font, border='0', command=lambda: add_digit(l,'8'))
btn9 = Button(text="9", bg=bg, fg=fg, font=font, border='0', command=lambda: add_digit(l,'9'))
btn0 = Button(text="0", bg=bg, fg=fg, font=font, border='0', command=lambda: add_digit(l,'0'))
btnp = Button(text="+", bg=bg, fg=fgs, font=font, border='0', command=lambda: add_symbol(l,'+'))
btnmin = Button(text="-", bg=bg, fg=fgs, font=font, border='0', command=lambda: add_symbol(l,'-'))
btnd = Button(text="/", bg=bg, fg=fgs, font=font, border='0', command=lambda: add_symbol(l,'/'))
btnm = Button(text="*", bg=bg, fg=fgs, font=font, border='0', command=lambda: add_symbol(l,'*'))
btnr = Button(text="=", bg='#ff7336', fg=fg, font=font, border='0', command=lambda: ravno_button(l))
btnls = Button(text="(", bg=bg, fg=fgs, font=font, border='0', command=lambda: add_skobka(l,'('))
btnrs = Button(text=")", bg=bg, fg=fgs, font=font, border='0', command=lambda: add_skobka(l,')'))
btnac = Button(text="AC", bg=bg, fg=fgs, font=font, border='0', command=acancel_button)
btndot = Button(text=".", bg=bg, fg=fg, font=font, border='0', command=dot_button)
btnc = Button(text="С", bg=bg, fg=fgs, font=font, border='0', command=cancel_button)
btn1.place(anchor='sw', height=height, width=width, x=border, y=wind_height-border*2-height*1) 
btn2.place(anchor='sw', height=height, width=width, x=border*2+width*1, y=wind_height-border*2-height*1) 
btn3.place(anchor='sw', height=height, width=width, x=border*3+width*2, y=wind_height-border*2-height*1) 
btn4.place(anchor='sw', height=height, width=width, x=border, y=wind_height-border*3-height*2) 
btn5.place(anchor='sw', height=height, width=width, x=border*2+width*1, y=wind_height-border*3-height*2)
btn6.place(anchor='sw', height=height, width=width, x=border*3+width*2, y=wind_height-border*3-height*2)
btn7.place(anchor='sw', height=height, width=width, x=border, y=wind_height-border*4-height*3)
btn8.place(anchor='sw', height=height, width=width, x=border*2+width*1, y=wind_height-border*4-height*3)
btn9.place(anchor='sw', height=height, width=width, x=border*3+width*2, y=wind_height-border*4-height*3)
btn0.place(anchor='sw', height=height, width=width, x=border*2+width*1, y=wind_height-border)
btnp.place(anchor='sw', height=height, width=width, x=border*4+width*3, y=wind_height-border*2-height*1)
btnmin.place(anchor='sw', height=height, width=width, x=border*4+width*3, y=wind_height-border*3-height*2)
btnd.place(anchor='sw', height=height, width=width, x=border*4+width*3, y=wind_height-border*5-height*4)
btnm.place(anchor='sw', height=height, width=width, x=border*4+width*3, y=wind_height-border*4-height*3) 
btnr.place(anchor='sw', height=height, width=width, x=border*4+width*3, y=wind_height-border)
btnls.place(anchor='sw', height=height, width=width, x=border*2+width*1, y=wind_height-border*5-height*4)
btnrs.place(anchor='sw', height=height ,width=width, x=border*3+width*2, y=wind_height-border*5-height*4)
btnac.place(anchor='sw', height=height, width=width, x=border, y=wind_height-border*5-height*4)
btndot.place(anchor='sw', height=height, width=width, x=border*3+width*2, y=wind_height-border)
btnc.place(anchor='sw', height=height, width=width, x=border, y=wind_height-border)

line = Label(bg=fg, border='0')
line.place(height=1, anchor='sw', width=wind_width-border*2, x=border, y=wind_height-border*6-height*5)

lablast.bind("<Button-1>", return_focus)
lab.bind("<Button-1>", return_focus)
frame.bind("<Button-1>", return_focus)
def one_bind(event): 
    if true_focus==True: add_digit(l,'1')
window.bind("1", one_bind)
def two_bind(event): 
    if true_focus==True: add_digit(l,'2')
window.bind("2", two_bind)
def three_bind(event): 
    if true_focus==True: add_digit(l,'3')
window.bind("3", three_bind)
def four_bind(event): 
    if true_focus==True: add_digit(l,'4')
window.bind("4", four_bind)
def five_bind(event): 
    if true_focus==True: add_digit(l,'5')
window.bind("5", five_bind)
def six_bind(event): 
    if true_focus==True: add_digit(l,'6')
window.bind("6", six_bind)
def seven_bind(event): 
    if true_focus==True: add_digit(l,'7')
window.bind("7", seven_bind)
def eight_bind(event): 
    if true_focus==True: add_digit(l,'8')
window.bind("8", eight_bind)
def nine_bind(event): 
    if true_focus==True: add_digit(l,'9')
window.bind("9", nine_bind)
def zero_bind(event): 
    if true_focus==True: zero_check()
window.bind("0", zero_bind)
def plus_bind(event): 
    if true_focus==True: add_symbol(l,'+')
window.bind("+", plus_bind)
def minus_bind(event): 
    if true_focus==True: add_symbol(l,'-')
window.bind("-", minus_bind)
def mult_bind(event): 
    if true_focus==True: add_symbol(l,'*')
window.bind("*", mult_bind)
def divide_bind(event): 
    if true_focus==True: add_symbol(l,'/')
window.bind("/", divide_bind)
def lskobka_bind(event): 
    if true_focus==True: add_skobka(l,'(')
window.bind("(", lskobka_bind)
def rskobka_bind(event): 
    if true_focus==True: add_skobka(l,')')
window.bind(")", rskobka_bind)
def dot_bind(event): 
    if true_focus==True: dot_button()
window.bind(".", dot_bind)
def cancel_bind(event): 
    if true_focus==True: cancel_button()
window.bind("<BackSpace>", cancel_bind)
def enter_bind(event): 
    if true_focus==True: ravno_button(l)
window.bind("<Return>", enter_bind)
window.bind("=", enter_bind)

export_lines=['------------------------'] 
def export(export_lines):
    if len(export_lines)!=1:
        outF = open("export.txt", "a")
        for i in export_lines:
            outF.write(i+'\n')
        outF.close()
        error('Експортировано!')
        export_lines=['------------------------']
    else: error('Нечего экспортировать')
export_button = Button(text="Экспорт",anchor="w", border='0', font=font_very_small, bg=bg, fg='#6C6C6C', command=lambda: export(export_lines))
export_button.place(x=10, y=border*2)

def sqr():
    try:
        sq=sqrt(int(sqr_entry.get()))
        add_chislo(sq)
    except: error('Не удалось добыть корень')
def stepa():
    try:
        stepa=pow(int(step2_entry.get()),int(step1_entry.get()))
        add_chislo(stepa)
    except: error('Не удалось найти логарифм')
def fact():
    try:
        fact=factorial(int(factor_entry.get()))
        add_chislo(fact)
    except: error('Не удалось просчитать факторал')
def loga():
    try:
        print(int(log2_entry.get()))
        loga=log(int(log2_entry.get()),int(log1_entry.get()))
        add_chislo(loga)
    except: error('Не удалось найти логарифм')

sqr_entry = StringVar()
step1_entry = StringVar()
step2_entry = StringVar()
factor_entry = StringVar()
log1_entry = StringVar()
log2_entry = StringVar()
sqr_e = Entry(textvariable=sqr_entry, justify=CENTER, font=font, highlightthickness=2, bg=bg, fg=fg)
step1 = Entry(textvariable=step1_entry, justify=CENTER, font=font_small, highlightthickness=2, bg=bg, fg=fg)
step2 = Entry(textvariable=step2_entry, justify=CENTER, font=font, highlightthickness=2, bg=bg, fg=fg)
fact_e = Entry(textvariable=factor_entry, justify=CENTER, font=font, highlightthickness=2, bg=bg, fg=fg)
log1 = Entry(textvariable=log1_entry, justify=CENTER, font=font_small, highlightthickness=2, bg=bg, fg=fg)
log2 = Entry(textvariable=log2_entry, justify=CENTER, font=font, highlightthickness=2, bg=bg, fg=fg)
sqr_e.config(highlightbackground = "white", highlightcolor= "white")
step1.config(highlightbackground = "white", highlightcolor= "white")
step2.config(highlightbackground = "white", highlightcolor= "white")
fact_e.config(highlightbackground = "white", highlightcolor= "white")
log1.config(highlightbackground = "white", highlightcolor= "white")
log2.config(highlightbackground = "white", highlightcolor= "white")
sqr_e.place(width=width*2+border, height=height, x=wind_width, y=wind_height-border*8-height*7, anchor='sw')
step1.place(width=width/3*2, height=height/3*2, x=wind_width+border+width-2, y=wind_height-border*7-height*(6+1/3), anchor='sw')
step2.place(width=width, height=height, x=wind_width+border, y=wind_height-border*7-height*6, anchor='sw')
fact_e.place(width=width*2+border, height=height, x=wind_width, y=wind_height-border*6-height*5, anchor='sw')
log1.place(anchor='se', width=width/3*2, height=height/3*2, y=wind_height-border*5-height*4, x=wind_width+border+width+2)
log2.place(anchor='sw', width=width, height=height, y=wind_height-border*5-height*4, x=wind_width+border+width)
sqr_e.bind("<FocusIn>", deny_focus)
step1.bind("<FocusIn>", deny_focus)
step2.bind("<FocusIn>", deny_focus)
fact_e.bind("<FocusIn>", deny_focus)
log1.bind("<FocusIn>", deny_focus)
log2.bind("<FocusIn>", deny_focus)
sqr_e = Button(text="Add SQRT",bg="#333437", fg=fg, font=font_small, border='0', command=sqr)
stepb = Button(text="Add STEP",bg="#333437", fg=fg, font=font_small, border='0', command=stepa)
fact_e = Button(text="Add FAC",bg="#333437", fg=fg, font=font_small, border='0', command=fact)
logb = Button(text="Add LOG",bg="#333437", fg=fg, font=font_small, border='0', command=loga)
stepb.place(anchor='sw', width=width*2, height=height, x=wind_width+border*2+width*2, y=wind_height-border*7-height*6)
sqr_e.place(anchor='sw', width=width*2, height=height, x=wind_width+border*2+width*2, y=wind_height-border*8-height*7)
fact_e.place(anchor='sw', width=width*2, height=height, x=wind_width+border*2+width*2, y=wind_height-border*6-height*5,)
logb.place(anchor='sw', width=width*2, height=height, y=wind_height-border*5-height*4, x=wind_width+border*2+width*2)

ll = Label(text="log",bg=bg, fg=fg, font=("Montserrat Medium", 16), border='0')
ll.place(width=width/3*2, height=height, x=wind_width, y=wind_height-border*5-height*4, anchor='sw')

def add_sin():
    try:
        sin_c=sin(int(sin_entry.get())*pi/180) 
        add_chislo(sin_c)
    except: error('Не существует')
def add_cos():
    try:
        cos_c=cos(int(cos_entry.get())*pi/180)
        add_chislo(cos_c)
    except: error('Не существует')
def add_tg():
    try:
        tg_c=tan(int(tg_entry.get())*pi/180)
        add_chislo(tg_c)
    except: error('Не существует')
def add_ctg():
    try:
        ctg_c=cos(int(ctg_entry.get())*pi/180)/sin(int(ctg_entry.get())*pi/180)
        add_chislo(ctg_c)
    except: error('Не существует')


sin_entry = StringVar()
cos_entry = StringVar()
tg_entry = StringVar()
ctg_entry = StringVar()
sin_e = Entry(textvariable=sin_entry, justify=CENTER, font=font, highlightthickness=2, bg=bg, fg=fg)
cos_e = Entry(textvariable=cos_entry, justify=CENTER, font=font, highlightthickness=2, bg=bg, fg=fg)
tg_e = Entry(textvariable=tg_entry, justify=CENTER, font=font, highlightthickness=2, bg=bg, fg=fg)
ctg_e = Entry(textvariable=ctg_entry, justify=CENTER, font=font, highlightthickness=2, bg=bg, fg=fg)
sin_e.config(highlightbackground = "white", highlightcolor= "white")
cos_e.config(highlightbackground = "white", highlightcolor= "white")
tg_e.config(highlightbackground = "white", highlightcolor= "white")
ctg_e.config(highlightbackground = "white", highlightcolor= "white")
sin_e.place(width=width*2+border, height=height, x=wind_width, y=wind_height-border*4-height*3, anchor='sw')
cos_e.place(width=width*2+border, height=height, x=wind_width, y=wind_height-border*3-height*2, anchor='sw')
tg_e.place(width=width*2+border, height=height, x=wind_width, y=wind_height-border*2-height*1, anchor='sw')
ctg_e.place(width=width*2+border, height=height, x=wind_width, y=wind_height-border*1-height*0, anchor='sw')
sin_e.bind("<FocusIn>", deny_focus)
cos_e.bind("<FocusIn>", deny_focus)
tg_e.bind("<FocusIn>", deny_focus)
ctg_e.bind("<FocusIn>", deny_focus)
sin_b = Button(text="Add SIN",bg="#333437", fg=fg, font=font_small, border='0', command=add_sin)
cos_b = Button(text="Add COS",bg="#333437", fg=fg, font=font_small, border='0', command=add_cos)
tg_b = Button(text="Add TG", bg="#333437", fg=fg, font=font_small, border='0', command=add_tg)
ctg_b = Button(text="Add CTG",bg="#333437", fg=fg, font=font_small, border='0', command=add_ctg)
sin_b.place(anchor='sw', width=width*2, height=height, x=wind_width+border*2+width*2, y=wind_height-border*4-height*3)
cos_b.place(anchor='sw', width=width*2, height=height, x=wind_width+border*2+width*2, y=wind_height-border*3-height*2)
tg_b.place(anchor='sw', width=width*2, height=height, x=wind_width+border*2+width*2, y=wind_height-border*2-height*1)
ctg_b.place(anchor='sw', width=width*2, height=height, x=wind_width+border*2+width*2, y=wind_height-border*1-height*0,)
gradus1 = Label(text="О", bg=bg, fg=fg, font=("Montserrat Medium", 13), border='0')
gradus2 = Label(text="О", bg=bg, fg=fg, font=("Montserrat Medium", 13), border='0')
gradus3 = Label(text="О", bg=bg, fg=fg, font=("Montserrat Medium", 13), border='0')
gradus4 = Label(text="О", bg=bg, fg=fg, font=("Montserrat Medium", 13), border='0')
gradus1.place(anchor='ne', height=height/3,width=width/3, x=wind_width+width*2+border-5, y=wind_height-border*4-height*4+5)
gradus2.place(anchor='ne', height=height/3,width=width/3, x=wind_width+width*2+border-5, y=wind_height-border*3-height*3+5)
gradus3.place(anchor='ne', height=height/3,width=width/3, x=wind_width+width*2+border-5, y=wind_height-border*2-height*2+5)
gradus4.place(anchor='ne', height=height/3,width=width/3, x=wind_width+width*2+border-5, y=wind_height-border*1-height*1+5)


if __name__ == "__main__": window.mainloop()
