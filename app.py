import time
import random
products = [
    {"id": 1, "name": "Product A", "price": 100, "min_age": 18},
    {"id": 2, "name": "Product B", "price": 200, "min_age": 21},
    {"id": 3, "name": "Product C", "price": 150, "min_age": 18},
    {"id": 4, "name": "Product D", "price": 300, "min_age": 25},
    {"id": 5, "name": "Product E", "price": 250, "min_age": 18},
    {"id": 6, "name": "Product F", "price": 350, "min_age": 30},
    {"id": 7, "name": "Product G", "price": 120, "min_age": 18}
]

database = {
    "12345678": {"name": "John Doe", "dob": "1990-01-01", "phone": "0801234567"},
    "98765432": {"name": "Jane Smith", "dob": "2005-03-15", "phone": "0897654321"}
}

def calculate_age(dob):
    current_year = 2025
    birth_year = int(dob.split("-")[0])
    age = current_year - birth_year
    return age

def verify_id_card(id_card_number):
    if id_card_number in database:
        return database[id_card_number]
    else:
        return None

def send_otp(phone_number):
    otp = random.randint(100000, 999999)
    print(f"OTP sent to {phone_number}: {otp}")
    return otp

def verify_otp(otp, user_input):
    if otp == int(user_input):
        print("OTP verified successfully!")
        return True
    else:
        print("Incorrect OTP!")
        return False

def choose_product(age):
    print("Available products:")
    available_products = [product for product in products if age >= product["min_age"]]
    
    if not available_products:
        print("Sorry, you are not eligible to purchase any products based on your age.")
        return None

    for product in available_products:
        print(f"{product['id']}. {product['name']} - Price: {product['price']} - Minimum Age: {product['min_age']}")

    product_id = int(input("Enter the product ID to select a product: "))
    selected_product = next((product for product in available_products if product['id'] == product_id), None)
    
    if selected_product:
        return selected_product
    else:
        print("Invalid product selection.")
        return None

def process_purchase(id_card_number):
    user_data = verify_id_card(id_card_number)
    
    if user_data:
        name = user_data["name"]
        dob = user_data["dob"]
        phone = user_data["phone"]
        age = calculate_age(dob)
        if age < 18:
            print("Sorry, you are not old enough to make a purchase.")
            return
        
        print(f"Welcome {name}! Age: {age}. You can now proceed to purchase.")
        
        selected_product = choose_product(age)
        
        if selected_product:
            otp = send_otp(phone)
            
            user_input = input("Enter the OTP sent to your phone: ")
            
            if verify_otp(otp, user_input):
                print(f"Purchase confirmed! You have successfully purchased {selected_product['name']} for {selected_product['price']} THB.")
            else:
                print("Purchase cancelled due to incorrect OTP.")
        
    else:
        print("Invalid ID card number!")

def return_id_card(id_card_number, timeout=3):
    print(f"Returning ID card {id_card_number} due to timeout.")
    time.sleep(timeout * 60)  

id_card_number = input("Please scan your ID card number: ")
process_purchase(id_card_number)
