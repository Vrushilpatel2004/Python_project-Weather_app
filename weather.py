import tkinter as tk
import requests
import time

def getweather(canvas):
    city = textfield.get()
    api ="https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=8bb6b0e77a27910dc40697e8eaa64c0e"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]['main']
    condition_1 = json_data["weather"][0]['description']

    country = json_data['sys']['country']
    lat = round(float(json_data['coord']['lat']),2)
    lon = round(float(json_data['coord']['lon']),2)
    temp = round(float(json_data['main']['temp'] - 273.15),2) #from kelvin
    #condition =json_data["weather"][0]['temp']
    min_temp = round(float(json_data['main']['temp_min'] - 273.15),2)
    max_temp = round(float(json_data['main']['temp_max'] - 273.15),2) 
    pressure = json_data['main']['pressure']
    feels_like = round(float(json_data['main']['feels_like'] - 273.15),2)
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    local_time = time.strftime("%I:%M:%S", time.gmtime(json_data['dt']+19800))
    timezone = time.strftime("%I:%M:%S", time.gmtime(json_data['timezone']))
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']+19800)) #Based on Gmt +5.5 clock
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']+19800))

    final_info = "City: "+city+"\n"+condition +"\n "+condition_1+ "\n"+ "Temperature: " + str(temp) + " °C"+"\n Local Time: "+local_time
    final_data ="\n" +"Country : "+country+"\n"+"Time Zone: "+timezone+"\n"+"Latitude: "+str(lat)+"°\n"+"Longitude: "+str(lon)+"°\n"+"Pressure: "+ str(pressure)+" hPa\n"+"Feels-like: "+ str(feels_like)+" °C\n"+"Humidity : "+ str(humidity)+" %\n"+"Wind-speed: "+str(wind)+"\n"+"Sun-rise: "+sunrise+"\n"+"Sun-set: "+sunset
    Label1.config(text = final_info)
    Label2.config(text = final_data)

canvas =tk.Tk()
#canvas.geometry("600 500")
canvas.title("Weather app")
# defining font style
f = ("Times-new-Roman",18,"bold")
t = ("Calibre",25,"bold")
c = ("Calibre",25,"bold")
#name_label = tk.Label(canvas, text = 'Enter city Name : ', font=('calibre',10, 'bold'))
#name_label.grid(row=0,column=0)
Label_city = tk.Label(canvas,text ='Enter City Name : ', font=c)
Label_city.place(relx = 0.1, rely = 0.08)
textfield = tk.Entry(canvas, font =t,justify="center")
#textfield.insert(0, "Enter city name ")   default text

textfield.pack(pady=50, padx=10)
textfield.focus()
textfield.bind('<Return>',getweather)  #After entering city name

Label1 =tk.Label(canvas, font =t)
Label1.pack()
Label2 = tk.Label(canvas, font = f)
Label2.pack()

canvas.mainloop()