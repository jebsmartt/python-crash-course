def city_country(city, country, population = ''):
    if population:
        formal_name = f"{city.title()}, {country.title()} - population {population}"
    else:
        formal_name = f"{city.title()}, {country.title()}"
    return formal_name