# Readme

## Setting up Cassandra
1. Download and Install the latest Cassandra Distribution for Windows from [here](https://academy.datastax.com/planet-cassandra//cassandra)
2. Run {installation dir}/bin/cassandra.bat
3. Run {installation dir}/bin/cqlsh.bat  and execute the following queries:
```cql
CREATE KEYSPACE receipts
WITH replication = {
	'class' : 'SimpleStrategy',
	'replication_factor' : 1
};

CREATE TABLE receipts.receipts (
	id uuid,
	products MAP<text, varint>,
	PRIMARY KEY (id)
);
```

## Setting up Spark
1. Download and install the latest distribution of spark-standalone/pyspark  from [here]()
2. Run {installation dir}/bin/spark-class.cmd org.apache.spark.deploy.master.Master
3. In 2 other separate command prompts, run {installation dir}/bin/spark-class.cmd org.apache.spark.deploy.worker.Worker spark://localhost:7077

## Setting up the REST Server
1. Navigate to the "REST Api" folder.
2. Rename the `.env.example` file to `.env` and set the environment variables with your values.
3. In a command prompt, execute the following commands:
```
npm i
npm run serve
```

## Using the system through the REST API

### Add receipt

```cURL
curl -X POST \
  'http://localhost:3000' \
  -H 'Content-Type: application/json' \
  -d '{ "id": "c534cf02-e8f3-11e8-9f32-f2801f1b92d1", 
        "products": { "Tomato": 10, "Banana": 123 }  
      }'
```

### Get products

```cURL
curl -X GET 'http://localhost:3000'
```

### Get frequent products

```cURL
curl -X GET 'http://localhost:3000/frequent'