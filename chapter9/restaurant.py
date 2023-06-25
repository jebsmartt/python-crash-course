class restaurant:
    """this is called a docstring"""

    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    
    def open_restaurant(self):
        print(f"The {self.restaurant_name} restaurant is open.")

restaurant1 = restaurant("Luigi's",'Italian')

restaurant.describe_restaurant(restaurant1)

restaurant2 = restaurant("Paulies",'Pasta')

restaurant.describe_restaurant(restaurant2)

restaurant3 = restaurant("Chiloso",'Mexican')

restaurant.describe_restaurant(restaurant3)