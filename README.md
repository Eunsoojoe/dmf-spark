# Spark
Spark : 대용량 데이터 처리를 위한 분석 프레임 워크 
Spark 프레임 워크의 구성 : 머신러닝, 스트림처리, SQL

RDD : 스파크가 다루는 추상적인 개체, 스파크의 본질
- 하둡과 달리 불러온 데이터를 RAM 위에 분산/저장
- transformation / action


# Install Process
- 스파크 설치(ubuntu vs code 통해)
- 스파크 환경변수 추가
- shell 새로고침 source.bashrc
- 설치 확인 echo $SPARK_HOME
- 터미널에서 파이썬 명령어 입력


# 분석 Process
- sc.parallelize([1,2,3,4,5]) 리스트 객체를 RDD에 저장
    - [1,2,3,4,5]를 rdd 객체로 변환
- map을 통한 데이터의 분리 후 reduce를 통해 집계
- .collect()를 실행해야만 결과 출력
- ramda라는 일회용 함수의 생성
- reduce 전에 sorting 필요함. (reduceByKey())
- hadoop과 연결 hadoop-3.3.6/sbin/start-all.sh (*오류 발생 => zeppelin으로 해결)

- acess_log 로 로컬에서 spark로 맵리듀싱
- https://www.mockaroo.com/ 랜덤 데이터 생성 
