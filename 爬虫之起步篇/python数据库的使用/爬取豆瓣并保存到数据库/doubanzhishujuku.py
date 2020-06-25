from sqlalchemy import create_engine
from sqlalchemy import Column,String,Text,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine(
    "mysql+pymysql://root:root@127.0.0.1:3306/test?charset=utf8",
    echo=True,
)
class Book(Base):
    #数据库的表的名字
    __tablename__ ='book'
    id = Column("id",Integer(),primary_key=True,autoincrement=True)
    #设置数据库，存储这些内容的格式，长度等
    title = Column('title',String(20))
    info = Column('info',String(50))
    star = Column('star',String(10))
    pingfeng = Column("pingfeng",String(20))
    text = Column("text",Text())

#Base.metadata.create_all(engine)
session = sessionmaker(engine)
sess = session()