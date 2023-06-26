class Restaurant:
    """this is called a docstring"""

    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    
    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open.")

    def increment_number_served(self,number_of_customers):
        self.number_served += number_of_customers

# restaurant1 = Restaurant("Luigi's",'Italian')
# restaurant2 = Restaurant("Paulies",'Pasta')
# restaurant3 = Restaurant("Chiloso",'Mexican')

# Restaurant.describe_restaurant(restaurant3)
# print(restaurant1.number_served)

# restaurant1.number_served = 14
# print(restaurant1.number_served)

# restaurant1.increment_number_served(12)
# print(restaurant1.number_served)

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print(f"\nThese are our ice cream flavors today:")
        for flavor in self.flavors:
            print(f"- {flavor}")

restaurant4 = IceCreamStand('Salt & Straw')
restaurant4.flavors.extend(['Vanilla','Chocolate','Strawberry'])
IceCreamStand.show_flavors(restaurant4)