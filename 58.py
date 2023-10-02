# Exercise: Tesla
def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too yound to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


age = int(input("Enter Your Age: "))
checkDriverAge(age)
