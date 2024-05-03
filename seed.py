from db import SessionLocal
from model import Name, Person

jd_name_1 = Name(fio="Doe John")
jd = Person(id=1, names=[jd_name_1])

dm_name_1 = Name(fio="Morgendorffer Daria")
dm = Person(id=2, names=[dm_name_1])

with SessionLocal() as session:
    session.add_all([jd, dm])
    session.commit()
