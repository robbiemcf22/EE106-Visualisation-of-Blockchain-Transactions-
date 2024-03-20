# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 12:00:32 2024

@author: nfb22170
"""

#Importing Libraries
import tkinter as gui 
import webbrowser 
from tkinter import ttk 
import requests
import matplotlib.pyplot as plt

a = [] 

def Bitcoin_Price():
    #API link for bitcoin from coingecko is inserted
    api_urls = ["https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin&order=price_desc&per_page=100&page=1&sparkline=true&locale=en"]
    #The data required is fetched for using an iterative loop
    for url in api_urls:
        response = requests.get(url,timeout=1)
    #Conditional loop used to check if API link is valid or not    
    if response.status_code == 200:
        data = response.json()
        data = data[0]['sparkline_in_7d']['price']
        print("Data received", data)
        plt.plot(data)
        plt.title('Bitcoin Price Over the Last 7 Days')
        plt.xlabel('Hours')
        plt.ylabel('Price')
        plt.show(block=False)
        global a
        a = data 
    else:
        print("Error:", response.status_code)
        
  
def Ethereum_Price():
    api_urls = ["https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum&order=price_desc&per_page=100&page=1&sparkline=true&locale=en"]
    for url in api_urls:
        response = requests.get(url,timeout=1) 
    if response.status_code == 200:
        data = response.json()
        data = data[0]['sparkline_in_7d']['price']
        print("Data received", data)
        plt.plot(data)
        plt.title('Ethereum Price Over The Last 7 Days')
        plt.xlabel('Hours')
        plt.ylabel('Price')
        plt.show(block=False)
        global a 
        a = data 
    else:
        print("Error:", response.status_code)
        
    
def Tether_Price():
    api_urls = ["https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=tether&order=price_desc&per_page=100&page=1&sparkline=true&locale=en"]
    for url in api_urls:
        response = requests.get(url,timeout=1)  
    if response.status_code == 200:
        data = response.json()
        data = data[0]['sparkline_in_7d']['price']
        print("Data received", data)
        plt.plot(data)
        plt.title('Tether Price Over The Last 7 Days')
        plt.xlabel('Hours')
        plt.ylabel('Price')
        plt.show(block=False)
        global a
        a = data 
    else:
        print("Error:", response.status_code)
        
        
def Solana_Price():
    api_urls = ["https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=solana&order=price_desc&per_page=100&page=1&sparkline=true&locale=en"]
    for url in api_urls:
        response = requests.get(url,timeout=1)  
    if response.status_code == 200:
        data = response.json()
        data = data[0]['sparkline_in_7d']['price']
        print("Data received", data)
        plt.plot(data)
        plt.title('Solana Price Over The Last 7 Days')
        plt.xlabel('Hours')
        plt.ylabel('Price')
        plt.show(block=False)
        global a  
        a = data 
    else:
        print("Error:", response.status_code)
    
    
def Bitcoin_Market_Cap():
    api_urls = ["https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=7&interval=daily&precision=2"]
    for url in api_urls:
        response = requests.get(url, timeout=1)  
    if response.status_code == 200:
        data = response.json()
        data = data[0]['sparkline_in_7d']['market_cap']
        print("Data received:", data)  # Print the entire JSON response
        plt.plot(data) 
        plt.title('Bitcoin Market Cap')
        plt.xlabel('Hours')
        plt.ylabel('Price')
        plt.show(block=False)
    else:
        print("Error:", response.status_code)



def open_website():
    url = "https://www.coingecko.com"
    webbrowser.open(url)
    
root = gui.Tk() #creating the GUI
root.title("Visualisation of Blockchain Transactions") #title of the GUI

b1 = gui.Button(root,text="Click to connect to CoinGecko.com", command=open_website, bg="green") 
b1.grid(row=1,column=4)

Cryptocurrencies=['Bitcoin','Ethereum','Tether','Solana']
sb1 = ttk.Combobox(root,values=Cryptocurrencies,width=15)
sb1.grid(row=10,column=3,padx=10,pady=20)     

def price():
    if sb1.get()=="Bitcoin":
        print("You have selected BITCOIN PRICE")
        Bitcoin_Price()
    elif sb1.get()=="Ethereum":
        print("You have selected ETHEREUM PRICE")
        Ethereum_Price()
    elif sb1.get()=="Tether": 
        print("You have selected TETHER PRICE") 
        Tether_Price()
    elif sb1.get()=="Solana": 
        print("You have selected SOLANA PRICE")
        Solana_Price() 
            
def market_cap():
    if sb1.get()=="Bitcoin":
        print("You have selected BITCOIN MARKET CAP")
        Bitcoin_Market_Cap()
    elif sb1.get()=="Ethereum":
        print("You have selected ETHEREUM MARKET CAP")
        Ethereum_Price()
    elif sb1.get()=="Tether": 
        print("You have selected TETHER MARKET CAP") 
        Tether_Price()
    elif sb1.get()=="Solana": 
        print("You have selected SOLANA MARKET CAP")
        Solana_Price() 
    
def trade_volume():
    if sb1.get()=="Bitcoin": 
        print("You have selected BITCOIN TRADING VOLUME")
        
    elif sb1.get()=="Ethereum":
        print("You have selected ETHEREUM TRADING VOLUME")
        
    elif sb1.get()=="Tether":
        print("You have selected TETHER TRADING VOLUME")
        
    elif sb1.get()=="Solana":
        print("You have selected SOLANA TRADING VOLUME") 

b2 = gui.Button(root,text="Price",width=15,command=price) 
b2.grid(row=10,column=8,padx=10,pady=20) 

b3 = gui.Button(root,text="Market Cap",width=15,command=market_cap)
b3.grid(row=20,column=3,padx=10,pady=20)

b5 = gui.Button(root,text="24hr Trade Vol",width=15,command=trade_volume)
b5.grid(row=20,column=8,padx=10,pady=20) 

root.mainloop() 