# **Python Classes and Objects**

## What is a Class?
- In Python, everything is an object. To create objects, we require a model, plan, or blueprint, which is nothing but a class.
- We can write a class to represent properties (attributes) and actions (behavior) of an object.
- Properties can be represented by variables.
- Actions can be represented by methods.
- Hence, a class contains both variables and methods.

## How to Define a Class?
- We can define a class by using the `class` keyword.

**Syntax:**
```python
class className:
    ''' documentation string '''
    variables: instance variables, static and local variables
    methods: instance methods, static methods, class methods
```
- The documentation string represents the description of the class. Within the class, the doc string is always optional.
- We can get the doc string by using the following two ways:
  1. `print(classname.__doc__)`
  2. `help(classname)`

**Example:**
```python
class Student:
    ''' This is a student class with required data '''
print(Student.__doc__)
help(Student)
```

- Within a Python class, we can represent data by using variables.
- There are three types of variables allowed:
  1. Instance Variables (Object-Level Variables)
  2. Static Variables (Class-Level Variables)
  3. Local Variables (Method-Level Variables)

## Types of Methods
- Within a Python class, we can represent operations by using methods. The following are the various types of allowed methods:
  1. Instance Methods
  2. Class Methods
  3. Static Methods

**Example for Class:**
```python
class Student:
    ''' Developed by Durga for Python demo '''
    def __init__(self):
        self.name = 'durga'
        self.age = 40
        self.marks = 80

    def talk(self):
        print("Hello I am:", self.name)
        print("My Age is:", self.age)
        print("My Marks are:", self.marks)
```

## What is an Object?
- The physical existence of a class is nothing but an object. We can create any number of objects for a class.

**Syntax to Create Object:**
```python
referencevariable = classname()
```

**Example:**
```python
s = Student()
```

## What is a Reference Variable?
- The variable which can be used to refer to an object is called a reference variable. By using a reference variable, we can access properties and methods of an object.

**Program: Write a Python program to create a Student class and create an object for it. Call the method `talk()` to display student details.**
```python
class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def talk(self):
        print("Hello My Name is:", self.name)
        print("My Rollno is:", self.rollno)
        print("My Marks are:", self.marks)

s1 = Student("Durga", 101, 80)
s1.talk()
```

**Output:**
```
D:\durgaclasses>py test.py
Hello My Name is: Durga
My Rollno is: 101
My Marks are: 80
```

## Self Variable
- `self` is the default variable which always points to the current object (like the `this` keyword in Java).
- By using `self`, we can access instance variables and instance methods of an object.

**Note:**
1. `self` should be the first parameter inside the constructor:
   ```python
   def __init__(self):
   ```
2. `self` should be the first parameter inside instance methods:
   ```python
   def talk(self):
   ```

## Constructor Concept
- A constructor is a special method in Python.
- The name of the constructor should be `__init__(self)`.
- The constructor will be executed automatically at the time of object creation.
- The main purpose of a constructor is to declare and initialize instance variables.
- Per object, a constructor will be executed only once.
- A constructor can take at least one argument (at least `self`).
- A constructor is optional, and if we are not providing any constructor, then Python will provide a default constructor.

**Example:**
```python
def __init__(self, name, rollno, marks):
    self.name = name
    self.rollno = rollno
    self.marks = marks
```

**Program to Demonstrate a Constructor Will Execute Only Once Per Object:**
```python
class Test:
    def __init__(self):
        print("Constructor execution...")

    def m1(self):
        print("Method execution...")

t1 = Test()
t2 = Test()
t3 = Test()
t1.m1()
```

**Output:**
```
Constructor execution...
Constructor execution...
Constructor execution...
Method execution...
```

**Program:**
```python
class Student:
    ''' This is a student class with required data '''
    def __init__(self, x, y, z):
        self.name = x
        self.rollno = y
        self.marks = z

    def display(self):
        print("Student Name:{}\nRollno:{} \nMarks:{}".format(self.name, self.rollno, self.marks))

s1 = Student("Durga", 101, 80)
s1.display()
s2 = Student("Sunny", 102, 100)
s2.display()
```

