def welcome_func(name):
    if name == "Mamadou":
        print("Hey, it's the awesome AI Director, Mamadou!")
    else:
        print(f"Welcome, {name}! We're glad to have you here.")
    
name = input("Enter your name: ")

welcome_func(name)
