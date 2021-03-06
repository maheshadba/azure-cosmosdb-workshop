# What is a NoSQL Database?

![nosql-history](img/nosql-history.png)

## Definition

- [Wikipedia](https://en.wikipedia.org/wiki/NoSQL)
- Defined more by what it isn't than what exactly it is
- It's a **Family** of databases; there is no "NoSQL Standard"
- **Non-Relational**
- **No Referential Integrity**
- Doesn't support **ANSI SQL Standards**, but may offer "SQL-like" syntaxes
- **Less support for Transactions**
- **Schemaless** or simplified schema
- Often [JSON](https://en.wikipedia.org/wiki/JSON) document-oriented
- Forrester: https://azure.microsoft.com/en-us/blog/microsoft-s-azure-cosmos-db-is-named-a-leader-in-the-forrester-wave-big-data-nosql/

## Reasons NoSQL Databases arose?

- Horizontal scaling; designed for massive scale
- Technology has evolved; disk is inexpensive now.  Y2K, CW50
- Designed to solve different problems
- Speed of Development - schemaless
- JavaScript resurgence, end-to-end JSON.  Node.js, MEAN Stack, Isomorphic
- [Object-Relational Impedance Mismatch](https://en.wikipedia.org/wiki/Object-relational_impedance_mismatch)

## Example NoSQL Databases

### Column
- **Cassandra**, HBase

### Document
- **CosmosDB**, **MongoDB**, Couchbase, Apache CouchDB

### Key-value
- **CosmosDB Table API**, Redis, Riak, MemcacheD

### Graph
- **Apache TinkerPop (Gremlin API)**, Neo4J, Apache Giraph
