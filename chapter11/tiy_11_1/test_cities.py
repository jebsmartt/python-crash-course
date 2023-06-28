from city_functions import city_country

def test_city_country():
    """Do cities like 'santiago' and 'chile' work?"""
    formatted_city_state = city_country('santiago','chile')
    assert formatted_city_state == 'Santiago, Chile'

def test_city_country_population():
    """Does the function handle passing in a 
    population in additon to city and country"""
    formatted_city_state_pop = city_country('santiago','chile',5_000_000)
    assert formatted_city_state_pop == 'Santiago, Chile - population 5000000'