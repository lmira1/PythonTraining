def define_year_zodiac_sign():
    print('Type any year to define the zodiac sign')
    y = int(input())
    signs = ["Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"]
    x = (y % 12)
    print(signs[x])


define_year_zodiac_sign()
