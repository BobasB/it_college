# Налаштування робочого середовища
> Перед початком роботи потрібно встановити Git, Python та редактор коду і переконатись, що все працює. Без цього наступні лабораторні виконати неможливо.

## Мета роботи
Встановити та перевірити інструменти, необхідні для курсу: Git, Python 3.13+, Visual Studio Code, акаунт GitHub.

## Що потрібно знати / підготувати
- доступ до інтернету та права на встановлення програм на комп'ютері;
- електронна пошта для реєстрації на GitHub;

---
## Хід роботи

### 1. Встановлення програм
#### Windows
1. [Git for Windows](https://git-scm.com/download/win) — уважно оберіть розрядність системи (32/64 біт);
1. [Python 3.13+](https://www.python.org/downloads/windows/) — під час встановлення **обов'язково** поставте галочку `Add python.exe to PATH`;
1. [Visual Studio Code](https://code.visualstudio.com/) (Community edition).

> [!IMPORTANT]
> Якщо у вас 32-бітна система, потрібна старіша версія VS Code: https://update.code.visualstudio.com/1.83.1/win32/stable

#### macOS / Linux
1. Git і Python зазвичай можна встановити через пакетний менеджер (`brew install git python` на macOS; `sudo apt install git python3 python3-venv python3-pip` на Ubuntu/Debian);
1. Visual Studio Code: https://code.visualstudio.com/;
1. На macOS/Linux команда запуску Python — `python3`, якщо `python` не знайдено.

### 2. Перевірка встановлення
1. Відкрийте термінал (у VS Code: `Terminal` → `New Terminal`) і виконайте:
    ```bash
    git --version
    python --version
    pip --version
    code --version
    ```
1. :star: Вкажіть у звіті версії Git та Python (скріншот терміналу або текст виводу).

> [!WARNING]
> Якщо термінал повідомляє `command not found` або `'python' is not recognized` — Python не додано до `PATH`. Перевстановіть його із галочкою `Add python.exe to PATH` та перезапустіть термінал.

### 3. Акаунт GitHub
1. Зареєструйте новий акаунт на [GitHub.com](https://github.com/);
1. Підтвердіть електронну пошту;
1. :star: Вкажіть у звіті ім'я свого акаунту.

> [!IMPORTANT]
> Якщо потрібно скинути збережені облікові дані GitHub на Windows, прочитайте https://stackoverflow.com/questions/15381198/remove-credentials-from-git

### 4. Перший запуск Python
1. Створіть будь-який файл `hello.py` із рядком `print("Hello, IT College!")`;
1. У VS Code відкрийте `Extensions` та встановіть розширення `Python` від Microsoft (`ms-python.python`);
1. Запустіть `hello.py` командою `python hello.py` та кнопкою `Run Python File` у VS Code;
1. :star: Вкажіть у звіті результат запуску.

---
## Критерії оцінювання
| Рівень | Що потрібно виконати |
| --- | --- |
| Достатній | встановлено Git, Python, VS Code; версії підтверджені у звіті |
| Високий | + створено акаунт GitHub та запущено `hello.py` двома способами |
| Відмінний | + налаштовано `git config` (ім'я та email) та описано, як виправили помилки встановлення, якщо вони були |

## Контрольні питання
1. Для чого потрібен Git і чим він відрізняється від GitHub?
1. Що таке `PATH` і чому від нього залежить запуск `python`?
1. Як перевірити версію встановленого Python?

---
