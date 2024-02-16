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
