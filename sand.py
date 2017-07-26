recipes = {"shrimp fettucine alfredo": ["fettucine", "butter", "shrimp", 'salt', "pepper", "garlic", "eggs", "whole milk", "Parmesan cheese", "parsley"],
    "greek salad": ["feta cheese", "cherry tomatoes", "kalamata olives", "red onion", "red wine vinegar", "oregano", "salt", "pepper", "olive oil"],
    "meatball casserole": ["butter", "garlic", "baguette", "cream cheese", "mayonnaise", "Italian seasoning", "meatballs", "spaghetti sauce", "mozzarella"],
    "philly cheesesteak": ["olive oil", "green peppers", "red peppers", "yellow onions", "salt", "pepper", "sirloin steak", "Provolone cheese", "hoagie rolls"],
    "roasted tomato bruschetta": ["cherry tomatoes", "garlic", "olive oil", "salt", "pepper", "pancetta", "sage leaves", "ricotta cheese", "country bread", "sea salt"]
}

def check_ingredients(myIngredients, ingredients_i_need):
    for m in myIngredients:
        if m in ingredients_i_need:
            ingredients_i_need.remove(m)
    return ingredients_i_need
