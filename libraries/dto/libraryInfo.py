class BasicLibraryInfo:
    """
    도서관 기본 정보를 담는 클래스
    기본 정보 : 도서관명, 시도명, 군구명
    """
    def __init__(self, name, sidoName, gunguName):
        self.name = name
        self.sidoName = sidoName
        self.gunguName = gunguName

    def __str__(self):
        return self.name + " " + self.sidoName + " " + self.gunguName

class OperatingInfo(BasicLibraryInfo):
    """
    이거 고민.. 나중에 sql문에서 가져온 정보를 어떻게 저장하지? 도서관 명도 같이 저장해야하나? 상속으로 이게 다 처리가 되나
    도서관 운영 정보를 담는 클래스
    운영 정보 : 휴관일, 평일오픈시각, 평일종료시각, 토요일오픈시각, 토요일종료시각, 공휴일오픈시각, 공휴일종료시각
    """
    def __init__(self, closeDay, everyOpen, everyClose):
        self.closeDay = closeDay