**Output:**
```
Student Name: Durga
Rollno: 101
Marks: 80
Student Name: Sunny
Rollno: 102
Marks: 100
```

## Differences Between Methods and Constructors
| **Method** | **Constructor** |
|------------|-----------------|
| The name of a method can be any name | The constructor name should always be `__init__` |
| A method will be executed if we call that method | A constructor will be executed automatically at the time of object creation |
| Per object, a method can be called any number of times | Per object, a constructor will be executed only once |
| Inside a method, we can write business logic | Inside a constructor, we have to declare and initialize instance variables |

## Types of Variables
- Inside a Python class, three types of variables are allowed:
  1. Instance Variables (Object-Level Variables)
  2. Static Variables (Class-Level Variables)
  3. Local Variables (Method-Level Variables)

### 1. Instance Variables
- If the value of a variable varies from object to object, then such variables are called instance variables.
- For every object, a separate copy of instance variables will be created.

#### Where We Can Declare Instance Variables:
1. Inside a constructor by using the `self` variable.
2. Inside an instance method by using the `self` variable.
3. Outside of the class by using an object reference variable.

#### 1. Inside Constructor by Using Self Variable
- We can declare instance variables inside a constructor by using the `self` keyword. Once we create an object, these variables will be added to the object automatically.

**Example:**
```python
class Employee:
    def __init__(self):
        self.eno = 100
        self.ename = 'Durga'
        self.esal = 10000

e = Employee()
print(e.__dict__)
```

**Output:**
```
{'eno': 100, 'ename': 'Durga', 'esal': 10000}
```

#### 2. Inside Instance Method by Using Self Variable
- We can also declare instance variables inside an instance method by using the `self` variable. If any instance variable is declared inside an instance method, that instance variable will be added once we call that method.

**Example:**
```python
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30

t = Test()
t.m1()
print(t.__dict__)
```

**Output:**
```
{'a': 10, 'b': 20, 'c': 30}
```

#### 3. Outside of the Class by Using Object Reference Variable
- We can also add instance variables outside of a class to a particular object.

**Example:**
```python
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def m1(self):
        self.c = 30

t = Test()
t.m1()
t.d = 40
print(t.__dict__)
```

**Output:**
```
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
```

#### How to Access Instance Variables
- We can access instance variables within the class by using the `self` variable and outside of the class by using an object reference.

**Example:**
```python
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

    def display(self):
        print(self.a)
        print(self.b)

t = Test()
t.display()
print(t.a, t.b)
```

**Output:**
```
10
20
10 20
```

#### How to Delete Instance Variables from the Object
1. Within a class, we can delete an instance variable as follows:
   ```python
   del self.variableName
   ```
2. From outside of a class, we can delete instance variables as follows:
   ```python
   del objectreference.variableName
   ```

**Example:**
```python
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m1(self):
        del self.d

t = Test()
print(t.__dict__)
t.m1()
print(t.__dict__)
del t.c
print(t.__dict__)
```

**Output:**
```
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'c': 30}
{'a': 10, 'b': 20}
```

**Note:**
- The instance variables which are deleted from one object will not be deleted from other objects.

**Example:**
```python
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

t1 = Test()
t2 = Test()
del t1.a
print(t1.__dict__)
print(t2.__dict__)
```

**Output:**
```
{'b': 20, 'c': 30, 'd': 40}
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
```

- If we change the values of instance variables of one object, then those changes won’t be reflected in the remaining objects, because for every object, a separate copy of instance variables is available.

**Example:**
```python
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20

t1 = Test()
t1.a = 888
t1.b = 999
t2 = Test()
print('t1:', t1.a, t1.b)
print('t2:', t2.a, t2.b)
```

**Output:**
```
t1: 888 999
t2: 10 20
```

---

