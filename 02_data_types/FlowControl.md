## Flow Control in Python

### Introduction
Flow control describes the order in which statements are executed at runtime in a Python program. It allows developers to guide how a program behaves based on conditions, repetitions, or interruptions. Python supports three main categories of flow control:

1. **Conditional Statements**: Execute code based on specific conditions.
2. **Iterative Statements**: Repeat code multiple times.
3. **Transfer Statements**: Alter the flow of execution.

visual breakdown:

```
                           Flow Control
                                   
Conditional Statements | Iterative Statements | Transfer Statements
       if              |      for            |   break
       if-elif         |      while          |   continue
       if-elif-else    |                     |   pass
```

---

### I. Conditional Statements
Conditional statements allow a program to make decisions by executing code blocks based on whether a condition evaluates to `True` or `False`.

#### 1. `if` Statement
The `if` statement executes a block of code only if its condition is `True`.

#### Syntax
```python
if condition:
    statement
```
Or with multiple statements:
```python
if condition:
    statement-1
    statement-2
    statement-3
```

#### Behavior
The code inside the `if` block runs only when the condition is `True`. If the condition is `False`, the block is skipped.

#### Example
```python
name = input("Enter Name: ")
if name == "durga":
    print("Hello Durga Good Morning")
print("How are you!!!")
```

#### Execution Output
  **Input**: `durga`
  ```
  Hello Durga Good Morning
  How are you!!!
  ```
  **Input**: `Ravi`
  ```
  How are you!!!
  ```

#### 2. `if-else` Statement
The `if-else` statement provides two paths: one for when the condition is `True` and another for when it’s `False`.

#### Syntax
```python
if condition:
    Action-1
else:
    Action-2
```

#### Behavior
If the condition is `True`, `Action-1` executes; otherwise, `Action-2` executes.

#### Example
```python
name = input("Enter Name: ")
if name == "durga":
    print("Hello Durga Good Morning")
else:
    print("Hello Guest Good Morning")
print("How are you!!!")
```

#### Execution Output
 **Input**: `durga`
  ```
  Hello Durga Good Morning
  How are you!!!
  ```
 **Input**: `Ravi`
  ```
  Hello Guest Good Morning
  How are you!!!
  ```

#### Example
```python
number = int(input("Enter a number: "))
if number % 2 == 0:#### Syntax
    print("Even number")
else:
    print("Odd number")
```

#### 3. `if-elif-else` Statement
The `if-elif-else` statement handles multiple conditions, executing the block for the first `True` condition or a default action if none are `True`.

#### Syntax
```python
if condition1:
    Action-1
elif condition2:
    Action-2
elif condition3:
    Action-3
else:
    Default Action
```

#### Behavior
Conditions are checked sequentially. The first `True` condition triggers its action, and if none are `True`, the `else` block runs.

#### Example
```python
day = input("Enter day of the week: ")
if day.lower() == "monday":
    print("Start of the work week!")
elif day.lower() == "friday":
    print("Almost the weekend!")
elif day.lower() == "saturday" or day.lower() == "sunday":
    print("It's the weekend!")
else:
    print("It's a regular workday.")
```

#### Execution Output
 **Input**: `Monday`
  ```
  Start of the work week!
  ```
 **Input**: `Friday`
  ```
  Almost the weekend!
  ```
 **Input**: `Saturday`
  ```
  It's the weekend!
  ```
 **Input**: `Wednesday`
  ```
  It's a regular workday.
  ```

#### Example
```python
score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: D")
```

---

### Conditional Programs

#### Program 1: Favorite Brand Check
Checks a user’s favorite brand and provides a response.

```python
brand = input("Enter Your Favourite Brand: ")
if brand == "RC":
    print("It is children's brand")
elif brand == "KF":
    print("It is not that much kick")
elif brand == "FO":
    print("Buy one get Free One")
else:
    print("Other Brands are not recommended")
```

#### Example Outputs
- **Input**: `RC`  
  **Output**: `It is children's brand`
- **Input**: `KF`  
  **Output**: `It is not that much kick`
