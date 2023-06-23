sandwich_orders = ['Reuben','Hoagie','PB&J','Meatball Sub','Bahn Mi','Muffaleta']

finished_sandwiches = []

while len(sandwich_orders) > 0:
    order = sandwich_orders.pop(0)
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)

print("\nList of sandwiches made:")
for item in finished_sandwiches:
    print(f"\t{item}")