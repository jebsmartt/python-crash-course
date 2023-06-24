def build_order(*ingredients):
    print("Here is what is on your sandwich:")
    for ingredient in ingredients:
        print(f"\t- {ingredient.title()}")
    

 
build_order('peppers')
build_order('oregeno','salami','lettuce','oil')
build_order('meatball','marinara','cheese')
    