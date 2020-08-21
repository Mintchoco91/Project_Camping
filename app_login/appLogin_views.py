from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
from django.contrib import messages
from camper import templates

def loginPage(request):
    return render(request, 'app_login/login.html', {"returnMsg" : ""})


def signUpPage(request):
    return render(request, 'app_login/signUp.html')


def logout(request):
    if request.session['id']:
        del request.session['id']
        
    return redirect('/camper/');


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
            returnPage = "app_login/login.html"
        else:
            print("Exist")
            
    except:
        print("DB ERR!!")
    finally:
        connection.close()    
    return render(request, returnPage)


def login(request):
    print("login시작")
    returnPage = "app_login/login.html"
    inputId = request.POST['id'];
    inputPw = request.POST['pw'];
    try:
        cursor = connection.cursor()
        sql = "SELECT COUNT(*) FROM MEMBER WHERE USER_ID = '"+inputId+"' and USER_PW= '" +inputPw+ "'"
        cursor.execute(sql)
        exist = cursor.fetchone()
        
        if exist[0] == 0:
            returnMsg = "로그인 실패. ID/PW를 확인해주세요."
            print("IF문안")
        else:
            request.session['id'] = inputId;
            
            #메인페이지로 보내줘야함
            returnMsg = "";
            returnPage = "/camper/"
            print("ELSE안")
            return redirect(returnPage);
    except:
        returnMsg = "DB 에러!!관리자에게 문의하세요."
    finally:
        connection.close()
        
    print("login끝")
    return render(request, returnPage, {"returnMsg" : returnMsg})