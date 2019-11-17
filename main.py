from tkinter import*
import random
import time
import datetime

root=Tk()
root.geometry("900x650")#size
root.title("A&W Restaurant")

Tops=Frame(root, width=1500)
Tops.pack(side=TOP)

winFrame=Frame(root,width=800,height=700)
winFrame.pack(side=LEFT)

# get time
localtime=time.asctime(time.localtime(time.time()))
# Top window label
lblInfo=Label(Tops,font=('times new roman',50,'bold'),text="A&W Restaurant",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo=Label(Tops,font=('times new roman',20,'bold'),text=localtime,fg="Black",bd=10,anchor='w')
lblInfo.grid(row=1,column=0)

def Ref():
    x=random.randint(100,50000)
    randomRef=str(x)
    rand.set(randomRef)

    if (Teen.get()==""):
        teenCost=0
    else:
        teenCost = float(Teen.get())

    if (CBUncle.get()==""):
        cbUncleCost=0
    else:
        cbUncleCost = float(CBUncle.get())
        

    if (Fries.get()==""):
        friesCost=0
    else:
        friesCost=float(Fries.get())


    if (Float.get()==""):
        floatCost=0
    else:
        floatCost=float(Float.get())


    if (Coffee.get()==""):
        coffeeCost=0
    else:
        coffeeCost=float(Coffee.get())


    if (Chicken.get()==""):
        chickenCost=0
    else:
        chickenCost=float(Chicken.get())

        
    if (BaconEgger.get()==""):
        bacconEggerCost=0
    else:
        bacconEggerCost=float(BaconEgger.get())

     
    if (Drinks.get()==""):
        drinkCost=0
    else:
        drinkCost=float(Drinks.get())
# se cost
    CostofTeen= teenCost * 6.49
    CostofCBUncle= cbUncleCost * 8.49
    CostofFries =friesCost * 2.99
    CostofDrinks=drinkCost * 2.89
    CostofFloat = floatCost* 4.29
    CostofCoffee = coffeeCost * 1.20
    CostofChicken = chickenCost* 6.89
    CostofBacconEgger=bacconEggerCost * 3.49
    foodItemsCost = CostofTeen+CostofCBUncle+CostofFries+CostofDrinks+CostofFloat+CostofCoffee+CostofChicken+CostofBacconEgger

    TotalCost=(foodItemsCost)
    BcTax=((foodItemsCost) * 0.13)
    
    CostofMeal= f"$ {foodItemsCost:.2f}"
    OverAllCost =f"$ {BcTax+TotalCost:.2f}"
    PaidTax= f"$ {BcTax:.2f}"

    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    Total.set(OverAllCost)
# exit    
def qExit():
    root.destroy()
# reset
def Reset():
    Teen.set("")
    CBUncle.set("")
    Fries.set("")
    Float.set("")
    Coffee.set("")
    Drinks.set("")
    Chicken.set("")
    BaconEgger.set("")
    rand.set("")
    Cost.set("")
    Tax.set("")
    Total.set("")
# stringVar()
Teen =StringVar()
CBUncle= StringVar()
Fries=StringVar()
Float=StringVar()
Coffee=StringVar()
Drinks=StringVar()
Burger=StringVar()
BaconEgger=StringVar()
Chicken =StringVar()
rand = StringVar()
Total=StringVar()
Tax=StringVar()
Cost=StringVar()
# label for menu
lblTeen= Label(winFrame, font=('times new roman', 15, 'bold'),text="Teen",bd=15,anchor="w")
lblTeen.grid(row=0, column=0)
txtTeen=Entry(winFrame, font=('times new roman',15,'bold'),textvariable=Teen,bd=10,insertwidth=4,bg="#d3d3d3")
txtTeen.grid(row=0,column=1)

lblCBUncle= Label(winFrame, font=('times new roman', 15, 'bold'),text="CBUncle",bd=15,anchor="w")
lblCBUncle.grid(row=1, column=0)
txtCBUncle=Entry(winFrame, font=('times new roman',15,'bold'),textvariable=CBUncle,bd=10,insertwidth=4,bg="#d3d3d3",justify='right')
txtCBUncle.grid(row=1,column=1)

lblFries= Label(winFrame, font=('times new roman', 15, 'bold'),text="Fries",bd=15,anchor="w")
lblFries.grid(row=2, column=0)
txtFries=Entry(winFrame, font=('times new roman',15,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="#d3d3d3",justify='right')
txtFries.grid(row=2,column=1)

lblFloat= Label(winFrame, font=('times new roman', 15, 'bold'),text="Float",bd=15,anchor="w")
lblFloat.grid(row=3, column=0)
txtFloat=Entry(winFrame, font=('times new roman',15,'bold'),textvariable=Float,bd=10,insertwidth=4,bg="#d3d3d3",justify='right')
txtFloat.grid(row=3,column=1)

lblCoffee= Label(winFrame, font=('times new roman', 15, 'bold'),text="Coffee",bd=15,anchor="w")
lblCoffee.grid(row=4, column=0)
txtCoffee=Entry(winFrame, font=('times new roman',15,'bold'),textvariable=Coffee,bd=10,insertwidth=4,bg="#d3d3d3",justify='right')
txtCoffee.grid(row=4,column=1)

lblDrinks= Label(winFrame, font=('times new roman', 15, 'bold'),text="Drinks",bd=15,anchor="w")
lblDrinks.grid(row=5, column=0)
txtDrinks=Entry(winFrame, font=('times new roman',15,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="#d3d3d3",justify='right')
txtDrinks.grid(row=5,column=1)

lblChicken= Label(winFrame, font=('times new roman', 15, 'bold'),text="Chicken",bd=15,anchor="w")
lblChicken.grid(row=6, column=0)
txtChicken=Entry(winFrame, font=('times new roman',15,'bold'),textvariable=Chicken,bd=10,insertwidth=4,bg="#d3d3d3",justify='right')
txtChicken.grid(row=6,column=1)

lblBaconEgger= Label(winFrame, font=('times new roman', 15, 'bold'),text="BaconEgger",bd=15,anchor="w")
lblBaconEgger.grid(row=7, column=0)
txtBaconEgger=Entry(winFrame, font=('times new roman',15,'bold'),textvariable=BaconEgger,bd=10,insertwidth=4,bg="#d3d3d3",justify='right')
txtBaconEgger.grid(row=7,column=1)

lblReference= Label(winFrame, font=('times new roman', 15, 'bold'),text="Order No.",bd=15,anchor="w")
lblReference.grid(row=0, column=2)
txtReference=Entry(winFrame, font=('times new roman',15,'bold'),textvariable=rand,bd=10,insertwidth=4,bg="#d3d3d3",justify='right')
txtReference.grid(row=0,column=3)

lblCost= Label(winFrame, font=('times new roman', 15, 'bold'),text="Cost of Meal",bd=15,anchor="w")
lblCost.grid(row=1, column=2)
txtCost=Entry(winFrame, font=('times new roman',15,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="#d3d3d3",justify='right')
txtCost.grid(row=1,column=3)

lblStateTax= Label(winFrame, font=('times new roman', 15, 'bold'),text="State Tax",bd=15,anchor="w")
lblStateTax.grid(row=2, column=2)
txtStateTax=Entry(winFrame, font=('times new roman',15,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="#d3d3d3",justify='right')
txtStateTax.grid(row=2,column=3)

lblTotalCost= Label(winFrame, font=('times new roman', 15, 'bold'),text="Total Cost",bd=15,anchor="w")
lblTotalCost.grid(row=3, column=2)
txtTotalCost=Entry(winFrame, font=('times new roman',15,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="#d3d3d3",justify='right')
txtTotalCost.grid(row=3,column=3)

#button for Total, Exit and Reset
btnTotal=Button(winFrame,padx=15,pady=8,bd=15,fg="black",font=('times new roman',15,'bold'),width=10,text="Total",bg="#d3d3d3",command=Ref).grid(row=8,column=1)

btnReset=Button(winFrame,padx=15,pady=8,bd=15,fg="black",font=('times new roman',15,'bold'),width=10,text="Reset",bg="#d3d3d3",command=Reset).grid(row=8,column=2)

btnExit=Button(winFrame,padx=15,pady=8,bd=15,fg="black",font=('times new roman',15,'bold'),width=10,text="Exit",bg="#d3d3d3",command=qExit).grid(row=8,column=3)

root.mainloop()


