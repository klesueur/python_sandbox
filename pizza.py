# Build a pizza!


user_pizza = []


size_price_sets = {
    "small": 6.99,
    "medium": 9.99,
    "large": 12.99,
    "x-large": 15.99
}

cheeses = {
    "no cheese": 0.00,
    "mozzarella": 0.00,
    "double mozzarella": 1.50
}

# Make all veggie toppings 0.50 each
toppings = {
    "Pepperoni": 1.50,
    "Sausage": 1.50,
    "Ham": 1.50,
    "Green Peppers": 1.00,
    "Olives": 1.00,
    "Mushrooms": 1.00,
    "Onion": 1.00,
    "Basil": 0.50,
    "Pineapple": 1.50
}


# Function to choose size
def choose_size():
    print("Choose size: Small, Medium, Large, or Extra Large?")
    size = input(f"Enter size: ").lower()
    if size in ["extra large", "x-large"]:
        size_set = size, size_price_sets["x-large"]
        user_pizza.append(size_set)
        return size_set
    elif size in size_price_sets:
        size_set = size, size_price_sets[size]
        user_pizza.append(size_set)
        return size_set
    else:
        print("Invalid size. Please enter a valid size.")
        return choose_size()
    

# Choose cheese
def choose_cheese():
    print("Would you like cheese?")
    wants_cheese = input("Yes or no: ").lower()
    cheese = "no cheese"
    if wants_cheese in ["no" , "nope" , "no thank you"]:
        if cheese in cheeses:
            print('Okay, no cheese. Got it.')
            cheese_set = cheese, cheeses[cheese]
            user_pizza.append(cheese_set)
            return cheese_set
        else:
            print("Cheese error. Did you want cheese?")
            return choose_cheese()
    elif wants_cheese == "yes":
        print("Great! Double cheese, or regular?")
        is_double_cheese = input("Type 'Double' or 'Regular': ")
        cheese = "double mozzarella"
        if is_double_cheese in ["double", "double cheese", "double mozzarella"]:
            if cheese in cheeses:
                cheese_set = cheese, cheeses[cheese]
                user_pizza.append(cheese_set)
                return cheese_set
        elif is_double_cheese in ["regular", "regular cheese"]:
            cheese = "mozzarella"
            if cheese in cheeses:
                cheese_set = cheese, cheeses[cheese]
                user_pizza.append(cheese_set)
                return cheese_set
        else:
            print("Error with cheese option. Please try again.")
            return choose_cheese()
        print("Awesome. Let's start working on your toppings... ")
    else:
        print("ERROR:  Please use 'Yes' or 'No' only.")
    

# Choose toppings
def choose_toppings():
    topping_choices = []
    print('Any toppings?')
    wants_toppings = input("Yes or No: ").lower()
    if wants_toppings in ["no","no thank you", "nope"]:
        is_just_cheese = input("Okay, so just cheese?: ")
        if is_just_cheese in ["yes", "correct", "ya", "yeah", "yep"]:
            print("Great! Let's review your pizza order...")
            return
        elif is_just_cheese == "no":
            print("Got it. Okay, what toppings would you like?")
            print("Toppings List: " + topping_choices)
            choose_toppings()
        else:
            print("Toppings error. Please try again.")
            print(toppings)
    print(topping_choices)



print("Hello, customer! Build your pizza:")
choose_size()
print(user_pizza)
choose_cheese()
print(user_pizza)
choose_toppings()
print("Pizza order: ")
print(user_pizza)