"""
AI ENGINE - Personalized Workout + Diet + Study Plan Generator
Designed for: 75kg, 5'9", 18yo, Male, Vegetarian, Bodyweight Only
"""

import math
from datetime import datetime, timedelta


def calculate_body_stats(weight, height_cm, age, gender="male"):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    if gender == "male":
        bmr = 10 * weight + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height_cm - 5 * age - 161

    tdee = bmr * 1.55
    target_calories = tdee - 500
    target_weight = weight - 8

    protein_g = weight * 1.4
    fat_g = weight * 0.8
    protein_cal = protein_g * 4
    fat_cal = fat_g * 9
    carb_cal = target_calories - protein_cal - fat_cal
    carb_g = carb_cal / 4

    return {
        "bmi": round(bmi, 1),
        "bmr": round(bmr),
        "tdee": round(tdee),
        "target_calories": round(target_calories),
        "target_weight": round(target_weight, 1),
        "protein_g": round(protein_g),
        "fat_g": round(fat_g),
        "carb_g": round(carb_g),
        "weight_loss_per_week": 0.6,
    }


def get_current_phase(day_number):
    if day_number <= 25:
        return 1, "FOUNDATION", "Build base strength & stamina"
    elif day_number <= 50:
        return 2, "BUILD", "Increase intensity & endurance"
    elif day_number <= 75:
        return 3, "INTENSITY", "Push limits & burn fat"
    else:
        return 4, "PEAK", "Maximum performance"


