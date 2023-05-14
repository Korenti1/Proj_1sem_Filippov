delete1 = """
delete from booking where id_tourist=1
"""
delete2 = """
delete from booking where id_tour=2
"""
delete3 = """
delete from booking where date_of_booking='2022-07-01'
"""
delete4 = """
delete from tourists where id in (select id_tourist from booking where id_tour=3)
"""
delete5 = """
delete from booking where id_tourist in (select id from tourists where phone_number='+789123456')
"""
delete6 = """
delete from booking where id_tourist in (select id from tourists where email='smirnov@mail.ru')
"""
delete7 = """
delete from booking where id_tour in (select id from tour where date_start > '2022-07-01')
"""
delete8 = """
delete from tourists where tourists.id in(select id_tourist from booking where id_tour in(select tour.id from tour where tour.country='Россия'))
"""
delete9 = """
delete from booking where id_tour in (select id from tour where date_start < '2022-07-01')
"""
delete10 = """
delete from booking where id_tour in (select id from tour where price < 20000.00)
"""

deletes = [delete1, delete2, delete3, delete4, delete5, delete6, delete7, delete8, delete9, delete10]
