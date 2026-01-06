
# python_practice_basics_to_collections.py
"""
Python Practice File: Basics → Collections

How to use:
- Run the file:    python3 python_practice_basics_to_collections.py
- Read examples and complete the TODOs.
- Tests at the bottom will print PASS/FAIL for quick feedback.

Covers:
1) Python Basics
2) Types & Comparisons
3) Conditional Statements
4) Loops
5) Lists
6) List Operations
7) String Operations
8) Functions
9) Tuples, Dictionaries, & Sets

Tip: You can search for the string "TODO" to find exercises.
"""

# -------------------------------
# 1) Python Basics
# -------------------------------

a = 10              # integer
b = 3.5             # float
c = True            # boolean
name = "Kara"       # string

# Arithmetic
sum_ab = a + b
prod = a * 2
power = a ** 2
quot = a / 3
floor_div = a // 3
mod = a % 3

# Demonstrate printing and f-strings
print(f"[Basics] a={a}, b={b}, sum_ab={sum_ab}, power={power}, quot={quot:.2f}, floor_div={floor_div}, mod={mod}")

# -------------------------------
# 2) Types & Comparisons
# -------------------------------

types_demo = [type(a), type(b), type(c), type(name)]
print(f"[Types] {types_demo}")

# Comparison operators
x, y = 7, 10
print(f"[Comparisons] x < y? {x < y}; x == y? {x == y}; x != y? {x != y}")

# Identity vs equality
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"[Identity] list1 == list2? {list1 == list2}")         # equality (values)
print(f"[Identity] list1 is list2? {list1 is list2}")         # identity (same object?)
print(f"[Identity] list1 is list3? {list1 is list3}")

# -------------------------------
# 3) Conditional Statements
# -------------------------------

def classify_number(n: int) -> str:
    """Return a label for a number.
    - negative
    - zero
    - small (1-9)
    - medium (10-99)
    - large (>=100)
    """
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    elif n < 10:
        return "small"
    elif n < 100:
        return "medium"
    else:
        return "large"

print(f"[Conditionals] classify_number(-5) -> {classify_number(-5)}")
print(f"[Conditionals] classify_number(0) -> {classify_number(0)}")
print(f"[Conditionals] classify_number(42) -> {classify_number(42)}")

# TODO: Write a function 'grade_letter(score)' returning A/B/C/D/F using typical cutoffs (>=90 A, >=80 B, etc.)
# def grade_letter(score: int) -> str:
#     pass

def grade_letter(score: int):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score < 60:
        return "F"
    
score_int = 72
grade = grade_letter(score_int)
print(f"You have received a score of {score_int}, which is a grade of {grade}!")

# -------------------------------
# 4) Loops
# -------------------------------

# for loop with range
squares = []
for n in range(5):  # 0..4
    squares.append(n * n)
print(f"[Loops] squares via for-range: {squares}")

# while loop with break
countdown = []
num = 5
while num > 0:
    countdown.append(num)
    num -= 1
print(f"[Loops] countdown via while: {countdown}")

# break / continue demo
nums = list(range(10))
first_even_over_5 = None
for val in nums:
    if val % 2 != 0:
        continue  # skip odd
    if val > 5:
        first_even_over_5 = val
        break
print(f"[Loops] first even over 5: {first_even_over_5}")

# TODO: Use a loop to compute the factorial of a number n (e.g., 5! = 120) without importing math.
# def factorial(n: int) -> int:
#     pass

# -------------------------------
# 5) Lists
# -------------------------------

fruits = ["apple", "banana", "cherry", "date"]
print(f"[Lists] fruits: {fruits}")
print(f"[Lists] indexing fruits[1]={fruits[1]}, fruits[-1]={fruits[-1]}")
print(f"[Lists] slicing fruits[1:3]={fruits[1:3]}, fruits[:2]={fruits[:2]}, fruits[2:]={fruits[2:]}")

# list comprehension
lengths = [len(f) for f in fruits]
print(f"[Lists] lengths via comprehension: {lengths}")

# nested comprehension: squares of even numbers 0..9
even_squares = [n*n for n in range(10) if n % 2 == 0]
print(f"[Lists] even squares: {even_squares}")

# TODO: Create a list comprehension that produces cubes of numbers 1..10 where the cube is divisible by 4.
# cubes_div4 = ...

# -------------------------------
# 6) List Operations
# -------------------------------

nums_ops = [5, 2, 9]
nums_ops.append(7)           # add single item
nums_ops.extend([1, 1, 3])   # add multiple items
nums_ops.insert(0, 99)       # insert at index
removed = nums_ops.pop()     # remove and return last
nums_ops.remove(1)           # remove first occurrence of value 1
copy_nums = nums_ops.copy()  # shallow copy

print(f"[List Ops] after ops: {nums_ops}; removed={removed}; copy={copy_nums}")
print(f"[List Ops] sorted copy: {sorted(nums_ops)}")
nums_ops.sort(reverse=True)
print(f"[List Ops] in-place sort desc: {nums_ops}")

# TODO: Deduplicate a list while preserving order; e.g. [1,2,2,3,1] -> [1,2,3]
# def dedupe_preserve_order(seq: list) -> list:
#     pass

# -------------------------------
# 7) String Operations
# -------------------------------