## Static Variables
- If the value of a variable does not vary from object to object, such variables should be declared within the class directly but outside of any methods. These are called static variables.
- For the entire class, only one copy of a static variable is created and shared by all objects of that class.
- We can access static variables either by using the class name or an object reference, but it is recommended to use the class name.

## Instance Variables vs. Static Variables
- **Instance Variables**: For every object, a separate copy of instance variables is created.
- **Static Variables**: For the entire class, only one copy of a static variable is created and shared by all objects of that class.

**Example:**
```python
class Test:
    x = 10  # Static variable
    def __init__(self):
        self.y = 20  # Instance variable

t1 = Test()
t2 = Test()
print('t1:', t1.x, t1.y)
print('t2:', t2.x, t2.y)
Test.x = 888
t1.y = 999
print('t1:', t1.x, t1.y)
print('t2:', t2.x, t2.y)
```

**Output:**
```
t1: 10 20
t2: 10 20
t1: 888 999
t2: 888 20
```

## Various Places to Declare Static Variables
Static variables can be declared in the following places:
1. Within the class directly, outside of any method.
2. Inside a constructor, using the class name.
3. Inside an instance method, using the class name.
4. Inside a class method, using either the class name or the `cls` variable.
5. Inside a static method, using the class name.

**Example:**
```python
class Test:
    a = 10  # Static variable declared within class
    def __init__(self):
        Test.b = 20  # Static variable declared in constructor
    
    def m1(self):
        Test.c = 30  # Static variable declared in instance method
    
    @classmethod
    def m2(cls):
        cls.d1 = 40  # Static variable declared in class method using cls
        Test.d2 = 400  # Static variable declared in class method using class name
    
    @staticmethod
    def m3():
        Test.e = 50  # Static variable declared in static method

print(Test.__dict__)
t = Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.f = 60  # Static variable declared outside class
print(Test.__dict__)
```

---

## How to Access Static Variables
Static variables (class-level variables) can be accessed in various ways depending on the context:

1. **Inside a constructor**: Using either `self` or the class name.
2. **Inside an instance method**: Using either `self` or the class name.
3. **Inside a class method**: Using either the `cls` variable or the class name.
4. **Inside a static method**: Using the class name.
5. **Outside of the class**: Using either an object reference or the class name.

**Example:**
```python
class Test:
    a = 10
    def __init__(self):
        print(self.a)
        print(Test.a)
    
    def m1(self):
        print(self.a)
        print(Test.a)
    
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)
    
    @staticmethod
    def m3():
        print(Test.a)

t = Test()
print(Test.a)
print(t.a)
t.m1()
t.m2()
t.m3()
```

## Where We Can Modify the Value of a Static Variable
- Static variables can be modified anywhere, either inside or outside the class, by using the class name. Inside a class method, they can also be modified using the `cls` variable.

**Example:**
```python
class Test:
    a = 777
    @classmethod
    def m1(cls):
        cls.a = 888
    
    @staticmethod
    def m2():
        Test.a = 999

print(Test.a)
Test.m1()
print(Test.a)
Test.m2()
print(Test.a)
```

**Output:**
```
777
888
999
```

## Effect of Changing a Static Variable Using `self` or Object Reference
- If we attempt to change the value of a static variable using `self` or an object reference, the static variable’s value remains unchanged. Instead, a new instance variable with the same name is created for that specific object.

**Example 1:**
```python
class Test:
    a = 10
    def m1(self):
        self.a = 888

t1 = Test()
t1.m1()
print(Test.a)
print(t1.a)
```

**Output:**
```
10
888
```

**Example 2:**
```python
class Test:
    x = 10
    def __init__(self):
        self.y = 20

t1 = Test()
t2 = Test()
print('t1:', t1.x, t1.y)
print('t2:', t2.x, t2.y)
t1.x = 888
t1.y = 999
print('t1:', t1.x, t1.y)
print('t2:', t2.x, t2.y)
```

