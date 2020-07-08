from django.shortcuts import render
import pymysql


# Create your views here.
def index(request):
    return render(request, 'camper/index.html')

def product(request):
    return render(request, 'camper/product.html')

def connectDb():
    # Connect to the database
    connection = pymysql.connect(host='enqhzd10cxh7hv2e.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                 user='e4yml2sku68njthx',
                                 password='o751zmjlxv9qmnmu',
                                 db='udm84d8ce234i5di',
                                 charset='utf8mb4')
    return connection

def db_selectTable(tableName):
    connection = connectDb()
    try:
        curs = connection.cursor()
        sql = "select * from MEMBER"
        curs.execute(sql)
        
        rows = curs.fetchall()     
        #for row in rows:
        #    print(row)
        
        print(curs)
    except:
        rows = "false";
    finally:
        connection.close()
        
    return rows

def db_insertMember(user_id, user_pw, user,name):
    result = "false"
    connection = connectDb()
    try:
        #SELECT 해서 마지막 ID 가져오는 쿼리 추가할것
        
        result = "success"
        curs = connection.cursor()
        sql = "insert into MEMBER values (5,'kiwon911','11222','기원',now());"
        curs.execute(sql)        
        connection.commit()
        
        print(curs)
    except:
        result = "false"
    finally:
        connection.close()
    return result

#Board 초기 페이지
def board(request):    
    results = db_selectTable("MEMBER")
    #result = db_insertMember()
    #print(results)
    
    for row in results:
        print(row)

    return render(request, 'camper/board.html',)