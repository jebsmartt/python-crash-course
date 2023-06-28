from city_functions import city_country

def test_city_country():
    """Do cities like 'santiago' and 'chile' work?"""
    formatted_city_state = city_country('santiago','chile')
    assert formatted_city_state == 'Santiago, Chile'