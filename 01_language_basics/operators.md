## Operators in Python

### Introduction
An **operator** in Python is a symbol that performs a specific operation on one or more operands. Python provides a variety of operator types to handle different tasks. These include:

1. Arithmetic Operators
2. Relational (or Comparison) Operators
3. Logical Operators
4. Bitwise Operators
5. Assignment Operators
6. Special Operators

---

### 1. Arithmetic Operators
Arithmetic operators perform basic mathematical operations like addition, subtraction, multiplication, and more. The operators are: `+`, `-`, `*`, `/`, `%`, `//`, and `**`.

#### Examples

```python
a = 10
b = 2
print('a + b =', a + b)   # Addition
print('a - b =', a - b)   # Subtraction
print('a * b =', a * b)   # Multiplication
print('a / b =', a / b)   # Division
print('a // b =', a // b) # Floor Division
print('a % b =', a % b)   # Modulo
print('a ** b =', a ** b) # Exponentiation
```

**Output**:
```
a + b = 12
a - b = 8
a * b = 20
a / b = 5.0
a // b = 5
a % b = 0
a ** b = 100
```

#### Key Notes
- The division operator `/` always returns a float, even if both operands are integers (e.g., `10 / 2` returns `5.0`).
- The floor division operator `//` returns an integer by rounding down the result. If either operand is a float, the result is a float (e.g., `5.5 // 2` returns `2.0`).
- The modulo operator `%` gives the remainder of division.
- The exponentiation operator `**` raises the first operand to the power of the second.

#### String Operations with `+` and `*`
- **Addition (`+`)**: Concatenates two strings when both operands are strings.
  ```python
  result = "durga" + "10"
  print(result)  # Output: 'durga10'
  ```
- **Multiplication (`*`)**: Repeats a string a specified number of times (one operand must be an integer).
  ```python
  result = "durga" * 2
  print(result)  # Output: 'durgadurga'
  ```


```python
name = "Hello"
count = 3
print(name + " World")  # Output: 'Hello World'
print(name * count)     # Output: 'HelloHelloHello'
```

#### Errors
- Using `+` with a string and an integer (e.g., `"durga" + 10`) raises a `TypeError`.
- Using `*` with a string and a float (e.g., `"durga" * 2.5`) raises a `TypeError`.

---

### 2. Relational Operators
Relational operators compare two values and return a boolean (`True` or `False`). The operators are: `>`, `>=`, `<`, and `<=`.

#### Descriptions
- `>`: Checks if the first operand is greater than the second.
- `>=`: Checks if the first operand is greater than or equal to the second.
- `<`: Checks if the first operand is less than the second.
- `<=`: Checks if the first operand is less than or equal to the second.

#### Examples
```python
a = 10
b = 20
print("a > b is", a > b)   # False
print("a >= b is", a >= b) # False
print("a < b is", a < b)   # True
print("a <= b is", a <= b) # True
```

#### Relational Operators with Strings
Strings are compared lexicographically based on the Unicode values of their characters (similar to dictionary order).

```python
a = "durga"
b = "durga"
print("a > b is", a > b)   # False
print("a >= b is", a >= b) # True
print("a < b is", a < b)   # False
print("a <= b is", a <= b) # True
```


```python
x = "apple"
y = "banana"
print(x < y)  # True (because 'a' comes before 'b' in Unicode)
```

#### Notes
1. **Chaining**: You can chain relational operators for multiple comparisons.
   - Example: `10 < 20 < 30` returns `True`.
   - Example: `10 < 20 < 30 < 40 > 50` returns `False`.
2. Relational operators cannot compare incompatible types (e.g., `int` and `str`).
   ```python
   print(10 > "durga")  # Raises TypeError
   ```

---

### Equality Operators
Equality operators compare two values for equality or inequality. The operators are: `==` and `!=`.

#### Definitions
- `==`: Returns `True` if both values are equal.
- `!=`: Returns `True` if both values are not equal.

#### Examples
```python
print(10 == 20)           # False
print(10 != 20)           # True
print(10 == True)         # False
print(False == False)     # True
print("durga" == "durga") # True
print(10 == "durga")      # False
```


```python
x = 5
y = "5"
print(x == y)  # False (different types)
print(x != y)  # True
```

#### Notes
- **Chaining**: Equality operators can be chained. If all comparisons are `True`, the result is `True`; if at least one is `False`, the result is `False`.
  ```python
  print(10 == 20 == 30 == 40)  # False
  print(10 == 10 == 10 == 10)  # True
  ```
