result: 70/100

### 1. Формулировка задания
Создать функцию `collect_stats`, которая:
- Принимает произвольное количество позиционных (`*args`) и именованных (`**kwargs`) числовых аргументов.
- Возвращает словарь с ключами: `count` (общее количество чисел), `sum` (сумма), `max` (максимум), `min` (минимум).
- Корректно обрабатывает вызов без аргументов (возврат `count=0`, `sum=0`, `max=None`, `min=None`).
- Функция `unpack_and_call` должна принимать список и словарь, распаковывать их и вызывать `collect_stats`.

**Ограничения:**
- Запрещено использовать циклы для обхода `args`/`kwargs` (только встроенные функции).
- Требуется использовать распаковку (`*`, `**`).

---

### 2. Результаты проверки
**Файл:** `tasks/3/Trudno` (строки 1-18)

**Тестирование:**
1. **Проверка `collect_stats` с аргументами:**
   ```python
   collect_stats(10, 20, 30, temp=15, pressure=1013)
   ```
   Результат: `{'count': 5, 'sum': 1088, 'max': 1013, 'min': 10}` (корректно).

2. **Проверка `collect_stats` без аргументов:**
   ```python
   collect_stats()
   ```
   Результат: `{'count': 0, 'sum': 0, 'max': None, 'min': None}` (корректно).

3. **Проверка `unpack_and_call`:**
   ```python
   unpack_and_call([5, 15, 25], {'reading': 100, 'offset': -5})
   ```
   **Ошибка:** Код после `return` в функции `unpack_and_call` не выполняется. Примеры вызовов и `print` находятся после `return`, что делает их недостижимыми.

---

### 3. Сильные стороны работы
- **Корректность:** Основная логика `collect_stats` реализована верно: обработка `args`/`kwargs`, расчёт статистики, обработка пустого ввода.
- **Читаемость:** Имена переменных (`numbers`, `list_of_numbers`, `dict_of_numbers`) соответствуют PEP8.
- **Архитектура:** Использование встроенных функций (`sum`, `max`, `min`) вместо циклов соответствует требованиям.

---

### 4. Ошибки
#### Блокирующие (снижение оценки на 30%)
- **Недостижимый код в `unpack_and_call`:**
  ```python
  def unpack_and_call(list_of_numbers, dict_of_numbers):
      return collect_stats(*list_of_numbers, **dict_of_numbers)
      # Весь код ниже return никогда не выполнится!
      my_list = [5, 15, 25]
      my_dict = {'reading': 100, 'offset': -5}
      result = unpack_and_call(my_list, my_dict)
      print("Результат второго примера:", result)
      result = collect_stats()
      print("Результат третьего примера:", result)
  ```
  **Исправление:** Удалить лишний код или переместить его вне функции:
  ```python
  def unpack_and_call(list_of_numbers, dict_of_numbers):
      return collect_stats(*list_of_numbers, **dict_of_numbers)
  
  # Примеры вызовов (в глобальной области видимости):
  my_list = [5, 15, 25]
  my_dict = {'reading': 100, 'offset': -5}
  result = unpack_and_call(my_list, my_dict)
  print("Результат второго примера:", result)
  result = collect_stats()
  print("Результат третьего примера:", result)
  ```

---

### 5. Оценка
- **Функциональность: 35/50**  
  Основная логика работает, но `unpack_and_call` содержит нерабочий код (снижено 15 баллов).
- **Качество кода: 25/30**  
  Ошибка с недопустимым расположением кода (снижено 5 баллов).
- **Стиль и тесты: 10/20**  
  Примеры вызовов не оформлены как тесты (снижено 10 баллов).

**Итог:** 70/100. Снижение за блокирующую ошибку и некорректное тестирование.

---

### 6. Вариант полного решения
```python
def collect_stats(*args, **kwargs):
    numbers = list(args) + list(kwargs.values())
    if not numbers:
        return {'count': 0, 'sum': 0, 'max': None, 'min': None}
    return {
        'count': len(numbers),
        'sum': sum(numbers),
        'max': max(numbers),
        'min': min(numbers)
    }

def unpack_and_call(num_list, num_dict):
    return collect_stats(*num_list, **num_dict)

# Примеры использования (для тестирования):
if __name__ == "__main__":
    # Пример 1
    result1 = collect_stats(10, 20, 30, temp=15, pressure=1013)
    print("Пример 1:", result1)
    
    # Пример 2
    my_list = [5, 15, 25]
    my_dict = {'reading': 100, 'offset': -5}
    result2 = unpack_and_call(my_list, my_dict)
    print("Пример 2:", result2)
    
    # Пример 3
    result3 = collect_stats()
    print("Пример 3:", result3)
```

---

Анализ выполнен моделью: GPT-4o.
