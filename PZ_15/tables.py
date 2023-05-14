"""Таблица "Туристы"

id (INT, PK) - уникальный идентификатор туриста
имя (VARCHAR)
фамилия (VARCHAR)
пол (VARCHAR)
дата_рождения (DATE)
номер_телефона (VARCHAR)
электронная_почта (VARCHAR)

Таблица "Туры"

id (INT, PK) - уникальный идентификатор тура
название (VARCHAR)
страна (VARCHAR)
город (VARCHAR)
дата_начала (DATE)
дата_окончания (DATE)
цена (DECIMAL)

Таблица "Бронирования"

id (INT, PK) - уникальный идентификатор бронирования
id_туриста (INT, FK) - идентификатор туриста, который сделал бронирование
id_тура (INT, FK) - идентификатор тура, на который было сделано бронирование
дата_бронирования (DATE)
"""

tourists = """
CREATE TABLE IF NOT EXISTS tourists(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR,
    surname VARCHAR,
    sex VARCHAR,
    country VARCHAR,
    date_of_birthday DATE,
    phone_number VARCHAR,
    email VARCHAR
)
"""

tours = """
CREATE TABLE IF NOT EXISTS tour(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR,
    country VARCHAR,
    city VARCHAR,
    date_start DATE,
    date_end DATE,
    price REAL
)
"""

booking = """
CREATE TABLE IF NOT EXISTS booking(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_of_booking DATE,
    tourists_count INTEGER,
    id_tourist INTEGER,
    id_tour INTEGER,
    FOREIGN KEY (id_tourist) REFERENCES tourists(id),
    FOREIGN KEY (id_tour) REFERENCES tour(id)
)
"""