from pyspark import SparkContext

# 스파크 객체 불러오기
sc = SparkContext()

file_path = '/home/ubuntu/dmf/spark/0.RDD/input.txt'
lines = sc.textFile(file_path)

# 공백 기준으로 쪼갠 후 한줄의 데이터로 뭉치기
words = lines.flatMap(lambda line: line.split())
# print(words.collect())

# 단어별 빈도수 세기
mapped_words = words.map(lambda word: (word, 1))
#print(mapped_words.collect())

reduced_words = mapped_words.reduceByKey(lambda a,b: a+b)
print(reduced_words.collect())