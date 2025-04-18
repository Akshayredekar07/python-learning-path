
## Code Examples from the Document

#### 1. Checking Data Types (`type()`, `id()`, `print()`)
```python
a = 10
print(type(a))  # Output: <class 'int'>

f = 1.234
print(type(f))  # Output: <class 'float'>

c = 'a'
print(type(c))  # Output: <class 'str'>
```

#### 2. `int` Data Type and Base Representations
```python
a = 10       # Decimal
b = 0o10     # Octal
c = 0x10     # Hexadecimal
d = 0b10     # Binary
print(a)     # Output: 10
print(b)     # Output: 8
print(c)     # Output: 16
print(d)     # Output: 2
```

#### 3. Base Conversions (`bin()`, `oct()`, `hex()`)
```python
print(bin(15))       # Output: '0b1111'
print(bin(0o11))     # Output: '0b1001'
print(bin(0x10))     # Output: '0b10000'

print(oct(10))       # Output: '0o12'
print(oct(0b1111))   # Output: '0o17'
print(oct(0x123))    # Output: '0o443'

print(hex(100))      # Output: '0x64'
print(hex(0b111111)) # Output: '0x3f'
print(hex(0o12345))  # Output: '0x14e5'
```

#### 4. `float` Data Type with Exponential Notation
```python
f = 1.234
print(type(f))       # Output: <class 'float'>

exponential_value = 1.2e3
print(exponential_value)  # Output: 1200.0
```

#### 5. `complex` Data Type
```python
a = 0b11 + 5j
print(a)  # Output: (3+5j)

a = 10 + 1.5j
b = 20 + 2.5j
c = a + b
print(c)  # Output: (30+4j)

c = 10.5 + 3.6j
print(c.real)  # Output: 10.5
print(c.imag)  # Output: 3.6
```

#### 6. `bool` Data Type
```python
b = True
print(type(b))  # Output: <class 'bool'>

a = 10
b = 20
c = a < b
print(c)  # Output: True

print(True + True)   # Output: 2
print(True - False)  # Output: 1
```

#### 7. `str` Data Type and Slicing
```python
s = "durga"
print(s[0])   # Output: 'd'
print(s[1])   # Output: 'u'
print(s[-1])  # Output: 'a'

print(s[1:40])  # Output: 'urga'
print(s[1:])    # Output: 'urga'
print(s[:4])    # Output: 'durg'
print(s[:])     # Output: 'durga'

print(s * 3)    # Output: 'durgadurgadurga'
print(len(s))   # Output: 5
```

#### 8. Multi-line Strings and Embedded Quotes
```python
s1 = '''durga soft'''
s2 = """durga soft"""
s3 = '''This is "character"'''
s4 = """This is 'character'"""
```

#### 9. Reserved Words (`keyword.kwlist`)
```python
import keyword
print(keyword.kwlist)
# Output: ['False', 'None', 'True', 'and', 'as', 'assert', ...]
```

#### 10. Type Casting
```python
print(int(123.987))  # Output: 123
print(int(True))     # Output: 1
print(int("10"))     # Output: 10

print(float(10))     # Output: 10.0
print(float("10.5")) # Output: 10.5

print(complex(10))   # Output: (10+0j)
print(complex(10, -2))  # Output: (10-2j)

print(bool(10))      # Output: True
print(bool(""))      # Output: False

print(str(10))       # Output: '10'
print(str(10+5j))    # Output: '(10+5j)'
```

#### 11. Immutability Examples
```python
# Integer example
a = 10
b = 10
print(a is b)        # Output: True
print(id(a), id(b))  # Output: same memory address
a = a + 1
print(a is b)        # Output: False
print(id(a), id(b))  # Output: different memory addresses

# String example
name1 = "Durga"
name2 = "Durga"
print(name1 is name2)  # Output: True
print(id(name1), id(name2))  # Output: same memory address
name1 = name1 + " Software"
print(name1 is name2)  # Output: False
print(id(name1), id(name2))  # Output: different memory addresses

# Boolean example
bool1 = True
bool2 = True
print(bool1 is bool2)  # Output: True
print(id(bool1), id(bool2))  # Output: same memory address
bool1 = False
print(bool1 is bool2)  # Output: False
print(id(bool1), id(bool2))  # Output: different memory addresses
```

