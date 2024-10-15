from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image():
    try:
        response=requests.get(url) #response-ответ, requests-запрос по ссылке, а то, что вернется, положим в response
        response.raise_for_status() #для обработки исключений
        image_data=BytesIO(response.content)
        img=Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None


window=Tk()
window.title('Cats!')
window.geometry('600x480')

label=Label()
label.pack()

url=('https://cataas.com/cat')
img=load_image(url)

if img:
    label.config(image=img)
    label.image=img #чтобы сборщик мусора картинку не убрал

window.mainloop()
