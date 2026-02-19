Вопросы с выбором варианта: 56/78%  
# Вопрос 1. Блок 3. Текстовый контент, ссылки, списки, изображения
  
### Содержание и вопросы

- Как сделать ссылку и какие бывают `href`?
- Чем `ul` отличается от `ol`?
- Зачем нужен `alt` у изображения?
- Как структурировать “карточку” проекта только HTML-ом?

### Материал (лаконично)

- Ссылка это тег `a`. Внутри должен быть текст, по которому понятно, куда ведет ссылка.
- `href` может быть:
  - обычным адресом сайта
  - якорем внутри страницы
  - `mailto:` для письма
- Списки:
  - `ul` когда порядок не важен, например “навыки”
  - `ol` когда это шаги, порядок важен
- Картинка это `img`. `alt` обязателен. Если картинка не загрузится, текст `alt` подскажет, что там должно быть.
- “Карточка” проекта это просто блок. Обычно внутри: заголовок, текст, ссылка.
  
Варианты ответов:
1) ✅ Прочитано
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 2. Практическое задание (Блок 3)
  
### Условия

Добавь контент в `index.html` пошагово:

1. В одной из секций добавь заголовок и под ним список.
2. Заполни список из 5 пунктов.
3. В секции с проектами создай контейнер для карточек.
4. Создай минимум 3 карточки. В каждой карточке сделай:
   - заголовок карточки
   - короткий текст-описание
   - ссылку
5. В шапке добавь изображение-аватар.
6. В подвале сделай блок контактов и добавь минимум 3 ссылки.
7. Проверь, что у всех `img` есть `alt`, а у всех `a` есть `href`.

Проверка:

- Все ссылки кликабельны.
- Все изображения имеют `alt`.

### Псевдокод решения

```text
IN SECTION_B
  CREATE LIST
    ADD LIST_ITEM (REPEAT 5 TIMES)

IN SECTION_C
  CREATE CARDS_CONTAINER
    REPEAT 3 TIMES
      CREATE CARD
        ADD CARD_TITLE
        ADD CARD_TEXT
        ADD CARD_LINK

IN HEADER
  ADD IMAGE_WITH_ALT

IN FOOTER
  CREATE CONTACTS_LIST
    ADD LINK_ITEM (REPEAT 3 TIMES)
END
```

### Если использовал ИИ, обязательные изменения вручную

- Замени один тип списка на другой (например, `ul` на `ol` или наоборот) и объясни почему это подходит.
- Добавь еще одну ссылку с другим типом `href` (например, `mailto:`).

---

**Вставь решение в комментарий ниже:**
  
### Ответ
<!DOCTYPE html>  
<html lang="ru">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Визитка Специалиста | Контент</title>  
    <link rel="stylesheet" href="styles.css">  
</head>  
<body>  
  
    <header class="header">  
        <div class="container">  
            <!-- Добавлено изображение-аватар -->  
            <img src="https://via.placeholder.com" alt="Аватар Алексея Технологова" class="avatar">  
            <h1>Алексей Технологов</h1>  
            <p>Создаю цифровые решения для вашего бизнеса</p>  
        </div>  
    </header>  
  
    <main class="content-wrapper">  
  
        <section id="skills" class="section">  
            <h2>Мои компетенции</h2>  
            <!-- Использован нумерованный список (ol) -->  
            <ol>  
                <li>Адаптивная верстка (HTML/CSS)</li>  
                <li>Работа с сетками Flexbox и Grid</li>  
                <li>Основы JavaScript и DOM</li>  
                <li>Оптимизация скорости загрузки</li>  
                <li>Работа с Git и GitHub</li>  
            </ol>  
        </section>  
  
        <section id="projects" class="section">  
            <h2>Мои проекты</h2>  
            <div class="cards-container">  
                <!-- Карточка 1 -->  
                <article class="card">  
                    <h3>Сайт-портфолио</h3>  
                    <p>Чистая верстка для личного бренда художника.</p>  
                    <a href="https://github.com">Смотреть код</a>  
                </article>  
  
                <article class="card">  
                    <h3>Интернет-магазин</h3>  
                    <p>Прототип главной страницы с корзиной товаров.</p>  
                    <a href="https://github.com">Смотреть демо</a>  
                </article>  
  
                <article class="card">  
                    <h3>Блог о путешествиях</h3>  
                    <p>Адаптивный шаблон для статей с галереей.</p>  
                    <a href="https://github.com">Открыть проект</a>  
                </article>  
            </div>  
        </section>  
  
        <section class="section">  
            <h2>Коротко обо мне</h2>  
            <p>Люблю технологии и постоянно учусь новому в мире фронтенда.</p>  
        </section>  
  
    </main>  
  
    <footer class="footer">  
        <div class="container">  
            <div class="contacts">  
                <h3>Связаться со мной:</h3>  
                <!-- Ссылки в футере -->  
                <a href="https://t.me">Telegram</a> |  
                <a href="https://linkedin.com">LinkedIn</a> |  
                <!-- Ссылка типа mailto (ручное изменение) -->  
                <a href="mailto:Dreakins@example.com">Написать на почту</a>  
            </div>  
            <p>2024 &copy; Все права защищены</p>  
        </div>  
    </footer>  
  
</body>  
</html>  
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 3. Какой HTML-тег используется для создания обычной ссылки на другую страницу?
  
  
Варианты ответов:
1) `p`
2) `span`
3) `img`
4) ✅ `a`
5) `div`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 4. Какой тип списка лучше подходит для раздела “навыки”, где порядок элементов не имеет значения?
  
  
Варианты ответов:
1) `nav`
2) `table`
3) `form`
4) ✅ `ul`
5) `ol`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 5. Зачем нужен атрибут `alt` у тега изображения `img`?
  
  
Варианты ответов:
1) Для создания отступов
2) ❌ Для изменения размера картинки
3) Для выравнивания текста
4) Для подключения CSS
5) Для текстового описания картинки
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 6. Какое значение атрибута `href` используется для создания ссылки, которая открывает почтовую программу?
  
  
Варианты ответов:
1) `file:`
2) `css:`
3) `mailto:`
4) ❌ `http:`
5) `ftp:`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 7. Какие элементы обычно должны быть внутри “карточки проекта” на странице-визитке?
  
  
Варианты ответов:
1) Только `meta` теги
2) Только картинка без текста
3) Только `script` код
4) Только таблица с данными
5) ✅ Заголовок, текст, ссылка
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 8. Что нужно проверить после добавления ссылок и изображений на страницу?
  
  
Варианты ответов:
1) Что нет `section`
2) ✅ Что все ссылки имеют `href`
3) Что `head` пустой
4) Что нет `footer`
5) Что нет `main`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 9. Какое главное требование к тексту внутри ссылки для удобства пользователей?
  
  
Варианты ответов:
1) ✅ Чтобы он был понятным
2) Чтобы он был скрыт стилями
3) Чтобы он был только цифрами
4) Чтобы он был пустым
5) Чтобы он был на одной букве
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
