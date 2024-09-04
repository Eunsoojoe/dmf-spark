from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import split, col, max, min, mean

file_path = '/home/ubuntu/dmf/spark/2.sparksql/access.log'

spark = SparkSession.builder.getOrCreate()

schema = StructType([
    StructField('ip', StringType()),
    StructField('date', StringType()),
    StructField('time', StringType()),
    StructField('url', StringType()),
    StructField('status', IntegerType()),
    StructField('bytes', IntegerType()),
])

df = spark.read.csv(file_path, schema=schema, sep=' ')

# sql로 접근할 수 있는 임시 테이블 생성 
df.createOrReplaceTempView('log')

# 파이썬 함수문을 통해 sql 호출

# 전체 데이터 확인
# spark.sql('''
#     SELECT * FROM log LIMIT 10;
# ''').show()

# status code == 200
# spark.sql('''
#     SELECT * FROM log
#     WHERE status = 200
# ''').show()

# method GET & path product
# spark.sql('''
#     SELECT * FROM log
#     WHERE url LIKE '%GET%' AND url LIKE '%/product/%'
# ''').show()

# method, status code별 count
spark.sql('''
    SELECT status, count(*) FROM log
    GROUP BY status
''').show()