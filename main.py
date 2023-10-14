from tkinter import *

screen = Tk()
screen.title("BMI Calculator")
screen.wm_minsize(200, 200)

labelcm = Label()
labelcm.config(text="Enter Your Height (cm)", font=("Arial", 10, "bold"))
labelcm.config(pady=10, padx=10)
labelcm.pack()

cmentry = Entry()
cmentry.focus()
cmentry.pack()

labelkg = Label()
labelkg.config(text="Enter Your Weight (kg)", font=("Arial", 10, "bold"))
labelkg.config(padx=10, pady=10)
labelkg.pack()

kgentry = Entry()
kgentry.pack()


def calculate_bmi():
    try:
        t1 = int(kgentry.get())
        t2 = int(cmentry.get())
        height = t2 * t2 / 10000
        bmical = t1 / height
        rounded_num = round(bmical, 2)
        if rounded_num <= 18.5:
            result.config(text=f"Your BMI is: {rounded_num}, you are underweight.")
        elif 18.5 < rounded_num <= 25:
            result.config(text=f"Your BMI is: {rounded_num}, you are normal weight.")
        elif 25 < rounded_num <= 30:
            result.config(text=f"Your BMI is: {rounded_num}, you are overweight.")
        elif 30 < rounded_num <= 35:
            result.config(text=f"Your BMI is: {rounded_num}, you are obesity class 1.")
        elif 35 < rounded_num <= 40:
            result.config(text=f"Your BMI is: {rounded_num}, you are obesity class 2.")
        elif rounded_num > 40:
            result.config(text=f"Your BMI is: {rounded_num}, you are obesity class 3.")
    except ValueError:
        result.config(text=f"Please put numbers only.")


result = Label()
result.config(font=("Arial", 10, "bold"))
result.pack()

calcutebutton = Button(text="Calculate BMI", command=calculate_bmi)
calcutebutton.config(padx=0, pady=0)
calcutebutton.pack()

mainloop()
