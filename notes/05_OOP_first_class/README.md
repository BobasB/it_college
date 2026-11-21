# Знайомство з ООП

## Мета роботи
Навчитись використовувати основні принципи ООП: розглянути конструкції побудови класу (атрибути, властивості, методи екземпляра, класу та статичні), створювати об'єкти та працювати з ними.

## Що потрібно знати / підготувати
- виконана робота [«Основи Python»](../04_python_basics/README.md) (функції, рядки, словники);
- лекційні матеріали про класи та об'єкти;
- Python 3.13+ (перевірте: `python --version`);

---
### Навіщо потрібні класи: словник проти об'єкта
Спершу розв'яжемо задачу «зберігати оцінки студентів» без класів. Створіть комірку ноутбука та виконайте:
```python
students_marks = {
    "Любомир": {"ООП": 90, "Бази даних": 80},
    "Василь": {"ООП": 30, "Бази даних": 40},
}
print(students_marks["Любомир"]["ООП"])
students_marks["Василь"]["Математика"] = 550   # помилка в даних ніхто не помітить
```
Тепер те саме з класом. Дані й правила роботи з ними зібрані в одному місці:
```python
class Student:
    def __init__(self, name: str, marks: dict[str, int]) -> None:
        self.name = name
        self._marks = marks

    @property
    def average(self) -> float:
        return sum(self._marks.values()) / len(self._marks)

    def set_mark(self, subject: str, mark: int) -> None:
        if not 0 <= mark <= 100:
            raise ValueError("Оцінка має бути від 0 до 100")
        self._marks[subject] = mark


lubomyr = Student("Любомир", {"ООП": 90, "Бази даних": 80})
lubomyr.set_mark("Математика", 70)
print(lubomyr.average)   # 80.0
lubomyr.set_mark("ООП", 150)   # ValueError
```
1. :star: Поясніть у звіті, які проблеми словникового підходу вирішує клас (перевірка даних, обчислювані значення, єдине місце для правил);
1. :star: Додайте до класу `Student` метод `best_subject()`, що повертає назву предмета з найвищою оцінкою;
1. Спробуйте додати «динамічний» атрибут після створення (`lubomyr.group = "КН-31"`) і поясніть, чим він відрізняється від атрибутів, заданих у `__init__`.

---
### Створюємо перший class
1. Створіть два python файли: для Ноутбука з розширенням `.ipynb` та для скрипта з розширенням `.py`;
1. Скопіюйте Python код наведений внизу у Ваш файл з розширенням `.py` та виконайте його натиснувши `Run Python File` (трикутник :arrow_forward:); 

### Перша програма на ООП
```python

class MyName:
    """Опис класу / Документація
    """
    total_names = 0 #Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу
        """
        self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
        MyName.total_names += 1 #modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self) -> str: 
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()
    
    def create_email(self) -> str:
        """Instance method
        """
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Classs method
        """
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        """Static method
        """
        return f"You say: {message}"


print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta", None)
all_names = {name: MyName(name) for name in names}

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")

print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")

```

1. :star: вкажіть у звіті що вивела програма або зробіть скріншот та вставте у звіт; 
1. Виконайте приклади які розглядали на лекції та вставте їх у Ноутбук (файл з розширенням `.ipynb`);
1. Ознайомтесь з кодом та спробуйте зрозуміти за що відповідає кожен з рядків. Після проходження всіх матеріалів з лекцій Ви повинні розуміти що робить даний клас;
1. Модифікуйте програму додавши своє імя в список;
1. :star: дайте відповідь на запитання та зробіть індивідуальні завдання (кожне — окремою коміркою ноутбука з коментарем): 
    - Чому коли передаємо значення `None` створюється обєкт з іменем `Anonymous`?
    - Як змінити текст привітання при виклику методу `say_hello()`? Допишіть цю частину коду.
    - Допишіть метод у класі, який порахує кількість букв імені (підказка: використайте функцію `len()`);
    - Порахуйте кількість імен у списку `names` та порівняйте із виведеним результатом. Дайте відповідь чому маємо різну кількість імен? (підказка: що робить `anonymous_user()` усередині `__init__`);
    - модифікуйте конструктор `__init__`, щоб значення `self.name` завжди починалося з великої літери, навіть якщо користувач ввів маленьку (підказка: `str.capitalize()`);
    - змініть метод `create_email` так щоб можна було модифікувати значення після `@` (параметр із значенням за замовчуванням);
    - додайте перевірку: якщо ім’я містить цифри або символи, підніміть помилку (підказка: `str.isalpha()`)
        ```python
        raise ValueError("Ім'я може містити лише літери!")
        ```
    - додайте нову властивість `full_name`, яка повертає результат у форматі:
        ```python
        "User #<id>: <name> (<email>)"
        ```
    - реалізуйте метод `save_to_file(filename="users.txt")`, який додає рядок із записом у файл (режим `"a"`, `encoding="utf-8"`);
1. :fire: Створіть клас `Student(MyName)`, що додає атрибут `group`, і перевизначте `full_name`.

> [!WARNING]
> Не комітьте згенерований файл `users.txt` — він містить результати запуску, а не код.

---
### Що має бути у звіті
- код програми та її вивід;
- відповіді на запитання про `None`/`Anonymous` та різну кількість імен;
- код і результат кожного індивідуального завдання;
- висновок за [шаблоном](../../reports/README.md).

### Контрольні питання
1. Чим відрізняються змінна класу та атрибут екземпляра?
1. Коли використовують `@classmethod`, а коли `@staticmethod`?
1. Для чого потрібен декоратор `@property`?
1. Що таке `self` та коли викликається `__init__`?

---
### Здача роботи
- :star: коли робота завершена та всі файли завантажено до репозиторію перейдіть у Веб-браузер та скопіюйте URL посилання на вашу роботу;
- :star: відправте URL посилання як відповідь на запитання до завдання у Google Classroom;
- :star: після того як Викладач перевірить роботу, Ви отримаєте оцінку у Google Classroom;

---
