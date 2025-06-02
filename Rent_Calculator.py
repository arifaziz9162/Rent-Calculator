import logging

# File handler and stream handler setup
logger = logging.getLogger("CoffeeShopLogger")
logger.setLevel(logging.DEBUG)

if logger.hasHandlers():
    logger.handlers.clear()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)  
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler("coffee_shop.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


class ZeroPersonError(Exception):
    """Raised when number of persons is zero or negative."""
    pass


class RentCalculator:
    
    def __init__(self,rent,food,electricity_units,unit_charge,persons):
        if not all(isinstance(i, (int, float)) for i in [rent, food, electricity_units, unit_charge, persons]):
            raise TypeError("All inputs must be numbers (int or float).")
        self.rent = rent
        self.food = food
        self.electricity_units = electricity_units
        self.unit_charge = unit_charge
        self.persons = persons


    def calculate_total(self):
        if self.persons <= 0:
            raise ZeroPersonError("Number of persons must be greater than zero.")
        
        electricity_bill = self.electricity_units * self.unit_charge
        total = self.food + self.rent + electricity_bill
        per_person = total / self.persons
        logger.info(f"Total : ₹{total}, Each person will pay : ₹{per_person:.2f}")
        return per_person
    

def main():
    try:

        rent = float(input("Enter your hostel/flat rent = "))
        food = float(input("Enter the amount of food ordered = "))
        units = float(input("Enter total electricity consumed = "))
        charge = float(input("Enter the charger per unit = "))
        persons = int(input("Enter numbers of persons living in room/flat = "))

        calculator = RentCalculator(rent , food , units , charge , persons)
        per_person = calculator.calculate_total() 
        print(f"Each person will pay = ₹{per_person:.2f}")

    except ValueError as ve:
        logger.error(f"Invalid input! Please enter numeric values: {ve}")
        print(str(ve))

    except ZeroPersonError as ze:
        logger.error(f"Custom error: {ze}")
        print(str(ze))

    except TypeError as te:
        logger.error(f"Type error: {te}")
        print(str(te))

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(str(e))


if __name__ == "__main__":
    main()
