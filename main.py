import pandas as pd
import math

print("Welcome to Diet_Forge! ")

df = pd.read_csv("Data/diet.csv")
df = df.drop(columns=['Date', 'User_ID'])
breakfast_df = df[df['Meal_Type'] == 'Breakfast']
lunch_df = df[df['Meal_Type'] == 'Lunch']
dinner_df = df[df['Meal_Type'] == 'Dinner']

def diet_Normal_NonVeg(total_cal,weight):
   protein = 2 * weight
   breakfast = total_cal * 0.173
   lunch = total_cal * 0.466
   dinner = total_cal * 0.24
   breakfast_protein_cal = breakfast * 0.30
   breakfast_carb_cal = breakfast * 0.50
   breakfast_carb = breakfast_carb_cal % 4
   lunch_protein_cal = lunch * 0.30
   lunch_carb_cal = lunch * 0.50
   lunch_carb = lunch_carb_cal % 4
   dinner_protein_cal = dinner * 0.30
   dinner_carb_cal = dinner * 0.50
   dinner_carb = dinner_carb_cal % 4
   breakfast_food_df = breakfast_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < breakfast_protein_cal) & (df['Fiber (g)'] <= breakfast_carb) & (df['Calories (kcal)'] < breakfast_carb_cal)]
   lunch_food_df = lunch_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < lunch_protein_cal) & (df['Fiber (g)'] <= lunch_carb) & (df['Calories (kcal)'] < lunch_carb_cal)]
   dinner_food_df = dinner_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < dinner_protein_cal) & (df['Fiber (g)'] <= dinner_carb) & (df['Calories (kcal)'] < dinner_carb_cal)]

   print("----------------------------------------------------------------------")
   print(breakfast_food_df)
   print("----------------------------------------------------------------------") 
   print(lunch_food_df)
   print("----------------------------------------------------------------------")
   print(dinner_food_df)
   print("----------------------------------------------------------------------")
   print("Thanks for using Diet_Forge!")

def diet_Normal_Veg(total_cal,weight):
   protein = 2 * weight
   breakfast = total_cal * 0.173
   lunch = total_cal * 0.466
   dinner = total_cal * 0.24
   breakfast_protein_cal = breakfast * 0.30
   breakfast_carb_cal = breakfast * 0.50
   breakfast_carb = breakfast_carb_cal % 4
   lunch_protein_cal = lunch * 0.30
   lunch_carb_cal = lunch * 0.50
   lunch_carb = lunch_carb_cal % 4
   dinner_protein_cal = dinner * 0.30
   dinner_carb_cal = dinner * 0.50
   dinner_carb = dinner_carb_cal % 4
   breakfast_food_df = breakfast_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < breakfast_protein_cal) & (df['Fiber (g)'] <= breakfast_carb) & (df['Calories (kcal)'] < breakfast_carb_cal) & (df['Category'] != 'Meat')]
   lunch_food_df = lunch_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < lunch_protein_cal) & (df['Fiber (g)'] <= lunch_carb) & (df['Calories (kcal)'] < lunch_carb_cal) & (df['Category'] != 'Meat')]
   dinner_food_df = dinner_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < dinner_protein_cal) & (df['Fiber (g)'] <= dinner_carb) & (df['Calories (kcal)'] < dinner_carb_cal) & (df['Category'] != 'Meat')]

   print("----------------------------------------------------------------------")
   print(breakfast_food_df)
   print("----------------------------------------------------------------------") 
   print(lunch_food_df)
   print("----------------------------------------------------------------------")
   print(dinner_food_df)
   print("----------------------------------------------------------------------")
   print("Thanks for using Diet_Forge!")

