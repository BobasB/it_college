## Основні парадигми ООП
### Мета роботи: __Ознайомитись з ключовими поняттями об’єктно-орієнтованого програмування (ООП) у Python та навчитися реалізовувати їх у власних класах на прикладі ігрової симуляції.__
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

account = BankAccount("Bohdan", 1000)
account.deposit(500)
print(account.get_balance())  # 1500
```
1. :star: Додайте генератор випадкових чисел та викличіть методи `deposit` та `withdraw` у циклі передаючи випадкові числа. Виведіть кінцевий результат;

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

car = Car("Toyota", "Camry", 5)
print(car.display_info())
```
1. :star: створіть ще один метод у класі `Vehicle` та викличіть його з обєкта класу `Car`; 

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
```
1. :star: створіть клас `Fish` у якого небуде метода `speak`. Як буде поводити себе обєкт класу `Fish` при виклику методу `speak`?

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

circle = Circle(5)
print(circle.area())
```

### Використання парадигм для створення простої гри
> Програма створює двох персонажів — меч і сокиру — та проводить бої між ними з випадковою генерацією сили удару.
> Кожен об’єкт має власну реалізацію методу attack, що і демонструє поліморфізм.
> Рандомізація (randint) додає ігровий елемент до симуляції.

| Парадигма        | Реалізація в коді                                        | Пояснення                                     |
| ---------------- | -------------------------------------------------------- | --------------------------------------------- |
| **Абстракція**   | `class Item(ABC)` + `@abstractmethod attack()`           | Задає спільний інтерфейс для усіх типів зброї |
| **Наслідування** | `class Sword(Item)`                                      | Використовує атрибути і методи базового класу |
| **Інкапсуляція** | `__attack_power`, `_sharp`, `@property get_attack_power` | Обмежує прямий доступ до внутрішніх змінних   |
| **Поліморфізм**  | `attack()` перевизначений у `Sword` і `Axe`              | Метод має однакове ім’я, але різну поведінку  |

```python
from abc import ABC, abstractmethod
from random import randint

class Item(ABC):
    def __init__(self, name:str, health = 500):
        self.name = name
        self.health = health
    
    @abstractmethod
    def attack(self):
        pass

class Sword(Item): # Це наслідування
    def __init__(self, name, attack_power:int):
        super().__init__(name=name) #  Це виклик конструктора наслідуваного класу
        self.__attack_power = attack_power # приватний атрибут який реалізує інкапсуляцію
        self._sharp = 0
    
    def attack(self, another_item:Item): # ми не можемо створити клас без цього методу
        current_attack = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= current_attack
        return f"Завдаємо удару мечем {self.name} та наносимо {current_attack} шкоди. У {another_item.name} залишалось здоровя: {another_item.health}"
    
    @property
    def get_attack_power(self):
        return f"Атака меча {self.name}: {self.__attack_power + self._sharp} одиниць"
    
    def sharpening(self):
        self._sharp += 1

class Axe(Item): # Це наслідування
    def __init__(self, name, attack_power:int):
        super().__init__(name=name) #  Це виклик конструктора наслідуваного класу
        self.__attack_power = attack_power # приватний атрибут який реалізує інкапсуляцію
        self._sharp = 0
    
    def attack(self, another_item:Item):  # ми не можемо створити клас без цього методу
        current_attack = self.__attack_power + randint(0, 20)
        another_item.health -= current_attack
        return f"Завдаємо удару сокирою {self.name} та наносимо {current_attack} шкоди. У {another_item.name} залишалось здоровя: {another_item.health}"

    @property
    def get_attack_power(self):
        return f"Атака сокири {self.name}: {self.__attack_power + self._sharp} одиниць"

S = Sword("Ескалібур", 100)
A = Axe("Кратос", 95)

for i in range(10):
    print(f"Хід {i}")

    S.sharpening()
    print(S.attack(A))
    if S.health <= 0:
        print(f"Перемога за {A.name}")
        break

    print(A.attack(S))
    if A.health <= 0:
        print(f"Перемога за {S.name}")
        break
```

### :star: Завдання
Додайте третій тип зброї — Bow (лук), який:
- має власний параметр `range_power` (дальність);
- метод `attack()` з формулою шкоди `attack_power + randint(5, 15) + range_power`;
- має метод `reload()`, який збільшує дальність `(range_power += 1)`;
Додайте випадковий вибір зброї з трьох можливих (Sword, Axe, Bow);
Зробіть гру покроковою, де користувач може робити хід та вибирати дії з своїм типом зброї (наприклад, атакувати або накласти підсилення щоб підвищити ефективність зброї на наступному кроці);

---
### Здача роботи
- :star: коли робота завершена та всі файли завантажено до репозиторію перейдіть у Веб-браузер та скопіюйте URL посилання на вашу роботу;
- :star: відправте URL посилання як відповідь на запитання до завдання у Google Classroom;
- :star: після того як Викладач перевірить роботу, Ви отримаєте оцінку у Google Classroom;

---