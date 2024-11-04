import random

# Exercise recommendations for different fitness goals
exercises = {
    "Strength": ["Push-ups", "Deadlift", "Bench Press", "Squats"],
    "Endurance": ["Running", "Cycling", "Jump Rope", "Swimming"],
    "Flexibility": ["Yoga", "Stretching", "Pilates", "Tai Chi"]
}

# Function to generate a weekly plan
def generate_plan(goal):
    if goal not in exercises:
        return "Invalid goal. Please choose from: Strength, Endurance, or Flexibility."
    
    plan = {}
    for day in ["Monday", "Wednesday", "Friday"]:
        plan[day] = random.choice(exercises[goal])
    return plan

# User input
goal = "Endurance"  # Example goal

# Generate weekly plan
weekly_plan = generate_plan(goal)
print(f"Weekly plan for {goal} training:")
for day, exercise in weekly_plan.items():
    print(f"{day}: {exercise}")
