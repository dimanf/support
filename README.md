Support
==

Для запуска проекта требуется утановить два приложения:

- $ pip install django-bootstrap-form
- $ pip install django-simple-history

Полный список зависимостей содержится в файле - requirements.txt

В данном проекте можно:

- Сздавать тикет
- Изменять тикет
- Назначить отдел
- Нзначить ответственный персонал за тикетом
- Комментировать тикет
- Просматривать статистику тикетов (не принят/в процесе/закрыт) с возможнотью фильтрации по периоду (за вчерашний день/за последнюю неделю/за месяц)

Все изменения в модели тикета сохраняются, если понадобится вернуть старые данные.
Посмотреть изменения или вернуть старые данные можно через админку в разделе "Тикеты" -> "История"
