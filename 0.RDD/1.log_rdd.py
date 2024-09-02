from pyspark import SparkContext

sc = SparkContext()

file_path = 'file:///home/ubuntu/dmf/spark/0.RDD/access.log'
lines = sc.textFile(file_path)

# print(lines.collect())

# 1. map
mapped_lines = lines.map(lambda line: line.split())
# print(mapped_lines.collect())
mapped_lines.foreach(print)    # 결과가 개행이 되어 출력

# 2-1. filter (4xx code만 출력)
def filter_4xx(line): 
    return line[6][0] == '4'

filtered_lines = mapped_lines.filter(filter_4xx)
# filtered_lines.foreach(print)

# 2-2. filter (POST & /product)
def filter_post_product(line):
    return line[3] == '"POST' and 'product' in line[4]

filtered_log = mapped_lines.filter(filter_post_product)
# filtered_log.foreach(print)

# 3. reduce
# 3-1. method별 요청수
method_rdd = mapped_lines.map(lambda line: (line[3], 1)) \
    .reduceBykey(lambda a, b: a+b)
method_rdd.foreach(print)

