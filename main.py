from flask import Flask, render_template, request, jsonify
import pandas as pd
import math
from io import StringIO

app = Flask(__name__)

# Load and process the diet data
diet_data = pd.read_csv('Data/diet.csv')
breakfast_data = diet_data[diet_data['Meal_Type'] == 'Breakfast']
lunch_data = diet_data[diet_data['Meal_Type'] == 'Lunch']
dinner_data = diet_data[diet_data['Meal_Type'] == 'Dinner']

def diet_Normal_NonVeg(weight, height, age, gender, activity_level):
    # Calculate BMR and calories
    bmr = calculate_bmr(gender, weight, height, age)
    calories = calculate_calories(bmr, activity_level)
    
    # Filter data for each meal type
    breakfast_data = diet_data[diet_data['Meal_Type'] == 'Breakfast']
    lunch_data = diet_data[diet_data['Meal_Type'] == 'Lunch']
    dinner_data = diet_data[diet_data['Meal_Type'] == 'Dinner']
    
    # Remove duplicates based on Food_Item
    breakfast_data = breakfast_data.drop_duplicates(subset=['Food_Item'])
    lunch_data = lunch_data.drop_duplicates(subset=['Food_Item'])
    dinner_data = dinner_data.drop_duplicates(subset=['Food_Item'])
    
    # Calculate meal plans
    breakfast_calories = calories * 0.3
    lunch_calories = calories * 0.4
    dinner_calories = calories * 0.3
    
    # Get meal options
    breakfast = breakfast_data[breakfast_data['Calories (kcal)'] <= breakfast_calories].head(3)
    lunch = lunch_data[lunch_data['Calories (kcal)'] <= lunch_calories].head(3)
    dinner = dinner_data[dinner_data['Calories (kcal)'] <= dinner_calories].head(3)
    
    return {
        'calories': calories,
        'breakfast': breakfast.to_dict('records'),
        'lunch': lunch.to_dict('records'),
        'dinner': dinner.to_dict('records')
    }

def diet_Normal_Veg(weight, height, age, gender, activity_level):
    # Calculate BMR and calories
    bmr = calculate_bmr(gender, weight, height, age)
    calories = calculate_calories(bmr, activity_level)
    
    # Filter data for each meal type
    breakfast_data = diet_data[diet_data['Meal_Type'] == 'Breakfast']
    lunch_data = diet_data[diet_data['Meal_Type'] == 'Lunch']
    dinner_data = diet_data[diet_data['Meal_Type'] == 'Dinner']
    
    # Remove duplicates based on Food_Item
    breakfast_data = breakfast_data.drop_duplicates(subset=['Food_Item'])
    lunch_data = lunch_data.drop_duplicates(subset=['Food_Item'])
    dinner_data = dinner_data.drop_duplicates(subset=['Food_Item'])
    
    # Calculate meal plans
    breakfast_calories = calories * 0.3
    lunch_calories = calories * 0.4
    dinner_calories = calories * 0.3
    
    # Get meal options
    breakfast = breakfast_data[breakfast_data['Calories (kcal)'] <= breakfast_calories].head(3)
    lunch = lunch_data[lunch_data['Calories (kcal)'] <= lunch_calories].head(3)
    dinner = dinner_data[dinner_data['Calories (kcal)'] <= dinner_calories].head(3)
    
    return {
        'calories': calories,
        'breakfast': breakfast.to_dict('records'),
        'lunch': lunch.to_dict('records'),
        'dinner': dinner.to_dict('records')
    }

def diet_Bulk_NonVeg(weight, height, age, gender, activity_level):
    # Calculate BMR and calories
    bmr = calculate_bmr(gender, weight, height, age)
    calories = calculate_calories(bmr, activity_level) * 1.2  # 20% more calories for bulking
    
    # Filter data for each meal type
    breakfast_data = diet_data[diet_data['Meal_Type'] == 'Breakfast']
    lunch_data = diet_data[diet_data['Meal_Type'] == 'Lunch']
    dinner_data = diet_data[diet_data['Meal_Type'] == 'Dinner']
    
    # Remove duplicates based on Food_Item
    breakfast_data = breakfast_data.drop_duplicates(subset=['Food_Item'])
    lunch_data = lunch_data.drop_duplicates(subset=['Food_Item'])
    dinner_data = dinner_data.drop_duplicates(subset=['Food_Item'])
    
    # Calculate meal plans
    breakfast_calories = calories * 0.3
    lunch_calories = calories * 0.4
    dinner_calories = calories * 0.3
    
    # Get meal options
    breakfast = breakfast_data[breakfast_data['Calories (kcal)'] <= breakfast_calories].head(3)
    lunch = lunch_data[lunch_data['Calories (kcal)'] <= lunch_calories].head(3)
    dinner = dinner_data[dinner_data['Calories (kcal)'] <= dinner_calories].head(3)
    
    return {
        'calories': calories,
        'breakfast': breakfast.to_dict('records'),
        'lunch': lunch.to_dict('records'),
        'dinner': dinner.to_dict('records')
    }