def generate_morning_workout(day_number):
    phase, phase_name, phase_desc = get_current_phase(day_number)
    day_type = day_number % 7

    warmup = [
        {"exercise": "Jumping Jacks", "duration": "2 min"},
        {"exercise": "High Knees", "duration": "1 min"},
        {"exercise": "Arm Circles", "duration": "1 min"},
        {"exercise": "Bodyweight Squats (slow)", "duration": "1 min"},
    ]

    cooldown = [
        {"exercise": "Standing Quad Stretch", "duration": "30 sec each"},
        {"exercise": "Hamstring Stretch", "duration": "30 sec each"},
        {"exercise": "Child's Pose", "duration": "1 min"},
        {"exercise": "Deep Breathing", "duration": "1 min"},
    ]

    if phase == 1:
        if day_type in [1, 4]:
            main = [
                {"exercise": "Knee Push-ups", "sets": 3, "reps": "8-10"},
                {"exercise": "Regular Push-ups", "sets": 2, "reps": "5-8"},
                {"exercise": "Wall Push-ups", "sets": 2, "reps": "15"},
                {"exercise": "Plank Hold", "sets": 3, "reps": "20 sec"},
                {"exercise": "Crunches", "sets": 3, "reps": "15"},
                {"exercise": "Mountain Climbers", "sets": 3, "reps": "10"},
            ]
        elif day_type in [2, 5]:
            main = [
                {"exercise": "Bodyweight Squats", "sets": 3, "reps": "15"},
                {"exercise": "Lunges", "sets": 3, "reps": "10 each leg"},
                {"exercise": "Glute Bridges", "sets": 3, "reps": "15"},
                {"exercise": "Calf Raises", "sets": 3, "reps": "20"},
                {"exercise": "Wall Sit", "sets": 3, "reps": "20 sec"},
                {"exercise": "Leg Raises", "sets": 3, "reps": "10"},
            ]
        elif day_type in [3, 6]:
            main = [
                {"exercise": "Push-ups", "sets": 3, "reps": "8"},
                {"exercise": "Squats", "sets": 3, "reps": "15"},
                {"exercise": "Plank", "sets": 3, "reps": "20 sec"},
                {"exercise": "Lunges", "sets": 2, "reps": "10 each"},
                {"exercise": "Crunches", "sets": 3, "reps": "15"},
                {"exercise": "Burpees (slow)", "sets": 2, "reps": "5"},
            ]
        else:
            main = [
                {"exercise": "Yoga Sun Salutation", "sets": 5, "reps": "1 flow"},
                {"exercise": "Deep Stretching", "sets": 1, "reps": "10 min"},
                {"exercise": "Light Walking", "sets": 1, "reps": "5 min"},
                {"exercise": "Meditation", "sets": 1, "reps": "5 min"},
            ]

    elif phase == 2:
        if day_type in [1, 4]:
            main = [
                {"exercise": "Push-ups", "sets": 4, "reps": "15"},
                {"exercise": "Diamond Push-ups", "sets": 3, "reps": "8"},
                {"exercise": "Wide Push-ups", "sets": 3, "reps": "12"},
                {"exercise": "Plank Hold", "sets": 3, "reps": "40 sec"},
                {"exercise": "Bicycle Crunches", "sets": 3, "reps": "20"},
                {"exercise": "Mountain Climbers", "sets": 3, "reps": "20"},
                {"exercise": "Shoulder Taps", "sets": 3, "reps": "12"},
            ]
        elif day_type in [2, 5]:
            main = [
                {"exercise": "Squats", "sets": 4, "reps": "20"},
                {"exercise": "Jump Squats", "sets": 3, "reps": "10"},
                {"exercise": "Bulgarian Split Squat", "sets": 3, "reps": "8 each"},
                {"exercise": "Glute Bridges", "sets": 3, "reps": "20"},
                {"exercise": "Wall Sit", "sets": 3, "reps": "40 sec"},
                {"exercise": "Calf Raises", "sets": 3, "reps": "25"},
                {"exercise": "Leg Raises", "sets": 3, "reps": "15"},
            ]
        elif day_type in [3, 6]:
            main = [
                {"exercise": "Burpees", "sets": 3, "reps": "10"},
                {"exercise": "Push-ups", "sets": 3, "reps": "15"},
                {"exercise": "Squats", "sets": 3, "reps": "20"},
                {"exercise": "Plank to Push-up", "sets": 3, "reps": "8"},
                {"exercise": "Lunges", "sets": 3, "reps": "12 each"},
                {"exercise": "V-ups", "sets": 3, "reps": "10"},
            ]
        else:
            main = [
                {"exercise": "Yoga Flow", "sets": 5, "reps": "1 flow"},
                {"exercise": "Deep Stretching", "sets": 1, "reps": "15 min"},
                {"exercise": "Meditation", "sets": 1, "reps": "5 min"},
            ]

    elif phase == 3:
        if day_type in [1, 4]:
            main = [
                {"exercise": "Decline Push-ups (bed)", "sets": 4, "reps": "15"},
                {"exercise": "Diamond Push-ups", "sets": 3, "reps": "12"},
                {"exercise": "Pike Push-ups", "sets": 3, "reps": "10"},
                {"exercise": "Pseudo Planche Push-ups", "sets": 3, "reps": "8"},
                {"exercise": "Plank Hold", "sets": 3, "reps": "60 sec"},
                {"exercise": "Clap Push-ups", "sets": 2, "reps": "5"},
            ]
        elif day_type in [2, 5]:
            main = [
                {"exercise": "Jump Squats", "sets": 4, "reps": "15"},
                {"exercise": "Pistol Squat (assisted)", "sets": 3, "reps": "5 each"},
                {"exercise": "Bulgarian Split Squat", "sets": 3, "reps": "12 each"},
                {"exercise": "Single Leg Glute Bridge", "sets": 3, "reps": "12 each"},
                {"exercise": "Wall Sit", "sets": 3, "reps": "60 sec"},
                {"exercise": "Hanging Leg Raises", "sets": 3, "reps": "10"},
            ]
        elif day_type in [3, 6]:
            main = [
                {"exercise": "HIIT: Burpees", "sets": 3, "reps": "40 sec"},
                {"exercise": "HIIT: Mountain Climbers", "sets": 3, "reps": "40 sec"},
                {"exercise": "HIIT: Jump Squats", "sets": 3, "reps": "40 sec"},
                {"exercise": "HIIT: Push-ups", "sets": 3, "reps": "40 sec"},
                {"exercise": "HIIT: High Knees", "sets": 3, "reps": "40 sec"},
                {"exercise": "HIIT: Plank Jacks", "sets": 3, "reps": "40 sec"},
            ]
        else:
            main = [
                {"exercise": "Yoga Flow", "sets": 8, "reps": "1 flow"},
                {"exercise": "Deep Stretching", "sets": 1, "reps": "20 min"},
                {"exercise": "Meditation", "sets": 1, "reps": "10 min"},
            ]

    else:
        if day_type in [1, 4]:
            main = [
                {"exercise": "Decline Push-ups", "sets": 4, "reps": "20"},
                {"exercise": "Pike Push-ups", "sets": 4, "reps": "12"},
                {"exercise": "Diamond Push-ups", "sets": 4, "reps": "15"},
                {"exercise": "Clap Push-ups", "sets": 3, "reps": "8"},
                {"exercise": "Handstand Hold (wall)", "sets": 3, "reps": "15 sec"},
                {"exercise": "Plank", "sets": 3, "reps": "90 sec"},
                {"exercise": "L-sit Attempt", "sets": 3, "reps": "10 sec"},
            ]
        elif day_type in [2, 5]:
            main = [
                {"exercise": "Pistol Squats", "sets": 3, "reps": "8 each"},
                {"exercise": "Jump Squats", "sets": 4, "reps": "20"},
                {"exercise": "Bulgarian Split Squat", "sets": 4, "reps": "15 each"},
                {"exercise": "Single Leg Deadlift", "sets": 3, "reps": "12 each"},
                {"exercise": "Box Jumps", "sets": 3, "reps": "15"},
                {"exercise": "Calf Raises (single)", "sets": 3, "reps": "20 each"},
                {"exercise": "Hanging Leg Raises", "sets": 4, "reps": "15"},
            ]
        elif day_type in [3, 6]:
            main = [
                {"exercise": "TABATA: Burpees", "sets": 4, "reps": "20 sec MAX"},
                {"exercise": "TABATA: Mountain Climbers", "sets": 4, "reps": "20 sec MAX"},
                {"exercise": "TABATA: Jump Squats", "sets": 4, "reps": "20 sec MAX"},
                {"exercise": "TABATA: Push-ups", "sets": 4, "reps": "20 sec MAX"},
                {"exercise": "TABATA: High Knees", "sets": 4, "reps": "20 sec MAX"},
                {"exercise": "TABATA: Star Jumps", "sets": 4, "reps": "20 sec MAX"},
            ]
        else:
            main = [
                {"exercise": "Advanced Yoga Flow", "sets": 10, "reps": "1 flow"},
                {"exercise": "Meditation", "sets": 1, "reps": "15 min"},
                {"exercise": "Full Body Mobility", "sets": 1, "reps": "15 min"},
            ]

    return {
        "phase": phase,
        "phase_name": phase_name,
        "phase_desc": phase_desc,
        "day_number": day_number,
        "workout": {
            "warmup": warmup,
            "main": main,
            "cooldown": cooldown,
        },
        "estimated_calories_burned": 250 + (phase * 50),
        "estimated_duration": "45-55 min",
    }


