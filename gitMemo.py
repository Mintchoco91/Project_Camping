1. 변경내용 초기화(commit 한 내용들)
git reset --hard

1_1. 변경내용 초기화(commit 하지 않은 변경파일들 전부 삭제)
git clean -f 

2. 원격 브랜치 목록 동기화
git remote update --prune

3. 브랜치 목록 확인
git branch -r    //원격 브랜치 목록
git branch -l    //로컬 브랜치 목록
git branch -a    //로컬 + 원격 브랜치 목록

4. checkout 으로 최신브랜치 가져옴
git checkout [브랜치명]

5. IDE 에서 로컬브랜치 만들어서 기존처럼 작업

6. 브랜치 삭제
git branch -D [브랜치명] //로컬 브랜치 삭제
git push origin :[브랜치명] //로컬 브랜치 삭제 후 원격 브랜치 삭제