def diet_Bulk_Veg(weight, height, age, gender, activity_level):
    # Calculate BMR and calories
    bmr = calculate_bmr(gender, weight, height, age)
    calories = calculate_calories(bmr, activity_level) * 1.2  # 20% more calories for bulking
    
    # Filter data for each meal type
    breakfast_data = diet_data[diet_data['Meal_Type'] == 'Breakfast']
    lunch_data = diet_data[diet_data['Meal_Type'] == 'Lunch']
    dinner_data = diet_data[diet_data['Meal_Type'] == 'Dinner']
    
    # Remove duplicates based on Food_Item
    breakfast_data = breakfast_data.drop_duplicates(subset=['Food_Item'])
    lunch_data = lunch_data.drop_duplicates(subset=['Food_Item'])
    dinner_data = dinner_data.drop_duplicates(subset=['Food_Item'])
    
    # Calculate meal plans
    breakfast_calories = calories * 0.3
    lunch_calories = calories * 0.4
    dinner_calories = calories * 0.3
    
    # Get meal options
    breakfast = breakfast_data[breakfast_data['Calories (kcal)'] <= breakfast_calories].head(3)
    lunch = lunch_data[lunch_data['Calories (kcal)'] <= lunch_calories].head(3)
    dinner = dinner_data[dinner_data['Calories (kcal)'] <= dinner_calories].head(3)
    
    return {
        'calories': calories,
        'breakfast': breakfast.to_dict('records'),
        'lunch': lunch.to_dict('records'),
        'dinner': dinner.to_dict('records')
    }

def diet_Cut_NonVeg(weight, height, age, gender, activity_level):
    # Calculate BMR and calories
    bmr = calculate_bmr(gender, weight, height, age)
    calories = calculate_calories(bmr, activity_level) * 0.8  # 20% fewer calories for cutting
    
    # Filter data for each meal type
    breakfast_data = diet_data[diet_data['Meal_Type'] == 'Breakfast']
    lunch_data = diet_data[diet_data['Meal_Type'] == 'Lunch']
    dinner_data = diet_data[diet_data['Meal_Type'] == 'Dinner']
    
    # Remove duplicates based on Food_Item
    breakfast_data = breakfast_data.drop_duplicates(subset=['Food_Item'])
    lunch_data = lunch_data.drop_duplicates(subset=['Food_Item'])
    dinner_data = dinner_data.drop_duplicates(subset=['Food_Item'])
    
    # Calculate meal plans
    breakfast_calories = calories * 0.3
    lunch_calories = calories * 0.4
    dinner_calories = calories * 0.3
    
    # Get meal options
    breakfast = breakfast_data[breakfast_data['Calories (kcal)'] <= breakfast_calories].head(3)
    lunch = lunch_data[lunch_data['Calories (kcal)'] <= lunch_calories].head(3)
    dinner = dinner_data[dinner_data['Calories (kcal)'] <= dinner_calories].head(3)
    
    return {
        'calories': calories,
        'breakfast': breakfast.to_dict('records'),
        'lunch': lunch.to_dict('records'),
        'dinner': dinner.to_dict('records')
    }

def diet_Cut_Veg(weight, height, age, gender, activity_level):
    # Calculate BMR and calories
    bmr = calculate_bmr(gender, weight, height, age)
    calories = calculate_calories(bmr, activity_level) * 0.8  # 20% fewer calories for cutting
    
    # Filter data for each meal type
    breakfast_data = diet_data[diet_data['Meal_Type'] == 'Breakfast']
    lunch_data = diet_data[diet_data['Meal_Type'] == 'Lunch']
    dinner_data = diet_data[diet_data['Meal_Type'] == 'Dinner']
    
    # Remove duplicates based on Food_Item
    breakfast_data = breakfast_data.drop_duplicates(subset=['Food_Item'])
    lunch_data = lunch_data.drop_duplicates(subset=['Food_Item'])
    dinner_data = dinner_data.drop_duplicates(subset=['Food_Item'])
    
    # Calculate meal plans
    breakfast_calories = calories * 0.3
    lunch_calories = calories * 0.4
    dinner_calories = calories * 0.3
    
    # Get meal options
    breakfast = breakfast_data[breakfast_data['Calories (kcal)'] <= breakfast_calories].head(3)
    lunch = lunch_data[lunch_data['Calories (kcal)'] <= lunch_calories].head(3)
    dinner = dinner_data[dinner_data['Calories (kcal)'] <= dinner_calories].head(3)
    
    return {
        'calories': calories,
        'breakfast': breakfast.to_dict('records'),
        'lunch': lunch.to_dict('records'),
        'dinner': dinner.to_dict('records')
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
                meal_plan = diet_Normal_Veg(weight, height, age, gender, activity)
            else:
                meal_plan = diet_Normal_NonVeg(weight, height, age, gender, activity)
        elif diet_type == 'Bulk':
            if is_vegetarian == 'Y':
                meal_plan = diet_Bulk_Veg(weight, height, age, gender, activity)
            else:
                meal_plan = diet_Bulk_NonVeg(weight, height, age, gender, activity)
        else:  # Cut
            if is_vegetarian == 'Y':
                meal_plan = diet_Cut_Veg(weight, height, age, gender, activity)
            else:
                meal_plan = diet_Cut_NonVeg(weight, height, age, gender, activity)

        return jsonify({
            'calories': calories,
            'meal_plan': meal_plan
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# For local development
if __name__ == '__main__':
    app.run(debug=True)
