from ctypes import resize
from tkinter.font import BOLD
from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import *
from  tkinter import ttk
from PIL import Image,ImageTk
import customtkinter as ctk
import random
from datetime import date

#Creating a GUI

window = ctk.CTk()  
window.title('Weather forecast')
window.minsize(height=1000,width=1700)
def wp():
    global wp01, wallpaper , img
    wp01 = Image.open('images/wallpaper01.png')
    resized_image = wp01.resize((700,700), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(resized_image)
    wallpaper = ctk.CTkLabel(text = '',image = img)
    wallpaper.place()

#Creating frames
upper = ctk.CTkFrame(window, width= 1000, height = 50,corner_radius=50,fg_color='#C35817')
upper.pack(pady = 40)
menu = ctk.CTkFrame(window, width=400,height=650,corner_radius=10,fg_color='#4D76BE')
menu.pack(padx = 20,side='left')
frame = ctk.CTkFrame(window, width=1100,height=700,corner_radius=10,fg_color='#4D76BE')
frame.pack(ipady = 100,pady=50)

#Styling
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('dark-blue')

#Time frame
def timeframe ():
    global img
    URL = 'https://www.timeanddate.com/worldclock/hong-kong/hong-kong'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find('div', class_ = 'bk-focus__qlook')
    temp = lists.find_all('span')[0]
    time = temp.text[:5]
    test = int(time[:2])
    today = date.today()
    date_object = today.strftime("%m/%d/%Y")
    Date = ctk.CTkLabel(upper,text=date_object,text_font = ('Consolas',12),text_color= 'black')
    Date.place(x=25,y=0)
    Time = ctk.CTkLabel(upper,text=time, text_font = ('Consolas',11),text_color= 'black')
    Time.place(x=45,y=20)
    if test < 12:
        greeting = ctk.CTkLabel(upper,text = 'Good Morning!',text_font = ('Consolas',20),text_color= 'black')
        greeting.place(x=400,y=8)
        num = random.randint(0,1)
        if num == 0:
            img = Image.open('images/sunraise01.png')
        elif num == 1:
            img = Image.open('images/sunraise02.png')
        resized_image= img.resize((70,70), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(resized_image)
        pic = ctk.CTkLabel(upper,text ='',image = img)
        pic.place(x=900,y=2,width=80)

    elif test < 18 and test >= 12:
        greeting = ctk.CTkLabel(upper,text = 'Good Afternoon!',text_font = ('Consolas',20),text_color= 'black')
        greeting.place(x=400,y=8)
        num = random.randint(0,1)
        if num == 0:
            img = Image.open('images/sunset01.png')
        elif num == 1:
            img = Image.open('images/sunset02.png')
        resized_image= img.resize((70,70), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(resized_image)
        pic = ctk.CTkLabel(upper,text = '',image = img)
        pic.place(x=900,y=2,width=80)
    
    else:
        greeting = ctk.CTkLabel(upper,text = 'Good Evening!',text_font = ('Consolas',20),text_color= 'black')
        greeting.place(x=400,y=8)
        num = random.randint(0,1)
        if num == 0:
            img = Image.open('images/night01.png')
        elif num == 1:
            img = Image.open('images/night02.png')
        resized_image= img.resize((70,70), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(resized_image)
        pic = ctk.CTkLabel(upper,text = '',image = img)
        pic.place(x=900,y=2,width = 80)

#Main menu
def main ():
    global img01 , img02
    img01 = Image.open('images/calendar.png')
    resized_image= img01.resize((40,40), Image.Resampling.LANCZOS)
    img01 = ImageTk.PhotoImage(resized_image)
    img02 = Image.open('images/current_weather.png')
    resized_image= img02.resize((440,164), Image.Resampling.LANCZOS)
    img02 = ImageTk.PhotoImage(resized_image)
    
    #Creating buttons in menu
    buttona= ctk.CTkButton(menu,image = img02,fg_color = '#4D76BE',text = '',command=lambda:[today()])
    buttona.pack()
    buttona.place(x=50, y=100,height=175,width = 450)
    buttonb= ctk.CTkButton(menu,image = img01,fg_color = '#4D76BE', text="14 Days Weather Forecast",corner_radius=5,text_font = ('arial',16),text_color= 'white' ,command=lambda:[wf14()]  )
    buttonb.pack()
    buttonb.place(x=50, y=275,height=175,width = 450)
    buttonc = ctk.CTkButton(menu, text="Local Temperature",fg_color = '#4D76BE',corner_radius=5,text_font = ('arial',16),text_color= 'white',command =lambda:[lweather()] )
    buttonc.pack()
    buttonc.place(x=50, y=450,height=175,width = 450)

def wf14():
    #clear frame
    for widget in frame.winfo_children():
            widget.destroy()
    
    #variables / constants
    URL = 'https://www.timeanddate.com/weather/hong-kong/hong-kong/ext'
    tempdate = []
    temptemp = []
    date = []
    week = []
    humi = []
    wind = []
    weather = []
    
    #Getting information in website
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find('table', class_ = 'zebra')

    #Searching the date
    for i in lists.find_all('th'):
        title = i.text
        tempdate.append(title)

    #Deleting unuseful information
    tempdate.reverse()

    for a in range(18):
        tempdate.pop()

    tempdate.reverse()

    #Searching information and input them into array
    for a in range(14):
        temp = tempdate[a][3:]
        date.append(temp)
        temp=tempdate[a][:3]
        week.append(temp)
        temp = soup.find_all('tr')[a+2]('td')[1]
        temptemp.append(temp.text)
        temp = soup.find_all('tr')[a+2]('td')[6]
        humi.append(temp.text)
        temp = soup.find_all('tr')[a+2]('td')[4]
        wind.append(temp.text)
        temp = soup.find_all('tr')[a+2]('td')[2]
        weather.append(temp.text)
        weather[a] = weather[a][:len(weather[a])-1]
        weather = [word.replace(".", ",") for word in weather]
    
    #Insert title
    title = ctk.CTkLabel(frame,text='14 Days-weather Forecast', text_font =('Arial',40,BOLD))
    title.pack()
    title.place(x= 275,y=130)

    #creating table
    table = ttk.Treeview(frame,height=14)
    table['columns']= ('Week','Date','Temperature','Humidity','Weather')

    #Styling
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview.Heading',background='#4D76BE',font=('Arial',16,'bold'))
    style.configure( 'Treeview',rowheight=35,font =('Comic Sans MS' , 13))
    table.tag_configure('odd', background = '#D1D0CE')
    table.tag_configure('even', background = 'silver')

    #Insert columns
    table.column("#0", width=0,  stretch=NO)
    table.column("Week",anchor=CENTER, width=150)
    table.column("Date",anchor=CENTER, width=150)
    table.column("Temperature",anchor=CENTER, width=410)
    table.column("Humidity",anchor=CENTER, width=270)
    table.column("Weather",anchor=CENTER, width=500)

    #Insert heading
    table.heading("#0",text="",anchor=CENTER)
    table.heading("Week",text="Week",anchor=CENTER)
    table.heading("Date",text="Date",anchor=CENTER)
    table.heading("Temperature",text="Temperature(max/min °C)",anchor=CENTER)
    table.heading("Humidity",text="Humidity(%)",anchor=CENTER)
    table.heading("Weather",text = 'Weather Conditions',anchor=CENTER)

    #Insert information to table
    table.insert(parent='',index='end',iid=0,text='', values=(week[0],date[0],temptemp[0],humi[0],weather[0]),tag = 'even')
    table.insert(parent='',index='end',iid=1,text='', values=(week[1],date[1],temptemp[1],humi[1],weather[1]),tag = 'odd')
    table.insert(parent='',index='end',iid=2,text='', values=(week[2],date[2],temptemp[2],humi[2],weather[2]),tag = 'even')
    table.insert(parent='',index='end',iid=3,text='', values=(week[3],date[3],temptemp[3],humi[3],weather[3]),tag = 'odd')
    table.insert(parent='',index='end',iid=4,text='', values=(week[4],date[4],temptemp[4],humi[4],weather[4]),tag = 'even')
    table.insert(parent='',index='end',iid=5,text='', values=(week[5],date[5],temptemp[5],humi[5],weather[5]),tag = 'odd')
    table.insert(parent='',index='end',iid=6,text='', values=(week[6],date[6],temptemp[6],humi[6],weather[6]),tag = 'even')
    table.insert(parent='',index='end',iid=7,text='', values=(week[7],date[7],temptemp[7],humi[7],weather[7]),tag = 'odd')
    table.insert(parent='',index='end',iid=8,text='', values=(week[8],date[8],temptemp[8],humi[8],weather[8]),tag = 'even')
    table.insert(parent='',index='end',iid=9,text='', values=(week[9],date[9],temptemp[9],humi[9],weather[9]),tag = 'odd')
    table.insert(parent='',index='end',iid=10,text='', values=(week[10],date[10],temptemp[10],humi[10],weather[10]),tag = 'even')
    table.insert(parent='',index='end',iid=11,text='', values=(week[11],date[11],temptemp[11],humi[11],weather[11]),tag = 'odd')
    table.insert(parent='',index='end',iid=12,text='', values=(week[12],date[12],temptemp[12],humi[12],weather[12]),tag = 'even')
    table.insert(parent='',index='end',iid=13,text='', values=(week[13],date[13],temptemp[13],humi[13],weather[13]),tag = 'odd')
    table.pack()
    table.place(x= 85,y=350)
    

    #Refresh Button
    img = Image.open('images/refresh.png')
    resized_image= img.resize((40,40), Image.Resampling.LANCZOS)
    refreshimg = ImageTk.PhotoImage(resized_image)
    refreshbt= ctk.CTkButton(frame,image= refreshimg,fg_color = 'silver',text_color = 'black',text = 'Refresh',text_font = ('arial',12),command=lambda:[wf14()])
    refreshbt.pack()
    refreshbt.place(x=500, y=650,height=50,width = 150)

def today ():
    URL = 'https://www.timeanddate.com/weather/hong-kong/hong-kong'
    
    #Clearing Frame
    for widget in frame.winfo_children():
            widget.destroy()
    
    #Searching information
    page = requests.get(URL)    
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find('section', class_ = 'bk-focus')
    temp = lists.find_all('div')[2]
    temptemp = temp.text[:2]
    temp = lists.find_all('tbody')[0]('td')[1]
    time = temp.text
    temp = lists.find_all('tbody')[0]('td')[5]
    humi = temp.text
    temp = lists.find_all('p')[0]
    weather = temp.text
    weather = weather[:len(weather)-1]

    #output result
    title = ctk.CTkLabel(frame ,text=('Current weather'), text_font =('Arial',30,BOLD))
    title.pack()
    title.place(x= 400,y=50)
    ctime = ctk.CTkLabel(frame ,text=('Time: '+ time), text_font =('Arial',14))
    ctime.pack()
    ctime.place(x= 300,y=150)
    ctime = ctk.CTkLabel(frame,text=('°C'), text_font =('Comic Sans MS',60,BOLD))
    ctime.pack()
    ctime.place(x= 500,y=387)
    ctemp = ctk.CTkLabel(frame ,text=(temptemp), text_font =('Comic Sans MS',120,BOLD))
    ctemp.pack()
    ctemp.place(x= 200,y=300)
    ctemp = ctk.CTkLabel(frame ,text='Temperature :', text_font =('Arial',14))
    ctemp.pack()
    ctemp.place(x= 200,y=300)
    ctemp = ctk.CTkLabel(frame ,fg = '#454545',text=(weather), text_font =('Comic Sans MS',30,BOLD))
    ctemp.pack()
    ctemp.place(x= 300,y = 200)
    ctemp = ctk.CTkLabel(frame ,text='Relative Humidity :', text_font =('Arial',14))
    ctemp.pack()
    ctemp.place(x= 700,y=300)
    ctemp = ctk.CTkLabel(frame ,fg = '#0C090A',text=(humi), text_font =('Comic Sans MS',30,BOLD))
    ctemp.pack()
    ctemp.place(x= 900,y = 290)
    
    #Refresh button
    img = Image.open('images/refresh.png')
    resized_image= img.resize((40,40), Image.Resampling.LANCZOS)
    refreshimg = ImageTk.PhotoImage(resized_image)
    refreshbt= ctk.CTkButton(frame,image= refreshimg,fg_color = 'silver',text_color = 'black',text = 'Refresh',text_font = ('arial',12),command=lambda:[today()])
    refreshbt.pack()
    refreshbt.place(x=500, y=650,height=50,width = 150)

def lweather ():
    
    #clear frame
    for widget in frame.winfo_children():
            widget.destroy()
    
    #Initialisation
    URL = 'https://rss.weather.gov.hk/rss/CurrentWeather.xml'
    location = []
    tempe = []
    
    #Getting information in website
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml') 
    lists = soup.find('table')
    for i in range (0,54,2):
        temp = lists.find_all('td')[i]
        location.append(temp.text)
    for i in range (1,54,2):
        temp = lists.find_all('td')[i] 
        tempe.append(temp.text[:3]+ '°C')
    
    #Creating scrollbar
    scroll = Scrollbar(frame,orient=VERTICAL)

    #Insert title
    title = ctk.CTkLabel(frame,text='Local Temperature', text_font =('Arial',40,BOLD))
    title.pack()
    title.place(x= 275,y=130)
    
    #creating table
    table = ttk.Treeview(frame,height=15,yscrollcommand=scroll.set)
    scroll.place(relx=0.715,rely=0.306,width=30,height=575)
    scroll.config(command=table.yview)

    #Styling
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Treeview.Heading',background='#4D76BE',font=('Arial',16,'bold'))
    style.configure( 'Treeview',rowheight=35,font =('Comic Sans MS' , 13))
    style.configure('Scrollbar',background = 'black')
    table['columns']= ('Locations','Temperature')
    table.tag_configure('odd', background = '#D1D0CE')
    table.tag_configure('even', background = 'silver')

    #Insert columns
    table.column("#0", width=0,  stretch=NO)
    table.column("Locations",anchor=CENTER, width=450)
    table.column("Temperature",anchor=CENTER, width=300)

    #Insert heading
    table.heading("#0",text="",anchor=CENTER)
    table.heading("Locations",text="Locations",anchor=CENTER)
    table.heading("Temperature",text="Temperature",anchor=CENTER)

    #Insert information to table
    table.insert(parent='',index='end',iid=0,text='', values=(location[0],tempe[0]),tag = 'even')
    table.insert(parent='',index='end',iid=1,text='', values=(location[1],tempe[1]),tag = 'odd')
    table.insert(parent='',index='end',iid=2,text='', values=(location[2],tempe[2]),tag = 'even')
    table.insert(parent='',index='end',iid=3,text='', values=(location[3],tempe[3]),tag = 'odd')
    table.insert(parent='',index='end',iid=4,text='', values=(location[4],tempe[4]),tag = 'even')
    table.insert(parent='',index='end',iid=5,text='', values=(location[5],tempe[5]),tag = 'odd')
    table.insert(parent='',index='end',iid=6,text='', values=(location[6],tempe[6]),tag = 'even')
    table.insert(parent='',index='end',iid=7,text='', values=(location[7],tempe[7]),tag = 'odd')
    table.insert(parent='',index='end',iid=8,text='', values=(location[8],tempe[8]),tag = 'even')
    table.insert(parent='',index='end',iid=9,text='', values=(location[9],tempe[9]),tag = 'odd')
    table.insert(parent='',index='end',iid=10,text='', values=(location[10],tempe[10]),tag = 'even')
    table.insert(parent='',index='end',iid=11,text='', values=(location[11],tempe[11]),tag = 'odd')
    table.insert(parent='',index='end',iid=12,text='', values=(location[12],tempe[12]),tag = 'even')
    table.insert(parent='',index='end',iid=13,text='', values=(location[13],tempe[13]),tag = 'odd')
    table.insert(parent='',index='end',iid=14,text='', values=(location[14],tempe[14]),tag = 'even')
    table.insert(parent='',index='end',iid=15,text='', values=(location[15],tempe[15]),tag = 'odd')
    table.insert(parent='',index='end',iid=16,text='', values=(location[16],tempe[16]),tag = 'even')
    table.insert(parent='',index='end',iid=17,text='', values=(location[17],tempe[17]),tag = 'odd')
    table.insert(parent='',index='end',iid=18,text='', values=(location[18],tempe[18]),tag = 'even')
    table.insert(parent='',index='end',iid=19,text='', values=(location[19],tempe[19]),tag = 'odd')
    table.insert(parent='',index='end',iid=20,text='', values=(location[20],tempe[20]),tag = 'even')
    table.insert(parent='',index='end',iid=21,text='', values=(location[21],tempe[21]),tag = 'odd')
    table.insert(parent='',index='end',iid=22,text='', values=(location[22],tempe[22]),tag = 'even')
    table.insert(parent='',index='end',iid=23,text='', values=(location[23],tempe[23]),tag = 'odd')
    table.insert(parent='',index='end',iid=24,text='', values=(location[24],tempe[24]),tag = 'even')
    table.insert(parent='',index='end',iid=25,text='', values=(location[25],tempe[25]),tag = 'odd')
    table.insert(parent='',index='end',iid=26,text='', values=(location[26],tempe[26]),tag = 'even')    
    table.pack()
    table.place(x= 425,y=350)
    
    #Refresh button
    img = Image.open('images/refresh.png')
    resized_image= img.resize((40,40), Image.Resampling.LANCZOS)
    refreshimg = ImageTk.PhotoImage(resized_image)
    refreshbt= ctk.CTkButton(frame,image= refreshimg,fg_color = 'silver',text_color = 'black',text = 'Refresh',text_font = ('arial',12),command=lambda:[lweather()])
    refreshbt.pack()
    refreshbt.place(x=500, y=650,height=50,width = 150)

try:
    wp()
    main()
    timeframe()
except:   
    global img
    errorframe = tk.Tk()  
    errorframe('Weather forecast')
    errorframe.minsize(height=500,width=500)
    for widget in frame.winfo_children():
            widget.destroy()
    errormsg = ctk.CTkLabel(errorframe,text = 'Please connect to the internet!',text_font = ('Consolas',28),text_color= 'red')
    errormsg.place(x=120,y=300)
    img = Image.open('images/refresh.png')
    resized_image= img.resize((40,40), Image.Resampling.LANCZOS)
    refreshimg = ImageTk.PhotoImage(resized_image)
    refreshbt= ctk.CTkButton(frame,image= refreshimg,fg_color = 'silver',text_color = 'black',text = 'Refresh',text_font = ('arial',12),command=lambda:[main(),timeframe()])
    refreshbt.pack()
    refreshbt.place(x=500, y=650,height=50,width = 150)
window.mainloop()