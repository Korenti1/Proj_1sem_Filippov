upd1 = """
update tour set date_start = '2023-05-01' where id=1
"""
upd2 = """
update tour set price=1500 where id=7
"""
upd3 = """
update tourists set phone_number='+15551234567' where id=5
"""
upd4 = """
update booking set date_of_booking='2023-04-05' where id=3
"""
upd5 = """
update booking set tourists_count=3 where id=8
"""
upd6 = """
update tour set date_end='2023-08-31' where id=2
"""
upd7 = """
update tourists set email='new_email@example.com' where id=1
"""
upd8 = """
update tour set date_start='2023-06-15' where id=4
"""
upd9 = """
update tour set date_start='2023-05-01' where country='Испания'
"""
upd10 = """
update tour set price=1500 where title='Греция-отдых на море'
"""
upd11 = """
update tour set date_start='2023-06-01' where title='Испания-путешествие по городам'
"""
upd12 = """
update booking set tourists_count=3 where id=2
"""
upd13 = """
update tourists set phone_number='+1234567890' where id=2
"""
upd14 = """
update tour set date_start='2024-07-01' where price < 2000
"""
upd15 = """
update tourists set email='new_email@example.com' where country='Россия'
"""
upd16 = """
...
"""
upd17 = """
...
"""

updates = [upd1, upd2, upd3, upd4, upd5, upd6, upd7, upd8, upd9, upd10, upd11, upd12, upd13, upd14, upd15]