- These operators work with all types, even incompatible ones, but comparisons between incompatible types always return `False`.

---

### Logical Operators
Logical operators perform logical operations on boolean and non-boolean values. The operators are: `and`, `or`, and `not`.

#### Boolean Types
| Operator | Behavior                                      | Example          | Output |
|----------|-----------------------------------------------|------------------|--------|
| `and`    | Returns `True` if both operands are `True`.   | `True and False` | `False`|
| `or`     | Returns `True` if at least one is `True`.     | `True or False`  | `True` |
| `not`    | Returns the opposite (`True` → `False`, etc.) | `not False`      | `True` |

#### Non-Boolean Types
- **`and`**: Returns the first operand if it’s `False` (e.g., `0`, `False`, empty value); otherwise, returns the second operand.
- **`or`**: Returns the first operand if it’s `True` (non-zero, non-empty); otherwise, returns the second operand.
- **`not`**: Returns `True` if the operand evaluates to `False`, and `False` if it evaluates to `True`.

#### Examples
```python
print(10 and 20)        # 20
print(0 and 20)         # 0
print(10 or 20)         # 10
print(0 or 20)          # 20
print(not 10)           # False
print(not 0)            # True

print("durga" and "durgasoft")  # 'durgasoft'
print("" and "durga")           # ''
print("durga" or "")            # 'durga'
print(not "")                   # True
print(not "durga")              # False
```


```python
x = 5
y = 0
z = "text"
print(x and z)  # 'text'
print(y or z)   # 'text'
print(not y)    # True
```

---

### Bitwise Operators
Bitwise operators manipulate bits of integers or booleans at the binary level. The operators are: `&`, `|`, `^`, `~`, `<<`, and `>>`.

#### Key Points
1. **`&` (AND)**: Returns `1` if both bits are `1`; otherwise, `0`.
2. **`|` (OR)**: Returns `1` if at least one bit is `1`; otherwise, `0`.
3. **`^` (XOR)**: Returns `1` if bits are different; otherwise, `0`.
4. **`~` (Complement)**: Inverts all bits.
5. **`<<` (Left Shift)**: Shifts bits left, filling with `0`.
6. **`>>` (Right Shift)**: Shifts bits right, filling with the sign bit.

#### Examples
```python
print(4 & 5)       # 4 (0100 & 0101 = 0100)
print(4 | 5)       # 5 (0100 | 0101 = 0101)
print(4 ^ 5)       # 1 (0100 ^ 0101 = 0001)
print(~5)          # -6 (bitwise complement)
print(10 << 2)     # 40 (1010 becomes 101000)
print(10 >> 2)     # 2 (1010 becomes 0010)

print(True & True) # True
print(True | False) # True
```


```python
x = 13  # Binary: 1101
y = 6   # Binary: 0110
print(x & y)  # 4 (0100)
print(x | y)  # 15 (1111)
print(x >> 1) # 6 (0110)
```

#### Notes
- Bitwise operators only work with `int` and `boolean` types. Using them with `float` raises a `TypeError`.
- The `~` operator uses 2’s complement, so `~5` becomes `-6`.

---

### Assignment Operators
Assignment operators assign values to variables, often combining other operations. Examples include: `=`, `+=`, `-=`, etc.

#### Examples
```python
x = 10
x += 20      # x = x + 20
print(x)     # 30

x = 10
x &= 5       # x = x & 5
print(x)     # 0
```

#### List of Compound Assignment Operators
- `+=`: Adds and assigns
- `-=`: Subtracts and assigns
- `*=`: Multiplies and assigns
- `/=`: Divides and assigns
- `%=`: Modulus and assigns
- `//=`: Floor divides and assigns
- `**=`: Exponentiates and assigns
- `&=`: Bitwise AND and assigns
- `|=`: Bitwise OR and assigns
- `^=`: Bitwise XOR and assigns
- `>>=`: Right shifts and assigns
- `<<=`: Left shifts and assigns


```python
x = 7
x *= 3
print(x)  # 21
```

---

### Ternary (Conditional) Operator
The ternary operator provides a concise way to write conditional statements.

#### Syntax
```python
x = firstValue if condition else secondValue
```
- If the condition is `True`, `x` gets `firstValue`; otherwise, `x` gets `secondValue`.

#### Examples
1. **Basic Example**:
   ```python
   a, b = 10, 20
   x = 30 if a < b else 40
   print(x)  # 30
   ```

