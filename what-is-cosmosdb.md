# What is CosmosDB?

![azure-cosmos-db](img/azure-cosmos-db.png)

- It's a **Family of NoSQL databases** built on a common PaaS foundation 

- Five Database Types Currently Supported
  - Microsoft:
    - SQL API
    - Table API
  - Open-Source:
    - MongoDB
    - Cassandra
    - Gremlin / TinkerPop

- You provision a specific type of database for each CosmosDB instance
  - One CosmosDB instance does not offer all five DB types!
  - Similar model to Azure HDInsight

- Programming APIs
  - SQL and Table
    - Microsoft publishes open-source libraries in DotNet, Java, Node.js, Python, Go, etc.
    - HTTP/REST also supported
  - MongoDB, Cassandra, Gremlin
    - Bring your own language and SDK library (i.e. - MongoDB, Python, and pymongo)

- Global Distribution
  - Deployable to [all 54 Azure Regions](https://docs.microsoft.com/en-us/azure/cosmos-db/regional-presence)
  - Single-Region
  - Multi-Region with one write-region
  - Multi-Region with multiple write-regions

- Elastic Scale
  - Simply Scale the Database by number of RUs 
  - Unit-of-measure is the [RU (Request Unit)](https://docs.microsoft.com/en-us/azure/cosmos-db/request-units)
  - A Unit of CPU, IOPS, and Memory
  - The cost to read a 1-KB item is 1.0 RU
  - Our SDKs return the cost of the DB operation in terms of RUs
  - Scale is achieved via **Partitions**

- Low Latency
  - 10ms reads, 15ms writes in 99th percentile
  - ![bell-curve](img/bell-curve.jpg)

- [Five Consistency Levels](https://docs.microsoft.com/en-us/azure/cosmos-db/consistency-levels)
  - Strong 
  - Bounded Staleness
  - Session
  - Consistent Prefix
  - Eventual

- SLAs
  - 99.99% single-region, 99.999% multi-region
  - See https://azure.microsoft.com/en-us/support/legal/sla/cosmos-db/v1_0/

## Links

- https://docs.microsoft.com/en-us/azure/cosmos-db/introduction
- https://docs.microsoft.com/en-us/azure/cosmos-db/
