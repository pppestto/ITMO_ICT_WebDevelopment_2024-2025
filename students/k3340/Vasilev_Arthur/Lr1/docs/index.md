# Отчеты по лабораторным работам

## Выберите лабораторную работу

<div class="lab-selection">
  <div class="lab-card" onclick="window.location.href='lr1.md'">
    <div class="lab-icon">🔌</div>
    <h3>Лабораторная работа 1</h3>
    <p>Работа с сетевыми сокетами в Python</p>
    <div class="lab-status">✅ Завершена</div>
  </div>

  <div class="lab-card" onclick="window.location.href='lr2.md'">
    <div class="lab-icon">🚀</div>
    <h3>Лабораторная работа 2</h3>
    <p>Django приложение для автогонок</p>
    <div class="lab-status">✅ Завершена</div>
  </div>

  <div class="lab-card" onclick="window.location.href='lr3.md'">
    <div class="lab-icon">🎯</div>
    <h3>Лабораторная работа 3</h3>
    <p>Хакатон API</p>
    <div class="lab-status">🔄 В разработке</div>
  </div>
</div>

## О проекте

Этот сайт содержит отчеты по лабораторным работам курса "Основы веб-разработки" в ITMO.

- **Дисциплина:** Основы Web-программирования
- **Студент:** Василев Артур
- **Группа:** К3340
- **Год:** 2024-2025

<style>
.lab-selection {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 30px;
  margin: 40px 0;
}

.lab-card {
  border: 2px solid #e0e0e0;
  border-radius: 15px;
  padding: 30px 20px;
  text-align: center;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.lab-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
  transition: left 0.5s;
}

.lab-card:hover::before {
  left: 100%;
}

.lab-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 15px 35px rgba(0,0,0,0.1);
  border-color: #1976d2;
}

.lab-icon {
  font-size: 3rem;
  margin-bottom: 15px;
}

.lab-card h3 {
  color: #1976d2;
  margin-bottom: 10px;
  font-size: 1.4rem;
}

.lab-card p {
  color: #666;
  margin: 15px 0;
  line-height: 1.5;
}

.lab-status {
  background: #4caf50;
  color: white;
  padding: 5px 15px;
  border-radius: 20px;
  font-size: 0.9rem;
  display: inline-block;
  margin-top: 10px;
}

@media (max-width: 768px) {
  .lab-selection {
    grid-template-columns: 1fr;
  }
}
</style>

.lab-card p {
  margin: 10px 0;
  color: #666;
}

.btn {
  display: inline-block;
  background: #1976d2;
  color: white;
  padding: 10px 20px;
  text-decoration: none;
  border-radius: 5px;
  margin-top: 10px;
  transition: background 0.2s;
}

.btn:hover {
  background: #1565c0;
}
</style>

## Практическое задание

### Задание 1

Реализовать клиентскую и серверную часть приложения. Клиент отправляет серверу сообщение «Hello, server», и оно должно отобразиться на стороне сервера. В ответ сервер отправляет клиенту сообщение «Hello, client», которое должно отобразиться у клиента.

**Требования:**

- Обязательно использовать библиотеку `socket`
- Реализовать с помощью протокола UDP

**Полезные ссылки:**

- [Habr: Основы работы с сокетами](https://habr.com/ru/post/149077/)
- [Андрей Малинин: Сокеты в Python](https://andreymal.org/socket3/)
- [Документация Python: Руководство по сокетам](https://docs.python.org/3.6/howto/sockets.html)
- [Python Library Reference: socket](https://docs.python.org/3.6/library/socket.html)
- [Видео: Введение в работу с сокетами](https://www.youtube.com/watch?v=Lbfe3-v7yE0)

### Задание 2

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает выполнение математической операции, параметры которой вводятся с клавиатуры. Сервер обрабатывает данные и возвращает результат клиенту.

**Варианты операций:**

1. Теорема Пифагора
2. Решение квадратного уравнения
3. Поиск площади трапеции
4. Поиск площади параллелограмма

Порядок выбора варианта: Выбирается по порядковому номеру в журнале (пятый студент получает вариант 1 и т.д.).

**Требования:**

- Обязательно использовать библиотеку `socket`
- Реализовать с помощью протокола TCP

**Полезные ссылки:**

- [ZetCode: Работа с сокетами](http://zetcode.com/python/socket/)

### Задание 3

Реализовать серверную часть приложения. Клиент подключается к серверу, и в ответ получает HTTP-сообщение, содержащее HTML-страницу, которая сервер подгружает из файла `index.html`.

**Требования:**

- Обязательно использовать библиотеку `socket`

**Полезные ссылки:**

- [ZetCode: Работа с сокетами](http://zetcode.com/python/socket/)

### Задание 4

Реализовать двухпользовательский или многопользовательский чат. Для максимального количества баллов реализуйте многопользовательский чат.

**Требования:**

- Обязательно использовать библиотеку `socket`
- Для многопользовательского чата необходимо использовать библиотеку `threading`

**Реализация:**

- Протокол TCP: 100% баллов
- Протокол UDP: 80% баллов
- Для UDP используйте `threading` для получения сообщений на клиенте
- Для TCP запустите клиентские подключения и обработку сообщений от всех пользователей в потоках. Не забудьте сохранять пользователей, чтобы отправлять им сообщения

**Полезные ссылки:**

- [Документация Python: threading](https://docs.python.org/3/library/threading.html)
- [WebDevBlog: Введение в потоки Python](https://webdevblog.ru/vvedenie-v-potoki-v-python/)

### Задание 5

Написать простой веб-сервер для обработки GET и POST HTTP-запросов с помощью библиотеки `socket` в Python.

**Задание:**

Сервер должен:

1. Принять и записать информацию о дисциплине и оценке по дисциплине
2. Отдать информацию обо всех оценках по дисциплинам в виде HTML-страницы

**Полезные ссылки:**

- [Базовый класс для веб-сервера](https://docs.google.com/document/d/1lv_3D9VtMxz8tNkA6rA1xu9zaWEIBGXiLWBo1cse-0k/edit?usp=sharing)
- [Мануал по созданию сервера](https://iximiuz.com/ru/posts/writing-python-web-server-part-3/)

## Выполнение работы

- Работа выполняется индивидуально
- По результатам необходимо подготовить отчет в виде текстового документа

## Оценивание

- Выполнение пунктов 1-4 и однопользовательского чата (без потоков) — 60% баллов
- Выполнение пунктов 1-5 и многопользовательского чата (с потоками) — 100% баллов