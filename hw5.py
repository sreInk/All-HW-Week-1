def age_counter():
    try:
       
        age = int(input("Enter your age: "))
        
        
        if age < 0 or age > 120:
            print("Error: The age entered is unrealistic.")
        else:
             
            if age % 2 == 0:
                print(f"The age {age} is even.")
            else:
                print(f"The age {age} is odd.")
    except ValueError:
        print("Error: Please enter a valid integer for age.")

age_counter()