#### 12. `bytearray` Data Type
```python
x = [10, 20, 30, 40]
b = bytearray(x)
for i in b:
    print(i)  # Output: 10, 20, 30, 40
b[0] = 100
for i in b:
    print(i)  # Output: 100, 20, 30, 40
```

#### 13. `list` Data Type
```python
list_example = [10, 10.5, 'durga', True, 10]
print(list_example)  # Output: [10, 10.5, 'durga', True, 10]

list_example = [10, 20, 30, 40]
print(list_example[0])   # Output: 10
print(list_example[-1])  # Output: 40
print(list_example[1:3]) # Output: [20, 30]
list_example[0] = 100
for i in list_example:
    print(i)  # Output: 100, 20, 30, 40

list_example = [10, 20, 30]
list_example.append("durga")
print(list_example)  # Output: [10, 20, 30, 'durga']
list_example.remove(20)
print(list_example)  # Output: [10, 30, 'durga']
list2 = list_example * 2
print(list2)  # Output: [10, 30, 'durga', 10, 30, 'durga']
```

#### 14. `tuple` Data Type
```python
t = (10, 20, 30, 40)
print(type(t))  # Output: <class 'tuple'>
```

#### 15. `range` Data Type
```python
r = range(10, 20)
print(r[0])  # Output: 10

l = list(range(10))
print(l)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### 16. `set` Data Type
```python
s = {100, 0, 10, 200, 10, 'durga'}
print(s)  # Output: {0, 100, 'durga', 200, 10}

s.add(60)
print(s)  # Output: {0, 100, 'durga', 200, 10, 60}
s.remove(100)
print(s)  # Output: {0, 'durga', 200, 10, 60}
```

#### 17. `frozenset` Data Type
```python
s = {10, 20, 30, 40}
fs = frozenset(s)
print(type(fs))  # Output: <class 'frozenset'>
print(fs)  # Output: frozenset({40, 10, 20, 30})
```

#### 18. `dict` Data Type
```python
d = {101: 'durga', 102: 'ravi', 103: 'shiva'}
d[101] = 'sunny'
print(d)  # Output: {101: 'sunny', 102: 'ravi', 103: 'shiva'}

d = {}
d['a'] = 'apple'
d['b'] = 'banana'
print(d)  # Output: {'a': 'apple', 'b': 'banana'}
```

#### 19. `None` Data Type
```python
def m1():
    a = 10
print(m1())  # Output: None
```

#### 20. Escape Characters
```python
s = "durga\nsoftware"
print(s)
# Output:
# durga
# software

s = "durga\tsoftware"
print(s)  # Output: durga    software

s = "This is \" symbol"
print(s)  # Output: This is " symbol
```

---

### Additional Examples for Better Understanding

#### 1. `int` Data Type and Base Representations
```python
# Additional Example
num_decimal = 25
num_binary = 0b11001  # 25 in binary
num_octal = 0o31      # 25 in octal
num_hex = 0x19        # 25 in hexadecimal

