# Q1
bot_name = "Aid"
birth_year = "2025"

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")

#Q2
def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

def remind_name():
    print("Please, remind me your name.")
    name = input()
    print(f"What a great name you have, {name}!")

greet("Aid", "2025")
remind_name()

#Q3
def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

def remind_name():
    print("Please, remind me your name.")
    name = input()
    print(f"What a great name you have, {name}!")

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")

greet("Aid", "2025")
remind_name()
guess_age()

#Q4
def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

def remind_name():
    print("Please, remind me your name.")
    name = input()
    print(f"What a great name you have, {name}!")

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")

def count():
    print("Now I will prove to you that I can count to any number you want.")
    num = int(input())
    for i in range(num + 1):
        print(f"{i} !")

greet("Aid", "2025")
remind_name()
guess_age()
count()
print("Completed, have a nice day!")

#Q5
def greet(bot_name, birth_year):
    print(f"Hello! My name is {bot_name}.")
    print(f"I was created in {birth_year}.")

def remind_name():
    print("Please, remind me your name.")
    name = input()
    print(f"What a great name you have, {name}!")

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    r3 = int(input())
    r5 = int(input())
    r7 = int(input())
    age = (r3 * 70 + r5 * 21 + r7 * 15) % 105
    print(f"Your age is {age}; that's a good time to start programming!")

def count():
    print("Now I will prove to you that I can count to any number you want.")
    n = int(input())
    for i in range(n + 1):
        print(f"{i} !")

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")
    while True:
        answer = int(input())
        if answer == 2:
            break
        print("Please, try again.")
    print("Congratulations, have a nice day!")

greet("Aid", "2025")
remind_name()
guess_age()
count()
test()