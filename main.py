import functions


function_allocation_dict = {
    "1": functions.name_and_age,
    "2": functions.weather_conversation,
    "3": functions.words_in_piglatin,
    "4": functions.simple_calculator,
    "5": functions.poliandrom_check,
    "6": functions.length_of_string_count,
    "7": functions.biggest_common_denominator,
    "8": functions.calculation_of_divisibles,
    "9": functions.big_number_generation,
    "10": functions.square_area,
    "11":functions.triangle_area,
    "12":functions.square_root_calc,
    "13":functions.conv_kmh_mph,
    "14":functions.conv_celcius_farenheit,
    "15":functions.check_num_pos_or_neg,
    "16":functions.punctuation_remove,
    "17":functions.largest_of_three_numbers,
    "18":functions.distance_on_xy_plane,
    "19":functions.prime_num_check,
    "20":functions.phrase_reverse,
    "21":functions.time_show,
    "22":functions.currency_exchange,
    "23":functions.horoscope,
    "24":functions.zodiac_sighns,
    "25":functions.planet_facts,
    "26":functions.tick_tack_toe,
    "27":functions.hangman,
    "28":functions.pi_monte_carlo,
    "29":functions.quadratic_equasions,
    "30":functions.countdown_timer,
    "31":functions.christmas_tree #  Additional function
    }   

while True:
    ans = "0"

    print(f'''\n
    ==Welcome in a program with 30 functionalities== 
               by Arkadiusz Kubiszewski             

    1.Name and age question
    2.Weather conversation
    3.Words in pig latin
    4.Simple calculator
    5.Palindrom check (eg: racecar reversed is racecar)
    6.Checking length of a sentence or a word (no space)
    7.Biggest common denominator of two numbers
    8.Calculation of devisibles of a chosen number
    9.Generation of a random number
    10.Area of a square
    11.Area of a triagle
    12.Calculation of square root or an aproximation
    13.Conversion of km/h to miles/h
    14.Conversion of Celcius to Farenheit
    15.Check if a number is positive, negative or equal to 0
    16.Removing punctuations from a string
    17.Finding the largest of three numbers
    18.Finding a distance on x,y plane
    19.Check for a prime number
    20.Reverse a given phrase in python
    21.Get current date and time to show it
    22.Currency calculation (euro/pln and pln/euro)
    23.Horoscope
    24.Zodiac sighns
    25.Planet facts from our solar system
    26.TickTackToe
    27.Hangman
    28.Counting PI using MonteCarlo method
    29.Solving quadratic equasions
    30.countdown timer
    \n
    ''')

    ans = input("Write selected functionality number or type exit:\n :")
    

    if ans.lower() == "exit":
        break
    else:
        function_allocation_dict[ans]()


