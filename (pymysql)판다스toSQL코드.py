# MySQL 데이터베이스에 새로운 테이블을 생성할 때, 주피터노트북과 연동하여 판다스 데이터프레임을 MySQL DB에 바로 적재하는 방법 
# 컬럼명, 순서와 데이터타입이 모두 일치해야 한다
# 데이터베이스에 테이블은 생성하고 실행

from sqlalchemy import create_engine
import pymysql

pymysql.install_as_MySQLdb()


engine = create_engine('mysql+mysqldb://root:{초기 설정 비밀번호}@localhost:3306/{DB 명}',encoding='utf-8')

conn = engine.connect()

{데이터프레임 명}.to_sql(name='{DB 컬럼명}', con=conn, if_exists='append', index=False)

conn.close()


# 오류가 몇 번 발생했었는데, date 타입을 변경하지 않았던 문제 
# sql 테이블 생성 당시 pk나 데이터 길이 설정 실수했던 문제 
