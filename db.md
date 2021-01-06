## Database 설계
- 사용할 데이터 : 전국 도서관 정보

<br>

### MySQL 계정, 데이터베이스 생성

1. root 계정 접속
```
mysql -u root -p
```
2. database 생성
```
create database libweb;
```
3. User 생성
```
create user 'ssacuser'@'%' identified by 'ssac123!@#';
```
4. 권한 부여
```
grant all privileges on libweb.* to 'ssacuser'@'%' with grant option;
```
5. 적용
```
flush privileges;
```
<br>

### 스키마 생성
- (library 테이블)사용할 컬럼  
  : 도서관명, 시도명, 시군구명, 휴관일, 평일/토요일/공휴일 운영시작시각, 평일/토요일/공휴일 운영종료시각,
    열람좌석수, 도서자료수, 대출가능권수, 대출가능일수, 도로명주소, 전화번호, 홈페이지 주소
- (blindbook 테이블)사용할 컬럼  
  : 저자, 책제목, 출판사  
- create-schema.sql 을 작성한 뒤 리디렉션
```
mysql -u ssacuser -p libweb < create-schema.sql
```
<br>

### 데이터 삽입  
- insert-data.py
<br>

### MySQL DB를 Djagno project 와 연결
- settings.py 에서 DATABASES 부분을 다음과 같이 변경
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': "libweb",
        'USER': "ssacuser",
        'PASSWORD': "ssac123!@#"
    }
}
```
- 기존 데이터베이스의 내용으로 models.py 를 자동 작성
```
python manage.py inspectdb > dashboard/models.py
```
- migration
```
python manage.py makemigrations
python manage.py migrate
```
