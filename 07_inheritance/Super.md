## **`super()` Method in Python**

The `super()` method is used to call the **superclass's constructor, variables, and methods** from the **child class**.

---

### **Demo Program 1: Using `super()` to Call Constructor and Method**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)

class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print('Roll No:', self.rollno)
        print('Marks:', self.marks)

s1 = Student('Durga', 22, 101, 90)
s1.display()
```

**Output:**

```
Name: Durga
Age: 22
Roll No: 101
Marks: 90
```

---

### **Demo Program 2: Using `super()` to Access Parent Members**

```python
class P:
    a = 10

    def __init__(self):
        self.b = 10

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    a = 888

    def __init__(self):
        self.b = 999
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()

c = C()
```

**Output:**

```
10
Parent instance method
Parent class method
Parent static method
```

---

### **Calling Method of a Particular Superclass**

#### **Approach 1:**

```python
super(D, self).m1()  # Calls m1() of D's parent
```

#### **Approach 2:**

```python
A.m1(self)  # Directly calls A class's m1()
```

#### **Example:**

```python
class A:
    def m1(self):
        print('A class Method')

class B(A):
    def m1(self):
        print('B class Method')

class C(B):
    def m1(self):
        print('C class Method')

class D(C):
    def m1(self):
        print('D class Method')

class E(D):
    def m1(self):
        A.m1(self)

e = E()
e.m1()
```

**Output:**

```
A class Method
```

---

### **Important Cases for `super()`**

---

### **Case 1: Accessing Variables**

```python
class P:
    a = 10
    def __init__(self):
        self.b = 20

class C(P):
    def m1(self):
        print(super().a)  # Valid (class variable)
        print(self.b)     # Valid (instance variable)
        print(super().b)  # Invalid (AttributeError)

c = C()
c.m1()
```

**Output:**

```
10
20
AttributeError: 'super' object has no attribute 'b'
```

---

### **Case 2: Accessing All Method Types via `super()` from Constructor and Instance Method**

```python
class P:
    def __init__(self):
        print('Parent Constructor')

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

    def m1(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()

c = C()
c.m1()
```

**Output:**

```
Parent Constructor
Parent instance method
Parent class method
Parent static method
Parent Constructor
Parent instance method
Parent class method
Parent static method
```

---

### **Case 3: Accessing Methods from Class Method (Direct vs Indirect)**

```python
class P:
    def __init__(self):
        print('Parent Constructor')

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    @classmethod
    def m1(cls):
        # super().__init__()    # Invalid
        # super().m1()          # Invalid
        super().m2()            # Valid
        super().m3()            # Valid

C.m1()
```

**Output:**

```
Parent class method
Parent static method
```

---

### **Calling Parent Instance Method from Class Method (Indirect)**

```python
class A:
    def __init__(self):
        print('Parent constructor')

    def m1(self):
        print('Parent instance method')

class B(A):
    @classmethod
    def m2(cls):
        super(B, cls).__init__(cls)
        super(B, cls).m1(cls)

B.m2()
```

**Output:**

```
Parent constructor
Parent instance method
```

---

### **Case 4: Accessing Parent Methods from Static Method**

```python
class P:
    def __init__(self):
        print('Parent Constructor')

    def m1(self):
        print('Parent instance method')

    @classmethod
    def m2(cls):
        print('Parent class method')

    @staticmethod
    def m3():
        print('Parent static method')

class C(P):
    @staticmethod
    def m1():
        super().m1()  # Invalid
        super().m2()  # Invalid
        super().m3()  # Invalid

C.m1()
```

**Output:**

```
RuntimeError: super(): no arguments
```

---

### **Correct Way: Calling Parent Static Method via `super()` from Child Static Method**

```python
class A:
    @staticmethod
    def m1():
        print('Parent static method')

class B(A):
    @staticmethod
    def m2():
        super(B, B).m1()

B.m2()
```

**Output:**

```
Parent static method
```

---

