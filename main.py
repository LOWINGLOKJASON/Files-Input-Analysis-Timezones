#****************************************************************
#Name: Wing Lok LO
#Link: https://replit.com/join/ajndhlwkmj-lowinglokjason
#****************************************************************

#import packages
import json
import urllib.request
import string
from collections import Counter
import datetime
import pytz

#############
#Question #1
#############

# Open a blank file and write a few lines about what I have learned in the course.
with open('python_learning.txt', 'w') as file:
  file.write("I have learned about creating a function in Python course.")

# Write a program that reads what I wrote and prints it to the terminal three times
with open('python_learning.txt', 'r') as file:
  content = file.read()
  for i in range(3):
    print(content)

#############
#Question #2
#############

users = []
while True:
  name = input("Please enter your name (or 'q' to quit): ")
  if name.lower() == 'q':
    break
  food = input("Please enter your favorite food: ")
  user = {"name": name, "food": food}
  users.append(user)
  with open('users.json', 'w') as file:
    json.dump(users, file)

# Read and display the choices from the json file
with open('users.json', 'r') as file:
  users = json.load(file)
  print("Users:")
  for user in users:
    print("Name: ", user["name"])
    print("Favorite Food: ", user["food"])

#############
#Question #3
#############

# Store  age input in age.txt file and calculate age in dog years in a while loop
while True:
  try:
    age = int(input("Please enter your age: "))
    if age <= 0:
      print("Please enter a valid age.")
      continue
    elif age > 0:
      dog_years = age * 7
      with open('age.txt', 'w') as file:
        file.write(f"Your age is: {age} years. In dog years, it's: {dog_years} years.")
      break
  except ValueError:
    print("Please enter a valid age.")

# Print the content of the age.txt file
with open('age.txt', 'r') as file:
  content = file.read()
  print(content)

#############
#Question #4
#############

# Check if input is a word or a number
input_value = input("Please enter a word or a number: ")
if input_value.isdigit():
  print("Input is a number.")
else:
  print("Input is a word.")

#############
#Question #5
#############

# Try to read a non-existent file without displaying an error message
try:
  with open('nonexistent_file.txt', 'r') as file:
    content = file.read()
except FileNotFoundError:
  pass  
  # Pass silently without displaying an error message

#############
#Question #6
#############

# Download the book in text format from Project Gutenberg
url = 'https://www.gutenberg.org/files/64317/64317-0.txt'
urllib.request.urlretrieve(url, 'book.txt')

# Read the downloaded book file
with open('book.txt', 'r', encoding='utf-8') as file:
  book_text = file.read()

# Clean the text by removing punctuation and converting to lowercase
book_text_cleaned = book_text.translate(str.maketrans('', '', string.punctuation)).lower()

# Count the occurrences of "the" and "The" separately
count_the = book_text_cleaned.count('the')
count_The = book_text_cleaned.count('The')

# Calculate the difference between "the" and "The" counts
difference = abs(count_the - count_The)

# Print the counts and the difference
print(f'Total occurrences of "the": {count_the}')
print(f'Total occurrences of "The": {count_The}')
print(f'Difference between "the" and "The": {difference}')

# Find the most common words in the book
words = book_text_cleaned.split()
common_words = Counter(words).most_common(10) # Get the top 10 most common words
print('Most common words:')
for word, count in common_words:
  print(f'{word}: {count} occurrences')


#############
#Question #7
#############

# Get the current date and time in the local timezone
local_tz = pytz.timezone('Canada/Eastern')
local_time = datetime.datetime.now(local_tz)

# Format the local time string
time_string = local_time.strftime("%b %d, %Y %H:%M:%S %p %Z")

# Replace the timezone abbreviation from EST to EDT if applicable
if local_time.dst():
  time_string = time_string.replace('EST', 'EDT')

# Print out the formatted string with local timezone
print("The local time is now", time_string)