print(f"Decimal: {num_decimal}")  # Output: Decimal: 25
print(f"Binary: {num_binary}")    # Output: Binary: 25
print(f"Octal: {num_octal}")      # Output: Octal: 25
print(f"Hex: {num_hex}")          # Output: Hex: 25
```

#### 2. Base Conversions
```python
# Additional Example
value = 42
print(f"Binary of {value}: {bin(value)}")      # Output: Binary of 42: 0b101010
print(f"Octal of {value}: {oct(value)}")       # Output: Octal of 42: 0o52
print(f"Hex of {value}: {hex(value)}")         # Output: Hex of 42: 0x2a
```

#### 3. `float` Data Type
```python
# Additional Example
small_float = 0.000123
large_float = 5.67e8  # 5.67 * 10^8
print(f"Small float: {small_float}")  # Output: Small float: 0.000123
print(f"Large float: {large_float}")  # Output: Large float: 567000000.0
```

#### 4. `complex` Data Type
```python
# Additional Example
x = 2.5 + 3j
y = -1 + 4.2j
result = x * y
print(f"Multiplication: {result}")  # Output: Multiplication: (-15.1+8.5j)
print(f"Real part: {result.real}, Imaginary part: {result.imag}")
# Output: Real part: -15.1, Imaginary part: 8.5
```

#### 5. `bool` Data Type
```python
# Additional Example
is_active = True
count = 0
print(f"Is active? {is_active}")          # Output: Is active? True
print(f"Is count zero? {bool(count)}")    # Output: Is count zero? False
print(f"Logical AND: {is_active and count > 0}")  # Output: Logical AND: False
```

#### 6. `str` Data Type and Slicing
```python
# Additional Example
text = "Python Programming"
print(text[::-1])        # Output: gnimmargorP nohtyP (reversed string)
print(text[7:])          # Output: Programming
print(text.upper())      # Output: PYTHON PROGRAMMING
print(f"Length: {len(text)}")  # Output: Length: 18
```

#### 7. Type Casting
```python
# Additional Example
num_str = "123.45"
bool_val = False
complex_val = complex(float(num_str), 2)

print(f"String to float: {float(num_str)}")      # Output: 123.45
print(f"Bool to int: {int(bool_val)}")           # Output: 0
print(f"To complex: {complex_val}")             # Output: (123.45+2j)
```

#### 8. Immutability
```python
# Additional Example
x = 5
y = x
x += 1
print(f"x: {x}, y: {y}")  # Output: x: 6, y: 5
print(f"Same object? {x is y}")  # Output: Same object? False

str1 = "Hello"
str2 = str1
str1 += " World"
print(f"str1: {str1}, str2: {str2}")  # Output: str1: Hello World, str2: Hello
```

#### 9. `bytearray` Data Type
```python
# Additional Example
data = [50, 75, 100]
ba = bytearray(data)
ba[1] = 80
print(list(ba))  # Output: [50, 80, 100]
```

#### 10. `list` Data Type
```python
# Additional Example
colors = ["red", "blue", "green"]
colors.insert(1, "yellow")
print(colors)  # Output: ['red', 'yellow', 'blue', 'green']
colors.pop(0)
print(colors)  # Output: ['yellow', 'blue', 'green']
```

#### 11. `tuple` Data Type
```python
# Additional Example
coordinates = (3, 4, 5)
x, y, z = coordinates
print(f"X: {x}, Y: {y}, Z: {z}")  # Output: X: 3, Y: 4, Z: 5
```

#### 12. `range` Data Type
```python
# Additional Example
even_numbers = range(2, 11, 2)
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]
```

#### 13. `set` Data Type
```python
# Additional Example
fruits = {"apple", "banana", "apple", "cherry"}
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}
fruits.discard("banana")
print(fruits)  # Output: {'apple', 'cherry', 'orange'}
```

#### 14. `frozenset` Data Type
```python
# Additional Example
fixed_set = frozenset([1, 2, 3, 2])
print(fixed_set)  # Output: frozenset({1, 2, 3})
```

#### 15. `dict` Data Type
```python
# Additional Example
student = {"name": "Alice", "age": 20}
student["grade"] = "A"
print(student)  # Output: {'name': 'Alice', 'age': 20, 'grade': 'A'}
del student["age"]
print(student)  # Output: {'name': 'Alice', 'grade': 'A'}
```

#### 16. `None` Data Type
```python
# Additional Example
def no_return():
    pass
result = no_return()
print(f"Result: {result}")  # Output: Result: None
```

#### 17. Escape Characters
```python
# Additional Example
message = "Hello\rWorld\tPython\\bCode"
print(message)  
# Output: World    PythonCode (behavior may vary by platform due to \r)
print("Path: C:\\Users\\Name")  # Output: Path: C:\Users\Name
```

---