def generate_running_plan(day_number):
    phase, phase_name, _ = get_current_phase(day_number)
    day_type = day_number % 7

    if phase == 1:
        target_distance = "2-3 km"
        target_pace = "8-9 min/km"
        calories = 200
        if day_type in [1, 3, 5]:
            plan = "Walk 2 min > Jog 1 min > Repeat 10x > Walk 5 min cooldown"
        elif day_type in [2, 4, 6]:
            plan = "Walk 1 min > Jog 2 min > Repeat 8x > Walk 5 min cooldown"
        else:
            plan = "Easy walk 30 min (recovery) + Stretching 15 min"

    elif phase == 2:
        target_distance = "4-5 km"
        target_pace = "7-8 min/km"
        calories = 350
        if day_type in [1, 3, 5]:
            plan = "Warmup 5 min > Steady jog 20 min > Walk 5 min > Jog 15 min > Cooldown 5 min"
        elif day_type in [2, 4]:
            plan = "Warmup 5 min > Sprint 30s / Jog 90s x 10 > Cooldown 10 min"
        elif day_type == 6:
            plan = "Long slow run: 35-40 min continuous at comfortable pace"
        else:
            plan = "Easy jog 20 min + Stretching 20 min (recovery)"

    elif phase == 3:
        target_distance = "5-7 km"
        target_pace = "6-7 min/km"
        calories = 450
        if day_type in [1, 3, 5]:
            plan = "Warmup 5 min > Tempo run 30 min (push pace) > Cooldown 10 min"
        elif day_type in [2, 4]:
            plan = "Warmup 5 min > Sprint 1 min / Jog 1 min x 12 > Cooldown 10 min"
        elif day_type == 6:
            plan = "Long run: 45-50 min continuous at steady pace"
        else:
            plan = "Easy jog 25 min + Mobility work 15 min"

    else:
        target_distance = "7-10 km"
        target_pace = "5:30-6:30 min/km"
        calories = 550
        if day_type in [1, 3, 5]:
            plan = "Warmup 5 min > Tempo run 35-40 min > Cooldown 5 min"
        elif day_type in [2, 4]:
            plan = "Warmup 5 min > Sprint 400m / Jog 200m x 8-10 > Cooldown 10 min"
        elif day_type == 6:
            plan = "Long run: 50-60 min continuous (your best distance!)"
        else:
            plan = "Recovery jog 20 min + Deep stretching 20 min"

    return {
        "phase": phase,
        "phase_name": phase_name,
        "day_number": day_number,
        "target_distance": target_distance,
        "target_pace": target_pace,
        "plan": plan,
        "calories": calories,
    }


