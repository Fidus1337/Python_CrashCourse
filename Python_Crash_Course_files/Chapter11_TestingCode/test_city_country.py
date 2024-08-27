from Task_11_1_City_Country import format_location


def test_city_and_country():
    str_to_test = format_location("Santiago", "Chile", 50000)
    assert str_to_test == "city - Santiago, country - Chile, population - 50000"