**Output:**
```
t1: 10 20
t2: 10 20
t1: 888 999
t2: 10 20
```

**Example 3:**
```python
class Test:
    a = 10
    def __init__(self):
        self.b = 20

t1 = Test()
t2 = Test()
Test.a = 888
t1.b = 999
print(t1.a, t1.b)
print(t2.a, t2.b)
```

**Output:**
```
888 999
888 20
```

**Example 4:**
```python
class Test:
    a = 10
    def __init__(self):
        self.b = 20
    
    def m1(self):
        self.a = 888
        self.b = 999

t1 = Test()
t2 = Test()
t1.m1()
print(t1.a, t1.b)
print(t2.a, t2.b)
```

**Output:**
```
888 999
10 20
```

**Example 5:**
```python
class Test:
    a = 10
    def __init__(self):
        self.b = 20
    
    @classmethod
    def m1(cls):
        cls.a = 888
        cls.b = 999

t1 = Test()
t2 = Test()
t1.m1()
print(t1.a, t1.b)
print(t2.a, t2.b)
print(Test.a, Test.b)
```

**Output:**
```
888 20
888 20
888 999
```

## How to Delete Static Variables of a Class
- Static variables can be deleted from anywhere using the following syntax:
  ```python
  del classname.variablename
  ```
- Inside a class method, they can also be deleted using:
  ```python
  del cls.variablename
  ```

**Example:**
```python
class Test:
    a = 10
    @classmethod
    def m1(cls):
        del cls.a

Test.m1()
print(Test.__dict__)
```

**Example with Multiple Operations:**
```python
class Test:
    a = 10
    def __init__(self):
        Test.b = 20
        del Test.a
    
    def m1(self):
        Test.c = 30
        del Test.b
    
    @classmethod
    def m2(cls):
        cls.d = 40
        del Test.c
    
    @staticmethod
    def m3():
        Test.e = 50
        del Test.d

print(Test.__dict__)
t = Test()
print(Test.__dict__)
t.m1()
print(Test.__dict__)
Test.m2()
print(Test.__dict__)
Test.m3()
print(Test.__dict__)
Test.f = 60
print(Test.__dict__)
del Test.e
print(Test.__dict__)
```

**Note:**
- Static variables can be read using an object reference or `self`, but they cannot be modified or deleted this way.
- Attempting to modify a static variable using `self` or an object reference creates a new instance variable for that object.
  ```python
  t1.a = 70
  ```
- Attempting to delete a static variable using an object reference results in an error.
  ```python
  class Test:
      a = 10

  t1 = Test()
  del t1.a  # AttributeError: a
  ```
- Static variables can only be modified or deleted using the class name or `cls` variable.

## Example: Banking Application Using Static Variables
```python
import sys

class Customer:
    ''' Customer class with bank operations '''
    bankname = 'DURGABANK'
    
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    
    def deposit(self, amt):
        self.balance = self.balance + amt
        print('Balance after deposit:', self.balance)
    
    def withdraw(self, amt):
        if amt > self.balance:
            print('Insufficient funds. Cannot perform this operation')
            sys.exit()
        self.balance = self.balance - amt
        print('Balance after withdraw:', self.balance)

print('Welcome to', Customer.bankname)
name = input('Enter Your Name: ')
c = Customer(name)
while True:
    print('d - Deposit\nw - Withdraw\ne - Exit')
    option = input('Choose your option: ')
    if option.lower() == 'd':
        amt = float(input('Enter amount: '))
        c.deposit(amt)
    elif option.lower() == 'w':
        amt = float(input('Enter amount: '))
        c.withdraw(amt)
    elif option.lower() == 'e':
        print('Thanks for banking')
        sys.exit()
    else:
        print('Invalid option. Please choose a valid option')
```

