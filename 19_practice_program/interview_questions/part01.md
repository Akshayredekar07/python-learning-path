## Question
**Q1. What is the difference between `is` operator and `==` operator in Python?**

## Answer
- **`is` Operator**:  
  In general, the `is` operator is meant for **reference comparison** or **address comparison**. It checks if two references are pointing to the same object in memory. If two references are pointing to the same object, then only the `is` operator returns `True`.  
  - Example: If two variables reference the same object (e.g., the same list or instance), `is` will return `True`. Otherwise, it returns `False`.

- **`==` Operator**:  
  The `==` operator is meant for **content comparison**. It checks if the contents or values of two objects are equal. Even though objects are different, if the content is the same, then the `==` operator returns `True`.  
  - Example: If two different objects (e.g., two separate lists with identical elements) have the same values, `==` will return `True`.

## Key Differences
| Aspect              | `is` Operator                  | `==` Operator                  |
|----------------------|--------------------------------|---------------------------------|
| **Purpose**          | Reference/Address comparison   | Content/Value comparison       |
| **Condition for True** | Same object in memory         | Same content/values            |
| **Example**          | `a is b` (same object)        | `a == b` (same value)          |

## Example Code
```python
# Example with `is` and `==`
a = [1, 2, 3]
b = a  # b points to the same object as a
c = [1, 2, 3]  # c is a different object with same content

print(a is b)  # True (same reference)
print(a is c)  # False (different references)
print(a == c)  # True (same content)
```
---


### 💡 What is a Ternary Operator?
The ternary operator in Python provides a way to assign a value to a variable based on a condition — all in **one line**.

```python
x = value_if_true if condition else value_if_false
```

---

### ✅ Example from the Code:

```python
a = int(input('Enter First Value:'))
b = int(input('Enter Second Value:'))
c = int(input('Enter Third Value:'))

biggestValue = a if a > b and a > c else b if b > c else c

print(f'Biggest Value: {biggestValue}')
```

🔍 **Explanation:**
- First, it compares `a` to `b` and `c`. If `a` is the largest, it's assigned to `biggestValue`.
- If not, it checks whether `b` is larger than `c`. If so, `b` is assigned.
- Otherwise, `c` is the biggest.

This nested ternary structure:
```python
a if a > b and a > c else b if b > c else c
```
is a **compact alternative** to using multiple `if-elif-else` statements.

---

## **Immutable Objects:**

These are objects whose state cannot be changed after they are created. If you try to modify an immutable object, Python will create a new object instead.

* **`int`**: Integers (e.g., `10`, `-5`, `0`)
* **`float`**: Floating-point numbers (e.g., `3.14`, `-0.5`, `2.0`)
* **`complex`**: Complex numbers (e.g., `3 + 2j`, `1j`)
* **`str` (string)**: Sequences of characters (e.g., `"hello"`, `"Python"`)
* **`bool`**: Boolean values (`True` or `False`)
* **`tuple`**: Ordered, immutable sequences of items (e.g., `(1, 2, "a")`)
* **`frozenset`**: Unordered, immutable collections of unique items
* **`bytes`**: Immutable sequences of single byte values (0-255)
* **`range`**: Immutable sequences of numbers, often used for looping

## **Mutable Objects:**

These are objects whose state can be changed after they are created. You can modify the object in place without creating a new one.

* **`list`**: Ordered, mutable sequences of items (e.g., `[1, 2, "a"]`)
* **`set`**: Unordered, mutable collections of unique items
* **`dict`**: Mutable mappings of keys to values (e.g., `{"name": "Alice", "age": 30}`)
* **`bytearray`**: Mutable sequences of single byte values (0-255)

**Why is this distinction important?**

Understanding mutability and immutability is crucial for several reasons:

* **How variables behave:** When you assign a mutable object to multiple variables, changes to one variable can affect the others because they all refer to the same underlying object. With immutable objects, each variable holds its own independent value.
* **Function arguments:** When you pass a mutable object to a function, the function can modify the original object. If you pass an immutable object, the function can only work with a copy of the value.
* **Hashing:** Immutable objects are hashable, meaning their value can be used to generate a unique hash value. This is why immutable types like strings and tuples can be used as keys in dictionaries and elements in sets. Mutable objects are not hashable.

---


## Differences Between Lists and Tuples in Python (Updated)

| List | Tuple |
|------|-------|
| 1. A group of comma-separated values within square brackets (mandatory). Example: `l = [10, 20, 30, 40]` | 1. A group of comma-separated values within parentheses (optional). Examples: `t = (10, 20, 30, 40)` or `t = 10, 20, 30, 40` |
| 2. Mutable - content can be changed after creation | 2. Immutable - content cannot be changed after creation |
| 3. Requires more memory | 3. Requires less memory |
| 4. Not reusable (different list objects with same values have different IDs) | 4. Reusable (tuple objects with same values may share the same ID) |
| 5. Lower performance - operations require more time | 5. Higher performance - operations require less time |
| 6. List comprehension is supported | 6. Tuple comprehension is not supported |
| 7. Unhashable - cannot be used as keys in dictionaries or as elements in sets | 7. Hashable - can be used as keys in dictionaries and as elements in sets |
| 8. Recommended when content is not fixed and may change | 8. Recommended when content is fixed and never changes |
| 9. Unpacking is possible but packing is not possible. Example: `a, b, c, d = l` (valid), but `l = a, b, c, d` (not a list) | 9. Both packing and unpacking are possible. Example: `t = a, b, c, d` (valid tuple packing), `a, b, c, d = t` (valid tuple unpacking) |

**Memory Usage Example:**
```python
import sys
l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print('The Size of List:', sys.getsizeof(l))
print('The Size of Tuple:', sys.getsizeof(t))

# Output:
# The Size of List: 136
# The Size of Tuple: 120
```

**Hashability Example:**
```python
# Invalid - Lists are unhashable
# s = {[10, 20, 30], [40, 50]}  # TypeError: unhashable type: 'list'
# d = {[10, 20]: 'value'}  # TypeError: unhashable type: 'list'

# Valid - Tuples are hashable
s = {10, 20, 30, (40, 50)}  # Valid
d = {(10, 20): 'value'}  # Valid
```