- **Input**: `KALYANI`  
  **Output**: `Other Brands are not recommended`

#### Program 2: Find the Biggest of Two Numbers
Compares two numbers to find the larger one.

```python
n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
if n1 > n2:
    print("Biggest Number is:", n1)
else:
    print("Biggest Number is:", n2)
```

#### Example Outputs
- **Input**: `10, 20`  
  **Output**: `Biggest Number is: 20`
- **Input**: `30, 25`  
  **Output**: `Biggest Number is: 30`

#### Program 3: Find the Biggest of Three Numbers
Compares three numbers to find the largest.

```python
n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))
n3 = int(input("Enter Third Number: "))
if n1 > n2 and n1 > n3:
    print("Biggest Number is:", n1)
elif n2 > n3:
    print("Biggest Number is:", n2)
else:
    print("Biggest Number is:", n3)
```

#### Example Outputs
 **Input**: `10, 20, 30`  
  **Output**: `Biggest Number is: 30`
 **Input**: `10, 30, 20`  
  **Output**: `Biggest Number is: 30`

#### Program 4: Check If a Number is Between 1 and 10
Verifies if a number falls within a range.

```python
n = int(input("Enter Number: "))
if n >= 1 and n <= 10:
    print(f"The number {n} is in between 1 to 10")
else:
    print(f"The number {n} is not in between 1 to 10")
```

#### Example Outputs
 **Input**: `5`  
  **Output**: `The number 5 is in between 1 to 10`
 **Input**: `15`  
  **Output**: `The number 15 is not in between 1 to 10`

#### Program 5: Convert Single Digit Number to English Word
Converts a digit (0-9) to its English word.

```python
n = int(input("Enter a digit from 0 to 9: "))
if n == 0:
    print("ZERO")
elif n == 1:
    print("ONE")
elif n == 2:
    print("TWO")
elif n == 3:
    print("THREE")
elif n == 4:
    print("FOUR")
elif n == 5:
    print("FIVE")
elif n == 6:
    print("SIX")
elif n == 7:
    print("SEVEN")
elif n == 8:
    print("EIGHT")
elif n == 9:
    print("NINE")
else:
    print("PLEASE ENTER A DIGIT FROM 0 TO 9")
```

#### Example Outputs
- **Input**: `3`  
  **Output**: `THREE`
- **Input**: `9`  
  **Output**: `NINE`
- **Input**: `11`  
  **Output**: `PLEASE ENTER A DIGIT FROM 0 TO 9`

#### Notes
1. The `else` clause in `if-elif-else` is optional.
2. Python supports `if`, `if-else`, `if-elif`, and `if-elif-else` syntaxes.
3. Unlike some languages (e.g., C or Java), Python does not have a `switch` statement. Use `if-elif-else` instead.

---

## II. Iterative Statements
Iterative statements (loops) allow a group of statements to be executed multiple times. Python provides two types: `for` loops and `while` loops.

#### 1. `for` Loop
The `for` loop iterates over a sequence (e.g., string, list) and executes its body for each element.

#### Syntax
```python
for x in sequence:
    Body
```

#### Examples

1. **Print Characters in a String**
   ```python
   s = "durga"
   for x in s:
       print(x)
   ```
   **Output**:
   ```
   d
   u
   r
   g
   a
   ```

2. **Print Characters with Index**
   ```python
   s = input("Enter some String: ")
   i = 0
   for x in s:
       print("The character present at", i, "index is:", x)
       i = i + 1
   ```
   **Input**: `Sunny`
   **Output**:
   ```
   The character present at 0 index is: S
   The character present at 1 index is: u
   The character present at 2 index is: n
   The character present at 3 index is: n
   The character present at 4 index is: y
   ```

3. **Print "Hello" 10 Times**
   ```python
   for x in range(10):
       print("Hello")
   ```
   **Output**:
   ```
   Hello
   Hello
   Hello
   ...
   ```

