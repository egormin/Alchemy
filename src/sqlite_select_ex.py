from sqlite_ex import Person, Base, Address
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:123456@localhost:5432/PERS')
Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
# Make a query to find all Persons in the database
res = session.query(Person).all()
print(res)

xx = []
for i in res:
    print(f'{i.name} was released on {i.name}')
    xx.append(i.name)

print(xx)

person = session.query(Person).first()
print(person.name)

# Find all Address whose person field is pointing to the person object
res1 = session.query(Address).filter(Address.person == person).all()
print(res1)

# Retrieve one Address whose person field is point to the person object
res3 = session.query(Address).filter(Address.person == person).one().post_code
print(res3)