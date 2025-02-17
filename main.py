import pandas as pd
# import math

# print("Welcome to Diet_Forge! ")

# name = input("Enter your name: ")
# weight = int(input("Enter your weight(in kg): "))
# height = int(input("Enter your height(in cm): "))
# age = int(input("Enter your age: "))
# gender = input("Enter your gender(M for male & F for female): ").capitalize()
# active = input("How active are you(Sedentary, Lightly, Moderately, Very, Super)? ").capitalize()

df = pd.read_csv("Data/diet.csv")
breakfast_df = df[df['Meal_Type'] == 'Breakfast']
lunch_df = df[df['Meal_Type'] == 'Lunch']
snack_df = df[df['Meal_Type'] == 'Snack']
dinner_df = df[df['Meal_Type'] == 'Dinner']

# def diet(total_cal):
#    protein = total_cal * 0.30
   

# def calcount(BMR, active):
#    total_cal = 0
#    bulk_cal = 0
#    cut_cal = 0
#    if(active == "Sedentary" or active == "Sed"):
#       total_cal = BMR * 1.2
#    elif(active == "Lightly" or active == "L"):
#       total_cal = BMR * 1.375
#    elif(active == "Moderately" or active == "M"):
#       total_cal = BMR * 1.55
#    elif(active == "Very" or active == "V"):
#       total_cal = BMR * 1.725
#    elif(active == "Super" or active == "Sup"):
#       total_cal = BMR * 1.9
#    else :
#       print("Enter correctly")

#    print(f"Your calorie intake should be {math.trunc(total_cal)}")
#    bulk_cal = total_cal + 500
#    cut_cal = total_cal - 500
#    print(f"Your bulking calorie should be {math.trunc(bulk_cal)}")
#    print(f"Your cutting calorie should be {math.trunc(cut_cal)}")
#    diet(total_cal)


# if(gender == 'M'):
#     BMR = 10 * weight + 6.25 * height - 5 * age + 5
# else:
#     BMR = 10 * weight + 6.25 * height - 5 * age - 161

# if(age<15):
#   print("Too young for a diet")
# else:
#   calcount(BMR,active)

protein = 30
filtered_df = df.loc[df['Protein (g)'] < protein]
print(filtered_df)