4. **Display Numbers from 0 to 10**
   ```python
   for x in range(11):
       print(x)
   ```
   **Output**:
   ```
   0
   1
   2
   ...
   10
   ```

5. **Display Odd Numbers from 0 to 20**
   ```python
   for x in range(21):
       if x % 2 != 0:
           print(x)
   ```
   **Output**:
   ```
   1
   3
   5
   ...
   19
   ```

6. **Display Numbers in Descending Order (10 to 1)**
   ```python
   for x in range(10, 0, -1):
       print(x)
   ```
   **Output**:
   ```
   10
   9
   8
   ...
   1
   ```

7. **Calculate Sum of Numbers in a List**
   ```python
   lst = eval(input("Enter List: "))
   total = 0
   for x in lst:
       total += x
   print("The Sum =", total)
   ```
   **Input**: `[10, 20, 30, 40]`  
   **Output**: `The Sum = 100`

#### Example
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
```
**Output**:
```
I like apple
I like banana
I like cherry
```

#### 2. `while` Loop
The `while` loop repeats a block of code as long as a condition remains `True`.

#### Syntax
```python
while condition:
    Body
```

#### Examples

1. **Print Numbers from 1 to 10**
   ```python
   x = 1
   while x <= 10:
       print(x)
       x = x + 1
   ```
   **Output**:
   ```
   1
   2
   3
   ...
   10
   ```

2. **Calculate Sum of First `n` Numbers**
   ```python
   n = int(input("Enter number: "))
   total = 0
   i = 1
   while i <= n:
       total += i
       i += 1
   print("The sum of first", n, "numbers is:", total)
   ```
   **Input**: `5`  
   **Output**: `The sum of first 5 numbers is: 15`

3. **Prompt Until 'durga' is Entered**
   ```python
   name = ""
   while name != "durga":
       name = input("Enter Name: ")
   print("Thanks for confirmation")
   ```
   **Output**:
   ```
   Enter Name: Akshay
   Enter Name: durga
   Thanks for confirmation
   ```

#### Example
```python
count = 0
while count < 3:
    print("Attempt", count + 1)
    count += 1
```
**Output**:
```
Attempt 1
Attempt 2
Attempt 3
```

#### Infinite Loops
An infinite loop runs forever unless interrupted (e.g., with `break`).

```python
i = 0
while True:
    i += 1
    print("Hello", i)
```

#### Nested Loops
Loops inside loops are called nested loops.

#### Example
```python
for i in range(4):
    for j in range(4):
        print("i=", i, "j=", j)
```
**Output**:
```
i= 0 j= 0
i= 0 j= 1
i= 0 j= 2
i= 0 j= 3
...
i= 3 j= 3
```

---

## III. Transfer Statements
Transfer statements alter the normal flow of loops or programs.

#### 1. `break` Statement
The `break` statement exits a loop immediately.

#### Example
```python
for i in range(10):
    if i == 7:
        print("Processing is enough... Please break")
        break
    print(i)
```
**Output**:
```
0
1
2
3
4
5
6
Processing is enough... Please break
```

#### 2. `continue` Statement
The `continue` statement skips the rest of the current iteration and moves to the next.

#### Example: Print Odd Numbers
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```
**Output**:
```
1
3
5
7
9
```

#### Example: Filter Cart Items
```python
cart = [10, 20, 500, 700, 50, 60]
for item in cart:
    if item >= 500:
        print(f"We cannot process this item: {item}")
        continue
    print(item)
```
**Output**:
```
10
20
We cannot process this item: 500
We cannot process this item: 700
50
60
```

#### 3. Loops with `else`
The `else` block in a loop runs if the loop completes without a `break`.

#### Example
```python
cart = [10, 20, 30, 40, 50]
for item in cart:
    if item >= 500:
        print("We cannot process this order")
        break
    print(item)
else:
    print("Congrats... all items processed successfully")
```
**Output**:
```
10
20
30
40
50
Congrats... all items processed successfully
```

#### 4. `pass` Statement
The `pass` statement is a placeholder that does nothing.

