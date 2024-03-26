# Автоматизація за допомогою GitHub Actions
> Налаштувати автоматизацію можна через графічний інтерфейс або вручну написавши кроки у файлі `yml`. Ми спробуємо зробити це використовуючи обидва методи.

### Створення першого Workflow з шаблону
1. Створіть базовий шаблон для Github Actions через графічний інтерфейс та обравши наперед визначені Workflow;
1. Зайдіть у вкладку `Actions`, знайдіть шаблон `Python application` та натисніть кнопку `Configure`. У Вас відкриється файл для редагування;
1. За бажанням змініть назву файлу на власну назву у змінній `name`, решту залишимо без зміни, та просто закомітьте даний файл до репозиторію натиснуши в правому кутку кнопку `Start Commit` та написавши повідомлення;
2. :star: Ознайомтесь з файлом та копентаріями до нього (вони англійькою мовою, однак легко зрозумілі);
3. Переконайтесь що у вкладці `Actions` відображається новий Workflow;

---
### Редагування Workflow
1. Ознайомтесь що робить шаблонний Workflow `Python application` на кожному кроці;
1. Модифікуємо один із кроків щоб він перевіряв наш python код. Для цього просто створимо крок який запустить пайтон файл що знаходиться в одній і папок лабораторних робіт.
    ```yml
    - name: Run Python # Це просто назва кроку
      run: |
        python ./lab.py # Запускаємо Пайтон файл який знаходиться у кореневій папці
    ```

2. :star: Cтворіть крок який запустить код програми написаного на попередніх заняттях;
3. Для зручності роботи у Vusial Studio можна поставити плагін `GitHub Actions` що дозволить підсвітку коду та автодоповнення;

---
### Запуск Workflow вручну та по Cron
1. Будь яку дію можна запускати вручну або налаштувати запуск у певний час. Для цього потрібно модифікувати файл `./github/workflows/actions.yml` (якщо Ви його переназвали він буде мати іншу назву, але шлях залишиться незмінним). Для створення тригеру запуску має бути присутня директива [`on:`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on). 
1. Щоб зробити запуск ручним побрібно додати директиву [`workflow_dispatch`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs):
    ```yml
    on:
        workflow_dispatch
    ```
1. :star: при ручному запуску є можливість передавати вхідні параметри. Зверніться до документації та передайте один параметр у Workflow;
1. При запуску у певний час використовується директива [`schedule`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onschedule). Викликів може бути один або декілька тому далі потрібно правильно налаштувати опцію `cron` яка може бути правильно підібрана за допомогою [CronTab GURU](https://crontab.guru/). Скориставшись даним сайтом задамо виконання раз на день о 9 ранку, для прикладу:
    ```yml
    on:
        schedule:
           - cron: '0 9 * * *'
    ```
2. :star: Задайте час виконання на вибраний день в тижні та виберіть іншу годину. Виконайте Workflow лише один раз щоб не використовувати безкоштовні хвилини!

---
### Створення декількох Workflow або завдань 
1. Якщо у репозиторії є декілька файлів e `./github/workflows/` тоді кожен з них буде окремим Workflow.  
2. :star: Створіть два файли з різними іменами та змініть назву Workflow через значення змінної `name`. Помістіть у звіт скріншот що відображає Ваші Workflow у вкладці `Actions`.
3. Кожен воркфлов може мати одне та більше завдань [`job`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobs). Для цього просто треба задати декілька назв завдань при описі Workflow.
```yml
jobs:
    name_one:
        name: Run first Job
        steps:
            - name: First
              run: echo "First"
    name_two:
        name: Run Second Job 
        steps:
            - name: Second
              run: echo "Second"
```
4. :star: Створіть свої завдання та виконайте їх. Представте скріншот з результатами.

---
### Перевірка умов для запуску завдань або кроків
1. Кожне завдання/крок може містити умову при якій він виконується. Для цього потрібно вказати директиву [`if:`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idif). Для прикладу, якщо ми передамо параметер за замовчуванням 'Executer' то можемо пропустити цей крок:
```yml
- name: Send greeting  # Виконуємо привітання тільки коли передано Імя
  run: echo "Hello ${{ github.event.inputs.name }}"
  if: github.event.inputs.name != 'Executer'
```
1. :star: Спробуйте зробити свою умову та виконати/пропустити якийсь крок або завдання.

---
### Баджі та статуси
1. `README.md` файли завжди використовуються на головній сторінці репозиторію і зазвичай поміж описом самого репозиторію там знаходяться Баджі/Статуси які вказують результат виконання CI/CD систем. Оскільки в нас вже є декілька Workflow давайте зробимо Баджі.
2. Перейдіть у вкладку `Actions`, виберіть Workflow (для прикладу `Manual workflow`) та у правому кутку натисніть на `...` звідки вийде меню де треба обрати `Create status badge`. Скопіюйте згенерований Markdown код та вставте в першу стрічку `README.md`. Для прикладу мій Workflow буде виглядати наступним чином:
 
  [![Manual workflow](https://github.com/BobasB/it_college/actions/workflows/manual.yml/badge.svg)](https://github.com/BobasB/it_college/actions/workflows/manual.yml)

---
### Інтеграція з Coverage (Додатково)
1. Перейдіть на сайт [codecov.io](https://about.codecov.io/) та здійсніть вхід (`Login`) за допомогою аккаунту GitHub.
2. Створіть крок Workflow у файлі `./github/workflows/actions.yml` який буде інсталювати необхадні пакети Python. Крок додаються у секції `steps`:
    ```yml
    # встановлюємо Python пакети
    - name: Install dependencies
      run: |
        pip install pytest coverage
    ```
3. Створіть крок який буде виконувати тести.
    ```yml
    # встановлюємо Python пакети
    - name: Install dependencies
      run: |
        pcd example/coverage_io/
        pytest test.py -v
    ```
4. Додаємо два кроки, перший крок який створює звіт та другий відсилає його в Coverage. Якщо тести знаходяться не в кореневій папці, не вказати правильний шлях або перейти в правильну папку. У даному прикладі тести знаходяться у папці `example/coverage_io/`:
    ```yml
    # генеруємо звіт
    - name: Generate Report
      run: |
        cd example/coverage_io/
        coverage run -m unittest -v
        coverage xml
    # відсилаємо його в Coverage
    - name: Upload Coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        directory: example/coverage_io/ 
    ```
5. Запустіть Workflow через вкладку `Actions` та переконайтесь що кроки виконались.
6. Додайте Бадж з результатами покриття. На сайті [codecov.io](https://about.codecov.io/) перейдіть у потрібний репозиторій, виберіть вкладку `Settings -> Badges & Grapth` та скопіюйте йже готовий Бадж у форматі Markdown. Вставте скопійований Бадж у README файл. Результат представлений внизу:

    [![codecov](https://codecov.io/gh/BobasB/it_college/branch/main/graph/badge.svg?token=QIL2SPR92K)](https://codecov.io/gh/BobasB/it_college)

---
### Здача роботи
- :star: коли робота завершена та всі файли завантажено до репозиторію перейдіть у Веб-браузер та скопіюйте URL посилання на вашу роботу;
- :star: відправте URL посилання як відповідь на запитання до завдання у Google Classroom;
- :star: після того як Викладач перевірить роботу, Ви отримаєте оцінку у Google Classroom;

---
