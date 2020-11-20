from django.shortcuts import render
from django.db import connection
from app_login import appLogin_views
from django.contrib import messages
from django.shortcuts import redirect
import pandas as pd
from camper.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import re

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


def reviewBoard(request):
    cursor = connection.cursor()
    sql = "select * from review_table"
    cursor.execute(sql)
    rows = cursor.fetchall()
    reviewInfo = []
    print(rows)
    for row in rows:
        dic = {'id': row[0], 'item_no': row[1], 'subject': row[2],
               'contents': row[3], 'created_id': row[4], 'created_at': row[5]}
        reviewInfo.append(dic)
    print(reviewInfo)
    return render(request, 'camper/review_board.html', {'reviewInfo': reviewInfo})

# ------------------------------상품 관련
def productList(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'camper/product_list.html', {'category': category, 'products': products})

def productDetail(request, category, no):
    product = Product.objects.get(pk=no)
    return render(request, 'camper/product_detail.html', {'product': product})

#------장바구니 관련 -----------
@csrf_exempt
def addItemToCart(request):
    pNo = request.POST['p_no']
    amount = request.POST['amount']
    cartItems = ''
    print(pNo)
    print(amount)
    
    if 'cart_items' in request.COOKIES:
        cartItems = request.COOKIES['cart_items']
        print(cartItems)
        match = re.search('|'+pNo+':', cartItems)
        print(match)
        if re.search('\|'+pNo+':', cartItems): #해당 아이템이 이미 장바구니에 있는 경우
            print('a')
            storedAmount = int(re.search('\|'+pNo+':(\d+)\|', cartItems).group(1))
            cartItems = re.sub('(?<=\|'+pNo+':)(\d+)(?=\|)', str(storedAmount+int(amount)), cartItems)
        else:
            print('b')
            cartItems += '|'+pNo+':'+amount+'|'
    else: #쿠키에 장바구니 아이템이 하나도 없는 경우
        cartItems = '|'+pNo+':'+amount+'|'
    
    res = JsonResponse({'success': True})
    res.set_cookie('cart_items', cartItems)
    return res

def myCart(request):
    if 'cart_items' in request.COOKIES:
        cart_item_list = []
        cartItems = request.COOKIES['cart_items']
        print(cartItems)
        cartItemList = cartItems.split('|')
        for item in cartItemList:
            if item:
                itemInfo = item.split(':')
                itemId = int(itemInfo[0])
                amount = itemInfo[1]
                product = Product.objects.get(pk=itemId)
                item_dict = {}
                item_dict['product'] = product
                item_dict['amount'] = amount
                cart_item_list.append(item_dict)
        print(cart_item_list)
    # return JsonResponse({'success': True})
    return render(request, 'camper/cart.html', {'cartList': cart_item_list})
    
    