#### Example
```python
for i in range(100):
    if i % 9 == 0:
        print(i)
    else:
        pass
```
**Output**:
```
0
9
18
...
99
```

#### 5. `del` Statement
The `del` statement removes a variable or object from memory.

#### Example
```python
x = 10
print(x)  # 10
del x
# print(x)  # Raises NameError
```

#### Immutable Object Example
```python
s = "durga"
del s  # Valid
# del s[0]  # Raises TypeError
```

#### Difference Between `del` and `None`
```python
s = "durga"
s = None  # Variable exists, value is None
print(s)  # None
```

---

### Star Patterns

#### 1. Right-Angled Triangle of `*`
Prints a triangle of stars.

```python
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print("* " * i)
```
**Input**: `4`  
**Output**:
```
* 
* * 
* * * 
* * * * 
```

#### 2. Pyramid (Equilateral Triangle) of `*`
Prints a centered pyramid of stars.

```python
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
```
**Input**: `5`  
**Output**:
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
```

---


### 1. What happens in this code?
```python
lst = [1, 2, 3]
for i in lst:
    if i > 1:
        lst.remove(i)
print(lst)
```
- A) [1]  
- B) [1, 2, 3]  
- C) RuntimeError  
- D) [1, 3]  

**Answer**: C) RuntimeError  
**Explanation**: Modifying a list (`remove`) while iterating over it disrupts the iterator, causing a `RuntimeError` or unpredictable behavior (e.g., skipping elements). Here, `i=2` removes 2, shifting the list, and the next iteration fails.  
**Difficulty**: Runtime list mutation trap.

---

### 2. What’s the output?
```python
x = 0
while x < 5:
    if x == 3:
        x += 2
        continue
    x += 1
    print(x)
```
- A) 1, 2, 3, 4, 5  
- B) 1, 2, 4, 5  
- C) 1, 2, 3, 5  
- D) Infinite loop  

**Answer**: C) 1, 2, 3, 5  
**Explanation**: At `x=3`, `continue` skips `x += 1`, but `x += 2` makes `x=5`, so the next iteration ends the loop. Prints 1, 2, 3, 5.  
**Difficulty**: `continue` with double increment logic.

---

### 3. What’s the result?
```python
for i in range(5):
    if i == 2:
        i = 4
    print(i)
```
- A) 0, 1, 4, 3, 4  
- B) 0, 1, 2, 3, 4  
- C) 0, 1, 4, 4, 4  
- D) Infinite loop  

**Answer**: B) 0, 1, 2, 3, 4  
**Explanation**: Changing `i` inside the loop doesn’t affect the `range` iterator; `i` is reassigned each iteration.  
**Difficulty**: Misunderstanding loop variable scope.

---

### 4. What error occurs?
```python
s = "abc"
for i in range(len(s)):
    if s[i] == "b":
        del s[i]
print(s)
```
- A) TypeError  
- B) IndexError  
- C) ValueError  
- D) No error  

**Answer**: A) TypeError  
**Explanation**: Strings are immutable; `del s[i]` attempts item deletion, raising `TypeError: 'str' object doesn't support item deletion`.  
**Difficulty**: Immutable object misuse.

---

### 5. What’s the output?
```python
x = 10
if x > 0 or x / 0:
    print("A")
elif x > 5 and x < 15:
    print("B")
else:
    print("C")
```
- A) A  
- B) B  
- C) ZeroDivisionError  
- D) C  

**Answer**: A) A  
**Explanation**: `x > 0` is `True`, and Python short-circuits the `or`, skipping `x / 0`. Prints "A".  
**Difficulty**: Short-circuiting with potential runtime error.

---

### 6. How many times does this loop run?
```python
n = 5
while n > 0:
    n -= 1
    if n == 2:
        n = -1
    print(n)
```
- A) 3  
- B) 4  
- C) 5  
- D) Infinite  

**Answer**: B) 4  
**Explanation**: `n` goes 5→4, 4→3, 3→2, 2→-1 (prints 4, 3, 2, -1), then stops. 4 iterations.  
**Difficulty**: Mid-loop condition jump.

