#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from pyspark.mllib.fpm import FPGrowth
from pyspark import SparkContext, SparkConf

import pyspark_cassandra
from pyspark_cassandra import CassandraSparkContext

if __name__ == "__main__":
    conf = SparkConf() \
    	.setAppName("Frequent Products") \
    	.setMaster("spark://192.168.56.1:7077") \
    	.set("spark.cassandra.connection.host", "127.0.0.1")

    sc = CassandraSparkContext(conf=conf)
    
    transactions = sc.cassandraTable("receipts", "receipts") \
                .select("products") \
                .map(lambda r: list(r["products"].keys()))

    model = FPGrowth.train(transactions, minSupport=0.2, numPartitions=10)
    result = model.freqItemsets().collect()
    for fi in result:
        print(fi)