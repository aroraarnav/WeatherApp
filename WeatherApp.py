from tkinter import *
from time import sleep
import requests
root = Tk()

# BY ARNAV ARORA

def test_function(entry):
    print ("This is the entry: " + entry)

def format_response (weather):
    try:
        temp = int(weather['list'][0]['main']['temp']) - 273.15
        desc = weather['list'][0]['weather'][0]['description']

        final_str = "Temperature (°C): " + str(temp)[:5]+ '\nConditions: ' + desc
    except:
        final_str = "Sorry, there was an error \nretrieving data.\n\nPlease check the city name and \ntry again."

    return final_str

def get_weather(city):
    weather_key = '' # Your Key Here
    url = 'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=' + weather_key
    response = requests.get(url)
    weather = response.json()

    label['text'] = "City: " + city + '\n' + format_response(weather)

Height = 500
Width = 500

canvas = Canvas(root, height = Height, width = Width)
canvas.pack()

background_image = PhotoImage(file = "") # Image Path Here
background_label = Label(root, image = background_image)
background_label.place (relwidth = 1, relheight = 1)

frame = Frame(root, bg = '#80c1ff', bd = 10)
frame.place(relwidth = 0.75, relheight = 0.1, relx = 0.5, rely = 0.1, anchor = 'n')

entry = Entry(frame, font = ('Courier', 18))
entry.place(relwidth = 0.65, relheight = 1)

button = Button(frame, text= "Get Weather", highlightbackground= 'lightgray', font = ('Courier', 14), command = lambda: get_weather(entry.get()))
button.place(relx = 0.7, relwidth = 0.3, relheight = 1)

lower_frame = Frame(root, bg = '#80c1ff', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = "n")

label = Label(lower_frame, text = "", bg = 'white', font = ('Courier', 18), anchor = 'nw', justify = 'left', bd = 5)
label.place (relwidth = 1, relheight = 1)

creditLabel = Label(root, text = "By Arnav Arora", font = ('Courier', 18), bg = '#80c1ff', fg = 'white')
creditLabel.place(relx = 0.8, rely = 0.8, anchor = "n", relwidth = 1.35)

root.mainloop()