2. **Minimum of Two Numbers**:
   ```python
   a = 15
   b = 25
   min_value = a if a < b else b
   print("Minimum Value:", min_value)  # 15
   ```

3. **Minimum of Three Numbers**:
   ```python
   a, b, c = 5, 2, 8
   min_value = a if a < b and a < c else b if b < c else c
   print("Minimum Value:", min_value)  # 2
   ```

4. **Number Comparison**:
   ```python
   a, b = 10, 20
   print("Both numbers are equal" if a == b else
         "First Number is Less than Second Number" if a < b else
         "First Number is Greater than Second Number")  # First Number is Less than Second Number
   ```


```python
x, y = 8, 8
result = "Equal" if x == y else "Not Equal"
print(result)  # Equal
```

---

### Special Operators

#### 1. Identity Operators
Identity operators (`is`, `is not`) compare the memory locations of two objects.

#### Examples
```python
a = 10
b = 10
print(a is b)  # True (same memory for small integers)

list1 = ["one", "two"]
list2 = ["one", "two"]
print(list1 is list2)  # False (different objects)
print(list1 == list2)  # True (same content)
```


```python
x = "hello"
y = "hello"
print(x is y)  # True (string interning)
```

#### Note
- Use `is` for identity, `==` for equality.

#### 2. Membership Operators
Membership operators (`in`, `not in`) check if a value exists in a collection.

#### Examples
```python
x = "hello, Python!"
print('h' in x)       # True
print('Python' in x)  # True
print('z' not in x)   # True

list1 = ["sunny", "bunny"]
print("sunny" in list1)  # True
```


```python
nums = [1, 2, 3]
print(4 not in nums)  # True
```

---

### Operator Precedence
Operator precedence determines the order of evaluation in expressions.

#### Precedence List
1. `()` – Parentheses
2. `**` – Exponentiation
3. `~`, `-` – Bitwise Complement, Unary Minus
4. `*`, `/`, `%`, `//` – Multiplication, Division, Modulus, Floor Division
5. `+`, `-` – Addition, Subtraction
6. `<<`, `>>` – Bitwise Shifts
7. `&` – Bitwise AND
8. `^` – Bitwise XOR
9. `|` – Bitwise OR
10. `>`, `>=`, `<`, `<=`, `==`, `!=` – Relational Operators
11. `=`, `+=`, `-=`, etc. – Assignment Operators
12. `is`, `is not` – Identity Operators
13. `in`, `not in` – Membership Operators
14. `not` – Logical NOT
15. `and` – Logical AND
16. `or` – Logical OR

#### Examples
```python
print(3 + 10 * 2)       # 23 (multiplication first)
print((3 + 10) * 2)     # 26 (parentheses first)
print(3 / 2 * 4 + 3 + (10 / 5) ** 3 - 2)  # 15.0
```


```python
x = 5 + 2 ** 3 - 4
print(x)  # 9 (2**3 = 8, then 5 + 8 - 4)
```

---

### Mathematical Functions (`math` Module)
The `math` module provides functions and constants for mathematical operations.

#### Importing the Module
```python
import math
print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793
```

#### Using an Alias
```python
import math as m
print(m.sqrt(25))  # 5.0
```

#### Importing Specific Functions
```python
from math import sqrt, pi
print(sqrt(9))  # 3.0
print(pi)       # 3.141592653589793
```

#### Key Functions
1. `ceil(x)`: Smallest integer ≥ `x`.
2. `floor(x)`: Largest integer ≤ `x`.
3. `pow(x, y)`: `x` raised to `y`.
4. `factorial(x)`: Factorial of `x`.
5. `trunc(x)`: Truncates decimal part.
6. `gcd(x, y)`: Greatest common divisor.
7. `sin(x)`, `cos(x)`, `tan(x)`: Trigonometric functions (radians).

#### Key Variables
1. `pi`: 3.141592653589793
2. `e`: 2.718281828459045
3. `inf`: Infinity
4. `nan`: Not a Number

#### Example: Area of a Circle
```python
from math import pi
r = 16
print("Area of Circle is:", pi * r ** 2)  # 804.247719318987
```


```python
import math
print(math.factorial(5))  # 120
print(math.gcd(48, 18))   # 6
```

---
## Examples:

### 1. User Login Check (Hashing for Passwords)
**Use Case**: Verifying a user’s password in a simple login system (e.g., a small app).  
**How It’s Used**: Hashing stores a password securely, and equality operators check if the input matches.  
**Operators Used**: Assignment (`=`), equality (`==`).  

