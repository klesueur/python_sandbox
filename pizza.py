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
    "double mozzarella": 2.00
}

toppings_protein = ["Pepperoni","Sausage","Ham"]

# Make all veggie toppings 0.50 each
toppings_veggies = [
    "Green Peppers",
    "Olives",
    "Mushrooms",
    "Onion",
    "Basil",
    "Pineapple"
]


# Function to choose size
def choose_size():
    print("Choose size: Small, Medium, Large, or Extra Large?")
    size = input(f"Enter size: ").lower()
    if size in ["extra large", "x-large"]:
        size_set = size, size_price_sets["x-large"]
        user_pizza.append(size_set)
        return size_set
    elif size in size_price_sets:
        size_set = size, size_price_sets["x-large"]
        user_pizza.append(size_set)
        return size_set
    else:
        print("Invalid size. Please enter a valid size.")
        return choose_size()

# def choose_size(size):
#     print(size)
    

# Choose cheese
def choose_cheese():
    print("Would you like cheese?")
    wants_cheese = input("Yes or no: ")
    cheese = "No cheese"
    if wants_cheese == "no":
        if cheese in cheeses:
            cheese_set = cheese, cheeses[cheese]
            return cheese_set
        else:
            print("Cheese error. Did you want cheese?")
            return choose_cheese()
    elif wants_cheese == "yes":
        print("Great! Double cheese, or regular?")
        is_double_cheese = input("double or regular? ")
        cheese = "Double Mozzarella"
        if is_double_cheese in ["double", "double cheese", "double mozzarella"]:
            if cheese in cheeses:
                return cheese, cheeses[cheese]
        elif is_double_cheese in ["regular", "regular cheese"]:
            cheese = "Mozzarella"
            if cheese in cheeses:
                return cheese, cheeses[cheese]
        else:
            print("Error with cheese option. Please try again.")
            return choose_cheese()
    print("Awesome. Let's start working on your toppings... ")
    

# Choose toppings
# def choose_toppings():



print("Hello, customer! Build your pizza:")
choose_size()
print(user_pizza)
choose_cheese()