###참고 사이트

#초반 셋팅
https://blog.naver.com/PostView.nhn?blogId=93immm&logNo=220906677791

#템플릿 경로 설정
https://nachwon.github.io/django-8-template/

    
# Superadmin생성 [Domain/admin 페이지]
python3 manage.py createsuperuser
ID : root
PW : 0000

### 메모
1. 프로젝트 설정 -> URL설정 -> 포트 변경
# [서버기동]
2. python manage.py runserver 0.0.0.0:80 //구름은 이렇게해줘야함
# [구름 IDE에서 브랜치처리]
3_1. 새 브런치(local_branch) 생성
3_2. 내용 수정 후 병합하기.
3_3. 병합 후 git에 branch생성 되고 PR생김.
3_4. merge 처리

### CMD 정리

# 프로젝트 생성
django-admin startproject [프로젝트명]

# 앱 생성
Python3 manage.py startapp [앱이름]


# DB -> Model
python manage.py inspectdb > models.py

# Model -> DB (모델 작성 후 테이블 생성)
python3 manage.py makemigrations [앱이름]
python3 manage.py migrate

# 마이그레이션 적용 현황 확인
python manage.py showmigrations app-name
#sql적용된거 내용 확인
python manage.py sqlmigrate [앱이름] [번호]
 ex)python manage.py sqlmigrate polls 0001

# *서버 실행 
python3 manage.py runserver 0.0.0.0:8000

# Mysql 실행
service mysql start
mysql -p 

# Pull 시 충돌날경우 해결(기존 작업하던 내용과 충돌나기때문)
1.새 브런치 생성 후 선택
2.커밋(커밋 후 푸시는 안해도됨)
3.master 브런치 선택
4.pull


# Cursor
1.pip install PyMySQL

install
#alias
path : cd /etc/bash.bashrc 
별명 = '명령어'
ex) stary='python manage.py runserver 0.0.0.0:80'