---

### 7. What’s the output?
```python
lst = [0, 1, 2]
for i in lst:
    if i < len(lst):
        lst[i] = lst[i] + 1
print(lst)
```
- A) [1, 2, 3]  
- B) [1, 1, 2]  
- C) IndexError  
- D) Infinite loop  

**Answer**: A) [1, 2, 3]  
**Explanation**: `i` takes values from the original list (`0, 1, 2`), incrementing each index. No error since `len(lst)` is checked.  
**Difficulty**: List modification with index access.

---

### 8. What error occurs?
```python
for i in range(3):
    if i == 1:
        break
        print("A")
    elif i == 2:
        continue
        print("B")
else:
    print("C")
```
- A) SyntaxError  
- B) No error, prints C  
- C) No error, prints nothing  
- D) RuntimeError  

**Answer**: C) No error, prints nothing  
**Explanation**: `break` at `i=1` exits the loop, skipping `else`. Unreachable `print` statements after `break` and `continue` don’t execute.  
**Difficulty**: Unreachable code with `else`.

---

### 9. What’s the output?
```python
n = 4
for i in range(n):
    for j in range(i, n):
        if j == i + 1:
            break
        print(j, end=" ")
```
- A) 0 1 2 3  
- B) 0 1 1 2  
- C) 0 1 2  
- D) 0  

**Answer**: C) 0 1 2  
**Explanation**: `i=0`: prints 0, breaks at 1; `i=1`: prints 1, breaks at 2; `i=2`: prints 2, breaks at 3; `i=3`: no print.  
**Difficulty**: Nested loop with early break.

---

### 10. What happens here?
```python
x = [1]
while x[-1] < 5:
    x.append(x[-1] + 1)
    if len(x) > 3:
        del x[0]
print(x)
```
- A) [1, 2, 3, 4, 5]  
- B) [3, 4, 5]  
- C) [2, 3, 4, 5]  
- D) Infinite loop  

**Answer**: B) [3, 4, 5]  
**Explanation**: `x` grows to [1, 2], [1, 2, 3], [1, 2, 3, 4] (len=4, deletes 1→[2, 3, 4]), then [2, 3, 4, 5]. Stops when `x[-1] = 5`.  
**Difficulty**: Dynamic list with deletion and boundary check.

---

## MCQs

### 1. What error occurs in this code?
```python
d = {1: "a", 2: "b"}
for k in d:
    if k == 1:
        del d[k]
print(d)
```
- A) KeyError  
- B) RuntimeError  
- C) TypeError  
- D) No error  

**Answer**: B) RuntimeError  
**Explanation**: Modifying a dictionary (deleting a key) during iteration disrupts the iterator, raising `RuntimeError: dictionary changed size during iteration`.  
**Difficulty**: Dictionary mutation trap.

---

### 2. What’s the output?
```python
x = 5
while x > 0:
    if x % 2 == 0:
        x -= 1
        continue
    x -= 2
    print(x)
```
- A) 3, 1  
- B) 3  
- C) 5, 3, 1  
- D) Infinite loop  

**Answer**: A) 3, 1  
**Explanation**: `x=5`: prints 3, `x=3`: prints 1, `x=1`: becomes -1, loop ends. `continue` skips even numbers.  
**Output**: 
```
3
1
```
**Difficulty**: Dual decrement with `continue`.

---

### 3. What happens here?
```python
for i in range(4):
    if i > 0:
        i -= 1
    elif i == 0:
        i += 2
    print(i)
```
- A) 2, 0, 1, 2  
- B) 0, 1, 2, 3  
- C) 0, 0, 1, 2  
- D) Infinite loop  

**Answer**: B) 0, 1, 2, 3  
**Explanation**: Modifying `i` doesn’t affect `range(4)`; it’s reassigned each iteration (0, 1, 2, 3).  
**Output**: 
```
0
1
2
3
```
**Difficulty**: Loop variable misconception.

---