```python
import hashlib

stored_password = hashlib.sha256("pass123".encode()).hexdigest()  # Stored hash
input_password = "pass123"
hashed_input = hashlib.sha256(input_password.encode()).hexdigest()

if hashed_input == stored_password:
    print("Login successful!")
else:
    print("Wrong password!")
```

---

### 2. Fast Name Lookup (Hashing in a Contact List)
**Use Case**: Finding a phone number in a contact list quickly (e.g., a phone app).  
**How It’s Used**: A hash table maps names to numbers for instant access.  
**Operators Used**: Assignment (`=`).  

```python
contacts = {}  # Hash table
contacts["anita"] = "123-4567"
contacts["bittu"] = "987-6543"

name = "anita"
print("Phone:", contacts.get(name, "Not found"))
```

---

### 3. Checking Duplicates (Hashing in a To-Do App)
**Use Case**: Preventing duplicate tasks in a to-do list app.  
**How It’s Used**: Hashing tracks tasks to see if they already exist.  
**Operators Used**: Membership (`in`), assignment (`=`).  

```python
tasks = {}
task = "Buy milk"
task_hash = hash(task)

if task_hash not in tasks:
    tasks[task_hash] = task
    print("Task added!")
else:
    print("Task already exists!")
```

---

### 4. Scoreboard Ranking (Operators for Comparison)
**Use Case**: Ranking players in a game by score (e.g., a mobile game).  
**How It’s Used**: Relational operators compare scores to find the highest.  
**Operators Used**: Relational (`>`), assignment (`=`).  

```python
player1_score = 50
player2_score = 75

if player1_score > player2_score:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
```

---

### 5. File Name Tracker (Hashing for Downloads)
**Use Case**: Tracking downloaded files in a download manager.  
**How It’s Used**: Hashing file names to check if they’ve been downloaded.  
**Operators Used**: Membership (`in`), assignment (`=`).  

```python
downloaded = {}
file = "setup.exe"
file_hash = hash(file)

if file_hash not in downloaded:
    downloaded[file_hash] = file
    print("File downloaded!")
else:
    print("File already downloaded!")
```

---

### 6. Simple Cache (Hashing for Speed)
**Use Case**: Storing results in a calculator app to avoid re-computation.  
**How It’s Used**: A hash table caches inputs and results.  
**Operators Used**: Assignment (`=`), membership (`in`).  

```python
cache = {}
input_num = 5

if input_num in cache:
    print("Cached result:", cache[input_num])
else:
    result = input_num * 2
    cache[input_num] = result
    print("New result:", result)
```

---

### 7. Permission Check (Bitwise Operators)
**Use Case**: Checking user permissions in a chat app (e.g., read/write access).  
**How It’s Used**: Bitwise operators manage permission flags.  
**Operators Used**: Bitwise (`&`), assignment (`=`).  

```python
READ = 1  # 001
WRITE = 2 # 010
user_permissions = READ | WRITE  # 011

if user_permissions & READ:
    print("User can read!")
if user_permissions & WRITE:
    print("User can write!")
```

---

### 8. Budget Tracker (Arithmetic Operators)
**Use Case**: Adding expenses in a budgeting app.  
**How It’s Used**: Arithmetic operators calculate totals.  
**Operators Used**: Addition (`+`), assignment (`=`).  

```python
budget = 100
expense1 = 30
expense2 = 20

total_spent = expense1 + expense2
remaining = budget - total_spent
print("Remaining budget:", remaining)
```

---

### 9. Unique ID Generator (Hashing for IDs)
**Use Case**: Creating unique IDs for users in a sign-up form.  
**How It’s Used**: Hashing generates a unique identifier from user input.  
**Operators Used**: Assignment (`=`), string concatenation (`+`).  

```python
users = {}
name = "John"
user_id = hash(name + "2025")

users[user_id] = name
print("User ID:", user_id)
```

---

### 10. Voting System (Operators for Counting)
**Use Case**: Counting votes in a simple poll app.  
**How It’s Used**: Operators increment and compare vote counts.  
**Operators Used**: Addition (`+=`), relational (`>`).  

```python
votes = {"Yes": 0, "No": 0}
votes["Yes"] += 1
votes["No"] += 2

if votes["Yes"] > votes["No"]:
    print("Yes wins!")
else:
    print("No wins!")
```

---
