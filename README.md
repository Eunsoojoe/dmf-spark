# Spark
Spark : 대용량 데이터 처리를 위한 분석 프레임 워크 
Spark 프레임 워크의 구성 : 머신러닝, 스트림처리, SQL

RDD : 스파크가 다루는 추상적인 개체, 스파크의 본질
- 하둡과 달리 불러온 데이터를 RAM 위에 분산/저장
- transformation / action

<br>

# Install Process
- 스파크 설치(ubuntu vs code 통해)
- 스파크 환경변수 추가
- shell 새로고침 source.bashrc
- 설치 확인 echo $SPARK_HOME
- 터미널에서 파이썬 명령어 입력

<br>

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

<br>

# zeppelin을 통해 웹에서 빅데이터 분석
- spark : 빅데이터 분석을 위한 프레임 워크
- zeppelin : spark를 사용하는 jupyternoetbook (둘 모두 scala 베이스)

1. `spark-3.1.2`,  `zeppelin-0.10.1`, `airline data` 설치
2. 압출 풀기 `tar -zxvf`
3. 환경변수 등록 : 패스 등록 시 경로를 일일이 입력해야 하는 것을 방지 / 편의성 높이고자
    - 최신 spark 버전 주석처리 후 등록
4. `zeppelin-0.10.1 > conf > zeppelin-site.xml` 에서 서버 변경
     - 로컬 -> 0.0.0.0 : 모든 address 허용 
     - 9090 : 스파크와의 서버 중복 방지
5. zeppelin 실행 : zeppelin-daemon.sh start
6. localhost 연결 / interpeter > spark > 설정
7. %pyspark / sc : zepplin과 spark 연결
8. 하둡에 다운받은 airline을 올려 spark로 분산 처리
    - 하둡 실행 (sbin/start-all.sh)
    - 하둡에 한번에 업로드 (sh airline.sh)
9. zeppelin 에서 airline data 집계
    - /home/ubuntu/hadoop-3.3.6/bin/hdfs dfs -ls /user/ubuntu/input/airline : 로컬과 원격 모두에서 데이터 확인
    - spark.read.text('/user/ubuntu/input/airline')
    - 데이터 프레임화 
10. 데이터 분석
    - 스키마 확인 : `printSchema()`
    - 가독성 높이기 위해 z.show(df)

