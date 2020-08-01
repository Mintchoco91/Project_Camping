from django.shortcuts import render
from django.db import connection

def loginPage(request):
    return render(request, 'login.html')

def signUpPage(request):
    return render(request, 'signUp.html')

def signUp(request):
    returnPage = "signUp.html"
    
    try:
        cursor = connection.cursor()
        sql = "SELECT COUNT(*) FROM MEMBER WHERE USER_ID = '"+request.POST['id']+"'"
        cursor.execute(sql)
        sql = "";
        exist = cursor.fetchone()
        
        if exist[0] == 0:
            sql = "INSERT INTO MEMBER (USER_ID,USER_PW,USER_NAME,ENROLLDATE) VALUES "
            sql += "('"+ request.POST['id'] + "','" + request.POST['pw'] + "','" + request.POST['name'] + "',NOW())"
            cursor.execute(sql)        
            connection.commit()
            returnPage = "login.html"
        else:
            print("Exist")
            
    except:
        print("DB ERR!!")
    finally:
        connection.close()    
    return render(request, returnPage)


def login(request):
    returnPage = "login.html"
    
    try:
        cursor = connection.cursor()
        sql = "SELECT COUNT(*) FROM MEMBER WHERE USER_ID = '"+request.POST['id']+"' and USER_PW= '" +request.POST['pw']+ "'"
        print(sql)
        cursor.execute(sql)
        sql = "";
        exist = cursor.fetchone()
        
        if exist[0] == 0:
            print("fail")
        else:
            #메인페이지로 보내줘야함
            returnPage = "../camper/camper/index.html"
            
    except:
        print("DB ERR!!")
    finally:
        connection.close()    
    return render(request, returnPage)