msg = "  hello, world!  "
print(f"[Strings] original: '{msg}'")
print(f"[Strings] strip: '{msg.strip()}'")
print(f"[Strings] upper: '{msg.upper()}'")
print(f"[Strings] replace: '{msg.replace('world', 'Python')}'")
print(f"[Strings] split: {msg.strip().split(', ')}")

words = ["join", "these", "words"]
joined = "-".join(words)
print(f"[Strings] joined with '-': {joined}")

# formatting
user = "Kara"
count = 3
print("[Strings] format: {} has {} tasks".format(user, count))
print(f"[Strings] f-string: {user} has {count} tasks")

# slicing
text = "abcdefg"
print(f"[Strings] slice text[2:5]={text[2:5]}, text[::-1]={text[::-1]}")

# TODO: Write a function normalize_whitespace(s) that collapses multiple spaces into a single space and trims ends.
# def normalize_whitespace(s: str) -> str:
#     pass

# -------------------------------
# 8) Functions
# -------------------------------

def add(a: int, b: int = 0) -> int:
    """Return sum of a and b (b default=0)."""
    return a + b

# *args and **kwargs
def summarize(*numbers, **options):
    """Return sum and average of numbers, optionally rounded.
    options: round_to=int (decimal places)
    """
    total = sum(numbers)
    avg = total / (len(numbers) or 1)
    round_to = options.get("round_to")
    if round_to is not None:
        total = round(total, round_to)
        avg = round(avg, round_to)
    return {"total": total, "avg": avg}

print(f"[Functions] add(5)= {add(5)}, add(5,7)= {add(5,7)}")
print(f"[Functions] summarize(1,2,3, round_to=2)= {summarize(1,2,3, round_to=2)}")

# lambda
square = lambda n: n * n
print(f"[Functions] lambda square(6)= {square(6)}")

# Scope example
GLOBAL_COUNTER = 0

def bump_counter(times: int) -> None:
    """Increment a global counter the given number of times."""
    global GLOBAL_COUNTER
    for _ in range(times):
        GLOBAL_COUNTER += 1

bump_counter(3)
print(f"[Functions] GLOBAL_COUNTER after bump: {GLOBAL_COUNTER}")

# TODO: Write a function apply_funcs(values, funcs) that applies each function to all values and returns a list of lists of results.
# Example: values=[1,2], funcs=[square, lambda x: x+1] -> [[1,4],[2,3]]
# def apply_funcs(values: list, funcs: list) -> list:
#     pass

# -------------------------------
# 9) Tuples, Dictionaries, & Sets
# -------------------------------

# Tuples (immutable sequences)
pt = (10, 20)
x, y = pt  # tuple unpacking
print(f"[Tuples] pt={pt}, x={x}, y={y}")

# Dictionary
person = {
    "name": "Kara",
    "role": "Data Engineer",
    "location": "South Jordan, Utah",
}
print(f"[Dict] person keys: {list(person.keys())}")
print(f"[Dict] person get('role'): {person.get('role')}")

# Update and iterate
person["skills"] = ["Python", "SQL", "ETL"]
for key, value in person.items():
    print(f"[Dict] {key} -> {value}")

# Dict comprehension: map fruit to length
fruit_lengths = {f: len(f) for f in fruits}
print(f"[Dict] fruit_lengths: {fruit_lengths}")

# Sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5}
print(f"[Sets] union: {set_a | set_b}")
print(f"[Sets] intersection: {set_a & set_b}")
print(f"[Sets] difference A-B: {set_a - set_b}")
print(f"[Sets] symmetric difference: {set_a ^ set_b}")

# Frozenset (immutable set)
fs = frozenset([1, 2, 2, 3])
print(f"[Sets] frozenset: {fs}")

# TODO: Given a list of words, build a dict mapping each first letter to the set of words starting with that letter.
# def index_words_by_initial(words: list) -> dict:
#     pass

# -------------------------------
# Quick Tests (basic assertions)
# -------------------------------
def _run_tests():
    print("\n[Tests] Running quick tests...")

    # Basics
    assert sum_ab == 13.5
    assert floor_div == 3
    assert mod == 1

    # Types & Comparisons
    assert (list1 == list2) is True
    assert (list1 is list2) is False
    assert (list1 is list3) is True

    # Conditionals
    assert classify_number(-1) == "negative"
    assert classify_number(0) == "zero"
    assert classify_number(5) == "small"
    assert classify_number(50) == "medium"
    assert classify_number(150) == "large"

    # Loops
    assert squares == [0, 1, 4, 9, 16]
    assert countdown == [5, 4, 3, 2, 1]

    # Lists
    assert lengths == [5, 6, 6, 4]
    assert even_squares == [0, 4, 16, 36, 64]

    # List Operations
    assert isinstance(copy_nums, list)

    # String Operations
    assert joined == "join-these-words"
    assert text[::-1] == "gfedcba"

    # Functions
    assert add(1) == 1
    assert add(2, 3) == 5
    assert summarize(1, 2, 3)["total"] == 6

    # Tuples, Dicts, Sets
    assert x == 10 and y == 20
    assert person.get("name") == "Kara"
    assert fruit_lengths["banana"] == 6
    assert (set_a | set_b) == {1, 2, 3, 4, 5}

    print("[Tests] PASS — core examples look good!")

if __name__ == "__main__":
    _run_tests()
