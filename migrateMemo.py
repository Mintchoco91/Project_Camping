// Model로 작업 시 꼬일경우

1.[apt-get install sqlite3]

2.[sqlite3 db.sqlite3]

3.[.table] 실행   //테이블확인

4.
[drop table polls_questions;]
[drop table polls_choice;] 실행(; 땀표시 중요함)

5.Ctrl+C 로 빠져나옴.

6.migrations 폴더안에 파일들 삭제

7.[python3 manage.py makemigrations polls]

8.[python3 manage.py migrate]

8_1. [python manage.py migrate --fake] (8번에서 혹시나 오류날경우 이걸로실행.)