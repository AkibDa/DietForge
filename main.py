from flask import Flask, render_template, request, jsonify
import pandas as pd
import math

app = Flask(__name__)

# Load and prepare the data
df = pd.read_csv("Data/diet.csv")
df = df.drop(columns=['Date', 'User_ID'])
breakfast_df = df[df['Meal_Type'] == 'Breakfast']
lunch_df = df[df['Meal_Type'] == 'Lunch']
dinner_df = df[df['Meal_Type'] == 'Dinner']

def diet_Normal_NonVeg(total_cal, weight):
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
    
    # Remove duplicates based on Food_Item
    breakfast_food_df = breakfast_food_df.drop_duplicates(subset=['Food_Item'])
    lunch_food_df = lunch_food_df.drop_duplicates(subset=['Food_Item'])
    dinner_food_df = dinner_food_df.drop_duplicates(subset=['Food_Item'])
    
    return {
        'breakfast': breakfast_food_df.to_dict('records'),
        'lunch': lunch_food_df.to_dict('records'),
        'dinner': dinner_food_df.to_dict('records')
    }

def diet_Normal_Veg(total_cal, weight):
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
    
    return {
        'breakfast': breakfast_food_df.to_dict('records'),
        'lunch': lunch_food_df.to_dict('records'),
        'dinner': dinner_food_df.to_dict('records')
    }

def diet_Bulk_NonVeg(total_cal, weight):
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
    
    # Remove duplicates based on Food_Item
    breakfast_food_df = breakfast_food_df.drop_duplicates(subset=['Food_Item'])
    lunch_food_df = lunch_food_df.drop_duplicates(subset=['Food_Item'])
    dinner_food_df = dinner_food_df.drop_duplicates(subset=['Food_Item'])
    
    return {
        'breakfast': breakfast_food_df.to_dict('records'),
        'lunch': lunch_food_df.to_dict('records'),
        'dinner': dinner_food_df.to_dict('records')
    }

def diet_Bulk_Veg(total_cal, weight):
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
    
    # Remove duplicates based on Food_Item
    breakfast_food_df = breakfast_food_df.drop_duplicates(subset=['Food_Item'])
    lunch_food_df = lunch_food_df.drop_duplicates(subset=['Food_Item'])
    dinner_food_df = dinner_food_df.drop_duplicates(subset=['Food_Item'])
    
    return {
        'breakfast': breakfast_food_df.to_dict('records'),
        'lunch': lunch_food_df.to_dict('records'),
        'dinner': dinner_food_df.to_dict('records')
    }

def diet_Cut_NonVeg(total_cal, weight):
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
    
    # Remove duplicates based on Food_Item
    breakfast_food_df = breakfast_food_df.drop_duplicates(subset=['Food_Item'])
    lunch_food_df = lunch_food_df.drop_duplicates(subset=['Food_Item'])
    dinner_food_df = dinner_food_df.drop_duplicates(subset=['Food_Item'])
    
    return {
        'breakfast': breakfast_food_df.to_dict('records'),
        'lunch': lunch_food_df.to_dict('records'),
        'dinner': dinner_food_df.to_dict('records')
    }

def diet_Cut_Veg(total_cal, weight):
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
    
    # Remove duplicates based on Food_Item
    breakfast_food_df = breakfast_food_df.drop_duplicates(subset=['Food_Item'])
    lunch_food_df = lunch_food_df.drop_duplicates(subset=['Food_Item'])
    dinner_food_df = dinner_food_df.drop_duplicates(subset=['Food_Item'])
    
    return {
        'breakfast': breakfast_food_df.to_dict('records'),
        'lunch': lunch_food_df.to_dict('records'),
        'dinner': dinner_food_df.to_dict('records')
    }

def calculate_bmr(height, weight, age, gender):
    if gender == 'M':
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == 'F':
        return (10 * weight) + (6.25 * height) - (5 * age) - 161
    return 0

def calculate_calories(bmr, activity_level):
    activity_multipliers = {
        'Sedentary': 1.20,
        'Lightly': 1.375,
        'Moderately': 1.55,
        'Very': 1.725,
        'Super': 1.9
    }
    return bmr * activity_multipliers.get(activity_level, 1.0)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        weight = float(data['weight'])
        height = float(data['height'])
        age = int(data['age'])
        gender = data['gender']
        activity = data['activity']
        is_vegetarian = data['is_vegetarian'] == 'Y'
        diet_type = data['diet_type']

        if age < 15:
            return jsonify({'error': 'Too young for a diet'}), 400

        bmr = calculate_bmr(height, weight, age, gender)
        base_calories = calculate_calories(bmr, activity)

        if diet_type == 'Bulk':
            total_calories = base_calories + 500
            if is_vegetarian:
                meal_plan = diet_Bulk_Veg(total_calories, weight)
            else:
                meal_plan = diet_Bulk_NonVeg(total_calories, weight)
        elif diet_type == 'Cut':
            total_calories = base_calories - 500
            if is_vegetarian:
                meal_plan = diet_Cut_Veg(total_calories, weight)
            else:
                meal_plan = diet_Cut_NonVeg(total_calories, weight)
        else:  # Normal
            total_calories = base_calories
            if is_vegetarian:
                meal_plan = diet_Normal_Veg(total_calories, weight)
            else:
                meal_plan = diet_Normal_NonVeg(total_calories, weight)

        return jsonify({
            'calories': {
                'base': math.trunc(base_calories),
                'bulk': math.trunc(base_calories + 500),
                'cut': math.trunc(base_calories - 500)
            },
            'meal_plan': meal_plan
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
