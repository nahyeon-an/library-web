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
- pie chart 의 경우 왼쪽 도시 차트에서 부분 조각을 클릭하면 해당 도시내의 군/구 차트를 오른쪽에 표시

![메인보드](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fw8ewb%2FbtqToxd4erp%2F6HQWqEe8tpYlc33zC7232k%2Fimg.png)

![메인보드](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FtoVPu%2FbtqTvQjbGVE%2Fsr7qxRn6DqNJWEiIYtctZK%2Fimg.png)

<br>

## 6. 데이터 서비스 기능 구현
1. 전국 도서관 조회
- 도서관명을 클릭하면 상세보기 가능
- 수정할 것
    * 상세보기 템플릿 수정해야 함 : 아래에 지도 보이게 + 네이버에서 조회한 결과 (이건 api 결과물을 봐야 기능 구현 가능할 듯?)
    * 나중에 html,css,js를 좀 더 공부하고 테이블 페이징 부분 디자인 수정하기 (기능은 잘 동작함)
    * base.html 에서 global search element를 지우고, 필요한 template 에서 삽입하여 이용하도록 수정
    * 검색이 너무 느린것 같다 - 데이터 조회 속도 개선방법 찾아보기
- 현재 상황

![전국도서관 초기화면](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fb309tp%2FbtqTrRQtoyD%2FzYvepjTAC6lKzc7jSDQr71%2Fimg.png)

![전국도서관 검색결과화면](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FohT9O%2FbtqTkhv6ae3%2FvvIga1um2tKQKRlpLMrjQK%2Fimg.png)

![도서관 클릭 후 상세보기](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FptZ5J%2FbtqSTJfiAPp%2FKDwlWfUhWqiyZ88s5xU7K0%2Fimg.png)

2. 지역별 도서관 조회
3. 대학 도서관
4. 도서관 이용 통계 dashboard
- 처음 시작 화면부터 dashboard 라서 이와 겹치지 않는 시각 요소를 넣으려면 데이터 및 통계에 대한 고민이 필요함 !

<br>

## 7. 사용자 인증 시스템 구현
1. 로그인
- 로그인되어 있지 않은 상태에서 드롭바에 나타남
- 자동 로그인 선택가능 (but 세션 타임아웃 형태)
- 로그인 정보는 session으로 관리하여 모든 페이지에서 프로필에 유저를 표시함

![로그인 페이지](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FBVzvD%2FbtqTvRoPEtD%2F1FKGjfHmHJKGKA9d3HkOXK%2Fimg.png)

2. 회원가입
- 로그인되어 있지 않은 상태에서 드롭바에 나타남
- 회원가입 완료 후 완료 페이지가 나타남
- 예외처리 필요한 부분 : user id 가 데이터베이스에 이미 존재하여 기본키 충돌 발생하는 경우를 처리해야 함  

![회원가입 페이지](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FpC3J5%2FbtqTwXPSC31%2Fk4ehqUyYZfaiGkF1kAOO2K%2Fimg.png)

![회원가입 성공 페이지](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FMvN6r%2FbtqTowl1HFH%2F3DB9hUCxt0dUnsFsN54N7K%2Fimg.png)

3. 로그아웃
- 로그인된 사용자의 드롭바에서만 나타나는 기능  
- 클릭하면 별도의 메시지 없이 로그아웃되어 User 표시가 나타남  

<br>

## 8. 서비스에 대한 코멘트 기능 구현

<br>

## 9. REST API 구현  
(아직 클라우드에 배포하지 않음)  

1. GET  
- libraries : 모든 도서관 리스트 데이터 조회  
- libraries/\<si> : 해당 시의 도서관 리스트 조회  
- 구현하고 싶은 것 : 도서관 명으로 조회 시 현재 날짜와 도서관의 오픈/클로즈 여부를 반환  

```
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/libraries/강원도
```

![호출1](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdjAiL5%2FbtqZSu76A5d%2F1ocF1sO4kbTu2kC1iaBmQk%2Fimg.png)

```
curl -H GET http://127.0.0.1:8000/libraries/서울특별시
```

![호출2](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fd3W3MF%2FbtqZRsvVtw7%2FkbqopdgGG1U4kHd44Qrv50%2Fimg.png)

2. POST, PUT, DELETE 에 대해서 어떤 데이터를 수정가능하게 할 지 고려해봐야 함  

<br>

## 10. 배포
1. Python Anywhere   
- [library web on python anywhere](http://anagetdone.pythonanywhere.com/)  
- 계정명.pythonanywhere.com 이라는 고정 주소로 접속 가능한 것이 가장 큰 장점
- mysql 데이터베이스를 사용할 때 호스트 ip, database 이름, user 이름, password 를 모두 수정해야 함에 유의   
- 시도해볼 것 : docker를 이용한 배포  

2. AWS - EC2  

<br>