**Output:**
```
D:\durga_classes>py test.py
Welcome to DURGABANK
Enter Your Name: Durga
d - Deposit
w - Withdraw
e - Exit
Choose your option: d
Enter amount: 10000
Balance after deposit: 10000.0
d - Deposit
w - Withdraw
e - Exit
Choose your option: d
Enter amount: 20000
Balance after deposit: 30000.0
d - Deposit
w - Withdraw
e - Exit
Choose your option: w
Enter amount: 2000
Balance after withdraw: 28000.0
d - Deposit
w - Withdraw
e - Exit
Choose your option: r
Invalid option. Please choose a valid option
d - Deposit
w - Withdraw
e - Exit
Choose your option: e
Thanks for banking
```

## Local Variables
- Sometimes, to meet temporary requirements, programmers can declare variables directly inside a method. Such variables are called local or temporary variables.
- Local variables are created when the method is executed and destroyed once the method completes.
- Local variables cannot be accessed outside the method.

**Example:**
```python
class Test:
    def m1(self):
        a = 1000
        print(a)
    
    def m2(self):
        b = 2000
        print(b)

t = Test()
t.m1()
t.m2()
```

**Output:**
```
1000
2000
```

**Example Demonstrating Local Variable Scope:**
```python
class Test:
    def m1(self):
        a = 1000
        print(a)
    
    def m2(self):
        b = 2000
        print(a)  # NameError: name 'a' is not defined
        print(b)

t = Test()
t.m1()
t.m2()
```

**Output:**
```
1000
NameError: name 'a' is not defined
```

---

## Types of Methods
Inside a Python class, three types of methods are allowed:
1. Instance Methods
2. Class Methods
3. Static Methods

### 1. Instance Methods
- If a method uses instance variables in its implementation, it is called an instance method.
- Instance methods must include a `self` parameter in their declaration to refer to the instance of the class.
- Inside the method, instance variables are accessed using the `self` variable.
- Within the class, instance methods are called using `self`. Outside the class, they are called using an object reference.

**Example:**
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print('Hi', self.name)
        print('Your Marks are:', self.marks)
    
    def grade(self):
        if self.marks >= 60:
            print('You got First Grade')
        elif self.marks >= 50:
            print('You got Second Grade')
        elif self.marks >= 35:
            print('You got Third Grade')
        else:
            print('You are Failed')

n = int(input('Enter number of students: '))
for i in range(n):
    name = input('Enter Name: ')
    marks = int(input('Enter Marks: '))
    s = Student(name, marks)
    s.display()
    s.grade()
    print()
```

**Output:**
```
Enter number of students: 2
Enter Name: Durga
Enter Marks: 90
Hi Durga
Your Marks are: 90
You got First Grade

Enter Name: Ravi
Enter Marks: 12
Hi Ravi
Your Marks are: 12
You are Failed
```
---

## Getter and Setter Methods
- Getter methods are used to retrieve the values of instance variables. They are also known as accessor methods.
- Setter methods are used to set the values of instance variables.

**Syntax for Getter Method:**
```python
def getVariable(self):
    return self.variable
```

**Example:**
```python
def getName(self):
    return self.name
```

**Example Program:**
```python
class Student:
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setMarks(self, marks):
        self.marks = marks
    
    def getMarks(self):
        return self.marks

n = int(input('Enter number of students: '))
for i in range(n):
    s = Student()
    name = input('Enter Name: ')
    s.setName(name)
    marks = int(input('Enter Marks: '))
    s.setMarks(marks)
    
    print('Hi', s.getName())
    print('Your Marks are:', s.getMarks())
    print()
```

**Output:**
```
D:\python_classes>py test.py
Enter number of students: 2
Enter Name: Durga
Enter Marks: 100
Hi Durga
Your Marks are: 100

Enter Name: Ravi
Enter Marks: 80
Hi Ravi
Your Marks are: 80
```

## Class Methods
- If a method uses only class variables (static variables) in its implementation, it should be declared as a class method.
- Class methods are explicitly declared using the `@classmethod` decorator.
- A class method requires a `cls` parameter at the time of declaration, which refers to the class itself.
- Class methods can be called using either the class name or an object reference.

**Example:**
```python
class Animal:
    legs = 4  # Static variable
    @classmethod
    def walk(cls, name):
        print('{} walks with {} legs...'.format(name, cls.legs))

