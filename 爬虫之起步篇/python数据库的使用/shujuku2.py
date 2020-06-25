from sqlalchemy import create_engine,Table, ForeignKey
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
engine = create_engine(
    "mysql+pymysql://root:root@127.0.0.1:3306/test",
    max_overflow=5,
    pool_size=10,
    echo=True,
)
User2Lan = Table('user_2_language',Base.metadata,
                 Column('user_id',ForeignKey('user.id'),primary_key=True),
                 Column('language_id',ForeignKey('language.id'),primary_key=True))
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer(),primary_key=True,autoincrement=True)
    name = Column(String(125),nullable=True)
    gender = Column(String(10),nullable=True,default="保密")
    town = Column(String(125))
    language = relationship('Language',backref='user',cascade='all,delete',secondary=User2Lan,)

class Language(Base):
    __tablename__ = 'language'
    id = Column(Integer(),primary_key=True,autoincrement=True)
    name = Column(String(125),nullable=True)
    advantage = Column(String(125),nullable=True)
    disadvantage = Column(String(125),nullable=True)



#Base.metadata.create_all(engine)
#使关联表失联
engine.execute("SET FOREIGN_KEY_CHECKS = 0")
if __name__ == '__main__':
    Session = sessionmaker(engine)
    session = Session()
    #添加用户
    # try:
    #     u1 = User(name='张三',gender='男',town='广州')
    #     u2 = User(name='李四', gender='女', town='深圳')
    #     session.add_all([u1,u2])
    #     session.commit()
    # except:
    #     session.rollback()#回滚操作

    #添加语言
    # l1 = Language(name='python',advantage='开发快',disadvantage='运行速度慢')
    # l1.user = u1
    # session.add(l1)
    # session.commit()
    # u3 = User(name='王五', gender='男', town='上海')
    # u3.language=[Language(name='python', advantage='开发快', disadvantage='运行速度慢'),Language(name='c', advantage='稳定', disadvantage='上手慢')]
    # session.add(u3)
    # session.commit()
    #更新数据表
    # u = session.query(User).filter(User.id==4).first()
    # u.language[0].name = 'python3'
    # #u.name = "赵六"
    # session.commit()
    #查询关联表的数据
    # u = session.query(User).filter_by(id=3).first()
    # print("name:",u.name)
    # lan = session.query(Language).filter_by(user_id = u.id)
    # for l in lan:
    #     print("language:",l.name)
    #查看总数量
    #session.query(User).filter(User.id>0).count()
    #如何用正则表达式找出相关内容出来
    m = session.query(User).filter(User.name.like("_三")).all()[0]
    print(m.name)
    #删除关联表的数据
    # u=session.query(User).filter(User.id ==3).first()
    # session.delete(u)
    # session.commit()