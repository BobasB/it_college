# Створення портфоліо за допомогою GitHub Pages
> GitHub Pages - дозволяє безплатно розміщати статичні WEB сторінки які найкраще підходять для портфоліо.

## Мета роботи
Опублікувати власний статичний сайт-портфоліо (резюме) на GitHub Pages, налаштувати його вигляд через `_config.yml` та тему Jekyll.

## Що потрібно знати / підготувати
- виконана робота [«GitHub і Markdown»](../02_github_repository/README.md): публічний репозиторій із `README.md`;
- приклад конфігурації: [_config.yml](../../_config.yml) цього репозиторію (тема `midnight`);

---
### Включаємо GitHub Pages
1. Для того щоб включити GitHub Pages, перейдіть у `Settings` далі виберіть `Pages`. У розділі `Build and deployment` оберіть `Source: Deploy from a branch`, гілку `main`, папку `/ (root)` та натисніть Save.
2. Згідно з документацією GitHub сайт буде доступний в межах 10 хв. Посилання на сайт буде зверху сторінки конфігурації, або можна самому здогадатись URL адресу яка буде у форматі `username.github.io/repository_name`.
3. Оскільки, у нашого репозиторія вже є файли `README.md` він і буде відображатись як вихідний матеріал для нашого сайту. Також якщо форматування Markdown мітить гіперлінки на інші `*.md` файли у нашому репозиторію - вони також будуть відображатись як сторінки сайту.

