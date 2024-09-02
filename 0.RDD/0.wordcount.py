from pyspark import SparkContext, SparkConf

# 하둡에서 파일을 읽기 위한 (spark와 yarn이 협업)
conf = SparkConf().setMaster('yarn')    # hadoop 접근시 yarn이 필요함.

# 스파크 객체 불러오기
sc = SparkContext(conf=conf)

# 로컬에서 파일 읽기
# file_path = '/home/ubuntu/dmf/spark/0.RDD/input.txt'
# lines = sc.textFile(file_path)

# HDFS에서 파일 읽기(hdfs 프로토콜)
file_path = 'hdfs://localhost:9000/user/ubuntu/input/input.txt'
lines = sc.textFile(file_path)


# 공백 기준으로 쪼갠 후 한줄의 데이터로 뭉치기
words = lines.flatMap(lambda line: line.split())
# print(words.collect())

# 단어별 빈도수 세기
mapped_words = words.map(lambda word: (word, 1))
#print(mapped_words.collect())

reduced_words = mapped_words.reduceByKey(lambda a,b: a+b)    #key값이 같은 친구들끼리만 더해줌.
print(reduced_words.collect())

# 위 코드가 돌면 sparkcontext 종료시키기
sc.stop()