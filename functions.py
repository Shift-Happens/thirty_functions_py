import random
import time
import datetime
import math
import cmath
import linecache
import re
#import tkinter

# 30 functionalities in one exectuable programme:
# - no graphical interface
# - using basic libaries

# functions:
#  1. [done] Name and age + string
#  2. [done] Weather with if statements
#  3. [done] Changing up words in pig latin
#  4. [done] Simple calculator (add, subtract, multiply, devide)
#  5. [done] Function that checks for palindrom for eg. Kamil Ślimak
#  6. [done]Check for length of characters in a word or sentence (without spaces)
#  7. [done]T wo numbers added and biggest common denominator calculated
#  8. [done] Calculation of devision for a chosen number
#  9. [done] Generation of a random number
# 10. [done] Area of a square
# 11. [done] Area of a triangle
# 12. [done] Calculation of square root
# 13. [done] Conversion of miles to km/h and vice versa https://www.youtube.com/watch?v=jtM9RLAENVE
# 14. [done] Conversion of Celcius to Farenheit and vice versa
# 15. [done]Checck if a number is positive, negative or equal to 0
# 16. [done]Removing punctuations from a string https://www.programiz.com/python-programming/examples/remove-punctuation
# 17. [done]Finding the largest of three numbers
# 18. [done] Finding a distance on x,y plane
# 19. [done] Check int input for a prime number
# 20. [done] Reverse a given string in python (I want to use reverse(examplestring)) https://www.geeksforgeeks.org/reverse-words-given-string-python/
# 21. [done] Get current time and show it https://www.geeksforgeeks.org/python-program-to-get-current-time/
# 22. [done] Currency calculation (offline, eg euro to pln)
# 23. Horoscope (random - probably extra file and a random finction)
# 24. Zodiac sighns (chineese and european) based on birthday date, additionaly showing relations
# 25. [done]Planets from solar system and after choosing from 1-9 some facts about them
# 26. TickTackToe 
# 27. Hangman 
# 28. [done] Counting PI using MonteCarlo method
# 29. [done]29. Solving quadratic equasions (a, b, c and -b formula) https://www.programiz.com/python-programming/examples/quadratic-roots
# 30. [done] countdown timer


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
    def addition():
        num1 = float(input("Enter your first number:"))
        num2 = float(input("Enter your second number:"))
        print(f"the result is: {num1 + num2}")

    def subtration():
        num1 = float(input("Enter your first number:"))
        num2 = float(input("Enter your second number:"))
        print(f"the result is: {num1 - num2}")

    def multiplication():
        num1 = float(input("Enter your first number:"))
        num2 = float(input("Enter your second number:"))
        print(f"the result is: {num1 * num2}")

    def devision():
        num1 = float(input("Enter your first number:"))
        num2 = float(input("Enter your second number:"))
        print(f"the result is: {num1 // num2}")
    while True:
        choice_list = {
            "1":addition,
            "2":subtration,
            "3":multiplication,
            "4":devision,
        }
        choice = input("Choose an option which interests you:")
        print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Devision\n5.Exit (press 5)")
        if choice == "5":
            break
        else:
            choice_list[choice]()


def poliandrom_check():
    
    while True:
        user_input = input("Input your string to check for poliandrom\n :")
        user_input_rev = user_input[::-1]
        if user_input == user_input_rev:
            print("Congratulations, your phrase is a poliandrom")
            break
        else:
            print("Your input is not a poliandrom")
            decision = input("do you want to try again? (yes or no)")
            decision_low = decision.lower()
            if decision_low == "yes":
                continue
            else:
                break
            

def length_of_string_count():  #  to finish
    user_input = input("Please input a word or a sentence\n :")
    user_input_clean = len(user_input) - user_input.count(" ")
    print(user_input_clean)


def biggest_common_denominator():
    print ("This program is finding a lowest common denominator between two numbers:")
    num_1 = int(input("Please input a number \n :"))
    num_2 = int(input("Please input a second number \n :"))
    answer = math.gcd(num_1, num_2)
    print("\n" * 2, "This is the answer", answer)
    time.sleep(5)


def calculation_of_divisibles():
    num = float(input("Input a number which you want to check divisibility of: "))
    div = float(input("Input a number which you want to devde by: "))

    if num%div == 0:
        print ("The number is divisible.")
    else:
        print ("The number is not divisible.")


def big_number_generation():
    print("This program will generate a big random number")
    user_input = int(input("Up to what number in range should we generate? \n: "))

    random_num = random.randrange((user_input * 0.2), user_input)
    print("Your random number is", random_num)
    time.sleep(5)


def square_area():
    #print("This program calculates the area of a square.")
    square_side = float(input("Input the length of your square to calculate area \n: "))
    area = square_side * square_side
    print("Your area is:", area)

    time.sleep(5)


def triangle_area():
    a = float(input("Input the 1 side: "))
    b = float(input("Input the 2 side: "))
    c = float(input("Input the 3 side:"))

    s = (a + b + c)/2
    area = (s*(s - a)*(s - b)*(s - c))** 0.5
    rounded_area = round(area, 2)
    print("Your area of triangle is:", rounded_area)

    time.sleep(5)


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
    user_input = int(input("Input your number to check (integer): "))
    if user_input < 0:
        print("Your number is negative")
        time.sleep(5)
    elif -1 < user_input < 1:
        print("Your number is a zero")
        time.sleep(5)
    else:
        print("Your number is positive")
        time.sleep(5)


