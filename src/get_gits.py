from sqlalchemy import Column, Integer, String
from connect import session, Base


def get_class(table_name):

   class GenericTable(Base):
       __tablename__ = table_name

       id = Column(Integer, primary_key=True)
       url = Column(String())

       def show(self):
           return session.query(GenericTable).all()
   return GenericTable




# class GITS(Base):
#     __tablename__ = 'gitlabs'
#     id = Column(Integer, primary_key=True)
#     url = Column(String())
#
#     def show(self):
#         return session.query(GITS).all()

#
# class SONARS(Base):
#     __tablename__ = 'sonars'
#     id = Column(Integer, primary_key=True)
#     url = Column(String())
#
#     def show(self):
#         return session.query(SONARS).all()
