Вопросы с выбором варианта: 78/78%  
# Вопрос 1. Блок 4. CSS: селекторы, каскад, специфичность, базовые стили
  
### Содержание и вопросы

- Как подключается CSS?
- Что такое селекторы по тегу и по классу?
- Почему класс предпочтительнее id для стилизации?
- Что такое каскад и почему “побеждает” одно правило?

### Материал (лаконично)

- `styles.css` это отдельный файл со стилями. Он подключается в `head`.
- Селекторы:
  - по тегу. Применяются ко всем элементам этого типа
  - по классу. Применяются только там, где ты добавил класс. Это удобнее для проекта
- Каскад это ситуация, когда несколько правил подходят к одному элементу. Тогда “побеждает” более конкретное правило.
- Специфичность в простом виде:
  - id обычно сильнее класса
  - класс сильнее тега
- Для обучения и для маленьких проектов лучше опираться на классы. Так проще поддерживать верстку.
  
Варианты ответов:
1) ✅ Прочитано
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
#  Вопрос 2. Практическое задание (Блок 4)
  
### Условия

Сделай базовый стиль страницы пошагово:

1. В `styles.css` добавь стиль для страницы целиком (например, для корневого элемента страницы):
   - задай шрифт
   - задай цвет текста
   - задай фон
2. Добавь стиль для ссылок:
   - задай цвет
   - убери или добавь подчеркивание
3. В HTML добавь классы:
   - общий контейнер для содержимого
   - класс для секций
   - класс для карточек проектов
4. В CSS создай правила для этих классов:
   - контейнер. Ограничь ширину и выровняй по центру
   - секции. Добавь вертикальные отступы
   - карточки. Добавь внутренние отступы и рамку или фон

Ограничения:

- Не используй id для стилизации.
- Не используй inline-style.

### Псевдокод решения

```text
IN CSS_FILE
  STYLE PAGE_ROOT
    SET FONT
    SET TEXT_COLOR
    SET BACKGROUND

  STYLE LINKS
    SET LINK_COLOR
    SET DECORATION

  DEFINE CLASS_CONTAINER
    SET MAX_WIDTH
    SET HORIZONTAL_CENTERING

  DEFINE CLASS_SECTION
    SET VERTICAL_SPACING

  DEFINE CLASS_CARD
    SET PADDING
    SET BORDER_OR_BACKGROUND
END
```

### Если использовал ИИ, обязательные изменения вручную

- Добавь отдельный класс-модификатор для одной карточки и сделай заметное отличие.
- Убери хотя бы одно лишнее правило и объясни, почему оно не нужно.

---

**Вставь решение в комментарий ниже:**
  
### Ответ
<!DOCTYPE html>  
<html lang="ru">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>Визитка | Стилизация</title>  
    <link rel="stylesheet" href="styles.css">  
</head>  
<body>  
  
    <header class="header page-container">  
        <img src="https://via.placeholder.com" alt="Аватар" class="avatar">  
        <h1>Алексей Технологов</h1>  
    </header>  
  
    <main class="page-container">  
        <!-- Класс main-section для всех секций -->  
        <section class="main-section">  
            <h2>Навыки</h2>  
            <ol>  
                <li>HTML5 / CSS3</li>  
                <li>JavaScript</li>  
                <li>Git</li>  
            </ol>  
        </section>  
  
        <section class="main-section">  
            <h2>Проекты</h2>  
            <div class="projects-grid">  
                <!-- Обычная карточка -->  
                <article class="project-card">  
                    <h3>Проект Один</h3>  
                    <p>Простое описание проекта.</p>  
                    <a href="#">Ссылка</a>  
                </article>  
  
                <!-- Карточка с модификатором card-featured (Ручное изменение) -->  
                <article class="project-card card-featured">  
                    <h3>Лучший Проект</h3>  
                    <p>Этот проект выделен как особенный.</p>  
                    <a href="#">Ссылка</a>  
                </article>  
  
                <article class="project-card">  
                    <h3>Проект Три</h3>  
                    <p>Еще один пример работы.</p>  
                    <a href="#">Ссылка</a>  
                </article>  
            </div>  
        </section>  
    </main>  
  
    <footer class="footer page-container">  
        <p>Контакты: <a href="mailto:alex@example.com" class="footer-link">alex@example.com</a></p>  
    </footer>  
  