### 4. What error is raised?
```python
lst = [1, 2, 3]
for i in range(len(lst)):
    if lst[i] == 2:
        lst.append(4)
print(lst)
```
- A) IndexError  
- B) No error  
- C) ValueError  
- D) RuntimeError  

**Answer**: B) No error  
**Explanation**: Appending to a list during iteration is safe with `range(len(lst))` since the range is fixed (0 to 2). Output: `[1, 2, 3, 4]`.  
**Difficulty**: Safe vs. unsafe list modification.

---

### 5. What’s the output?
```python
x = 0
if not x and x + 1 or x - 1:
    print("A")
elif x == 0 or x / 0:
    print("B")
else:
    print("C")
```
- A) A  
- B) B  
- C) ZeroDivisionError  
- D) C  

**Answer**: B) B  
**Explanation**: `not x` is `True` (x=0), but `x + 1 or x - 1` evaluates to 1, making the first condition `False`. Second condition `x == 0` is `True`, short-circuiting `x / 0`.  
**Difficulty**: Logical precedence and short-circuiting.

---

### 6. How many iterations?
```python
n = 6
while n > 0:
    if n % 3 == 0:
        n -= 3
    else:
        n -= 1
    print(n)
```
- A) 3  
- B) 4  
- C) 5  
- D) 6  

**Answer**: C) 5  
**Explanation**: `n=6`: 3, `n=3`: 0, `n=0` stops. Then `n=5`: 4, `n=4`: 3, `n=3`: 0. Total 5 prints (6, 3, 0, 4, 3).  
**Output**: 
```
3
0
```
**Difficulty**: Conditional decrement tracking.

---

### 7. What’s the result?
```python
s = "abc"
for i in range(len(s)):
    if i == 1:
        s = s[:i] + "x" + s[i+1:]
    print(s)
```
- A) abc, axc, axc  
- B) abc, abc, abc  
- C) TypeError  
- D) IndexError  

**Answer**: A) abc, axc, axc  
**Explanation**: `i=1` modifies `s` to "axc" mid-loop, but the range is fixed (0 to 2). Prints original and modified string.  
**Output**: 
```
abc
axc
axc
```
**Difficulty**: String reassignment in loop.

---

### 8. What error occurs?
```python
for i in range(5):
    if i == 2:
        break
    elif i == 3:
        continue
    print(i)
else:
    if i / 0:
        print("Done")
```
- A) ZeroDivisionError  
- B) No error, prints 0, 1  
- C) SyntaxError  
- D) No error, prints 0, 1, Done  

**Answer**: B) No error, prints 0, 1  
**Explanation**: `break` at `i=2` skips `else`, avoiding `i / 0`. Prints 0, 1.  
**Output**: 
```
0
1
```
**Difficulty**: `else` with unreachable error.

---

### 9. What’s the output?
```python
n = 3
for i in range(n):
    for j in range(n, 0, -1):
        if i + j == n:
            print(i, j)
            break
```
- A) 0 3, 1 2, 2 1  
- B) 0 1, 1 2, 2 3  
- C) 1 2, 2 1  
- D) 0 3  

**Answer**: A) 0 3, 1 2, 2 1  
**Explanation**: `i=0`: `j=3` (0+3=3), `i=1`: `j=2` (1+2=3), `i=2`: `j=1` (2+1=3). Breaks at match.  
**Output**: 
```
0 3
1 2
2 1
```
**Difficulty**: Reverse nested loop logic.

---

### 10. What happens?
```python
x = [0]
while x[0] < 10:
    x[0] += 1
    if x[0] > 5:
        x.pop(0)
    print(x)
```
- A) [1], [2], [3], [4], [5], []  
- B) [1], [2], [3], [4], [5], [6]  
- C) IndexError  
- D) Infinite loop  

**Answer**: C) IndexError  
**Explanation**: After `x[0]=6`, `pop(0)` empties the list. Next iteration, `x[0]` raises `IndexError`.  
**Output**: 
```
[1]
[2]
[3]
[4]
[5]
[]
```
**Difficulty**: List shrinkage with indexing.

---

