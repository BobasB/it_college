# Знайомство з ООП

### Створюємо перший class
1. Створіть два python файли: для Ноутбука з розширенням `.ipynb` та для скрипта з розширенням `.py`;
1. Скопіюйте Python код наведений внизу у Ваші файли та виконайте їх натиснувши `Run Python File` (трикутник :arrow_forward:); 

<details><summary> >>>>>> Python Code <<<<<< </summary>

### Перша програма на ООП
```python

class MyName:
    def __init__(self, name=None) -> None:
        self.name = name if name is not None else self.anonymous_user().name # Class attributes
    
    @property
    def whoami(self): #Class property
        return f"My name is {self.name}"
    
    def create_email(self): #Instance method
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls): #Classs method
        return MyName("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!"): #Static method
        return f"You say: {message}"


print("Let's Start!")
names = ["Bohdan", "Marta", None]
for name in names:
    me = MyName(name)
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} 
This is {type(MyName.whoami)}: {me.whoami} 
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
{"<*>"*20}""")

print("We are done.")

```
</details>

1. :star: вкажіть у звіті що вивела пограма або зробіть скріншот та вставте у звіт;
1. ознайомтесь з кодом та зрозумійте за що відповідає кожен з рядків;
1. Модифікуйте програму додавши своє імя в список;
1. :star: дайте відповідь на запитання: 
    - Чому коли передаємо значення `None` створюється обєкт з іменем `Anonymous`?
    - Як змінити текст привітання при виклику методу `say_hello()`? Допишіть цю частину коду.
    - Допишіть функцію в класі яка порахує кількість букв і імені (підказка: використайте функцію `len()`);

---

### Здача роботи
- :star: коли робота завершена та всі файли завантажено до репозиторію перейдіть у Веб-браузер та скопіюйте URL посилання на вашу роботу;
- :star: відправте URL посилання як відповідь на запитання до завдання у Google Classroom;
- :star: після того як Викладач перевірить роботу, Ви отримаєте оцінку у Google Classroom;
---