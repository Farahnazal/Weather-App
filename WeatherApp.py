from tkinter import *
import tkinter as tk 
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime 
import requests
import pytz 

root= Tk()
root.title('Weather display ')
root.geometry('900x500+300+200')
root.resizable(False,False )

def getWeather(): 

    try:
         city=textfield.get()

         geolocator = Nominatim(user_agent="geoapiExercises")
         location = geolocator.geocode(city)
         obj=TimezoneFinder()
         result = obj.timezone_at(lng=location.longitude,lat=location.latitude)


         home=pytz.timezone(result)
         local_time=datetime.now(home)
         current_time=local_time.strftime("%H:%M:%S")
         clock.config(text=current_time)
         name.config(text="Current Weather")
    

    #api
         api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a1e837b8e0bcd81fec403ce94f75d469"



         json_data = requests.get(api).json()
         condition = json_data['weather'][0]['main']
         description = json_data['weather'][0]['description']
         temp = int(json_data['main']['temp']-273.15)
         pressure = json_data['main']['pressure']
         humidity = json_data['main']['humidity']
         wind= json_data['wind']['speed']
    
         t.config(text=(temp,"°"))
         c.config(text=(condition,"|","Feels","Like",temp,"°"))
         w.configure(text=wind)
         h.configure(text=humidity)
         d.configure(text=description)
         p.configure(text=pressure)
    
    except Exception as e:
       messagebox.showerror("Weather App","Invalid Entry")


#search section and the textfield
search_image=PhotoImage(file ="search.png")
myImage=Label(image=search_image)
myImage.place(x=20,y=20)


textfield=tk.Entry(root,justify='center',width=17,font=('TimesNewRoman',25,'bold'),bg='grey',border=0,fg='white')
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file='search_icon.png')
myImage_icon=Button(image=search_icon,borderwidth=0,cursor='hand2',bg='#404040',command=getWeather)
myImage_icon.place(x=400,y=34)

#weather image 
logo_image=PhotoImage(file='logo.png')
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#bottom image 
frame_image=PhotoImage(file='box.png')
frame_myImage=Label(image=frame_image)
frame_myImage.pack(padx=5,pady=5,side=BOTTOM)


#TIME
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("TimesNewRoman",20))
clock.place(x=30,y=130)


#label of bottom image 
label1=Label(root,text='Wind',font=('TimesNewRoman',15,'bold'),fg='white',bg='#1ab5ef')
label1.place(x=120,y=400)
label2=Label(root,text='Humidity',font=('TimesNewRoman',15,'bold'),fg='white',bg='#1ab5ef')
label2.place(x=225,y=400)
label3=Label(root,text='Description',font=('TimesNewRoman',15,'bold'),fg='white',bg='#1ab5ef')
label3.place(x=430,y=400)
label4=Label(root,text='Pressure',font=('TimesNewRoman',15,'bold'),fg='white',bg='#1ab5ef')
label4.place(x=650,y=400)


t=Label(font=("arial",70,'bold'),fg="#ee666d")
t.place(x=400,y=150)

c=Label(font=("arial",15,'bold'))
c.place(x=400,y=250)


w=Label(text="...",font=('arial',20,'bold'),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=('arial',20,'bold'),bg="#1ab5ef")
h.place(x=260,y=430)
d=Label(text="...",font=('arial',20,'bold'),bg="#1ab5ef")
d.place(x=420,y=430)
p=Label(text="...",font=('arial',20,'bold'),bg="#1ab5ef")
p.place(x=670,y=430)

root.mainloop()