def generate_diet_plan(day_number, target_calories=1900):
    phase, _, _ = get_current_phase(day_number)
    idx = (day_number - 1) % 7

    breakfast_options = [
        {"meal": "Poha + 1 Glass Milk + Banana", "calories": 420, "protein": "20g", "note": "Quick energy breakfast"},
        {"meal": "2 Roti + Soya Chunk Curry + Curd (200g)", "calories": 440, "protein": "28g", "note": "Soya = cheapest protein!"},
        {"meal": "Upma + Sprouts (50g) + 1 Glass Milk", "calories": 400, "protein": "22g", "note": "Soak sprouts overnight"},
        {"meal": "3 Idli + Sambhar + Banana + Curd", "calories": 380, "protein": "18g", "note": "Add peanut chutney"},
        {"meal": "2 Paratha + Curd + Roasted Chana (30g)", "calories": 460, "protein": "20g", "note": "Keep chana in room"},
        {"meal": "Oats Porridge (milk) + Banana + 5 Almonds", "calories": 380, "protein": "18g", "note": "Buy oats - cheap & filling"},
        {"meal": "2 Roti + Dal + Curd + Banana", "calories": 430, "protein": "22g", "note": "Simple but effective"},
    ]

    lunch_options = [
        {"meal": "3 Roti + Dal (extra) + Sabzi + Salad + Curd", "calories": 550, "protein": "22g", "note": "Ask for extra dal!"},
        {"meal": "Rice (1 bowl) + Rajma + Salad + Curd", "calories": 530, "protein": "20g", "note": "Rajma = great protein"},
        {"meal": "3 Roti + Chole + Salad + Buttermilk", "calories": 520, "protein": "22g", "note": "Chole is protein-rich"},
        {"meal": "Rice (1 bowl) + Dal + Paneer Sabzi + Salad", "calories": 560, "protein": "25g", "note": "Paneer day = best!"},
        {"meal": "3 Roti + Mixed Veg + Dal + Curd + Salad", "calories": 500, "protein": "18g", "note": "Load up on salad"},
        {"meal": "Rice + Sambhar + Curd + Salad", "calories": 480, "protein": "16g", "note": "Add sprouts from room"},
        {"meal": "3 Roti + Soya Curry + Salad + Buttermilk", "calories": 540, "protein": "28g", "note": "Soya power!"},
    ]

    snack_options = [
        {"meal": "Roasted Chana (50g) + 1 Fruit", "calories": 200, "protein": "12g"},
        {"meal": "Peanuts (30g) + 1 Banana", "calories": 220, "protein": "10g"},
        {"meal": "Makhana (30g) + Green Tea", "calories": 150, "protein": "5g"},
        {"meal": "Sprouts Chaat (50g) + Lemon", "calories": 180, "protein": "12g"},
        {"meal": "Peanut Butter Toast + Apple", "calories": 250, "protein": "10g"},
        {"meal": "Roasted Soya Nuts (30g) + Fruit", "calories": 180, "protein": "14g"},
        {"meal": "Curd (200g) + Honey + 5 Almonds", "calories": 200, "protein": "12g"},
    ]

    dinner_options = [
        {"meal": "2 Roti + Dal + Light Sabzi + Warm Milk", "calories": 450, "protein": "20g", "note": "No rice at night"},
        {"meal": "2 Roti + Paneer + Salad + Milk", "calories": 480, "protein": "25g", "note": "Slow protein release"},
        {"meal": "Khichdi (light) + Curd + Salad", "calories": 400, "protein": "15g", "note": "Great for digestion"},
        {"meal": "2 Roti + Dal + Sabzi + Buttermilk", "calories": 420, "protein": "18g", "note": "Aids digestion"},
        {"meal": "2 Roti + Chole + Salad + Milk", "calories": 470, "protein": "22g", "note": "Protein-rich dinner"},
        {"meal": "1 Roti + Dal Soup + Salad + Curd", "calories": 350, "protein": "16g", "note": "Light = better sleep"},
        {"meal": "2 Roti + Mixed Dal + Sabzi + Haldi Milk", "calories": 440, "protein": "20g", "note": "Recovery booster"},
    ]

    pre_workout = {
        "meal": "1 Banana + 1 Glass Warm Water",
        "calories": 100,
        "protein": "1g",
        "time": "4:45 AM",
    }

    post_workout = {
        "meal": "1 Glass Milk + 1 Tbsp Peanut Butter",
        "calories": 200,
        "protein": "15g",
        "time": "6:00 AM",
    }

    before_bed = {
        "meal": "Warm Milk + Turmeric (Haldi)",
        "calories": 120,
        "protein": "8g",
        "time": "10:00 PM",
    }

    total_calories = (
        pre_workout["calories"]
        + post_workout["calories"]
        + breakfast_options[idx]["calories"]
        + snack_options[idx]["calories"]
        + lunch_options[idx]["calories"]
        + snack_options[(idx + 3) % 7]["calories"]
        + dinner_options[idx]["calories"]
        + before_bed["calories"]
    )

    return {
        "day_number": day_number,
        "target_calories": target_calories,
        "actual_calories": total_calories,
        "meals": [
            {"time": "4:45 AM", "name": "Pre-Workout", **pre_workout},
            {"time": "6:00 AM", "name": "Post-Workout", **post_workout},
            {"time": "7:30 AM", "name": "Breakfast", **breakfast_options[idx]},
            {"time": "11:00 AM", "name": "Mid-Morning Snack", **snack_options[idx]},
            {"time": "1:00 PM", "name": "Lunch", **lunch_options[idx]},
            {"time": "4:30 PM", "name": "Evening Snack", **snack_options[(idx + 3) % 7]},
            {"time": "8:30 PM", "name": "Dinner", **dinner_options[idx]},
            {"time": "10:00 PM", "name": "Before Bed", **before_bed},
        ],
        "water_target": "4+ litres",
        "water_schedule": [
            "5:00 AM - 1 glass (wake up)",
            "6:00 AM - 1 glass (post workout)",
            "8:00 AM - 1 glass",
            "10:00 AM - 1 glass",
            "12:00 PM - 1 glass",
            "2:00 PM - 1 glass",
            "4:00 PM - 1 glass",
            "6:00 PM - 1 glass",
            "7:00 PM - 1 glass (before run)",
            "8:00 PM - 1 glass (after run)",
            "9:00 PM - 1 glass",
        ],
        "supplements_to_buy": [
            "Peanut Butter (Rs.200/month)",
            "Roasted Chana (Rs.50/month)",
            "Soya Chunks (Rs.40/kg)",
            "Bananas (Rs.30/dozen)",
            "Almonds (Rs.100/month)",
            "Sprouts - soak moong overnight (Rs.20/month)",
            "Honey (Rs.150)",
            "Oats (Rs.100/month)",
        ],
    }


