out_list = ['Pastrami']

sandwich_orders = ['Reuben','Hoagie','PB&J','Meatball Sub','Pastrami','Bahn Mi','Muffaleta','Pastrami','Pastrami']

finished_sandwiches = []

while len(sandwich_orders) > 0:
    order = sandwich_orders.pop(0)
    if order in out_list:
        while order in sandwich_orders:
            sandwich_orders.remove(order)
        print(f"We are currently out of {order} sandwiches. Order something else.")
        continue
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nList of sandwiches made:")
for item in finished_sandwiches:
    print(f"\t{item}")