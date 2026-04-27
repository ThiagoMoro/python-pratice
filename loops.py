# Random list of numbers for the exercise
numbers = [14, 21, 33, 45, 49, 63, 100, 105, 200, 315, 420, 500]

# PART 1: For loop with continue and break
for num in numbers:
  # Stop the interations if the number 315 is encountered
  if num == 315:
    break
  # Skip the number if it is divisible by 7
  if num % 7 == 0:
    continue
  # Otherwise, print the number
  print(num)

# PART 2: List Comprehension
# Generate cube only if the number is divisible by 3

# The syntax: [expression for item in list if condition]
cubes = [num ** 3 for num in numbers if num % 3 == 0]

print("\nCubes of numbers divisible by 3: ")
print(cubes)