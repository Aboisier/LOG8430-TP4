# Readme

## Setting up Cassandra

Execute the following queries.

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