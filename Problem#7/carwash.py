''' Name: Brady Korsmo
    Date: Thursday @2'''


def calculate_car_wash_price(service_choice1, service_choice2):
    services = {'Air freshener': 1, 'Rain repellent': 2, 'Tire shine': 2, 'Wax': 3, 'Vacuum': 5}
    base_wash = 10
    total = base_wash  
    
    print("ZyCar Wash")
    print('Base car wash - $10')
    
    # Check the first service choice
    if service_choice1 in services:
        print(f"{service_choice1} - ${services[service_choice1]}")
        total += services[service_choice1]
  

    # Check the second service choice
    if service_choice2 in services:
        print(f"{service_choice2} - ${services[service_choice2]}")
        total += services[service_choice2]
 

    print("-----")
    print(f"Total price: ${total}")

if __name__ == '__main__':
    # Get user input for service choices
    service_choice1 = input("Enter first service choice: ")
    service_choice2 = input("Enter second service choice: ")

    # Call the function to calculate car wash price
    calculate_car_wash_price(service_choice1, service_choice2)
