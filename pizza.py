# Build a pizza!


size_price_sets = {
    "Small": 6.99,
    "Medium": 9.99,
    "Large": 12.99,
    "X-Large": 15.99
}

# topping_cheese = ["No cheese", "Mozzarella" ]

cheeses = {
    "No cheese": 0.00,
    "Mozzarella": 0.00,
    "Double Mozzarella": 2.00
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

user_pizza = []


# Function to choose size
def choose_size(size):
    print("Choose size: Small, Medium, Large, or Extra Large?")
    input(f"Enter size: {size}")
    #print("Enter size: ")
    if size in size_price_sets:
        # return size, size_price_sets[size]
        print(f"you have chosen size {size}.")
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
    if wants_cheese == "No":
        if cheese in topping_cheese:
            return cheese, cheeses[cheese]
        else:
            print("Cheese error")
    elif wants_cheese == "Yes":
        print("Double cheese, or regular?")
        is_double_cheese = input("Double or Regular? ")
        if is_double_cheese == "Double":
            cheese = "Double Mozzarella"
            if cheese in cheeses:
                return cheese, cheeses[cheese]
        elif is_double_cheese == "Regular":
            cheese = "Mozzarella"
            if cheese in cheeses:
                return cheese, cheeses[cheese]
        else:
            print("Error with cheese option. Please try again.")
            return choose_cheese()
    

# Choose toppings
# def choose_toppings():

    



print("Hello, customer! Build your pizza:")
    
    
user_size = "Small"

choose_size(user_size)
