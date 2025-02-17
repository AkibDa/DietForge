print("Welcome to Diet_Forge! ")

name = input("Enter your name: ")
weight = int(input("Enter your weight(in kg): "))
height = int(input("Enter your height(in cm): "))
age = int(input("Enter your age: "))
gender = input("Enter your gender(M for male & F for female): ").capitalize()
active = input("How active are you(Sedentary, Lightly, Moderately, Very, Super)? ")
total_cal = 0

def calcount(BMR active):
  if(active == "Sedentary"):
     total_cal = BMR * 1.2
     print(total_cal)
  elif(active == "Lightly"):
     total_cal = BMR * 1.375
     print(total_cal)
  elif(active == "Moderately"):
     total_cal


if(gender == 'M'):
    BMR = 10 * weight + 6.25 * height - 5 * age + 5
else:
    BMR = 10 * weight + 6.25 * height - 5 * age + - 161

if(age<15):
  print("Too young for a diet")
else:
  calcount(BMR,active)




  

  