---
### Змінюємо вигляд сайту
1. Опублікований сайт можна кастомізувати та змінювати його вигляд. Для цього потрібно додати у кореневу папку файл `_config.yml`. У ньому можна вказувати [певні директиви які описані в документації](https://docs.github.com/en/pages/quickstart).
2. Для прикладу, ми можемо змінити заголовок та опис нашого сайту. Для цього додайте наступну конфігурацію та зробіть коміт:
    ```yml
    title: Portfolio Example
    description: Shows how to create portfolio for students.
    ```
3. Через дякілька хвилин всі зміни будуть доступні на сайті. Всі зміни виконуються за допомогою Github Actions. Для того щоб подивитись його статус, перейдіть у вкладку `Actions` в якій повинен бути новий новий Workflow `pages-build-deployment`. Цей Workflow відповідає за деплоймент найого сайту і буде виконуватись при кожному коміті.
4. Для більш привабливої кастомізації сайту можна використати Теми. [Для цього скористаємось документацією.](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll) Для прикладу виберемо тему яка називається [midnight](https://github.com/pages-themes/midnight). Конфігурація вказана на офіційній сторінці. Приклад `_config.yml` з темою (як у цьому репозиторії):
    ```yml
    title: Portfolio Example
    description: Shows how to create portfolio for students.
    remote_theme: pages-themes/midnight@v0.2.0
    plugins:
      - jekyll-remote-theme
    ```
5. Використовуйте AI/Copilot щоб наповнити сторінки та зробити їх більш привабливішими. Запитайте AI/Copilot як би він оформив головну сторінку та що написав би у файлі `README.md`.

> [!WARNING]
> Якщо сайт показує 404 або старий вміст: перевірте вкладку `Actions` (Workflow `pages-build-deployment` має бути зеленим), що файл називається саме `README.md` або `index.md` і що репозиторій публічний. Зміни можуть з'являтись із затримкою до 10 хвилин.

---
### Тема-резюме: готовий шаблон портфоліо
Окрім загальних тем (`midnight`), існують теми для резюме. Тема [`sproogen/resume-theme`](https://github.com/sproogen/modern-resume-theme) будує сторінку-резюме з розділами «Про мене», «Проєкти», «Досвід», «Освіта» прямо з файлу `_config.yml` — програмувати HTML не потрібно:
```yml
remote_theme: sproogen/resume-theme
plugins:
  - jekyll-seo-tag
  - jekyll-remote-theme

name: Ім'я Прізвище
title: Junior Python Developer
email: your_email@example.com
github_username: your-github-login
darkmode: true

about_title: Про мене
about_content: |
  Привіт! Я навчаюсь у Львівському ІТ Коледжі та вивчаю Python.

  Найкраще вмію: <mark>Python</mark>, <mark>Git</mark>.

content:
  - title: Проєкти
    layout: list
    content:
      - layout: top-middle
        title: Бібліотека (ООП-проєкт)
        link: github.com/your-github-login/your-repo
        quote: >
          Симуляція видачі книг студентам з тестами та UML-діаграмою.
        description: |
          Використано класи, `Enum`, `pytest`.

  - title: Освіта
    layout: list
    content:
      - layout: left
        title: Львівський ІТ Коледж
        caption: 2024 - 2028
        sub_title: Комп'ютерні науки
        description: |
          Python, ООП, тестування, бази даних.
```
1. Створіть окремий публічний репозиторій `cv` та додайте файл `_config.yml` з прикладом вище (замініть дані на власні) і порожній `index.md` із рядками `---` та `layout: default` (front matter):
    ```markdown
    ---
    layout: default
    ---
    ```
1. Увімкніть GitHub Pages для репозиторію (див. вище) та дочекайтесь публікації;
1. :star: Додайте у резюме мінімум 2 проєкти з посиланнями на репозиторії лабораторних (наприклад, ООП-проєкт або агента) та розділ «Навички»;
1. :star: Додайте скріншот опублікованої сторінки та URL у звіт.

> [!WARNING]
> У резюме, що доступне всім в інтернеті, не вказуйте домашню адресу, телефон та інші особисті дані, які не потрібні роботодавцю. Достатньо імені, електронної пошти й профілю GitHub/LinkedIn.

---
### Публікація через GitHub Actions (власний Workflow)
За замовчуванням GitHub сам збирає сайт (`pages-build-deployment`). Якщо потрібен контроль над збіркою, у `Settings` → `Pages` → `Build and deployment` оберіть `Source: GitHub Actions` та додайте `.github/workflows/pages.yml`:
```yml
name: Deploy GitHub Pages

on:
  workflow_dispatch:           # ручний запуск; для автоматичного додайте push у гілку main

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/configure-pages@v6
      - uses: actions/jekyll-build-pages@v1
        with:
          source: ./
          destination: ./_site
      - uses: actions/upload-pages-artifact@v5

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v5
```
- збірка (`build`) та публікація (`deploy`) — окремі завдання, пов'язані через `needs`;
- `permissions` дозволяють Workflow публікувати сторінки;
- у `_config.yml` можна приховати від сайту зайві файли: `exclude: [".github/", "*.ipynb", "*.py", "Gemfile"]`; плагін `jekyll-relative-links` робить робочими відносні посилання на `.md` файли між сторінками.

1. :fire: Налаштуйте публікацію через Actions та покажіть у звіті зелений Workflow і посилання на сайт. Чим цей спосіб відрізняється від публікації «з гілки»?
1. :fire: Опублікуйте як сайт README-файли з ваших лабораторних: у `_config.yml` додайте `plugins: [jekyll-relative-links]` та `relative_links: {enabled: true, collections: true}`.

---
### Що має бути у звіті
- URL опублікованого сайту та скріншот його головної сторінки;
- вміст `_config.yml` та скріншот зеленого Workflow `pages-build-deployment`;
- короткий опис (3-5 речень), які розділи резюме ви додали і чому;
- висновок за [шаблоном](../../reports/README.md).

### Контрольні питання
1. Що таке статичний сайт і чим він відрізняється від динамічного?
1. Для чого потрібен файл `_config.yml`?
1. Що відбувається при кожному коміті в гілку, з якої публікується сайт?
1. Які персональні дані не варто публікувати в резюме на публічному сайті?

---
### Здача роботи
- :star: надішліть URL опублікованого сайту та URL репозиторію як відповідь на завдання у Google Classroom;

---
