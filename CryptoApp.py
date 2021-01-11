import tkinter as tk
from bs4 import BeautifulSoup
import requests
import numpy as np
import time
from ClassCoin import *
import os
import tkinter.messagebox



b = ''
cap = 0
valu = 0
chg_r = 0
highh = 0
loww = 0
def input():
    '''
    Obtains input from the entry at the root window,
    and designates a variable to it.
    :return:
    None
    '''
    global startEntry
    global a
    a = startEntry.get()
    time.sleep(0.38)
    root.destroy()


#Displaying the first window and taking input from user
a = 0
root = tk.Tk()
root.title('Crypto Currency Finder')
root.geometry('480x80')
startLabel = tk.Label(root, text="Input the coin you are looking for(Ex: 'bitcoin'):  ")
startEntry = tk.Entry(root)
startLabel.pack()
startEntry.pack()
plotButton = tk.Button(root, text="Find", command=input)
plotButton.pack()
root.mainloop()

def display_currency(x):
    '''
    The function firstly goes to the website, obtains html data with requests module,
    processes the data and obtains values for say, value, market cap, etc.
    And then using ClassCoin.py it stores all the coin data in a class named coin in a list.
    So that it would be easier to use in the future.
    :param x:
    x parameter comes in handy while creating the url link for the website.
    :return:
    None
    '''
    text = str(x)
    text.lower()
    link = 'https://coinmarketcap.com/en/currencies/' + text + '/'
    m_source = requests.get(link)
    src = m_source.content
    soup = BeautifulSoup(src,"html.parser")
    today_low = soup.find('span',{"class":"highLowValue___GfyK7"})
    today_low = str(today_low)
    today_low = today_low.split('>')[1]
    today_low = today_low.split('<')[0]
    today_high = soup.find_all('span',{"class":"highLowValue___GfyK7"})[1]
    today_high = str(today_high)
    today_high = today_high.split('>')[1]
    today_high = today_high.split('<')[0]
    mark_cap = soup.find('div',{"class":"statsValue___2iaoZ"})
    mark_cap = str(mark_cap)
    mark_cap = mark_cap.split('>')[1]
    mark_cap = mark_cap.split('<')[0]
    value_try = soup.find_all('div',{"class":"priceValue___11gHJ"})
    value_try = str(value_try)
    first = value_try.split('>')[1]
    second = first.split('<')[0]
    change_rate = soup.find('span',{"class":"qe1dn9-0 RYkpI"})
    rate_arrow = soup.find('span', attrs={'style':'background-color:var(--down-color);color:#fff;padding:5px 10px;border-radius:8px;font-size:14px;font-weight:600'})
    change_rate = str(change_rate)
    eins = change_rate.split('>')[3]
    zwitte = eins.split('<')[0]
    if rate_arrow == None:
        zwitte = '+'+zwitte
    else:
        zwitte = '-'+zwitte

    global valu
    global chg_r
    global cap
    global highh
    global loww
    valu = second
    chg_r = zwitte
    cap = mark_cap
    highh = today_high
    loww = today_low
    coin_list = np.array([a, valu, chg_r, cap, highh, loww], dtype=str)
    global coin_obj
    global j
    coin_obj = Coin(coin_list[0], coin_list[1], coin_list[2], coin_list[3], coin_list[4], coin_list[5])
    j = coin_obj.get_val()


display_currency(a)

def coin_perceiver(x):
    '''
    The function is responsible for correcting the data that gathered from the coin object, and the get_val() method of it.
    :param x:
    x parameter is the string that obtained from coin object with dollar sign.
    :return:
    returns the corrected float value of coin from object.
    '''
    if x[0]=='$':
        x = x[1:]
    d = x.strip().split('.')
    decimal = d[1]
    esas = ''
    for x in d[0]:
        if x.isdigit():
            esas = esas+x
    decimal =float(decimal)
    decimal = float(decimal/100)
    tum = float(esas) + decimal
    tum = float(tum)
    return tum

def input_perceiver(x):
    '''
    The function is responsible for correcting the data that gathered from the user input.
    :param x:
    x parameter is the string that obtained from user input with false significant numbers.
    :return:
    returns the corrected float value of user input.
    '''
    first = x[:-2]
    last = x[-2:]
    last1 = '0.'+last
    last1 = float(last1)
    first = float(first)
    son = first + last1
    return son
'''
print('Current value of {} with respect to USD is: '.format(a) + second)
print('24 Hour change rate of {} is: '.format(a) + zwitte)
print('Market capacity of the {} is: '.format(a) + mark_cap)
print('Highest value of {} today is: '.format(a) + today_high)
print('Lowest value of {} today is: '.format(a) + today_low)
'''
o = ''

def Alarm():
    '''
    Creates, sets and applies the alarm at the right time.
    :return:
    None
    '''
    global entre
    global s
    s = entre.get()
    s = input_perceiver(s)
    para = coin_perceiver((coin_obj.get_val()))
    if s>para:
        wind.destroy()

        while True:
            display_currency(a)
            h = coin_perceiver(j)
            if h>s:
                os.system("start world-war-2-air-raid-siren-sound-effect.mp3")
                wind.destroy()

    elif s==para:
        tk.messagebox.showwarning(title='NJET!', message='Invalid Move')
        wind.destroy()
        quit()
    else:
        wind.destroy()

        while True:
            display_currency(a)
            h = coin_perceiver(j)
            if s>h:
                os.system("start world-war-2-air-raid-siren-sound-effect.mp3")


z = 0
l = 0

def display(coin_obj):
    '''
    Function displays the datas of the coin which the input were taken in the first place.
    Takes an input later as upper or lower value set for alarm, then triggers Alarm() function.
    :param coin_obj:
    parameter provides coin datas from the coin object, the class that created.
    :return:
    None
    '''
    global window
    window = tk.Tk()
    window.title('Crypto Currency Displayer')
    window.geometry('640x150')
    Label = tk.Label(window, text="Datas of the coin you wanted to be displayed: ")
    Label.pack()
    Datas = tk.Label(window,text=coin_obj)
    Datas.pack()
    def question():
        global wind
        wind = tk.Tk()
        wind.title('Alarm')
        label = tk.Label(wind,text='Input the upper or lower value for alarm, last two decimals are cents: ')
        global entre
        entre = tk.Entry(wind)
        c4 = tk.Button(wind, text="Set!", command=Alarm)
        entre.pack()
        label.pack()
        c4.pack()
        wind.mainloop()



    c3 = tk.Button(window,text="Let's set the alarm!",command=question).pack()
    window.mainloop()

display(coin_obj)