Animal.walk('Dog')
Animal.walk('Cat')
```

**Output:**
```
D:\python_classes>py test.py
Dog walks with 4 legs...
Cat walks with 4 legs...
```

**Program to Track the Number of Objects Created for a Class:**
```python
class Test:
    count = 0  # Static variable to track object count
    def __init__(self):
        Test.count = Test.count + 1
    
    @classmethod
    def noOfObjects(cls):
        print('The number of objects created for Test class:', cls.count)

t1 = Test()
t2 = Test()
Test.noOfObjects()
t3 = Test()
t4 = Test()
t5 = Test()
Test.noOfObjects()
```

**Output:**
```
The number of objects created for Test class: 2
The number of objects created for Test class: 5
```

## Static Methods
- Static methods are general utility methods that do not use instance or class variables.
- They do not require `self` or `cls` arguments at the time of declaration.
- Static methods are explicitly declared using the `@staticmethod` decorator.
- They can be accessed using either the class name or an object reference.

**Example:**
```python
class DurgaMath:
    @staticmethod
    def add(x, y):
        print('The Sum:', x + y)
    
    @staticmethod
    def product(x, y):
        print('The Product:', x * y)
    
    @staticmethod
    def average(x, y):
        print('The average:', (x + y) / 2)

DurgaMath.add(10, 20)
DurgaMath.product(10, 20)
DurgaMath.average(10, 20)
```

**Output:**
```
The Sum: 30
The Product: 200
The average: 15.0
```

**Note:**
- Typically, instance and static methods are used most often. Inside static methods, class-level variables can be accessed using the class name.
- Class methods are rarely used in Python.

## Passing Members of One Class to Another Class
- Members (attributes or methods) of one class can be accessed and modified by another class.

**Example:**
```python
class Employee:
    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal
    
    def display(self):
        print('Employee Number:', self.eno)
        print('Employee Name:', self.ename)
        print('Employee Salary:', self.esal)

class Test:
    @staticmethod
    def modify(emp):
        emp.esal = emp.esal + 10000
        emp.display()

e = Employee(100, 'Durga', 10000)
Test.modify(e)
```

**Output:**
```
D:\python_classes>py test.py
Employee Number: 100
Employee Name: Durga
Employee Salary: 20000
```

**Explanation:**
- In this example, the `Employee` class members are accessed and modified by the `Test` class.

## Inner Classes
- A class can be declared inside another class; such classes are called inner classes.
- Inner classes are used when the existence of one type of object depends on the existence of another type of object.
  - **Example**: An `Engine` object cannot exist without a `Car` object, so `Engine` should be an inner class of `Car`.
  - **Example**: A `Department` object cannot exist without a `University` object.
  - **Example**: A `Head` object cannot exist without a `Human` object.
- An inner class object is always associated with an outer class object; without an outer class object, an inner class object cannot exist.

**Demo Program-1:**
```python
class Outer:
    def __init__(self):
        print("Outer class object creation")
    
    class Inner:
        def __init__(self):
            print("Inner class object creation")
        
        def m1(self):
            print("Inner class method")

o = Outer()
i = o.Inner()
i.m1()
```

**Output:**
```
Outer class object creation
Inner class object creation
Inner class method
```

**Possible Syntaxes for Calling Inner Class Methods:**
1. ```python
   o = Outer()
   i = o.Inner()
   i.m1()
   ```
2. ```python
   i = Outer().Inner()
   i.m1()
   ```
3. ```python
   Outer().Inner().m1()
   ```

**Demo Program-2:**
```python
class Person:
    def __init__(self):
        self.name = 'durga'
        self.db = self.Dob()
    
    def display(self):
        print('Name:', self.name)
    
    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 5
            self.yy = 1947
        
        def display(self):
            print('Dob={}/{}/{}'.format(self.dd, self.mm, self.yy))