def diet_Bulk_NonVeg(total_cal,weight):
   protein = 2 * weight
   breakfast = total_cal * 0.173
   lunch = total_cal * 0.466
   dinner = total_cal * 0.24
   breakfast_protein_cal = breakfast * 0.30
   breakfast_carb_cal = breakfast * 0.50
   breakfast_carb = breakfast_carb_cal % 4
   lunch_protein_cal = lunch * 0.30
   lunch_carb_cal = lunch * 0.50
   lunch_carb = lunch_carb_cal % 4
   dinner_protein_cal = dinner * 0.30
   dinner_carb_cal = dinner * 0.50
   dinner_carb = dinner_carb_cal % 4
   breakfast_food_df = breakfast_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < breakfast_protein_cal) & (df['Fiber (g)'] <= breakfast_carb) & (df['Calories (kcal)'] < breakfast_carb_cal)]
   lunch_food_df = lunch_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < lunch_protein_cal) & (df['Fiber (g)'] <= lunch_carb) & (df['Calories (kcal)'] < lunch_carb_cal)]
   dinner_food_df = dinner_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < dinner_protein_cal) & (df['Fiber (g)'] <= dinner_carb) & (df['Calories (kcal)'] < dinner_carb_cal)]

   print("----------------------------------------------------------------------")
   print(breakfast_food_df)
   print("----------------------------------------------------------------------") 
   print(lunch_food_df)
   print("----------------------------------------------------------------------")
   print(dinner_food_df)
   print("----------------------------------------------------------------------")
   print("Thanks for using Diet_Forge!")

def diet_Bulk_Veg(total_cal,weight):
   protein = 2 * weight
   breakfast = total_cal * 0.173
   lunch = total_cal * 0.466
   dinner = total_cal * 0.24
   breakfast_protein_cal = breakfast * 0.30
   breakfast_carb_cal = breakfast * 0.50
   breakfast_carb = breakfast_carb_cal % 4
   lunch_protein_cal = lunch * 0.30
   lunch_carb_cal = lunch * 0.50
   lunch_carb = lunch_carb_cal % 4
   dinner_protein_cal = dinner * 0.30
   dinner_carb_cal = dinner * 0.50
   dinner_carb = dinner_carb_cal % 4
   breakfast_food_df = breakfast_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < breakfast_protein_cal) & (df['Fiber (g)'] <= breakfast_carb) & (df['Calories (kcal)'] < breakfast_carb_cal) & (df['Category'] != 'Meat')]
   lunch_food_df = lunch_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < lunch_protein_cal) & (df['Fiber (g)'] <= lunch_carb) & (df['Calories (kcal)'] < lunch_carb_cal) & (df['Category'] != 'Meat')]
   dinner_food_df = dinner_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < dinner_protein_cal) & (df['Fiber (g)'] <= dinner_carb) & (df['Calories (kcal)'] < dinner_carb_cal) & (df['Category'] != 'Meat')]

   print("----------------------------------------------------------------------")
   print(breakfast_food_df)
   print("----------------------------------------------------------------------") 
   print(lunch_food_df)
   print("----------------------------------------------------------------------")
   print(dinner_food_df)
   print("----------------------------------------------------------------------")
   print("Thanks for using Diet_Forge!")

def diet_Cut_NonVeg(total_cal,weight):
   protein = 2 * weight
   breakfast = total_cal * 0.173
   lunch = total_cal * 0.466
   dinner = total_cal * 0.24
   breakfast_protein_cal = breakfast * 0.30
   breakfast_carb_cal = breakfast * 0.50
   breakfast_carb = breakfast_carb_cal % 4
   lunch_protein_cal = lunch * 0.30
   lunch_carb_cal = lunch * 0.50
   lunch_carb = lunch_carb_cal % 4
   dinner_protein_cal = dinner * 0.30
   dinner_carb_cal = dinner * 0.50
   dinner_carb = dinner_carb_cal % 4
   breakfast_food_df = breakfast_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < breakfast_protein_cal) & (df['Fiber (g)'] <= breakfast_carb) & (df['Calories (kcal)'] < breakfast_carb_cal)]
   lunch_food_df = lunch_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < lunch_protein_cal) & (df['Fiber (g)'] <= lunch_carb) & (df['Calories (kcal)'] < lunch_carb_cal)]
   dinner_food_df = dinner_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < dinner_protein_cal) & (df['Fiber (g)'] <= dinner_carb) & (df['Calories (kcal)'] < dinner_carb_cal)]

   print("----------------------------------------------------------------------")
   print(breakfast_food_df)
   print("----------------------------------------------------------------------") 
   print(lunch_food_df)
   print("----------------------------------------------------------------------")
   print(dinner_food_df)
   print("----------------------------------------------------------------------")
   print("Thanks for using Diet_Forge!")

