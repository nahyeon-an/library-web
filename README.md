# library-web  
- 어릴 때부터 도서관을 자주 이용해왔는데 공공도서관 운영정보, 소장자료, 위치 등을 한 곳에 모아 보고 싶어서 선정
- 기능, 데이터 등이 추가될 것 같다 (전자책 관련 데이터를 수집할 수 있다면 전자책 현황 등을 서비스)

<br>

## 1. 서비스 설계  
1. 서비스 데이터 : 전국 도서관 표준 데이터  

2. 기능
    - 도서관 기본 정보 제공 (도서관명, 휴관일, 운영시간, 도서자료수, 대출가능권수, 대출가능일수, 주소 등)
    - 지역/구별 도서관의 개수 시각화 (목표는 지도!)
    - 네이버 검색 API를 이용한 리뷰/책 정보 보여주기
    - (위치 api 이용한다면? 일단, 보류)가까운 도서관 찾기

<br>

## 2. 데이터 운영 설계 및 구현
1. 수집 방법
    - 공공 데이터 포털에서 .csv 파일 다운
    - naver search api

2. 데이터 저장 방법
    - 데이터 베이스(MySQL)에 저장
    - .csv 파일에서 사용할 컬럼만 pymysql을 이용하여 저장
    - open api 의 경우 따로 저장하지 

3. 데이터베이스 구축

<br>

## 3. 대시보드 웹 템플릿 검토 및 선정
[선정한 대시보드 템플릿](https://github.com/puikinsh/kiaalap)  
[참고사이트](https://colorlib.com/wp/free-dashboard-templates/)

<br>

## 4. 웹 프로젝트 구성
1. django project 만들기
```
django-admin startproject libraries
```
2. settings.py
3. 애플리케이션 생성
```
python manage.py startapp dashboard
```
4. ORM 모델 구현 및 데이터베이스로 마이그레이션 : db.md 를 참조
5. admin 을 통한 확인 : http://localhost:8000/admin/ 에서 확인 가능
```
python manage.py createsuperuser
```

<br>

## 5. 화면 구조 설계 및 공통 영역 구현
1. 공통 화면 모듈 구현
2. 공통 템플릿 구현
3. 웹사이트 시작 화면 

<br>