p = Person()
p.display()
x = p.db
x.display()
```

**Output:**
```
Name: durga
Dob=10/5/1947
```

**Demo Program-3 (Multiple Inner Classes):**
- A class can contain any number of inner classes.

```python
class Human:
    def __init__(self):
        self.name = 'Sunny'
        self.head = self.Head()
        self.brain = self.Brain()
    
    def display(self):
        print("Hello..", self.name)
    
    class Head:
        def talk(self):
            print('Talking...')
    
    class Brain:
        def think(self):
            print('Thinking...')

h = Human()
h.display()
h.head.talk()
h.brain.think()
```

**Output:**
```
Hello.. Sunny
Talking...
Thinking...
```

## Garbage Collection
- In older languages like C++, programmers are responsible for both creating and destroying objects. Neglecting to destroy unused objects can lead to memory issues, potentially causing the application to crash with an "Out of Memory" error.
- In Python, a garbage collector runs in the background to automatically destroy unused objects, reducing the likelihood of memory-related issues.
- The main objective of the garbage collector is to destroy objects that are no longer needed.
- An object is eligible for garbage collection if it has no reference variables pointing to it.

**How to Enable and Disable the Garbage Collector:**
- By default, the garbage collector is enabled, but it can be disabled if needed using the `gc` module.
- Functions in the `gc` module:
  1. `gc.isenabled()`: Returns `True` if the garbage collector is enabled.
  2. `gc.disable()`: Disables the garbage collector explicitly.
  3. `gc.enable()`: Enables the garbage collector explicitly.

**Example:**
```python
import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())
```

**Output:**
```
True
False
True
```

## Destructors
- A destructor is a special method named `__del__`.
- The garbage collector calls the destructor just before destroying an object to perform cleanup activities, such as deallocating resources (e.g., closing a database connection).
- After the destructor completes, the garbage collector automatically destroys the object.

**Note:**
- The destructor's role is not to destroy the object but to perform cleanup activities.

**Example:**
```python
import time
class Test:
    def __init__(self):
        print("Object Initialization...")
    
    def __del__(self):
        print("Fulfilling last wish and performing cleanup activities...")

t1 = Test()
t1 = None
time.sleep(5)
print("End of application")
```

**Output:**
```
Object Initialization...
Fulfilling last wish and performing cleanup activities...
End of application
```

**Note:**
- An object is eligible for garbage collection only if its reference count is zero (i.e., no reference variables point to it).

**Example with Multiple References:**
```python
import time
class Test:
    def __init__(self):
        print("Constructor Execution...")
    
    def __del__(self):
        print("Destructor Execution...")

t1 = Test()
t2 = t1
t3 = t2
del t1
time.sleep(5)
print("Object not yet destroyed after deleting t1")
del t2
time.sleep(5)
print("Object not yet destroyed even after deleting t2")
print("I am trying to delete the last reference variable...")
del t3
```

**Example with List of Objects:**
```python
import time
class Test:
    def __init__(self):
        print("Constructor Execution...")
    
    def __del__(self):
        print("Destructor Execution...")

list = [Test(), Test(), Test()]
del list
time.sleep(5)
print("End of application")
```

**Output:**
```
Constructor Execution...
Constructor Execution...
Constructor Execution...
Destructor Execution...
Destructor Execution...
Destructor Execution...
End of application
```

## How to Find the Number of References to an Object
- The `sys` module provides the `getrefcount()` function to determine the number of references to an object.
- Syntax: `sys.getrefcount(objectreference)`

**Example:**
```python
import sys
class Test:
    pass

t1 = Test()
t2 = t1
t3 = t1
t4 = t1
print(sys.getrefcount(t1))
```

**Output:**
```
5
```

**Note:**
- Python internally maintains a default reference to every object (e.g., `self`), which contributes to the reference count.