def diet_Cut_Veg(total_cal,weight):
   protein = 2 * weight
   breakfast = total_cal * 0.173
   lunch = total_cal * 0.466
   dinner = total_cal * 0.24
   breakfast_protein_cal = breakfast * 0.30
   breakfast_carb_cal = breakfast * 0.50
   breakfast_carb = breakfast_carb_cal % 4
   lunch_protein_cal = lunch * 0.30
   lunch_carb_cal = lunch * 0.50
   lunch_carb = lunch_carb_cal % 4
   dinner_protein_cal = dinner * 0.30
   dinner_carb_cal = dinner * 0.50
   dinner_carb = dinner_carb_cal % 4
   breakfast_food_df = breakfast_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < breakfast_protein_cal) & (df['Fiber (g)'] <= breakfast_carb) & (df['Calories (kcal)'] < breakfast_carb_cal) & (df['Category'] != 'Meat')]
   lunch_food_df = lunch_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < lunch_protein_cal) & (df['Fiber (g)'] <= lunch_carb) & (df['Calories (kcal)'] < lunch_carb_cal) & (df['Category'] != 'Meat')]
   dinner_food_df = dinner_df.loc[(df['Protein (g)'] <= protein) & (df['Calories (kcal)'] < dinner_protein_cal) & (df['Fiber (g)'] <= dinner_carb) & (df['Calories (kcal)'] < dinner_carb_cal) & (df['Category'] != 'Meat')]

   print("----------------------------------------------------------------------")
   print(breakfast_food_df)
   print("----------------------------------------------------------------------") 
   print(lunch_food_df)
   print("----------------------------------------------------------------------")
   print(dinner_food_df)
   print("----------------------------------------------------------------------")
   print("Thanks for using Diet_Forge!")

def calcount(BMR, active, weight, veg):
   total_cal = 0
   bulk_cal = 0
   cut_cal = 0
   try:
      if(active == "Sedentary" or active == "Sed"):
         total_cal = BMR * 1.20
      elif(active == "Lightly" or active == "L"):
         total_cal = BMR * 1.375
      elif(active == "Moderately" or active == "M"):
         total_cal = BMR * 1.55
      elif(active == "Very" or active == "V"):
         total_cal = BMR * 1.725
      elif(active == "Super" or active == "Sup"):
         total_cal = BMR * 1.9
      else :
         total_cal = BMR
   except:
      print("U have entered something wrong")

   print(f"Your calorie intake should be {math.trunc(total_cal)}")
   bulk_cal = total_cal + 500
   cut_cal = total_cal - 500
   print(f"Your bulking calorie should be {math.trunc(bulk_cal)}")
   print(f"Your cutting calorie should be {math.trunc(cut_cal)}")

   choice = input("You want a normal diet or bulking diet or cutting diet? ").capitalize()
   if(choice == 'Normal' or choice == 'N'):
      if(veg == 'Y'):
         diet_Normal_Veg(total_cal,weight)
      elif(veg == 'N'):
        diet_Normal_NonVeg(total_cal,weight)
      else:
         print("Enter correctly")
   elif(choice == 'Bulk' or choice == 'B'):
      if(veg == 'Y'):
         diet_Bulk_Veg(bulk_cal,weight)
      elif(veg == 'N'):
        diet_Bulk_NonVeg(bulk_cal,weight)
      else:
         print("Enter correctly") 
   elif(choice == 'Cut' or choice == 'C'):
      if(veg == 'Y'):
         diet_Cut_Veg(cut_cal,weight)
      elif(veg == 'N'):
        diet_Cut_NonVeg(cut_cal,weight)
      else:
         print("Enter correctly") 
   else:
      print("Choose correctly")

def checker(height,weight,age,gender,veg,active):
   if(gender == 'M'):
      BMR = (10 * weight) + (6.25 * height) - (5 * age )+ 5
   elif(gender == 'F'):
      BMR = (10 * weight) +( 6.25 * height) - (5 * age )- 161
   else:
      print('Enter correctly ')

   if(age<15):
      print("Too young for a diet")
   else:
      calcount(BMR,active,weight,veg)

def main():
   name = input("Enter your name: ")
   try:
      weight = int(input("Enter your weight(in kg): "))
      height = int(input("Enter your height(in cm): "))
      age = int(input("Enter your age: "))
      gender = input("Enter your gender(M for male & F for female): ").capitalize()
      active = input("How active are you(Sedentary, Lightly, Moderately, Very, Super)? ").capitalize()
      veg = input("Are you a vegetarian or not(Y for yes, N for no)? ").capitalize()
   except ValueError:
      print("U have entered in wrong format.")

   checker(height,weight,age,gender,veg,active)

if __name__ == "__main__":
    main()
