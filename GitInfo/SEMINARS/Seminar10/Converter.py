from tkinter import *
import requests

root = Tk()
root.geometry ("400x200")
root.resizable(0,0)
root.title('Currency converter')

Label(root, text='Currency converter', font='arial 26 bold').pack()

var1 = StringVar(root)
var2 = StringVar(root)
cost = StringVar(root)
currency_list = ['RUB','USD','EUR','JPY','CNH']

Label(root, text='Choose №1', font='arial 15 bold').place(x=50,y=50)
OptionMenu(root,var1,*currency_list).place(x=180,y=50)

Label(root, text='Choose №2', font='arial 15 bold').place(x=50,y=100)
Label(root, text='How much', font='arial 10 bold').place(x=270,y=60)
Entry(root,width=11, textvariable=cost).place(x=270,y=85)
OptionMenu(root,var2,*currency_list).place(x=180,y=100)

def get_currency():
    cur1=var1.get()
    cur2=var2.get()
    sum=cost.get()

    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={cur1}&to_currency={cur2}&apikey=YI4569XD91QHCYB2'
    r = requests.get(url)
    data = r.json()

    val1 = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    result = val1 * float(sum)
    Label(root,text=f'{result}', font='arial 15').place(x=270,y=140)

Button(root, text='Convert',font='arial 15 bold', bg='white', padx=2, command=get_currency).place(x=60,y=140)

root.mainloop()