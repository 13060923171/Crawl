from sqlalchemy import create_engine,MetaData,Table
from sqlalchemy import Column,String,Integer,select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#创建基类
Base = declarative_base()
engine = create_engine(
    #固定写法root表示你数据库的名称，第二个root是你数据库的名字,test是你数据库的表
    "mysql+pymysql://root:root@127.0.0.1:3306/test",
    #超过连接池大小外最多可以创建的链接
    max_overflow=5,
    #连接池的大小
    pool_size=10,
    #调试信息展示
    echo=True,
)
#用于第一二种创建方法
#取得元数据，介绍数据库
# metadata = MetaData()
#定义表
# user= Table("user",metadata,
#             Column("id",Integer,primary_key=True,autoincrement=True,),
#             Column("name",String(10)))
#创建数据表
#metadata.create_all(engine)
# #插入数据库
# conn = engine.connect()
# conn.execute(user.insert(),{"name":"python"})
# conn.close()
# #更改数据库
# conn = engine.connect()
# conn.execute(user.update().where(user.c.id == 6).values(name = "python"))
# conn.close()
# #查询数据库
# conn = engine.connect()
# res = conn.execute(select([user.c.name,]))
# print(res.fetchall())
# conn.close()
# #删除数据库
# conn = engine.connect()
# conn.execute(user.delete().where(user.c.id == 6))
# conn.close()

#爬虫必须掌握的操控数据库的语法！！！
class Host(Base):
    #表名为hosts
    __tablename__ ="hosts"
    #表结构 primary_key等于主键 unique唯一 nullable非空
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=8080)

#Base.metadata.create_all(engine)
if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    sess = Session()#创建实例
    h = Host(hostname='test1',ip_addr='127.0.0.1')
    h2 = Host(hostname='test2',ip_addr='192.168.0.1',port=80001)
    h3 = Host(hostname='test3',ip_addr='192.168.0.2',port=80002)
    # #添加一条语句
    # sess.add(h)
    # #添加多条语句
    # sess.add_all([h2,h3])
    # #查询并删除语句
        # sess.query(Host).filter(Host.id>1).delete()
    #修改语句
    #sess.query(Host).filter(Host.id ==1).update({'port':9999})
    #查询语句
    res = sess.query(Host).filter_by(id =1).all()
    for r in res:
        print(r.hostname,r.port)
    sess.commit()