## Основні парадигми ООП
> Об'єктно-орієнтоване програмування (ООП) базується на кількох ключових парадигмах, які дозволяють організовувати програму у вигляді взаємодіючих об'єктів. 

### 1. **Інкапсуляція**
Інкапсуляція означає приховування деталей реалізації об'єкта, забезпечуючи доступ до них лише через спеціальні методи. В Python інкапсуляція реалізується за допомогою:
- **Публічних атрибутів і методів** (public): доступні звідусіль.
- **Приватних атрибутів і методів** (private): позначаються символом `_` або `__` (наприклад, `_attr`, `__attr`).

**Приклад:**
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # публічний атрибут
        self.__balance = balance  # приватний атрибут

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance

# Використання:
account = BankAccount("Bohdan", 1000)
account.deposit(500)
print(account.get_balance())  # 1500
```

### 2. **Наслідування**
Наслідування дозволяє створювати нові класи на основі існуючих. Новий клас (дочірній) успадковує атрибути та методи базового класу.

**Приклад:**
```python
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)  # виклик конструктора базового класу
        self.seats = seats

    def display_info(self):
        return f"{super().display_info()}, Seats: {self.seats}"

# Використання:
car = Car("Toyota", "Camry", 5)
print(car.display_info())  # Toyota Camry, Seats: 5
```

### 3. **Поліморфізм**
Поліморфізм означає, що одна і та сама дія може виконуватись по-різному в залежності від об'єкта. Це забезпечується за допомогою перевизначення методів.

**Приклад:**
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Використання:
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())
# Вивід:
# Woof!
# Meow!
```

### 4. **Абстракція**
Абстракція приховує складність та залишає лише необхідні деталі. В Python це реалізується через **абстрактні класи** (використовуючи модуль `abc`).

**Приклад:**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Використання:
circle = Circle(5)
print(circle.area())  # 78.5
```

---
### Здача роботи
- :star: коли робота завершена та всі файли завантажено до репозиторію перейдіть у Веб-браузер та скопіюйте URL посилання на вашу роботу;
- :star: відправте URL посилання як відповідь на запитання до завдання у Google Classroom;
- :star: після того як Викладач перевірить роботу, Ви отримаєте оцінку у Google Classroom;

---