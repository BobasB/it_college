# Знайомство з ООП

### Створюємо перший class
1. Створіть два python файли: для Ноутбука з розширенням `.ipynb` та для скрипта з розширенням `.py`;
1. Скопіюйте Python наведений внизу у Ваші файли та виконайте їх натиснувши `Run Python File` (трикутник :arrow_forward:); 
<details><summary>Python Code</summary>

### Перша програма на ООП
```python
class MyName:
    def __init__(self, name="NoName") -> None:
        self.name = name # Class attributes
    
    @property
    def whoami(self): #Class property
        return f"My name is {self.name}"
    
    def create_email(self): #Classs method
        return f"{self.name}@itcollege.com"

me = MyName("Bohdan")
print(f"""
This is object: {me} 
This is attribute: {me.name} 
This is property: {me.whoami} 
This is method call: {me.create_email()}
""")
```
</details>

---