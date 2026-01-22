Время затраченное на выполнение: 0:21

result: 0/100

1) **Сильные стороны**
- Студент начал правильно с импорта `ABC` и `abstractmethod`.
- Создан абстрактный класс `NotificationChannel` с конструктором, принимающим `sender_name`.
- Метод `format_message` реализован точно по условию, возвращает строку в требуемом формате.

2) **Ошибки и недочёты**

**Блокирующие (ломает выполнение требований задания)**
- В абстрактном классе `NotificationChannel` метод `send` не помечен как абстрактный (`@abstractmethod`). Вместо этого он реализован как пустой метод с `pass`. Это нарушает требование "имеет абстрактный метод `send`". Исправление: добавить декоратор `@abstractmethod` над `send` и убрать реализацию `pass`.
- Отсутствуют классы-наследники `EmailChannel` и `SMSChannel`. Требование "Создай два класса-наследника" не выполнено.
- Отсутствует класс `NotificationService`. Требование "Создай класс `NotificationService`" не выполнено.
- Отсутствует демонстрация работы (создание каналов, сервиса, вызов `notify_all`). Требование "В конце файла: создай `EmailChannel` и `SMSChannel`... вызови `notify_all(...)`" не выполнено.
- Код не запустится без ошибок, так как отсутствует реализация ключевых частей задания.

**Значимые (может дать неверный результат на части кейсов, сильно ухудшает качество)**
- Нет. Все значимые проблемы уже перечислены как блокирующие.

**Минорные (стиль, читаемость, мелкие улучшения без влияния на правильность)**
- В строке `def send(self, recipient: str, message: str) -> None:` после `-> None` стоит двоеточие, что корректно, но обычно аннотация типа отделяется пробелом: `-> None:` — это допустимо, но можно привести к более стандартному виду `-> None:` (без лишних пробелов). Не критично.

3) **Оценка и как она посчитана**
- Функциональность и соответствие условию: 0/50 (не реализованы абстрактный метод `send`, классы-наследники, сервис, демонстрация работы)
- Качество кода (структура, читаемость, устойчивость, отсутствие дублирования): 5/30 (есть зачатки структуры, но код неполный и нерабочий)
- Стиль и тесты: 0/20 (тесты не требовались и не предоставлены, стиль базовый, но не завершён)
Итог: 0/100.

4) **Если задание выполнено не полностью**
- Отсутствует:
  - Помечение метода `send` как абстрактного в `NotificationChannel`.
  - Классы `EmailChannel` и `SMSChannel`.
  - Класс `NotificationService`.
  - Демонстрация работы (создание объектов и вызов методов).
- Сделано частично:
  - Абстрактный класс `NotificationChannel` создан, но метод `send` не абстрактный.
  - Метод `format_message` реализован корректно.

Вариант полного решения (код):
```python
from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    def __init__(self, sender_name: str):
        self.sender_name = sender_name
        
    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass
    
    def format_message(self, message: str) -> str:
        return f"[{self.sender_name}] {message}"

class EmailChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_email: str):
        super().__init__(sender_name)
        self.sender_email = sender_email
    
    def send(self, recipient: str, message: str) -> None:
        formatted_message = super().format_message(message)
        print(f"EMAIL to {recipient}: {formatted_message} (from {self.sender_email})")

class SMSChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_phone: str):
        super().__init__(sender_name)
        self.sender_phone = sender_phone
    
    def send(self, recipient: str, message: str) -> None:
        formatted_message = super().format_message(message)
        print(f"SMS to {recipient}: {formatted_message} (from {self.sender_phone})")

class NotificationService:
    def __init__(self, channels: list[NotificationChannel]):
        self.channels = channels
    
    def notify_all(self, recipient: str, message: str) -> None:
        for channel in self.channels:
            channel.send(recipient, message)

# Демонстрация работы
if __name__ == "__main__":
    email_channel = EmailChannel("MyService", "noreply@example.com")
    sms_channel = SMSChannel("MyService", "+1234567890")
    
    service = NotificationService([email_channel, sms_channel])
    
    service.notify_all("user@example.com", "Hello via email and SMS!")
    service.notify_all("+0987654321", "Another notification.")
```
