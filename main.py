# while True:
#     age = input("Enter your age (or 'stop' to exit): ").strip()
#     if age.lower() == "stop":
#         break
#     if age.isdigit():
#         age = int(age)
#         if age < 18:
#             print("You are a minor.")
#         elif age <= 60:
#             print("You are an adult.")
#         else:
#             print("You are a senior citizen.")
#     else:
#         print("Please enter a valid number.")

# while True:
#     vehicle = input("Enter the name of a vehicle: ").strip().lower()
#     if vehicle == "bus":
#         print("Finally, the wait is over!")
#         break
#     else:
#         print("Waiting...")

# while True:
#     fruit = input("Enter a fruit: ").strip().lower()
#     if fruit == "apple":
#         print("You got it!")
#         break
#     else:
#         print("Try again.")

# while True:
#     password = input("Guess the password: ").strip()
#     if password == "open sesame":
#         print("Access granted!")
#         break
#     else:
#         print("Wrong password, try again.")

# while True:
#     day = input("Enter a day of the week: ").strip().capitalize()
#     if day == "Sunday":
#         print("Enjoy your weekend!")
#         break
#     else:
#         print("It's not the weekend yet.")

# import random

# random_number = random.randint(1, 10)
# attempts = 0

# while True:
#     guess = input("Guess the number between 1 and 10: ").strip()
#     attempts += 1
#     if guess.isdigit():
#         guess = int(guess)
#         if guess < random_number:
#             print("Guess higher!")
#         elif guess > random_number:
#             print("Guess lower!")
#         else:
#             print(f"Correct! You guessed it in {attempts} attempts.")
#             break
#     else:
#         print("Please enter a valid number.")

# username = "admin"
# password = "1234"
# attempts = 0
# max_attempts = 3

# while attempts < max_attempts:
#     user_input = input("Enter username: ").strip()
#     pass_input = input("Enter password: ").strip()
#     if user_input == username and pass_input == password:
#         print("Login successful.")
#         break
#     else:
#         attempts += 1
#         print(f"Invalid credentials. {max_attempts - attempts} attempts left.")
# if attempts == max_attempts:
#     print("Too many failed attempts.")

# import random

# while True:
#     num1 = random.randint(1, 30)
#     num2 = random.randint(1, 30)
#     correct_answer = num1 * num2
#     print(f"What is {num1} x {num2}?")
#     answer = input("Your answer (or 'exit' to quit): ").strip()
#     if answer.lower() == "exit":
#         print("Quiz ended.")
#         break
#     if answer.isdigit() and int(answer) == correct_answer:
#         print("Correct!")
#     else:
#         print("Incorrect, try again.")

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# while True:
#     user_input = input("Enter a number (or 'exit' to quit): ").strip()
#     if user_input.lower() == "exit":
#         break
#     if user_input.isdigit():
#         number = int(user_input)
#         if is_prime(number):
#             print("The number is prime.")
#         else:
#             print("The number is not prime.")
#     else:
#         print("Please enter a valid number.")

# secret_word = "python"

# while True:
#     guess = input("Guess the secret word (or 'quit' to exit): ").strip()
#     if guess.lower() == "quit":
#         break
#     elif guess.lower() == secret_word:
#         print("Congratulations, you guessed the word!")
#         break
#     else:
#         print("Incorrect, try again.")

# count = 0

# while count < 3:
#     phrase = input("Enter a phrase: ").strip().lower()
#     if phrase == "good luck":
#         count += 1
#         print(f"You typed the same word {count} times.")
#         if count == 3:
#             print("You typed good luck three times.")
#     else:
#         print("Keep going!")

