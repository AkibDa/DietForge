from flask import Flask, render_template, request, jsonify
import pandas as pd
import math
from io import StringIO

app = Flask(__name__)

# Load and process the diet data
diet_data = pd.read_csv('Data/diet.csv')
breakfast_data = diet_data[diet_data['Meal'] == 'Breakfast']
lunch_data = diet_data[diet_data['Meal'] == 'Lunch']
dinner_data = diet_data[diet_data['Meal'] == 'Dinner']

def diet_Normal_NonVeg(total_calories, weight):
    breakfast = breakfast_data[
        (breakfast_data['Protein (g)'] >= 0.3 * weight) &
        (breakfast_data['Calories (kcal)'] <= 0.3 * total_calories) &
        (breakfast_data['Fiber (g)'] >= 5)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    lunch = lunch_data[
        (lunch_data['Protein (g)'] >= 0.4 * weight) &
        (lunch_data['Calories (kcal)'] <= 0.4 * total_calories) &
        (lunch_data['Fiber (g)'] >= 8)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    dinner = dinner_data[
        (dinner_data['Protein (g)'] >= 0.3 * weight) &
        (dinner_data['Calories (kcal)'] <= 0.3 * total_calories) &
        (dinner_data['Fiber (g)'] >= 5)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    return {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner
    }

def diet_Normal_Veg(total_calories, weight):
    breakfast = breakfast_data[
        (breakfast_data['Protein (g)'] >= 0.25 * weight) &
        (breakfast_data['Calories (kcal)'] <= 0.3 * total_calories) &
        (breakfast_data['Fiber (g)'] >= 5)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    lunch = lunch_data[
        (lunch_data['Protein (g)'] >= 0.35 * weight) &
        (lunch_data['Calories (kcal)'] <= 0.4 * total_calories) &
        (lunch_data['Fiber (g)'] >= 8)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    dinner = dinner_data[
        (dinner_data['Protein (g)'] >= 0.25 * weight) &
        (dinner_data['Calories (kcal)'] <= 0.3 * total_calories) &
        (dinner_data['Fiber (g)'] >= 5)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    return {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner
    }

def diet_Bulk_NonVeg(total_calories, weight):
    breakfast = breakfast_data[
        (breakfast_data['Protein (g)'] >= 0.4 * weight) &
        (breakfast_data['Calories (kcal)'] <= 0.3 * total_calories) &
        (breakfast_data['Fiber (g)'] >= 5)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    lunch = lunch_data[
        (lunch_data['Protein (g)'] >= 0.5 * weight) &
        (lunch_data['Calories (kcal)'] <= 0.4 * total_calories) &
        (lunch_data['Fiber (g)'] >= 8)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    dinner = dinner_data[
        (dinner_data['Protein (g)'] >= 0.4 * weight) &
        (dinner_data['Calories (kcal)'] <= 0.3 * total_calories) &
        (dinner_data['Fiber (g)'] >= 5)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    return {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner
    }

def diet_Bulk_Veg(total_calories, weight):
    breakfast = breakfast_data[
        (breakfast_data['Protein (g)'] >= 0.35 * weight) &
        (breakfast_data['Calories (kcal)'] <= 0.3 * total_calories) &
        (breakfast_data['Fiber (g)'] >= 5)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    lunch = lunch_data[
        (lunch_data['Protein (g)'] >= 0.45 * weight) &
        (lunch_data['Calories (kcal)'] <= 0.4 * total_calories) &
        (lunch_data['Fiber (g)'] >= 8)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    dinner = dinner_data[
        (dinner_data['Protein (g)'] >= 0.35 * weight) &
        (dinner_data['Calories (kcal)'] <= 0.3 * total_calories) &
        (dinner_data['Fiber (g)'] >= 5)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    return {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner
    }

def diet_Cut_NonVeg(total_calories, weight):
    breakfast = breakfast_data[
        (breakfast_data['Protein (g)'] >= 0.35 * weight) &
        (breakfast_data['Calories (kcal)'] <= 0.3 * total_calories) &
        (breakfast_data['Fiber (g)'] >= 8)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    lunch = lunch_data[
        (lunch_data['Protein (g)'] >= 0.45 * weight) &
        (lunch_data['Calories (kcal)'] <= 0.4 * total_calories) &
        (lunch_data['Fiber (g)'] >= 10)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    dinner = dinner_data[
        (dinner_data['Protein (g)'] >= 0.35 * weight) &
        (dinner_data['Calories (kcal)'] <= 0.3 * total_calories) &
        (dinner_data['Fiber (g)'] >= 8)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    return {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner
    }

def diet_Cut_Veg(total_calories, weight):
    breakfast = breakfast_data[
        (breakfast_data['Protein (g)'] >= 0.3 * weight) &
        (breakfast_data['Calories (kcal)'] <= 0.3 * total_calories) &
        (breakfast_data['Fiber (g)'] >= 8)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    lunch = lunch_data[
        (lunch_data['Protein (g)'] >= 0.4 * weight) &
        (lunch_data['Calories (kcal)'] <= 0.4 * total_calories) &
        (lunch_data['Fiber (g)'] >= 10)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    dinner = dinner_data[
        (dinner_data['Protein (g)'] >= 0.3 * weight) &
        (dinner_data['Calories (kcal)'] <= 0.3 * total_calories) &
        (dinner_data['Fiber (g)'] >= 8)
    ].drop_duplicates(subset=['Food_Item']).head(3).to_dict('records')

    return {
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner
    }

def calculate_bmr(gender, weight, height, age):
    if gender == 'M':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

def calculate_calories(bmr, activity):
    activity_multipliers = {
        'Sedentary': 1.2,
        'Lightly': 1.375,
        'Moderately': 1.55,
        'Very': 1.725,
        'Super': 1.9
    }
    return bmr * activity_multipliers[activity]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        
        # Validate input
        if not all(key in data for key in ['weight', 'height', 'age', 'gender', 'activity', 'is_vegetarian', 'diet_type']):
            return jsonify({'error': 'Missing required fields'}), 400

        weight = float(data['weight'])
        height = float(data['height'])
        age = int(data['age'])
        gender = data['gender']
        activity = data['activity']
        is_vegetarian = data['is_vegetarian']
        diet_type = data['diet_type']

        # Validate age
        if age < 18:
            return jsonify({'error': 'You must be at least 18 years old to use this calculator'}), 400

        # Calculate BMR and calories
        bmr = calculate_bmr(gender, weight, height, age)
        base_calories = calculate_calories(bmr, activity)
        
        # Calculate calories for different goals
        calories = {
            'base': int(base_calories),
            'bulk': int(base_calories * 1.1),  # 10% surplus for bulking
            'cut': int(base_calories * 0.9)   # 10% deficit for cutting
        }

        # Get meal plan based on diet type and preference
        if diet_type == 'Normal':
            if is_vegetarian == 'Y':
                meal_plan = diet_Normal_Veg(calories['base'], weight)
            else:
                meal_plan = diet_Normal_NonVeg(calories['base'], weight)
        elif diet_type == 'Bulk':
            if is_vegetarian == 'Y':
                meal_plan = diet_Bulk_Veg(calories['bulk'], weight)
            else:
                meal_plan = diet_Bulk_NonVeg(calories['bulk'], weight)
        else:  # Cut
            if is_vegetarian == 'Y':
                meal_plan = diet_Cut_Veg(calories['cut'], weight)
            else:
                meal_plan = diet_Cut_NonVeg(calories['cut'], weight)

        return jsonify({
            'calories': calories,
            'meal_plan': meal_plan
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# For local development
if __name__ == '__main__':
    app.run(debug=True)
