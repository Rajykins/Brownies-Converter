from tkinter import *           #GUI
import time
from PIL import Image, ImageTk  #To import cover photo --> pip/pillow
import ssl
import urllib.request as ur
import re
import json

root = Tk()

class mainWindow(Frame):            #Display main window
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Brownies Converters")        #Window title
        self.pack(fill=BOTH, expand=1)

        self.Img()
        root.after(6300, self.Buttons)
        
    def Buttons(self):
        startButton = Button(self, text="Start", command = self.start)
        startButton.place(x=295,y=400)

        quitbutton = Button(self, text="Quit Application", command=self.app_exit)
        quitbutton.place(x=260, y=450)

    def Img(self):                                  #Loading Screen
        load = Image.open("Logo_2.gif")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=120, y=0)
        root.after(700, self.Img2)
    def Img2(self):
        load = Image.open("Logo_2-2.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=120, y=0)
        root.after(700, self.Img3)
    def Img3(self):
        load = Image.open("Logo_2-3.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=120, y=0)
        root.after(700, self.Img4)
    def Img4(self):
        load = Image.open("Logo_2-4.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=120, y=0)
        root.after(700, self.Img5)
    def Img5(self):
        load = Image.open("Logo_2-5.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=120, y=0)
        root.after(700, self.Img6)
    def Img6(self):
        load = Image.open("Logo_2-6.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=120, y=0)
        root.after(700, self.Img7)
    def Img7(self):
        load = Image.open("Logo_2-7.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=120, y=0)
        root.after(700, self.Img8)
    def Img8(self):
        load = Image.open("Logo_2-8.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=120, y=0)
        root.after(700, self.Img9)
    def Img9(self):
        load = Image.open("Logo_2-9.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=120, y=0)
        
    def intro(self):
        intro1 = Label(root, text = "Welcome to Currency Converter, prsented by Brownies converters!")
        intro1.place(x=10, y=0)
        intro2 = Label(root, text = "Currencies are updated everyday at 3:00 PM")
        intro2.place(x=10, y=30)
        intro3 = Label(root, text = "Click proceed or Enter/Return to continue")
        intro3.place(x=10, y=60)
        e = Label(root, text="   ")
        intro1.place(x=10, y=90)
        
    def start(self):
        load = Image.open("bg.jpg")                 #Replace cover photo with background for
        photo = ImageTk.PhotoImage(load)            #aesthetics

        img = Label(self, image=photo)
        img.image = photo
        img.pack() 
        
        self.intro()
        global conget
        global toget

        OPTIONS = ["---", "CAD", "USD", "EUR", "INR", "JPY", "BRL", "GBP"]
        conget = StringVar(root)
        conget.set(OPTIONS[0])
        OPTIONS2 = ["---", "CAD", "USD", "EUR", "INR", "JPY", "BRL", "GBP"]
        toget = StringVar(root)
        toget.set(OPTIONS[0])
        
        con = Label(root, text="What currency do you want to convert from: ")
        con.place(x=50, y=145)
        var = OptionMenu(root, conget, *OPTIONS)
        var.place(x=370, y=145)

        to = Label(root, text="What currency do you want to convert to: ")
        to.place(x=50, y=185)
        var2 = OptionMenu(root, toget, *OPTIONS2)
        var2.place(x=370, y=185)

        convertButton = Button(self, text="Proceed", command=self.convert)
        convertButton.place(x=268, y=450)
        root.bind("<Return>", self.convertLink)
    def convertLink(self, event=None):
        self.convert()
    def convert(self):          #Loads conversion for user
        conget.get()
        toget.get()

        if conget.get() == "CAD" and toget.get() == "USD":
            self.CAD_to_USD()
        elif conget.get() == "CAD" and toget.get() == "EUR":
            self.CAD_to_EUR()
        elif conget.get() == "CAD" and toget.get() == "INR":
            self.CAD_to_INR()
        elif conget.get() == "CAD" and toget.get() == "JPY":
            self.CAD_to_JPY()
        elif conget.get() == "CAD" and toget.get() == "BRL":
            self.CAD_to_BRL()
        elif conget.get() == "CAD" and toget.get() == "GBP":
            self.CAD_to_GBP()
            
        elif conget.get() == "USD" and toget.get() == "CAD":
            self.USD_to_CAD()
        elif conget.get() == "USD" and toget.get() == "EUR":
            self.USD_to_EUR()
        elif conget.get() == "USD" and toget.get() == "INR":
            self.USD_to_INR()
        elif conget.get() == "USD" and toget.get() == "JPY":
            self.USD_to_JPY()
        elif conget.get() == "USD" and toget.get() == "BRL":
            self.USD_to_BRL()
        elif conget.get() == "USD" and toget.get() == "GBP":
            self.USD_to_GBP()
            
        elif conget.get() == "EUR" and toget.get() == "CAD":
            self.EUR_to_CAD()
        elif conget.get() == "EUR" and toget.get() == "USD":
            self.EUR_to_USD()
        elif conget.get() == "EUR" and toget.get() == "INR":
            self.EUR_to_INR()
        elif conget.get() == "EUR" and toget.get() == "JPY":
            self.EUR_to_JPY()
        elif conget.get() == "EUR" and toget.get() == "BRL":
            self.EUR_to_BRL()
        elif conget.get() == "EUR" and toget.get() == "GBP":
            self.EUR_to_GBP()

        elif conget.get() == "INR" and toget.get() == "CAD":
            self.INR_to_CAD()
        elif conget.get() == "INR" and toget.get() == "USD":
            self.INR_to_USD()
        elif conget.get() == "INR" and toget.get() == "EUR":
            self.INR_to_EUR()
        elif conget.get() == "INR" and toget.get() == "JPY":
            self.INR_to_JPY()
        elif conget.get() == "INR" and toget.get() == "BRL":
            self.INR_to_BRL()
        elif conget.get() == "INR" and toget.get() == "GBP":
            self.INR_to_GBP()
            
        elif conget.get() == "JPY" and toget.get() == "CAD":
            self.JPY_to_CAD()
        elif conget.get() == "JPY" and toget.get() == "USD":
            self.JPY_to_USD()
        elif conget.get() == "JPY" and toget.get() == "EUR":
            self.JPY_to_EUR()
        elif conget.get() == "JPY" and toget.get() == "INR":
            self.JPY_to_INR()
        elif conget.get() == "JPY" and toget.get() == "BRL":
            self.JPY_to_BRL()
        elif conget.get() == "JPY" and toget.get() == "GBP":
            self.JPY_to_GBP()
            
        elif conget.get() == "BRL" and toget.get() == "CAD":
            self.BRL_to_CAD()
        elif conget.get() == "BRL" and toget.get() == "USD":
            self.BRL_to_USD()
        elif conget.get() == "BRL" and toget.get() == "EUR":
            self.BRL_to_EUR()
        elif conget.get() == "BRL" and toget.get() == "INR":
            self.BRL_to_INR()
        elif conget.get() == "BRL" and toget.get() == "JPY":
            self.BRL_to_JPY()
        elif conget.get() == "BRL" and toget.get() == "GBP":
            self.BRL_to_GBP()

        elif conget.get() == "GBP" and toget.get() == "CAD":
            self.GBP_to_CAD()
        elif conget.get() == "GBP" and toget.get() == "USD":
            self.GBP_to_USD()
        elif conget.get() == "GBP" and toget.get() == "EUR":
            self.GBP_to_EUR()
        elif conget.get() == "GBP" and toget.get() == "INR":
            self.GBP_to_INR()
        elif conget.get() == "GBP" and toget.get() == "JPY":
            self.GBP_to_JPY()
        elif conget.get() == "GBP" and toget.get() == "BRL":
            self.GBP_to_BRL()
            
        elif conget.get() == "---" and toget.get() == "---":
            global pls
            pls = Label(self, text="Please choose currencies")
            pls.place(x=227, y=370)
            root.after(750, self.plsDestroy)
        else:
            error = Label(self, text="Sorry, Not Supported")
            error.place(x=240, y=370)
    def plsDestroy(self):
        pls.destroy()
    def again(self):                                            #convert again or not
        global ag
        again = Label(root, text="Would you like to convert again?")
        again.place(x=90, y=300)
        agButton = Button(self, text="Yes", command=self.ting)
        agButton.place(x=400, y=300)
        agButton2 = Button(self, text="No", command=self.endingTitle)
        agButton2.place(x=460, y=300)
    def ting(self):
        self.pack_forget()
        app=mainWindow(root)
            
    def CAD_to_USD(self):                                           #Conversion rates 
        global user_value
        user_ask = Label(root, text ="How many Canadian dollars? ")
        user_ask.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value.place(x=370, y=225)

        calcButton = Button(self, text=" Convert ", command=self.cal)
        calcButton.place(x=265, y=450)
        root.bind("<Return>", self.linkCal)
    def linkCal(self, event=None):
        self.cal()
    def cal(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        usd_rate = parsed["rates"]["USD"]

        val= float(user_value.get()) * (usd_rate)
        int(val)

        x = Label(root, text="USD: ")
        x.place(x=250, y=265)
        out = Label(root)
        out.config(text = '{:0.2f}'.format(val))
        out.place(x=380, y=265)
        self.again()

    def CAD_to_EUR(self):
        global user_value2
        user_ask2 = Label(root, text ="How many Canadian dollars? ")
        user_ask2.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value2 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value2.place(x=370, y=225)

        calcButton2 = Button(self, text=" Convert ", command=self.cal2)
        calcButton2.place(x=265, y=450)
        root.bind("<Return>", self.linkCal2)
    def linkCal2(self, event=None):
        self.cal2()
    def cal2(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        eur_rate = parsed["rates"]["EUR"]

        val2= float(user_value2.get()) * (eur_rate)
        int(val2)

        x2 = Label(root, text="EUR: ")
        x2.place(x=250, y=265)
        out2 = Label(root)
        out2.config(text = '{:0.2f}'.format(val2))
        out2.place(x=380, y=265)

        self.again()

    def CAD_to_INR(self):
        global user_value6
        user_ask6 = Label(root, text ="How many Canadian dollars? ")
        user_ask6.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value6 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value6.place(x=370, y=225)

        calcButton6 = Button(self, text=" Convert ", command=self.cal6)
        calcButton6.place(x=265, y=450)
        root.bind("<Return>", self.linkCal6)
    def linkCal6(self, event=None):
        self.cal6()
    def cal6(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        inr_rate = parsed["rates"]["INR"]

        val6= float(user_value6.get()) * (inr_rate)
        int(val6)

        x6 = Label(root, text="INR: ")
        x6.place(x=250, y=265)
        out6 = Label(root)
        out6.config(text = '{:0.2f}'.format(val6))
        out6.place(x=380, y=265)

        self.again()

    def CAD_to_JPY(self):
        global user_value12
        user_ask12 = Label(root, text ="How many Canadian dollars? ")
        user_ask12.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value12 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value12.place(x=370, y=225)

        calcButton12 = Button(self, text=" Convert ", command=self.cal12)
        calcButton12.place(x=265, y=450)
        root.bind("<Return>", self.linkCal12)
    def linkCal12(self, event=None):
        self.cal12()
    def cal12(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        jpy_rate = parsed["rates"]["JPY"]

        val12= float(user_value12.get()) * (jpy_rate)
        int(val12)

        x12 = Label(root, text="JPY: ")
        x12.place(x=250, y=265)
        out12 = Label(root)
        out12.config(text = '{:0.2f}'.format(val12))
        out12.place(x=380, y=265)

        self.again()

    def CAD_to_BRL(self):
        global user_value20
        user_ask20 = Label(root, text ="How many Canadian dollars? ")
        user_ask20.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value20 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value20.place(x=370, y=225)

        calcButton20 = Button(self, text=" Convert ", command=self.cal20)
        calcButton20.place(x=265, y=450)
        root.bind("<Return>", self.linkCal20)
    def linkCal20(self, event=None):
        self.cal20()
    def cal20(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        brl_rate = parsed["rates"]["BRL"]

        val20= float(user_value20.get()) * (brl_rate)
        int(val20)

        x20 = Label(root, text="BRL: ")
        x20.place(x=250, y=265)
        out20 = Label(root)
        out20.config(text = '{:0.2f}'.format(val20))
        out20.place(x=380, y=265)

        self.again()

    def CAD_to_GBP(self):
        global user_value29
        user_ask29 = Label(root, text ="How many Canadian dollars? ")
        user_ask29.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value29 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value29.place(x=370, y=225)

        calcButton29 = Button(self, text=" Convert ", command=self.cal29)
        calcButton29.place(x=265, y=450)
        root.bind("<Return>", self.linkCal29)
    def linkCal29(self, event=None):
        self.cal29()
    def cal29(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        gbp_rate = parsed["rates"]["GBP"]

        val29= float(user_value29.get()) * (gbp_rate)
        int(val29)

        x29 = Label(root, text="GBP: ")
        x29.place(x=250, y=265)
        out29 = Label(root)
        out29.config(text = '{:0.2f}'.format(val29))
        out29.place(x=380, y=265)

        self.again()

        
    def USD_to_CAD(self):
        global user_value1
        user_ask1 = Label(root, text ="How many US dollars? ")
        user_ask1.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value1 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value1.place(x=370, y=225)

        calcButton1 = Button(self, text=" Convert ", command=self.cal1)
        calcButton1.place(x=265, y=450)
        root.bind("<Return>", self.linkCal1)
    def linkCal1(self, event=None):
        self.cal1()
    def cal1(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        cad_rate = parsed["rates"]["CAD"]

        val1= float(user_value1.get()) * (cad_rate)
        int(val1)

        x1 = Label(root, text="CAD: ")
        x1.place(x=250, y=265)
        out1 = Label(root)
        out1.config(text = '{:0.2f}'.format(val1))
        out1.place(x=380, y=265)

        self.again()
        
    def USD_to_EUR(self):
        global user_value4
        user_ask4 = Label(root, text ="How many US Dollars? ")
        user_ask4.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value4 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value4.place(x=370, y=225)

        calcButton4 = Button(self, text=" Convert ", command=self.cal4)
        calcButton4.place(x=265, y=450)
        root.bind("<Return>", self.linkCal4)
    def linkCal4(self, event=None):
        self.cal4()
    def cal4(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        eur_rate = parsed["rates"]["EUR"]

        val4= float(user_value4.get()) * (eur_rate)
        int(val4)

        x4 = Label(root, text="EUR: ")
        x4.place(x=250, y=265)
        out4 = Label(root)
        out4.config(text = '{:0.2f}'.format(val4))
        out4.place(x=380, y=265)

        self.again()
        
    def USD_to_INR(self):
        global user_value8
        user_ask8 = Label(root, text ="How many US Dollars? ")
        user_ask8.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value8 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value8.place(x=370, y=225)

        calcButton8 = Button(self, text=" Convert ", command=self.cal8)
        calcButton8.place(x=265, y=450)
        root.bind("<Return>", self.linkCal8)
    def linkCal8(self, event=None):
        self.cal8()
    def cal8(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        inr_rate = parsed["rates"]["INR"]

        val8= float(user_value8.get()) * (inr_rate)
        int(val8)

        x8 = Label(root, text="INR: ")
        x8.place(x=250, y=265)
        out8 = Label(root)
        out8.config(text = '{:0.2f}'.format(val8))
        out8.place(x=380, y=265)

        self.again()

    def USD_to_JPY(self):
        global user_value13
        user_ask13 = Label(root, text ="How many US Dollars? ")
        user_ask13.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value13 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value13.place(x=370, y=225)

        calcButton13 = Button(self, text=" Convert ", command=self.cal13)
        calcButton13.place(x=265, y=450)
        root.bind("<Return>", self.linkCal13)
    def linkCal13(self, event=None):
        self.cal13()
    def cal13(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        jpy_rate = parsed["rates"]["JPY"]

        val13= float(user_value13.get()) * (jpy_rate)
        int(val13)

        x13 = Label(root, text="JPY: ")
        x13.place(x=250, y=265)
        out13 = Label(root)
        out13.config(text = '{:0.2f}'.format(val13))
        out13.place(x=380, y=265)

        self.again()

    def USD_to_BRL(self):
        global user_value21
        user_ask21 = Label(root, text ="How many US Dollars? ")
        user_ask21.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value21 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value21.place(x=370, y=225)

        calcButton21 = Button(self, text=" Convert ", command=self.cal21)
        calcButton21.place(x=265, y=450)
        root.bind("<Return>", self.linkCal21)
    def linkCal121(self, event=None):
        self.cal21()
    def cal21(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        brl_rate = parsed["rates"]["BRL"]

        val21= float(user_value21.get()) * (brl_rate)
        int(val21)

        x21 = Label(root, text="BRL: ")
        x21.place(x=250, y=265)
        out21 = Label(root)
        out21.config(text = '{:0.2f}'.format(val21))
        out21.place(x=380, y=265)

        self.again()

    def USD_to_GBP(self):
        global user_value30
        user_ask30 = Label(root, text ="How many US Dollars? ")
        user_ask30.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value30 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value30.place(x=370, y=225)

        calcButton30 = Button(self, text=" Convert ", command=self.cal30)
        calcButton30.place(x=265, y=450)
        root.bind("<Return>", self.linkCal30)
    def linkCal130(self, event=None):
        self.cal30()
    def cal30(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        gbp_rate = parsed["rates"]["GBP"]

        val30= float(user_value30.get()) * (gbp_rate)
        int(val30)

        x30 = Label(root, text="GBP: ")
        x30.place(x=250, y=265)
        out30 = Label(root)
        out30.config(text = '{:0.2f}'.format(val30))
        out30.place(x=380, y=265)

        self.again()
        

    def EUR_to_CAD(self):
        global user_value3
        user_ask3 = Label(root, text ="How many Euros? ")
        user_ask3.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value3 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value3.place(x=370, y=225)

        calcButton3 = Button(self, text=" Convert ", command=self.cal3)
        calcButton3.place(x=265, y=450)
        root.bind("<Return>", self.linkCal3)
    def linkCal3(self, event=None):
        self.cal3()
    def cal3(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        cad_rate = parsed["rates"]["CAD"]

        val3= float(user_value3.get()) * (cad_rate)
        int(val3)

        x3 = Label(root, text="CAD: ")
        x3.place(x=250, y=265)
        out3 = Label(root)
        out3.config(text = '{:0.2f}'.format(val3))
        out3.place(x=380, y=265)

        self.again()

    def EUR_to_USD(self):
        global user_value5
        user_ask5 = Label(root, text ="How many Euros? ")
        user_ask5.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value5 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value5.place(x=370, y=225)

        calcButton5 = Button(self, text=" Convert ", command=self.cal5)
        calcButton5.place(x=265, y=450)
        root.bind("<Return>", self.linkCal5)
    def linkCal5(self, event=None):
        self.cal5()
    def cal5(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        usd_rate = parsed["rates"]["USD"]

        val5= float(user_value5.get()) * (usd_rate)
        int(val5)

        x5 = Label(root, text="USD: ")
        x5.place(x=250, y=265)
        out5 = Label(root)
        out5.config(text = '{:0.2f}'.format(val5))
        out5.place(x=380, y=265)

        self.again()

    def EUR_to_INR(self):
        global user_value9
        user_ask9 = Label(root, text ="How many Euros? ")
        user_ask9.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value9 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value9.place(x=370, y=225)

        calcButton9 = Button(self, text=" Convert ", command=self.cal9)
        calcButton9.place(x=265, y=450)
        root.bind("<Return>", self.linkCal9)
    def linkCal9(self, event=None):
        self.cal9()
    def cal9(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        inr_rate = parsed["rates"]["INR"]

        val9= float(user_value9.get()) * (inr_rate)
        int(val9)

        x9 = Label(root, text="INR: ")
        x9.place(x=250, y=265)
        out9 = Label(root)
        out9.config(text = '{:0.2f}'.format(val9))
        out9.place(x=380, y=265)

        self.again()

    def EUR_to_JPY(self):
        global user_value14
        user_ask14 = Label(root, text ="How many Euros? ")
        user_ask14.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value14 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value14.place(x=370, y=225)

        calcButton14 = Button(self, text=" Convert ", command=self.cal14)
        calcButton14.place(x=265, y=450)
        root.bind("<Return>", self.linkCal14)
    def linkCal14(self, event=None):
        self.cal14()
    def cal14(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        jpy_rate = parsed["rates"]["JPY"]

        val14= float(user_value14.get()) * (jpy_rate)
        int(val14)

        x14 = Label(root, text="JPY: ")
        x14.place(x=250, y=265)
        out14 = Label(root)
        out14.config(text = '{:0.2f}'.format(val14))
        out14.place(x=380, y=265)

        self.again()

    def EUR_to_BRL(self):
        global user_value21
        user_ask21 = Label(root, text ="How many Euros? ")
        user_ask21.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value21 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value21.place(x=370, y=225)

        calcButton21 = Button(self, text=" Convert ", command=self.cal21)
        calcButton21.place(x=265, y=450)
        root.bind("<Return>", self.linkCal21)
    def linkCal21(self, event=None):
        self.cal21()
    def cal21(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        brl_rate = parsed["rates"]["BRL"]

        val21= float(user_value21.get()) * (brl_rate)
        int(val21)

        x21 = Label(root, text="BRL: ")
        x21.place(x=250, y=265)
        out21 = Label(root)
        out21.config(text = '{:0.2f}'.format(val21))
        out21.place(x=380, y=265)

        self.again()

    def EUR_to_GBP(self):
        global user_value31
        user_ask31 = Label(root, text ="How many Euros? ")
        user_ask31.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value31 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value31.place(x=370, y=225)

        calcButton31 = Button(self, text=" Convert ", command=self.cal31)
        calcButton31.place(x=265, y=450)
        root.bind("<Return>", self.linkCal31)
    def linkCal131(self, event=None):
        self.cal31()
    def cal31(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        gbp_rate = parsed["rates"]["GBP"]

        val31= float(user_value31.get()) * (gbp_rate)
        int(val31)

        x31 = Label(root, text="GBP: ")
        x31.place(x=250, y=265)
        out31 = Label(root)
        out31.config(text = '{:0.2f}'.format(val31))
        out31.place(x=380, y=265)

        self.again()
        
        
    def INR_to_CAD(self):
        global user_value7
        user_ask7 = Label(root, text ="How many Indian Rs? ")
        user_ask7.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value7 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value7.place(x=370, y=225)

        calcButton7 = Button(self, text=" Convert ", command=self.cal7)
        calcButton7.place(x=265, y=450)
        root.bind("<Return>", self.linkCal7)
    def linkCal7(self, event=None):
        self.cal7()
    def cal7(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        cad_rate = parsed["rates"]["CAD"]

        val7= float(user_value7.get()) * (cad_rate)
        int(val7)

        x7 = Label(root, text="CAD: ")
        x7.place(x=250, y=265)
        out7 = Label(root)
        out7.config(text = '{:0.2f}'.format(val7))
        out7.place(x=380, y=265)

        self.again()

    def INR_to_USD(self):
        global user_value10
        user_ask10 = Label(root, text ="How many Indian Rs? ")
        user_ask10.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value10 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value10.place(x=370, y=225)

        calcButton10 = Button(self, text=" Convert ", command=self.cal10)
        calcButton10.place(x=265, y=450)
        root.bind("<Return>", self.linkCal10)
    def linkCal10(self, event=None):
        self.cal10()
    def cal10(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        usd_rate = parsed["rates"]["USD"]

        val10= float(user_value10.get()) * (usd_rate)
        int(val10)

        x10 = Label(root, text="USD: ")
        x10.place(x=250, y=265)
        out10 = Label(root)
        out10.config(text = '{:0.2f}'.format(val10))
        out10.place(x=380, y=265)

        self.again()

    def INR_to_EUR(self):
        global user_value11
        user_ask11 = Label(root, text ="How many Indian Rs? ")
        user_ask11.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value11 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value11.place(x=370, y=225)

        calcButton11 = Button(self, text=" Convert ", command=self.cal11)
        calcButton11.place(x=265, y=450)
        root.bind("<Return>", self.linkCal11)
    def linkCal11(self, event=None):
        self.cal11()
    def cal11(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        eur_rate = parsed["rates"]["EUR"]

        val11= float(user_value11.get()) * (eur_rate)
        int(val11)

        x11 = Label(root, text="EUR: ")
        x11.place(x=250, y=265)
        out11 = Label(root)
        out11.config(text = '{:0.2f}'.format(val11))
        out11.place(x=380, y=265)

        self.again()

    def INR_to_JPY(self):
        global user_value15
        user_ask15 = Label(root, text ="How many Indian Rs? ")
        user_ask15.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value15 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value15.place(x=370, y=225)

        calcButton15 = Button(self, text=" Convert ", command=self.cal15)
        calcButton15.place(x=265, y=450)
        root.bind("<Return>", self.linkCal15)
    def linkCal15(self, event=None):
        self.cal15()
    def cal15(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        jpy_rate = parsed["rates"]["JPY"]

        val15= float(user_value15.get()) * (jpy_rate)
        int(val15)

        x15 = Label(root, text="JPY: ")
        x15.place(x=250, y=265)
        out15 = Label(root)
        out15.config(text = '{:0.2f}'.format(val15))
        out15.place(x=380, y=265)

        self.again()

    def INR_to_BRL(self):
        global user_value22
        user_ask2 = Label(root, text ="How many Indian Rs? ")
        user_ask22.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value22 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value22.place(x=370, y=225)

        calcButton22 = Button(self, text=" Convert ", command=self.cal22)
        calcButton22.place(x=265, y=450)
        root.bind("<Return>", self.linkCal22)
    def linkCal22(self, event=None):
        self.cal22()
    def cal22(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        brl_rate = parsed["rates"]["BRL"]

        val22= float(user_value22.get()) * (brl_rate)
        int(val22)

        x22 = Label(root, text="BRL: ")
        x22.place(x=250, y=265)
        out22 = Label(root)
        out22.config(text = '{:0.2f}'.format(val22))
        out22.place(x=380, y=265)

        self.again()

    def INR_to_GBP(self):
        global user_value32
        user_ask32 = Label(root, text ="How many Indian Rs? ")
        user_ask32.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value32 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value32.place(x=370, y=225)

        calcButton32 = Button(self, text=" Convert ", command=self.cal32)
        calcButton32.place(x=265, y=450)
        root.bind("<Return>", self.linkCal32)
    def linkCal32(self, event=None):
        self.cal32()
    def cal32(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        gbp_rate = parsed["rates"]["GBP"]

        val32= float(user_value32.get()) * (gbp_rate)
        int(val32)

        x32 = Label(root, text="GBP: ")
        x32.place(x=250, y=265)
        out32 = Label(root)
        out32.config(text = '{:0.2f}'.format(val32))
        out32.place(x=380, y=265)

        self.again()
        

    def JPY_to_CAD(self):
        global user_value16
        user_ask16 = Label(root, text ="How many Japanese Yen? ")
        user_ask16.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value16 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value16.place(x=370, y=225)

        calcButton16 = Button(self, text=" Convert ", command=self.cal16)
        calcButton16.place(x=265, y=450)
        root.bind("<Return>", self.linkCal16)
    def linkCal16(self, event=None):
        self.cal16()
    def cal16(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        cad_rate = parsed["rates"]["CAD"]

        val16= float(user_value16.get()) * (cad_rate)
        int(val16)

        x16 = Label(root, text="CAD: ")
        x16.place(x=250, y=265)
        out16 = Label(root)
        out16.config(text = '{:0.2f}'.format(val16))
        out16.place(x=380, y=265)

        self.again()

    def JPY_to_USD(self):
        global user_value17
        user_ask17 = Label(root, text ="How many Japanese Yen? ")
        user_ask17.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value17 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value17.place(x=370, y=225)

        calcButton17 = Button(self, text=" Convert ", command=self.cal17)
        calcButton17.place(x=265, y=450)
        root.bind("<Return>", self.linkCal17)
    def linkCal17(self, event=None):
        self.cal17()
    def cal17(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        usd_rate = parsed["rates"]["USD"]

        val17= float(user_value17.get()) * (usd_rate)
        int(val17)

        x17 = Label(root, text="USD: ")
        x17.place(x=250, y=265)
        out17 = Label(root)
        out17.config(text = '{:0.2f}'.format(val17))
        out17.place(x=380, y=265)

        self.again()

    def JPY_to_EUR(self):
        global user_value18
        user_ask18 = Label(root, text ="How many Japanese Yen? ")
        user_ask18.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value18 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value18.place(x=370, y=225)

        calcButton18 = Button(self, text=" Convert ", command=self.cal18)
        calcButton18.place(x=265, y=450)
        root.bind("<Return>", self.linkCal18)
    def linkCal18(self, event=None):
        self.cal18()
    def cal18(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        eur_rate = parsed["rates"]["EUR"]

        val18= float(user_value18.get()) * (eur_rate)
        int(val18)

        x18 = Label(root, text="EUR: ")
        x18.place(x=250, y=265)
        out18 = Label(root)
        out18.config(text = '{:0.2f}'.format(val18))
        out18.place(x=380, y=265)

        self.again()

    def JPY_to_INR(self):
        global user_value19
        user_ask19 = Label(root, text ="How many Japanese Yen? ")
        user_ask19.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value19 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value19.place(x=370, y=225)

        calcButton19 = Button(self, text=" Convert ", command=self.cal19)
        calcButton19.place(x=265, y=450)
        root.bind("<Return>", self.linkCal19)
    def linkCal19(self, event=None):
        self.cal19()
    def cal19(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        inr_rate = parsed["rates"]["INR"]

        val19= float(user_value19.get()) * (inr_rate)
        int(val19)

        x19 = Label(root, text="INR: ")
        x19.place(x=250, y=265)
        out19 = Label(root)
        out19.config(text = '{:0.2f}'.format(val19))
        out19.place(x=380, y=265)

        self.again()

    def JPY_to_BRL(self):
        global user_value23
        user_ask23 = Label(root, text ="How many Japanese Yen? ")
        user_ask23.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value23 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value23.place(x=370, y=225)

        calcButton23 = Button(self, text=" Convert ", command=self.cal23)
        calcButton23.place(x=265, y=450)
        root.bind("<Return>", self.linkCal23)
    def linkCal23(self, event=None):
        self.cal23()
    def cal23(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        brl_rate = parsed["rates"]["BRL"]

        val23= float(user_value23.get()) * (brl_rate)
        int(val23)

        x23 = Label(root, text="BRL: ")
        x23.place(x=250, y=265)
        out23 = Label(root)
        out23.config(text = '{:0.2f}'.format(val23))
        out23.place(x=380, y=265)

        self.again()

    def JPY_to_GBP(self):
        global user_value33
        user_ask33 = Label(root, text ="How many Japanese Yen? ")
        user_ask33.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value33 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value33.place(x=370, y=225)

        calcButton33 = Button(self, text=" Convert ", command=self.cal33)
        calcButton33.place(x=265, y=450)
        root.bind("<Return>", self.linkCal33)
    def linkCal33(self, event=None):
        self.cal33()
    def cal33(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        gbp_rate = parsed["rates"]["GBP"]

        val33= float(user_value33.get()) * (gbp_rate)
        int(val33)

        x33 = Label(root, text="GBP: ")
        x33.place(x=250, y=265)
        out33 = Label(root)
        out33.config(text = '{:0.2f}'.format(val33))
        out33.place(x=380, y=265)

        self.again()
        

    def BRL_to_CAD(self):
        global user_value24
        user_ask24 = Label(root, text ="How many Brazilian Reals? ")
        user_ask24.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value24 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value24.place(x=370, y=225)

        calcButton24 = Button(self, text=" Convert ", command=self.cal24)
        calcButton24.place(x=265, y=450)
        root.bind("<Return>", self.linkCal24)
    def linkCal24(self, event=None):
        self.cal24()
    def cal24(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        cad_rate = parsed["rates"]["CAD"]

        val24= float(user_value24.get()) * (cad_rate)
        int(val24)

        x24 = Label(root, text="CAD: ")
        x24.place(x=250, y=265)
        out24 = Label(root)
        out24.config(text = '{:0.2f}'.format(val24))
        out24.place(x=380, y=265)

        self.again()

    def BRL_to_USD(self):
        global user_value25
        user_ask25 = Label(root, text ="How many Brazilian Reals? ")
        user_ask25.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value25 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value25.place(x=370, y=225)

        calcButton25 = Button(self, text=" Convert ", command=self.cal25)
        calcButton25.place(x=265, y=450)
        root.bind("<Return>", self.linkCal24)
    def linkCal25(self, event=None):
        self.cal25()
    def cal25(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        usd_rate = parsed["rates"]["USD"]

        val25= float(user_value25.get()) * (usd_rate)
        int(val25)

        x25 = Label(root, text="USD: ")
        x25.place(x=250, y=265)
        out25 = Label(root)
        out25.config(text = '{:0.2f}'.format(val25))
        out25.place(x=380, y=265)

        self.again()

    def BRL_to_EUR(self):
        global user_value26
        user_ask26 = Label(root, text ="How many Brazilian Reals? ")
        user_ask26.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value26 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value26.place(x=370, y=225)

        calcButton26 = Button(self, text=" Convert ", command=self.cal26)
        calcButton26.place(x=265, y=450)
        root.bind("<Return>", self.linkCal26)
    def linkCal26(self, event=None):
        self.cal26()
    def cal26(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        eur_rate = parsed["rates"]["EUR"]

        val26= float(user_value26.get()) * (eur_rate)
        int(val26)

        x26 = Label(root, text="EUR: ")
        x26.place(x=250, y=265)
        out26 = Label(root)
        out26.config(text = '{:0.2f}'.format(val26))
        out26.place(x=380, y=265)

        self.again()

    def BRL_to_INR(self):
        global user_value27
        user_ask27 = Label(root, text ="How many Brazilian Reals? ")
        user_ask27.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value27 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value27.place(x=370, y=225)

        calcButton27 = Button(self, text=" Convert ", command=self.cal27)
        calcButton27.place(x=265, y=450)
        root.bind("<Return>", self.linkCal27)
    def linkCal27(self, event=None):
        self.cal27()
    def cal27(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        inr_rate = parsed["rates"]["INR"]

        val27= float(user_value27.get()) * (inr_rate)
        int(val27)

        x27 = Label(root, text="INR: ")
        x27.place(x=250, y=265)
        out27 = Label(root)
        out27.config(text = '{:0.2f}'.format(val27))
        out27.place(x=380, y=265)
        self.again()

    def BRL_to_JPY(self):
        global user_value28
        user_ask28 = Label(root, text ="How many Brazilian Reals? ")
        user_ask28.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value28 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value28.place(x=370, y=225)

        calcButton28 = Button(self, text=" Convert ", command=self.cal28)
        calcButton28.place(x=265, y=450)
        root.bind("<Return>", self.linkCal28)
    def linkCal28(self, event=None):
        self.cal28()
    def cal28(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        jpy_rate = parsed["rates"]["JPY"]

        val28= float(user_value28.get()) * (jpy_rate)
        int(val28)

        x28 = Label(root, text="JPY: ")
        x28.place(x=250, y=265)
        out28 = Label(root)
        out28.config(text = '{:0.2f}'.format(val28))
        out28.place(x=380, y=265)
        self.again()

    def BRL_to_GBP(self):
        global user_value34
        user_ask34 = Label(root, text ="How many Brazilian Reals? ")
        user_ask34.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value34 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value34.place(x=370, y=225)

        calcButton34 = Button(self, text=" Convert ", command=self.cal34)
        calcButton34.place(x=265, y=450)
        root.bind("<Return>", self.linkCal34)
    def linkCal34(self, event=None):
        self.cal34()
    def cal34(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        gbp_rate = parsed["rates"]["GBP"]

        val34= float(user_value34.get()) * (gbp_rate)
        int(val34)

        x34 = Label(root, text="GBP: ")
        x34.place(x=250, y=265)
        out34 = Label(root)
        out34.config(text = '{:0.2f}'.format(val34))
        out34.place(x=380, y=265)

        self.again()


    def GBP_to_CAD(self):
        global user_value35
        user_ask35 = Label(root, text ="How many Great Britain Pounds? ")
        user_ask35.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value35 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value35.place(x=370, y=225)

        calcButton35 = Button(self, text=" Convert ", command=self.cal35)
        calcButton35.place(x=265, y=450)
        root.bind("<Return>", self.linkCal35)
    def linkCal35(self, event=None):
        self.cal35()
    def cal35(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        cad_rate = parsed["rates"]["CAD"]

        val35= float(user_value35.get()) * (cad_rate)
        int(val35)

        x35 = Label(root, text="CAD: ")
        x35.place(x=250, y=265)
        out35 = Label(root)
        out35.config(text = '{:0.2f}'.format(val35))
        out35.place(x=380, y=265)

        self.again()

    def GBP_to_USD(self):
        global user_value36
        user_ask36 = Label(root, text ="How many Great Britain Pounds? ")
        user_ask36.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value36 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value36.place(x=370, y=225)

        calcButton36 = Button(self, text=" Convert ", command=self.cal36)
        calcButton36.place(x=265, y=450)
        root.bind("<Return>", self.linkCal36)
    def linkCal36(self, event=None):
        self.cal36()
    def cal36(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        usd_rate = parsed["rates"]["USD"]

        val36= float(user_value36.get()) * (usd_rate)
        int(val36)

        x36 = Label(root, text="USD: ")
        x36.place(x=250, y=265)
        out36 = Label(root)
        out36.config(text = '{:0.2f}'.format(val36))
        out36.place(x=380, y=265)

        self.again()

    def GBP_to_EUR(self):
        global user_value37
        user_ask37 = Label(root, text ="How many Great Britain Pounds? ")
        user_ask37.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value37 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value37.place(x=370, y=225)

        calcButton37 = Button(self, text=" Convert ", command=self.cal37)
        calcButton37.place(x=265, y=450)
        root.bind("<Return>", self.linkCal37)
    def linkCal37(self, event=None):
        self.cal37()
    def cal37(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        eur_rate = parsed["rates"]["EUR"]

        val37= float(user_value37.get()) * (eur_rate)
        int(val37)

        x37 = Label(root, text="EUR: ")
        x37.place(x=250, y=265)
        out37 = Label(root)
        out37.config(text = '{:0.2f}'.format(val37))
        out37.place(x=380, y=265)

        self.again()

    def GBP_to_INR(self):
        global user_value38
        user_ask38 = Label(root, text ="How many Great Britain Pounds? ")
        user_ask38.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value38 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value38.place(x=370, y=225)

        calcButton38 = Button(self, text=" Convert ", command=self.cal38)
        calcButton38.place(x=265, y=450)
        root.bind("<Return>", self.linkCal38)
    def linkCal38(self, event=None):
        self.cal38()
    def cal38(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        inr_rate = parsed["rates"]["INR"]

        val38= float(user_value38.get()) * (inr_rate)
        int(val38)

        x38 = Label(root, text="INR: ")
        x38.place(x=250, y=265)
        out38 = Label(root)
        out38.config(text = '{:0.2f}'.format(val38))
        out38.place(x=380, y=265)

        self.again()

    def GBP_to_JPY(self):
        global user_value39
        user_ask39 = Label(root, text ="How many Great Britain Pounds? ")
        user_ask39.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value39 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value39.place(x=370, y=225)

        calcButton39 = Button(self, text=" Convert ", command=self.cal39)
        calcButton39.place(x=265, y=450)
        root.bind("<Return>", self.linkCal39)
    def linkCal39(self, event=None):
        self.cal39()
    def cal39(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        jpy_rate = parsed["rates"]["JPY"]

        val39= float(user_value39.get()) * (jpy_rate)
        int(val39)

        x39 = Label(root, text="JPY: ")
        x39.place(x=250, y=265)
        out39 = Label(root)
        out39.config(text = '{:0.2f}'.format(val39))
        out39.place(x=380, y=265)

        self.again()

    def GBP_to_BRL(self):
        global user_value40
        user_ask40 = Label(root, text ="How many Great Britain Pounds? ")
        user_ask40.place(x=130, y= 225)
        vcmd = root.register(self.validate)
        user_value40 = Entry(root, validate = "key", validatecommand=(vcmd, "%P"))
        user_value40.place(x=370, y=225)

        calcButton40 = Button(self, text=" Convert ", command=self.cal40)
        calcButton40.place(x=265, y=450)
        root.bind("<Return>", self.linkCal40)
    def linkCal40(self, event=None):
        self.cal40()
    def cal40(self):
        context = ssl._create_unverified_context() #allow for unverified link
        fixerdata = ur.urlopen("https://api.fixer.io/latest?base={}".format(conget.get()), context=context)

        data = fixerdata.read().decode('utf-8') #Read link
        parsed = json.loads(data)
        date = parsed["date"] #import date
        rates = parsed["rates"] #import rates
        brl_rate = parsed["rates"]["BRL"]

        val40= float(user_value40.get()) * (brl_rate)
        int(val40)

        x40 = Label(root, text="BRL: ")
        x40.place(x=250, y=265)
        out40 = Label(root)
        out40.config(text = '{:0.2f}'.format(val40))
        out40.place(x=380, y=265)

        self.again()
        
    def validate(self, new_text):           #currency value validation (float -->  vcmd)
        if new_text == "-":
            return True
        elif not new_text:
            return True

        try:
            self.entered_number=float(new_text)
            return True
        except ValueError:
            return False
        
    def app_exit(self):                             #Exit app
        exit()

    def endingTitle(self):                          #Ending title
        endTitle = Label(self, text="Thank you for using Currency Converter")
        endTitle.place(x=200, y=335)
        subTitle = Label(self, text="Presented by Brownies Converters")
        subTitle.place(x=220, y=370)
        lastTitle = Label(self, text="App will close in 3 seconds...")
        lastTitle.place(x=235, y=400)
        
        root.after(1000, self.lastTitle2)
        root.after(2000, self.lastTitle3)
        root.after(3000, self.app_exit)
    def lastTitle2(self):
        lastTitle = Label(self, text="App will close in 2 seconds...")
        lastTitle.place(x=235, y=400)
    def lastTitle3(self):
        lastTitle = Label(self, text="App will close in 1 seconds...")
        lastTitle.place(x=235, y=400)

root.geometry("650x500")        #Display size
app = mainWindow(root)

root.mainloop()
