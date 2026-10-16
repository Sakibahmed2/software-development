# Python OOP — Important Questions and Answers

Simple explanations, examples, and quick revision notes for learning Python Object-Oriented Programming (OOP).

## Table of Contents

1. [Operator Overloading and Method Overriding](#1-operator-overloading-and-method-overriding)
2. [Find the Oldest Player Using Operator Overloading](#2-find-the-oldest-player-using-operator-overloading)
3. [Class Method vs. Static Method](#3-class-method-vs-static-method)
4. [Getters and Setters](#4-getters-and-setters)
5. [Inheritance vs. Composition](#5-inheritance-vs-composition)
6. [Quick Revision](#6-quick-revision)

---

## 1. Operator Overloading and Method Overriding

### A. Operator Overloading

**Definition:** Operator overloading is a feature in Python that allows us to define how operators such as `+`, `-`, `==`, and `>` work with objects of a class.

For example, the `+` operator normally adds numbers. We can overload it to add the values stored in two objects.

**Example:**

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

print(num1 + num2)
```

**Output:**

```text
30
```

**Explanation:**

- `__add__()` is a special method that overloads the `+` operator.
- When we write `num1 + num2`, Python calls `num1.__add__(num2)`.
- The method adds the values of both objects.

Common operator overloading methods:

| Operator | Special method |
| -------- | -------------- |
| `+`      | `__add__()`    |
| `-`      | `__sub__()`    |
| `==`     | `__eq__()`     |
| `>`      | `__gt__()`     |
| `<`      | `__lt__()`     |

### B. Method Overriding

**Definition:** Method overriding occurs when a child class defines a method with the same name as a method in its parent class, providing its own implementation.

**Example:**

```python
class Person:
    def work(self):
        print("Person is working")


class Cricketer(Person):
    def work(self):
        print("Cricketer is playing cricket")


person = Person()
player = Cricketer()

person.work()
player.work()
```

**Output:**

```text
Person is working
Cricketer is playing cricket
```

**Explanation:**

- `Person` is the parent class.
- `Cricketer` is the child class.
- Both classes have a `work()` method.
- The child class overrides the parent's `work()` method.

### Differences

| Operator Overloading                      | Method Overriding                                          |
| ----------------------------------------- | ---------------------------------------------------------- |
| Defines how operators work with objects.  | Changes a parent's method implementation in a child class. |
| Uses special methods such as `__add__()`. | Uses the same method name in parent and child classes.     |
| Example: overloading `+`.                 | Example: overriding `work()`.                              |

---

## 2. Find the Oldest Player Using Operator Overloading

We can overload the `>` operator using the `__gt__()` method to compare the ages of two cricketers.

```python
class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class Cricketer(Person):
    def __init__(self, name, age, height, weight):
        super().__init__(name, age, height, weight)

    def __gt__(self, other):
        return self.age > other.age


sakib = Cricketer('Sakib', 38, 68, 91)
musfiq = Cricketer('Rahim', 36, 68, 88)
kamal = Cricketer('Kamal', 39, 68, 94)
jack = Cricketer('Jack', 38, 68, 91)
kalam = Cricketer('Kalam', 37, 68, 95)

oldest = sakib

if musfiq > oldest:
    oldest = musfiq

if kamal > oldest:
    oldest = kamal

if jack > oldest:
    oldest = jack

if kalam > oldest:
    oldest = kalam

print("Oldest player:", oldest.name)
print("Age:", oldest.age)
```

**Output:**

```text
Oldest player: Kamal
Age: 39
```

### How does it work?

```python
def __gt__(self, other):
    return self.age > other.age
```

- `__gt__()` means “greater than.”
- `self` represents the first player.
- `other` represents the second player.
- `self.age > other.age` compares their ages.

For example:

```python
print(kamal > sakib)
```

Output:

```text
True
```

Kamal is 39 years old, while Sakib is 38.

**Remember:**

- `>` calls `__gt__()`.
- `<` calls `__lt__()`.
- `==` calls `__eq__()`.

---

## 3. Class Method vs. Static Method

### A. Class Method

**Definition:** A class method is a method that works with the class itself. It takes `cls` as its first parameter and uses the `@classmethod` decorator.

### B. Static Method

**Definition:** A static method belongs to a class but does not automatically receive the class (`cls`) or an instance (`self`). It uses the `@staticmethod` decorator.

### Example

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def add(a, b):
        return a + b


Student.change_school("XYZ School")

print(Student.school)
print(Student.add(10, 20))
```

**Output:**

```text
XYZ School
30
```

**Explanation:**

- `change_school()` uses `cls` to change a class variable.
- `add()` performs a calculation without needing instance or class data.

### Four Differences

| Class Method                                                              | Static Method                                               |
| ------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 1. Uses the `@classmethod` decorator.                                     | 1. Uses the `@staticmethod` decorator.                      |
| 2. Takes `cls` as its first parameter.                                    | 2. Does not automatically take `self` or `cls`.             |
| 3. Can access and modify class variables through `cls`.                   | 3. Does not automatically receive class or instance data.   |
| 4. Commonly used for class-level operations and alternative constructors. | 4. Commonly used for utility operations related to a class. |

**Easy way to remember:**

- Instance method → `self`
- Class method → `cls`
- Static method → neither automatically

---

## 4. Getters and Setters

### Getter

**Definition:** A getter is a method used to access or retrieve the value of an object's attribute.

### Setter

**Definition:** A setter is a method used to update or modify an object's attribute, often with validation.

In Python, getters and setters can be implemented using `@property` and `@attribute.setter`.

### Example

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Age must be positive")


student = Student("Sakib", 22)

print(student.age)

student.age = 23
print(student.age)

student.age = -5
print(student.age)
```

**Output:**

```text
22
23
Age must be positive
23
```

### Explanation

**Getter:**

```python
@property
def age(self):
    return self._age
```

This returns the student's age when we write `student.age`.

**Setter:**

```python
@age.setter
def age(self, value):
    if value > 0:
        self._age = value
    else:
        print("Age must be positive")
```

This checks the new value before updating the age.

Here, `_age` is a convention indicating that the attribute is intended for internal use. It is not strictly private.

### Why do we use getters and setters?

1. To control access to attributes.
2. To validate values before updating them.
3. To prevent invalid data from being stored.
4. To keep the internal implementation flexible while maintaining a simple interface.

**Remember:** A getter reads a value; a setter changes a value.

---

## 5. Inheritance vs. Composition

### A. Inheritance

**Definition:** Inheritance is an OOP feature in which a child class acquires attributes and methods from a parent class.

It represents an **“is-a” relationship**.

For example, a `Cricketer` is a `Person`.

### Example

```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)


class Cricketer(Person):
    def play(self):
        print("Playing cricket")


player = Cricketer("Sakib")

player.introduce()
player.play()
```

**Output:**

```text
My name is Sakib
Playing cricket
```

**Explanation:** `Cricketer` inherits `introduce()` from `Person`, so it can use that method without defining it again.

### B. Composition

**Definition:** Composition is an OOP concept in which one class contains an object of another class to use its functionality.

It represents a **“has-a” relationship**.

For example, a `Car` has an `Engine`.

### Example

```python
class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")


car = Car()
car.start_car()
```

**Output:**

```text
Engine started
Car started
```

**Explanation:**

- `Engine` is a separate class.
- `Car` creates and stores an `Engine` object.
- The car uses the engine's `start()` method through `self.engine`.

### Four Differences

| Inheritance                                             | Composition                                                                  |
| ------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 1. Represents an “is-a” relationship.                   | 1. Represents a “has-a” relationship.                                        |
| 2. A child class inherits from a parent class.          | 2. A class contains an object of another class.                              |
| 3. Promotes reuse through a class hierarchy.            | 3. Promotes reuse by combining objects.                                      |
| 4. Creates a parent-child relationship between classes. | 4. Connects objects and can make components easier to replace independently. |

### Real-World Examples

**Inheritance — “is-a”**

- A `Cricketer` is a `Person`.
- A `Bus` is a `Vehicle`.

**Composition — “has-a”**

- A `Car` has an `Engine`.
- A `Computer` has a `CPU`.

---

## 6. Quick Revision

| Question                                                    | Short Answer                                                                                |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| What is operator overloading?                               | Defining how operators such as `+`, `>`, and `==` work with objects using special methods.  |
| What is method overriding?                                  | When a child class provides its own implementation of a method defined in its parent class. |
| Which method overloads the `>` operator?                    | `__gt__()`                                                                                  |
| What is the first parameter of a class method?              | `cls`                                                                                       |
| Does a static method automatically receive `self` or `cls`? | No.                                                                                         |
| What is a getter?                                           | A method used to retrieve an attribute's value.                                             |
| What is a setter?                                           | A method used to modify an attribute's value, often with validation.                        |
| What relationship does inheritance represent?               | An “is-a” relationship.                                                                     |
| What relationship does composition represent?               | A “has-a” relationship.                                                                     |

### Important Methods and Decorators to Remember

- `__init__()` — initializes an object.
- `__add__()` — overloads the `+` operator.
- `__gt__()` — overloads the `>` operator.
- `__lt__()` — overloads the `<` operator.
- `__eq__()` — overloads the `==` operator.
- `super()` — accesses methods from a parent class.
- `@classmethod` — defines a class method.
- `@staticmethod` — defines a static method.
- `@property` — defines a getter-style property.
- `@attribute.setter` — defines a setter for a property.

**Study tip:** Understand each example, then practise writing the definitions and differences without looking at the answers.
