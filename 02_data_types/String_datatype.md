# **Ⅰ. String Datatype 🎀**

The most commonly used object in any project and in any programming language is String only. Hence we should be aware of complete information about the String data type.

## **💥What is String?**
Any sequence of characters within either single quotes or double quotes is considered a String.  

```py
# Syntax
string1 = 'durga'  
string2 = "drishya"
```

**Note:**  
In most other languages like C, C++, Java, a single character within single quotes is treated as a `char` data type value. However, in Python, there is no `char` data type; it is treated as a String.

```py
# Example
var = 'a'  
type(var) #output: str
```

**Note** _We can also use triple quotes to include single quotes or double quotes as symbols inside the String literal._ 

**Examples:**

```py
# s = 'This is ' single quote symbol' # → Invalid  
s = 'This is \' single quote symbol' # → Valid 
s = "This is ' single quote symbol" #→ Valid
s = 'This is " double quotes symbol' # → Valid 
s = 'The "Python Notes" by 'durga'' # → Invalid  
s = "The "Python Notes" by 'durga'" # → Invalid  
s = 'The \"Python Notes\" by \'durga\'' # → Valid 
s = '''The "Python Notes" by 'durga'''' # → Valid  
```
---
## **Ⅰ. Accessing Characters of a String**

We can access characters of a string using the following ways:  
1. *By using Index*  
2. *By using Slice Operator*


### **1. Accessing Characters By Using Index**  
Python supports both **positive (+ve)** and **negative (-ve)** indices.  
  - **Positive Index**: Left to Right (Forward Direction)  
  - **Negative Index**: Right to Left (Backward Direction)  

```py
s = 'durga'
s[0] # 'd'
s[4] # 'a'
s[-1] # 'a'
# s[10] #IndexError: string index out of range
```
**Example Program**  
Write a program to accept a string from the keyboard and display its characters by index (both positive and negative).

```py
s = input("Enter Some String:")
i = 0
for x in s:
    print("The character present at positive index {} and at negative index {} is {}".format(i, i - len(s), x))
    i += 1
```


### **2. Accessing Characters by Using Slice Operator**

**Syntax**  
`s[beginindex: endindex: step]`  

- **Begin Index**: Starting point of the slice (substring).  
- **End Index**: The slice terminates at `endindex-1`.  
- **Step**: Increment value for slicing.

**Note**  
- If the **begin index** is not specified, slicing starts from the beginning of the string.  
- If the **end index** is not specified, slicing continues to the end of the string.  
- The default value for the **step** is `1`.  

**Examples**  
```py
s = "Python and MongoDB!"

s[1:7:1] #s[1:7:1]
s[1:7]
s[1:7:2]
s[:7]
s[7:]
s[::]
s[:]
s[::-1]
```

#### **Behaviour of Slice Operator**

- `s[begin: end: step]`  
- **Step Value**:  
    > If **step** is positive, slicing is done in the forward direction (left to right), considering characters from `begin` to `end-1`.  
    > If **step** is negative, slicing is done in the backward direction (right to left), considering characters from `begin` to `end+1`.  

**Notes**  
- In the **backward direction**, if the **end value** is `-1`, the result is always empty.  
- In the **forward direction**, if the **end value** is `0`, the result is always empty.  