</body>  
</html>  
  
  
  
css  
/* 1. Стиль для страницы целиком */  
body {  
    font-family: 'Segoe UI', sans-serif;  
    color: #2c3e50;  
    background-color: #f0f2f5;  
    line-height: 1.5; /* Удалил лишнее: margin: 0 здесь не нужен, если есть сброс */  
}  
  
/* 2. Стиль для ссылок */  
a {  
    color: #3498db;  
    text-decoration: none; /* Убираем подчеркивание */  
    font-weight: bold;  
}  
  
a:hover {  
    text-decoration: underline; /* Возвращаем при наведении для удобства */  
}  
  
/* 3. Контейнер: ширина и центрирование */  
.page-container {  
    max-width: 800px;  
    margin: 0 auto;  
    padding: 0 20px;  
}  
  
/* 4. Секции: вертикальные отступы */  
.main-section {  
    padding: 40px 0;  
    border-bottom: 1px solid #ddd;  
}  
  
/* 5. Карточки: внутренние отступы и фон */  
.project-card {  
    background: #ffffff;  
    padding: 20px;  
    margin-bottom: 15px;  
    border-radius: 8px;  
    border: 1px solid #e1e4e8;  
}  
  
/* Класс-модификатор (Ручное изменение) */  
.card-featured {  
    border: 2px solid #e67e22; /* Выделяем рамкой */  
    background-color: #fffaf0; /* И легким фоном */  
    transform: scale(1.02);    /* Чуть увеличиваем визуально */  
}  
  
.footer {  
    text-align: center;  
    padding: 30px 0;  
    font-size: 0.9rem;  
}  
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 3. Где должны находиться CSS-стили согласно правилам этого занятия?
  
  
Варианты ответов:
1) Только в браузере
2) Только в `title`
3) Только в картинках
4) Только внутри `body`
5) ✅ Только в `styles.css`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 4. Что делает CSS-селектор по тегу, например `p` (применяется ко всем абзацам на странице)?
  
  
Варианты ответов:
1) Меняет только картинки
2) Меняет только один элемент
3) ✅ Меняет все `p` на странице
4) Меняет только `header`
5) Меняет только ссылки
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 5. Почему стилизация через классы часто удобнее, чем через теги?
  
  
Варианты ответов:
1) ✅ Так легче выбирать нужные элементы
2) Так не нужен `head`
3) Так не нужен `body`
4) Так отключаются отступы
5) Так включается JavaScript
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 6. Что такое каскад в CSS простыми словами (когда несколько правил применяются к одному элементу)?
  
  
Варианты ответов:
1) Список тегов в HTML
2) Способ вставки картинок
3) ✅ Правила могут перекрывать друг друга
4) Способ добавить мета-теги
5) Способ рисовать таблицы
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 7. Какой селектор обычно “сильнее” по специфичности (имеет приор приоритет при применении стилей)?
  
  
Варианты ответов:
1) тег сильнее id
2) ✅ id сильнее класса
3) пробел сильнее селектора
4) любой текст сильнее CSS
5) комментарий сильнее правила
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 8. Что запрещено использовать при работе со стилями в этом блоке?
  
  
Варианты ответов:
1) Классы в HTML
2) Файл `styles.css`
3) ✅ Inline-style в HTML
4) Тег `section`
5) Тег `link`
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 9. Зачем создавать класс-модификатор для одной карточки проекта?
  
  
Варианты ответов:
1) Чтобы удалить карточку
2) Чтобы сломать сетку
3) ✅ Чтобы показать вариант оформления
4) Чтобы отключить ссылки
5) Чтобы заменить HTML на CSS
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
