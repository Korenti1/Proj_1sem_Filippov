select1 = """
SELECT * FROM tourists
"""
select2 = """
select * from tour order by price asc
"""
select3 = """
select booking.date_of_booking, t.title, t.country, t.city, t.price from booking join tour t on t.id = booking.id_tour where city='Москва'
"""
select4 = """
select t.name,t.surname ,t.sex from booking join tourists t on t.id = booking.id_tourist where date_of_booking = '2022-07-01'
"""
select5 = """
select city, country from tour
"""
select6 = """
select * from tourists where sex='Ж' and date_of_birthday > '1990-01-01'
"""
select7 = """
select * from tour where price > 5000
"""
select8 = """
select t.name, t.surname, t.sex, t.email from booking join tourists t on t.id = booking.id_tourist where id_tour = 2
"""
select9 = """
select t.name, t.surname, t.sex from booking join tourists t on t.id = booking.id_tourist join tour t2 on t2.id = booking.id_tour where booking.id_tour = 2 and booking.date_of_booking='2022-05-10'
"""
select10 = """
select * from tourists where phone_number like '+7%'
"""
selects = [select1, select2, select3, select4, select5, select6, select7, select8, select9, select10]
