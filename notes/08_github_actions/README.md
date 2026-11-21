# Автоматизація за допомогою GitHub Actions
> Налаштувати автоматизацію можна через графічний інтерфейс або вручну написавши кроки у файлі `yml`. Ми спробуємо зробити це використовуючи обидва методи.

## Мета роботи
Навчитись створювати та запускати Workflow у GitHub Actions: за шаблоном, вручну та за розкладом (cron), використовувати кілька завдань (`jobs`), умови (`if`), запускати тести та передавати звіт покриття у Codecov.

## Що потрібно знати / підготувати
- власний репозиторій на GitHub з кодом та тестами (див. [роботу №07](../07_testing/README.md));
- розуміння синтаксису YAML: відступи (лише пробіли, не табуляції) формують структуру файлу;
- безкоштовний ліміт хвилин Actions обмежений — не запускайте Workflow без потреби;

### Приклад із цього репозиторію
Робочі Workflow знаходяться у [.github/workflows](../../.github/workflows): [manual.yml](../../.github/workflows/manual.yml) (ручний запуск з параметром), [coverage.yml](../../.github/workflows/coverage.yml) (тести + coverage + Codecov) та [cron.md](../../.github/workflows/cron.md) (вимкнений запуск за розкладом, збережений для прикладу).

---
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
1. Будь яку дію можна запускати вручну або налаштувати запуск у певний час. Для цього потрібно модифікувати файл `.github/workflows/actions.yml` (якщо Ви його переназвали він буде мати іншу назву, але шлях залишиться незмінним). Для створення тригеру запуску має бути присутня директива [`on:`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#on). 
1. Щоб зробити запуск ручним потрібно додати директиву [`workflow_dispatch`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs):
    ```yml
    on:
      workflow_dispatch:
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
        runs-on: ubuntu-latest   # обов'язковий параметр: на якій машині виконується завдання
        steps:
            - name: First
              run: echo "First"
    name_two:
        name: Run Second Job 
        runs-on: ubuntu-latest
        needs: name_one          # необов'язково: виконати лише після name_one
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
### Запуск тестів у CI: тригери, матриця, залежності між завданнями
Головна користь Actions — автоматично запускати тести при кожній зміні коду. Повний приклад Workflow, який перевіряє два приклади з цього репозиторію на двох версіях Python:
```yml
name: Tests

on:
  push:
    branches: [main]
    paths: ["example/**"]     # запускати лише якщо змінились файли у example/
  pull_request:               # та при кожному Pull Request

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false        # не зупиняти інші комбінації, якщо одна впала
      matrix:
        project: [example/testing/02_pytest, example/testing/05_project_layout]
        python: ["3.10", "3.13"]
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-python@v7
        with:
          python-version: ${{ matrix.python }}
      - run: pip install pytest
      - name: Run tests
        working-directory: ${{ matrix.project }}   # аналог cd у shell
        run: python -m pytest -v

  report:
    needs: test               # виконається лише після успішного завершення всіх комбінацій test
    runs-on: ubuntu-latest
    steps:
      - run: echo "Усі тести пройшли"
```
- `matrix` створює окреме завдання для кожної комбінації значень (тут 2 × 2 = 4 запуски) — так перевіряють підтримку кількох версій Python;
- `needs` задає порядок: без нього завдання виконуються паралельно;
- `working-directory` задає папку, у якій виконуються команди кроку;
- `on.push.paths` та `branches` обмежують запуск, економлячи безкоштовні хвилини.

Якщо проєкт використовує Poetry (є `poetry.lock`), установіть його до `setup-python`, щоб увімкнути кеш залежностей:
```yml
      - run: pipx install poetry
      - uses: actions/setup-python@v7
        with:
          python-version: "3.13"
          cache: poetry
      - run: poetry install
        working-directory: notes/06_python_agents
```
Окремий скрипт теж можна запустити як крок (`run: bash ./scripts/check.sh` або `run: python scripts/check.py`) — зручно, коли перевірка складніша за одну команду.

> [!WARNING]
> Якщо Workflow не з'явився у вкладці `Actions`: перевірте, що файл лежить саме у `.github/workflows/` (з крапкою!), має розширення `.yml`/`.yaml` та коректні відступи. Помилку синтаксису GitHub показує на сторінці Workflow.

1. :star: Створіть Workflow, який запускає тести одного з прикладів на двох версіях Python через `matrix`, та додайте завдання `report` із `needs`. Додайте скріншот вкладки `Actions` у звіт;
1. :star: Навмисно зламайте тест, зробіть Pull Request і покажіть червоний статус перевірки. Виправте тест і покажіть зелений;
1. :fire: Додайте до Workflow крок `pip install flake8` та `flake8 .` і поясніть, чому перевірку стилю варто виконувати в CI.

---
### Баджі та статуси
1. `README.md` файли завжди використовуються на головній сторінці репозиторію і зазвичай поміж описом самого репозиторію там знаходяться Баджі/Статуси які вказують результат виконання CI/CD систем. Оскільки в нас вже є декілька Workflow давайте зробимо Баджі.
2. Перейдіть у вкладку `Actions`, виберіть Workflow (для прикладу `Manual workflow`) та у правому кутку натисніть на `...` звідки вийде меню де треба обрати `Create status badge`. Скопіюйте згенерований Markdown код та вставте в першу стрічку `README.md`. Для прикладу мій Workflow буде виглядати наступним чином:
 
  [![Manual workflow](https://github.com/BobasB/it_college/actions/workflows/manual.yml/badge.svg)](https://github.com/BobasB/it_college/actions/workflows/manual.yml)

---
### Інтеграція з Coverage (Додатково)
1. Перейдіть на сайт [codecov.io](https://about.codecov.io/) та здійсніть вхід (`Login`) за допомогою аккаунту GitHub.
2. Створіть крок Workflow у файлі `.github/workflows/actions.yml` який буде інсталювати необхідні пакети Python. Кроки додаються у секції `steps`:
    ```yml
    # встановлюємо Python пакети
    - name: Install dependencies
      run: |
        pip install pytest coverage
    ```
3. Створіть крок який буде виконувати тести.
    ```yml
    # запускаємо тести
    - name: Run tests
      run: |
        cd example/coverage_io/
        pytest test.py -v
    ```
4. Додаємо два кроки: перший створює звіт, другий відсилає його в Codecov. Якщо тести знаходяться не в кореневій папці, потрібно вказати правильний шлях або перейти в потрібну папку. У даному прикладі тести знаходяться у папці `example/coverage_io/`:
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
### Що має бути у звіті
- посилання на файли `.github/workflows/*.yml` та скріншот вкладки `Actions` з успішним запуском;
- скріншот логів кроку з вашим `run`;
- пояснення, як працюють `on`, `jobs`, `steps`, `if`;
- (додатково) бадж у `README.md` та результат Codecov.

### Контрольні питання
1. Що таке Workflow, Job та Step?
1. Які події (`on`) можуть запускати Workflow?
1. Чому YAML чутливий до відступів і що станеться, якщо використати табуляцію?
1. Як передати вхідний параметр у Workflow і використати його в умові `if`?
1. Чому не варто зберігати паролі й токени прямо в yml (див. `secrets`)?

> [!TIP]
> Актуальні версії дій (`actions/checkout`, `actions/setup-python`) шукайте на сторінці Releases відповідного репозиторію або в Marketplace; старі версії можуть видавати попередження про застарілість (наприклад, через стару версію Node.js).

---
### Здача роботи
- :star: коли робота завершена та всі файли завантажено до репозиторію перейдіть у Веб-браузер та скопіюйте URL посилання на вашу роботу;
- :star: відправте URL посилання як відповідь на запитання до завдання у Google Classroom;
- :star: після того як Викладач перевірить роботу, Ви отримаєте оцінку у Google Classroom;

---