def generate_study_plan(day_number):
    study_plans = {}

    python_topics = [
        "Python Setup + Variables + Data Types",
        "Strings + String Methods",
        "Lists + Tuples + Sets",
        "Dictionaries + Loops",
        "Functions + Lambda",
        "File Handling + Exceptions",
        "OOP: Classes + Objects",
        "OOP: Inheritance + Polymorphism",
        "Comprehensions + Generators",
        "Intermediate Python Part 1",
        "Intermediate Python Part 2",
        "Python Project Day",
    ]
    for d in range(1, 13):
        study_plans[d] = {
            "phase": "PYTHON FUNDAMENTALS",
            "topic": python_topics[d - 1],
            "session1": "Watch lecture: " + python_topics[d - 1],
            "session2": "Practice coding exercises + HackerRank",
        }

    math_topics = [
        "Linear Algebra (Vectors, Matrices)",
        "Calculus (Derivatives, Gradients)",
        "Probability (Bayes Theorem)",
        "Statistics (Distributions)",
        "Information Theory + Revision",
    ]
    for i, d in enumerate(range(13, 18)):
        study_plans[d] = {
            "phase": "MATH FOR ML",
            "topic": math_topics[i],
            "session1": "Watch: " + math_topics[i],
            "session2": "Implement in Python + Problems",
        }

    ds_topics = [
        "NumPy Arrays + Operations",
        "NumPy Advanced",
        "Pandas Series + DataFrames",
        "Pandas Filtering + GroupBy",
        "Pandas Merge + Missing Data",
        "Matplotlib Plotting",
        "Seaborn Visualization",
        "EDA Part 1",
        "EDA Part 2",
        "EDA Project",
    ]
    for i, d in enumerate(range(18, 28)):
        study_plans[d] = {
            "phase": "DATA SCIENCE TOOLKIT",
            "topic": ds_topics[i],
            "session1": "Watch: " + ds_topics[i],
            "session2": "Practice with real datasets",
        }

    ml_topics = [
        "What is ML? Types + Bias/Variance",
        "Linear Regression (from scratch)",
        "Linear Regression (sklearn)",
        "Multiple + Polynomial Regression",
        "Regularization (Ridge, Lasso)",
        "Regression Metrics",
        "Logistic Regression",
        "Classification Metrics",
        "KNN",
        "Decision Trees",
        "Random Forest",
        "SVM",
        "Naive Bayes",
        "Ensemble Methods",
        "XGBoost + Gradient Boosting",
        "LightGBM + CatBoost",
        "K-Means Clustering",
        "Hierarchical + DBSCAN",
        "PCA",
        "Feature Engineering",
        "Feature Selection",
        "Cross Validation",
        "Hyperparameter Tuning",
        "Imbalanced Data",
        "ML Pipelines",
        "ML Project 1",
        "ML Project 2",
        "ML Revision",
    ]
    for i, d in enumerate(range(28, 56)):
        study_plans[d] = {
            "phase": "MACHINE LEARNING",
            "topic": ml_topics[i],
            "session1": "Watch: " + ml_topics[i],
            "session2": "Implement + Practice",
        }

    dl_topics = [
        "Neural Network Intuition",
        "Backpropagation",
        "Loss Functions + Optimizers",
        "TensorFlow + Keras Basics",
        "TensorFlow Advanced",
        "PyTorch Basics",
        "DL Regularization",
        "Weight Init + Gradients",
        "CNN Intuition",
        "Build CNN (TensorFlow)",
        "Build CNN (PyTorch)",
        "Famous CNN Architectures",
        "Transfer Learning",
        "Data Augmentation",
        "Object Detection (YOLO)",
        "CNN Project",
        "RNN Basics",
        "LSTM + GRU",
        "Word Embeddings",
        "Text Classification",
        "Time Series",
        "Autoencoders + VAE",
        "GANs",
    ]
    for i, d in enumerate(range(56, 79)):
        study_plans[d] = {
            "phase": "DEEP LEARNING",
            "topic": dl_topics[i],
            "session1": "Watch: " + dl_topics[i],
            "session2": "Build + Train models",
        }

    nlp_topics = [
        "NLP Basics (Tokenization)",
        "TF-IDF + Text Classification",
        "Attention Mechanism",
        "Transformer Architecture",
        "Build GPT from Scratch",
        "BERT + Hugging Face",
        "Hugging Face Transformers",
        "Fine-tuning BERT",
        "GPT + LLMs + Prompting",
        "LangChain Basics",
        "RAG",
        "NLP Project",
    ]
    for i, d in enumerate(range(79, 91)):
        study_plans[d] = {
            "phase": "NLP & TRANSFORMERS",
            "topic": nlp_topics[i],
            "session1": "Watch: " + nlp_topics[i],
            "session2": "Build NLP apps",
        }

    deploy_topics = [
        "Flask API",
        "Streamlit Web Apps",
        "Model Serialization",
        "Docker + HF Spaces",
        "Capstone Project 1 Start",
        "Capstone Project 1 Complete",
        "Capstone Project 2 Start",
        "Capstone Project 2 Complete",
        "Capstone Project 3",
        "Portfolio + LinkedIn + CELEBRATE!",
    ]
    for i, d in enumerate(range(91, 101)):
        study_plans[d] = {
            "phase": "DEPLOYMENT & PROJECTS",
            "topic": deploy_topics[i],
            "session1": "Watch: " + deploy_topics[i],
            "session2": "Build + Deploy",
        }

    if day_number in study_plans:
        return study_plans[day_number]
    else:
        return {
            "phase": "BEYOND 100",
            "topic": "Keep learning!",
            "session1": "Advanced topics",
            "session2": "Kaggle competitions",
        }