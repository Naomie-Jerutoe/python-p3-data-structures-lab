spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # names = [food["name"] for food in spicy_foods]
    # return names

    names = []
    for food in spicy_foods:
        for key, value in food.items():
            if key == "name":
                names.append(value)
    return names

def get_spiciest_foods(spicy_foods):
    spicy_food =[]
    for food in spicy_foods:
        for key, value in food.items():
            if key == "heat_value" and value > 5:
                spicy_food.insert(key, value)
    return spicy_food

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = "🌶" * food["heat_level"]
        print(f"{name} ({cuisine}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_food = [food for food in spicy_foods if food.get("heat_level",0) > 5]
    print_spicy_foods(spiciest_food)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food.get("heat_level",0) for food in spicy_foods)
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    return spicy_foods + [spicy_food]