def punctuation_remove():
    string = input("Input your string to be stripped of special characters: ")
    new_string = re.sub(r'[^\w\s]', ' ', string)
    print(new_string)
    time.sleep(5)


def largest_of_three_numbers():
    a = int(input("Input your number 1 to compare"))
    b = int(input("Input your number 2 to compare"))
    c = int(input("Input your number 3 to compare"))
    largest = 0

    if a > b and a > c:
        largest = a
    elif b > c:
        largest = b
    else:
        largest = c

    print (f"{largest} is your biggest number out of three")


def distance_on_xy_plane():
    print("Calculating distance between two points on x,y plane:")
    x=int(input("input x of first point: "))
    y=int(input("input y of first point: "))
    print("Now second point:")
    x2=int(input("input x of second point: "))
    y2=int(input("input y of second point: "))
    answer = round(math.sqrt((x-x2)**2 + (y-y2)**2), 2)
    print(f"Your answer is: {answer}")

    time.sleep(5)


def prime_num_check():
    user_num = int(input("Enter a number to check if it's a prime: "))
    div_by_self = user_num % user_num
    div_by_one = user_num % 1

    if div_by_self == 0 and div_by_one ==0:
        print("Your number is a prime number.")
        time.sleep(5)
    else:
        print("Your number is not a prime number.")
        time.sleep(5)


def phrase_reverse():
    user_input = input("Input your string to reverse it\n :")
    user_input_rev = user_input[::-1]
    print("This is your reversed phrase:\n", user_input_rev)
    time.sleep(5)    


def time_show():
    current_time = datetime.datetime.now()
    print(f"The current time is {current_time}")
    time.sleep(5)


def currency_exchange():
    user_choice = "0"
    user_input = 0.0
    pln = 4.7
    eur = 1.0
    
    def eur_to_pln():
        user_input = float(input("How much euro to exchange? \n: "))
        ans = user_input * pln
        print(f"You have{ans} pln.") 
    def pln_to_eur():
        user_input = float(input("How much pln to exchange? \n"))
        ans = user_input // pln
        print(f"You have {ans} euro.") 

    dict_choice = {
        "1":eur_to_pln,
        "2":pln_to_eur
    }

    while True:
        print("""
        1.Euro to Pln
        2.Pln to Euro
        3.Exit
        """)
        user_choice = input("State your choice: ")
        if user_choice == "3":
            break
        else:
            dict_choice[user_choice]()

def horoscope():
    print("placeholder")


def zodiac_sighns():
    print("placeholder")


def planet_facts():
    numer= int(input("""
    Hi, choose a number from 1 to 8, each one will tell you about a different planet
    If you can't decide, press 9, will choose a random planet
    To exit press 0 
    """))

    plik=open("planets.txt")

    def funkcja(numer):
        wiersz = linecache.getline("planety.txt", numer)
        print(wiersz)

    while True:
        if numer == 0:
            break

        elif numer==9:
            numer=(random.randint(1,8))
            funkcja(numer)
            time.sleep(5)
            return
        else:
            funkcja(numer)
            time.sleep(5)
            return

    plik.close()


def tick_tack_toe():
    print("placeholder")


def hangman():
    print("placeholder")

def pi_monte_carlo():
    print("Now a program will try to estimate Pi using the Monte carlo method.")
    print("more info here: https://en.wikipedia.org/wiki/Monte_Carlo_method")
    INTERVAL = 1000
    
    circle_points = 0
    square_points = 0
    
    # Total Random numbers generated= possible x
    # values* possible y values
    for i in range(INTERVAL**2):
    
        # Randomly generated x and y values from a
        # uniform distribution
        # Range of x and y values is -1 to 1
        rand_x = random.uniform(-1, 1)
        rand_y = random.uniform(-1, 1)
    
        # Distance between (x, y) from the origin
        origin_dist = rand_x**2 + rand_y**2
    
        # Checking if (x, y) lies inside the circle
        if origin_dist <= 1:
            circle_points += 1
    
        square_points += 1
    
        # Estimating value of pi,
        # pi= 4*(no. of points generated inside the
        # circle)/ (no. of points generated inside the square)
        pi = 4 * circle_points / square_points
    
    ##    print(rand_x, rand_y, circle_points, square_points, "-", pi)
    # print("\n")
    
    print("Final Estimation of Pi= ", pi)
    time.sleep(5)


def quadratic_equasions():

    a = int(input("input a:"))
    b = int(input("input b:"))
    c = int(input("input c:"))

    d = (b**2) - (4*a*c)
    sqrt = cmath.sqrt(d)
    #sqrt_git = round(sqrt, 4)
    sol_1 = (-b-sqrt)/(2*a)
    sol_2 = (-b+sqrt)/(2*a)

    # sol_1 = round(sol_1_before, 3)
    # sol_2 = round(sol_2_before, 3)
    
    print("Solution 1:", sol_1)
    print("Solution 2:", sol_2)


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
    
    
  






        