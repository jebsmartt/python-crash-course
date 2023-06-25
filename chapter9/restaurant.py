class Restaurant:
    """this is called a docstring"""

    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    
    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open.")

restaurant1 = Restaurant("Luigi's",'Italian')

Restaurant.describe_restaurant(restaurant1)

restaurant2 = Restaurant("Paulies",'Pasta')

Restaurant.describe_restaurant(restaurant2)

restaurant3 = Restaurant("Chiloso",'Mexican')

Restaurant.describe_restaurant(restaurant3)