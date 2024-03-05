import antigravity
import antigravity


def main():
    antigravity.fly()


if __name__ == '__main__':
    main()

# Check if list contains integer x:
this = [3, 3, 4, 5, 2, 333, 5]
print(111 in this)  # Evaluates to and prints False

""" STACK """
# via the two list operations append() and pop()
"""
stack = [3]

stack: list[int] = [3]
"""
# stack.append(42)  # outputs [3, 42]
# stack.pop()  # outputs 42 (stack [3])
# stack.pop()  # when ran again
#  outputs 3 this time (stack[])

"""List Comprehension"""


# l= [('Hi ' + x) for x in ['Alice', 'Bob', 'Pete']]
# print(l) = # ['Hi Alice', 'Hi Bob', 'Hi Pete']


# Check if string is palindrome:
def is_palindrome(phrase):
    return phrase == phrase[::-1]


print(is_palindrome("anna"))  # True

print(is_palindrome("congratulations"))  # False

""" 
dmopc15c7p2

Sample Input
problem one is really long

Sample Output
5

Take input. Count the number of words. Provide count of output to user.
"""
line = input()
total_words = line.count(' ') + 1
print(total_words)

'''
dmopc14c5p1

The Challenge
Calculate the volume of a right circular cone.

Input
The input consists of two lines of text. The first line contains integer r, the
radius of the cone. The second line contains integer h, the height of the
cone. Both r and h are between 1 and 100. (That is, the minimum value for r
and h is 1, and the maximum value is 100.)

Output
Output the volume of the right circular cone with radius r and height h. The
formula to calculate the volume is (πr2h)/3.

'''
PI = 3.141592653589793
radius = int(input())
height = int(input())
volume = (PI * radius ** 2 * height) / 3
print(volume)

# EXERCISES:
'''
Sample Input
problem one is really long

Sample Output
5

Hint
V is the volume of the right circular cone with radius r and height h .
V = π r 2 h 3

'''
line = input()
total_words = line.count(' ') + 1
print(total_words)

'''
Sample Input
5

Sample Output
spoooooky

'''
in_number = int(input())

if in_number <= 2:
    print("spooky")
elif in_number >= 3:
    count = in_number - 2
    additional = count * "o"
    print("spoo" + additional + "ky")

'''
Output a single integer, the temperature in degrees Fahrenheit 
which is equivalent to C degrees Celsius.
Sample Input
20

Sample Output
68
'''
cTemp = int(input())
conv = (cTemp * (9 / 5)) + 32
print(conv)

'''
This is DMOJ problem ccc19j1.
The output is a single character.
• If the Apples scored more points than the Bananas, output A (A for
Apples).
• If the Bananas scored more points than the Apples, output B (B for
Bananas).
• If the Apples and Bananas scored the same number of points, output T (T for Tie).

'''
a3 = int(input())
a2 = int(input())
a1 = int(input())
atotal = (a3 * 3) + (a2 * 2) + a1
b3 = int(input())
b2 = int(input())
b1 = int(input())
btotal = (b3 * 3) + (b2 * 2) + b1
if atotal < btotal:
    print("B")
elif atotal > btotal:
    print("A")
else:
    print("T")

'''
ccc18j1
Sample Input 1
9
6
6
8

Sample Output 1
ignore

Explanation for Sample Output 1

The first digit is 9 , the last digit is 8 , 
and the second and third digit are both 6 , so this is a telemarketer number.

Matching index at 0 (>=8) AND 3 (>=8)

1ST DIGIT = 8 OR 9
4TH DIGIT = 8 OR 9
'''
# telenum = []

# first, second, third, fourth = int(input())
# telenum = telenum.append(first).append(second).append(third).append(fourth)

# # # # # #  # # # # #
telenum = []

first = int(input())
second = int(input())
third = int(input())
fourth = int(input())
# first, second, third, fourth = int(input())

telenum.append(first)
telenum.append(second)
telenum.append(third)
telenum.append(fourth)

if (telenum[0] >= 8) and (telenum[3] >= 8) and (telenum[1] == telenum[2]):
    print("ignore")
else:
    print("answer")

'''

Here are the three burger choices:
1 – Cheeseburger (461 Calories)
2 – Fish Burger (431 Calories)
3 – Veggie Burger (420 Calories)
4 – no burger 	
burger = [461, 431, 420, 0]

Here are the three drink choices:
1 – Soft Drink (130 Calories)
2 – Orange Juice (160 Calories)
3 – Milk (118 Calories)
4 – no drink
drink = [130, 160, 118, 0]

Here are the three side order choices:
1 – Fries (100 Calories)
2 – Baked Potato (57 Calories)
3 – Chef Salad (70 Calories)
4 – no side order 	
side = [100, 57, 70, 0]

Here are the three dessert choices:
1 – Apple Pie (167 Calories)
2 – Sundae (266 Calories)
3 – Fruit Cup (75 Calories)
4 – no dessert
dessert = [167, 266, 75, 0]

Sample Input
2
1
3
4

Sample Output
Your total Calorie count is 649.

'''
burger = [461, 431, 420, 0]
drink = [130, 160, 118, 0]
side = [100, 57, 70, 0]
dessert = [167, 266, 75, 0]

first = int(input())
thirst = int(input())
third = int(input())
final = int(input())

#   maincal = burger.index(first+1)
#   liqcal = drink.index(thirst+1)
#   sidecal = side.index(third+1)
#   desscal = dessert.index(final+1)

#   totalCalories = int(maincal + liqcal + sidecal + desscal)

print("Your total Calorie count is ", totalCalories)




'''
Write a program that asks the user for a numerical month and numerical day of the month and then determines whether that date occurs before, after, or on February 18.

    If the date occurs before February 18, output the word Before.
    If the date occurs after February 18, output the word After.
    If the date is February 18, output the word Special.

'''

month = int(input())
day = int(input())

if month == 1:
    print("Before")

elif (month == 2) and (day < 18):
    print("Before")

elif (month == 2) and (day == 18):
    print("Special")

elif (month == 2) and (day >= 19):
    print("After")

else:
    print("After")
