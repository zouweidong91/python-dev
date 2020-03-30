
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


Base = declarative_base()
metadata = MetaData()
engine = create_engine('mydb')

# 需要提前创建表
def create_table():
    user = Table(
        'user', metadata,
        Column('id', String(20), primary_key=True),
        Column('name', String(20))
        )
    metadata.create_all(engine)
create_table()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


DBSession = sessionmaker(bind=engine) # type: OrmSession
session = DBSession()


def insert():
    new_user = User(id='5', name='Bob')
    session.add(new_user)
    session.commit()
    session.close()
def select():
    session = DBSession()
    user = session.query(User).filter(User.id=='5').one()
    print(type(user))
    print(user.name)

'''
python -m SQLAlchemy.quick_start
'''