from django.shortcuts import render
from django.db import connection
from app_login import appLogin_views
from django.contrib import messages
from django.shortcuts import redirect

def must_login(func):
    def wrapper(request,*args, **kwargs):
        try:
            print(request.session['id']);
        except:
            return redirect("/camper/loginPage")
        
        return func(request,*args, **kwargs)
        
    return wrapper

def index(request):
    return render(request, 'camper/index.html')

def product(request):
    return render(request, 'camper/product.html')

def db_selectTable(tableName):
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
# def board(request):    
#     results = db_selectTable("MEMBER")
#     #result = db_insertMember()
#     #print(results)
    
#     for row in results:
#         print(row)

#     return render(request, 'camper/board.html',)


def board(request):
    cursor = connection.cursor()
    sql = "select * from MEMBER"
    cursor.execute(sql)
    rows = cursor.fetchall()
    members = []
    for row in rows:
        dic = {'id': row[1], 'name': row[3]}
        members.append(dic)
    print(members)
    return render(request, 'camper/board.html', {'members': members})

def productList(request):
    cursor = connection.cursor()
    sql = "select * from PRODUCT"
    cursor.execute(sql)
    rows = cursor.fetchall()
    images = []
    for row in rows:
        images.append(row[4])
    print(images)
    return render(request, 'camper/product_list.html', {'images': images})
