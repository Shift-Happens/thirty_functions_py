import random
import time
import math
#import tkinter

# 30 functionalities in one exectuable programme:
# - no graphical interface
# - using basic libaries

# functions:
#  1. [done] Name and age + string
#  2. [done] Weather with if statements
#  3. [done] Changing up words in pig latin
#  4. [to do] Simple calculator (add, subtract, multiply, devide)
#  5. [to do] Function that checks for palindrom for eg. Kamil Ślimak
#  6. [working]Check for length of characters in a word or sentence (without spaces)
#  7. Two numbers added and biggest common denominator calculated
#  8. Calculation of devision for a big number (up to ten thousand)
#  9. Generation of a random number
# 10. Area of a square
# 11. Area of a triangle
# 12. Calculation of square root
# 13. [done]Conversion of miles to km/h and vice versa https://www.youtube.com/watch?v=jtM9RLAENVE
# 14. [done]Conversion of Celcius to Farenheit and vice versa
# 15. Checck if a number is positive, negative or equal to 0
# 16. Removing punctuations from a string https://www.programiz.com/python-programming/examples/remove-punctuation
# 17. Finding the largest of three numbers
# 18. Finding a distance on x,y plane
# 19. Check int input for a prime number
# 20. Reverse a given string in python (I want to use reverse(examplestring)) https://www.geeksforgeeks.org/reverse-words-given-string-python/
# 21. Get current time and show it https://www.geeksforgeeks.org/python-program-to-get-current-time/
# 22. Currency calculation (offline, eg euro to pln)
# 23. Horoscope (random - probably extra file and a random finction)
# 24. Zodiac sighns (chineese and european) based on birthday date, additionaly showing relations
# 25. Planets from solar system and after choosing from 1-9 some facts about them
# 26. TickTackToe 
# 27. Hangman 
# 28. Counting PI using MonteCarlo method
# 29. Solving quadratic equasions (a, b, c and -b formula) https://www.programiz.com/python-programming/examples/quadratic-roots
# 30. [done]countdown timer


# if __name__ == '__main__':
# # to sie wykona tylko jesli uruchomimy glowny plik, jesli na przyklad zaimportujemy, 
# # to do innego kodu, to wszystko w tym ifie sie nie wykona
def name_and_age():
    user_name = input("Please input your name:\n :")
    user_age = int(input("Please input your age:\n :"))
    print(f"{user_name} was born {user_age} years ago")


def weather_conversation():
    rain_state = str.lower(input("Is it raining today? (yes or no\n :"))
    wind_state = str.lower(input("Is it windy today? (yes or no\n :)"))

    if rain_state == "yes" and wind_state == "yes":
        print ("You shouldn't go outside today, but if you must please take a taxi.")
    elif rain_state == "yes" and wind_state == "no":
         print ("You should take an umbrella with you.")
    elif rain_state == "no" and wind_state == "yes":
        print ("It is windy, so remember to suit up before leaving!")
    elif rain_state == "no" and wind_state == "no":
        print ("No need to take an umbrella :D")
    else:
        print("You have entered some other answer than yes or no, please select again:")


def words_in_piglatin():
    vowels = ['a','e','i','o','u']
    word = input("Enter a word \n: ")

    if word[0] in vowels:
        print (word+'way')
    else:  
        last = word[0] + 'ay'
        print(word[1:]+last)


def simple_calculator():  #  https://www.programiz.com/python-programming/examples/calculator
    num1 = input("Enter your first number:")
    num2 = input("Enter your second number:")

def poliandrom_check():
     print("placeholder")

def length_of_string_count():  #  to finish
    bad_chars = [';', ':', '!', "*", " "]
    user_input = input("Please input a word or a sentence\n :")
    user_input.replace
    print(user_input)


def biggest_common_denominator():
    print("placeholder")


def calculation_of_divisibles():
    print("placeholder")


def big_number_generation():
    print("placeholder")


def square_area():
    print("placeholder")


def triangle_area():
    print("placeholder")


def square_root_calc():
    num_to_sqrt = float(input("Enter a number you want to check the square root of\n :"))
    result_before = math.sqrt(num_to_sqrt)
    result = round(result_before, 3)
    print(f"This is the result: {result}")

def conv_kmh_mph():  # need to be able to choose which conversion
    kmph = float(input("How many km/h?\n :"))
    mph = (kmph * 0.621371)
    print (kmph," km/h is equal to " 
          ,round(mph, 3) ," miles per hour.")

def conv_celcius_farenheit(): #  need to be able to choose which converison
    celsius = float(input("How many Caelsius degrees?\n :"))
    fahrenheit = (celsius * 1.8) + 32
    print (celsius," degree Celsius is equal to " 
          ,fahrenheit," degree Fahrenheit.")


def check_num_pos_or_neg():
    print("placeholder")


def punctuation_remove():
    print("placeholder")


def largest_of_three_numbers():
    print("placeholder")


def distance_on_xy_plane():
    print("placeholder")


def prime_num_check():
    print ("placehlder")


def phrase_reverse():
    print("placeholder")


def time_show():
    print("placeholder")


def currency_exchange():
    print("placeholder")


def horoscope():
    print("placeholder")


def zodiac_sighns():
    print("placeholder")


def planet_facts():
    print("placeholder")


def tick_tack_toe():
    print("placeholder")


def hangman():
    print("placeholder")

def pi_monte_carlo():
    print("placeholder")



def quadratic_equasions():
    print("placeholder")


# 30. countdown timer
def countdown_timer():
     #   input time in seconds
    t = int(input("Enter the time in seconds: "))
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Time's up")
    
    
  






        