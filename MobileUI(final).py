import pandas as pd
from joblib import load

reg=load("regress.joblib")
sc=load("scaler.joblib")
    
def display():
    sim1=a2.get()
    if sim1=='Yes':
        sim2=1
    else:
        sim2=0
      
    four1 = a3.get()
    if four1 =='Yes':
        four2=1
    else:
        four2=0
        
        
    three1 = a7.get()
    if three1 =='Yes':
        three2=1
    else:
        three2=0
        
        
        
    touch1 = a8.get()
    if touch1 =='Yes':
        touch2=1
    else:
        touch2=0
        
        
        
    wifi1 = a9.get()
    if wifi1 =='Yes':
        wifi2=1
    else:
        wifi2=0
        
  
    
  
    df = pd.DataFrame({"battery power":[int(a1.get())],"dual sim":[(sim2)]
                   ,"four g":[(four2)],"int memory":[int(a4.get())],
                   "n cores":[int(a5.get())],"ram":[int(a6.get())],
                   "three g":[(three2)],"touch screen":[(touch2)],
                   "wifi":[(wifi2)]})
    
    print(df)
    df=sc.transform(df)
    ony=(reg.predict(df))
    l.config(text=ony[0])
    


    z1=Tk()
    z1.resizable(0,0)
    if ony == 0:
        ony = ("Mobile Price Ranges below : 10000")
    elif ony == 1:
        ony = ("Mobile Price Ranges between 10000 to 20000")
    else:
        ony = ("Mobile Price Ranges above : 30000")
        
    

    
    result=Label(z1,text=ony,font=("ARIAL",35,"bold"),fg="white", bg="black")
    result.pack()








from tkinter import *
root=Tk() 
root.geometry("800x500")
root.title("Mobile Price Range")

photo = PhotoImage(file = "155901.png",master=root)
aLabel = Label(root,image=photo)
aLabel.pack()


a1 = StringVar()
a2 = StringVar(root)
a3 = StringVar(root)
a4 = StringVar()
a5 = StringVar()
a6 = StringVar()
a7 = StringVar(root)
a8 = StringVar(root)
a9 = StringVar(root)

label_head=Label(root,text="Price Prediction for Mobile Phones",font=("ARIAL",18,"bold")).place(x=15,y=5)


battery_power = Entry(root,textvariable=a1,width = 15).place(x=280,y=55)
l1 = Label(root,text = "Enter Battery power(in mAh)",font=("Comic Sans MS",12) ).place(x=10,y=50)


dual_sim = Label(root,text="Dual Sim Yes/No",width = 15,font=("Comic Sans MS",12)).place(x=0,y=90)
simlist=['Yes','No']
a2.set('Dual Sim Available or not')
l2 = OptionMenu(root,a2,*simlist).place(x=280,y=95)

four_g = Label(root,text = "4G Enabled or not",font=("Comic Sans MS",12) ).place(x=10,y=130)
fourlist=['Yes','No']
a3.set('4G enabled or not')
l3 = OptionMenu(root,a3,*fourlist).place(x=280,y=135)


three_g = Label(root,text = "3G Enabled or not",font=("Comic Sans MS",12) ).place(x=10,y=290)
threelist=['Yes','No']
a7.set('3G enabled or not')
l7 = OptionMenu(root,a7,*threelist).place(x=280,y=295)


touch_screen = Label(root,text = "Touch Screen Available or not",font=("Comic Sans MS",12) ).place(x=10,y=330)
touchlist=['Yes','No']
a8.set('Touch enabled or not')
l8 = OptionMenu(root,a8,*touchlist).place(x=280,y=335)


wifi = Label(root,text = "Wifi Available or not",font=("Comic Sans MS",12) ).place(x=10,y=370)
wifilist=['Yes','No']
a9.set('Wifi enabled or not')
l9 = OptionMenu(root,a9,*wifilist).place(x=280,y=375)


int_memory = Entry(root,textvariable=a4,width = 15).place(x=280,y=175)
l4 = Label(root,text = "Enter Internal Memory (in GB)",font=("Comic Sans MS",12) ).place(x=10,y=170)


n_cores = Entry(root,textvariable=a5,width = 15).place(x=280,y=215)
l5 = Label(root,text = "Enter Number of Cores",font=("Comic Sans MS",12) ).place(x=10,y=210)

ram = Entry(root,textvariable=a6,width = 15).place(x=280,y=255)
l6 = Label(root,text = "Enter Ram (in MB)",font=("Comic Sans MS",12) ).place(x=10,y=250)


submit = Button(root,text = "Check",bg="Grey",width = 15,command= display).place(x=200,y=450)


l=Label(root)
l.place(x=600,y=500)

root.mainloop()

