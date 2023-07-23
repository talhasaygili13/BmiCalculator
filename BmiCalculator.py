from tkinter import *

window = Tk()
window.title('BMI Calculator')
window.config( padx=24, pady=18)
window.minsize(width=260, height=200)
def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string

def calculateBmi():
    height = height_entry.get()
    weight = weight_entry.get()
    if height is None or height == "" or height == " " or weight is None or weight == "" or weight == " ":
        result_label.config(text='Enter both weight and height')
    elif height.isalpha() or height.isalpha():
        result_label.config(text='Enter a valid number')
    else:
        bmi =float(weight) / ((float(height) / 100) ** 2)
        result_text = write_result(bmi)
        result_label.config(text=result_text)

calculate_button = Button(text='Calculate', pady=10, padx=10, command=calculateBmi)


height_label = Label(text='Enter your height(cm)', pady=15, padx=15)
height_entry = Entry(width=18)

weight_label = Label(text='Enter your weight(kg)', pady=15, padx=15)
weight_entry = Entry(width=18)

weight_label.pack()
weight_entry.pack()
height_label.pack()
height_entry.pack()
calculate_button.pack()
result_label = Label()
result_label.pack()
window.mainloop()