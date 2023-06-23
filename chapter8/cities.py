
def describe_city(name, country='United States'):
    print(f"{name.title()} is in {country.title()}")

describe_city('Oakland')
describe_city('Seattle')
describe_city('Paris', 'France')