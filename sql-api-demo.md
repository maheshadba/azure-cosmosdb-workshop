# Azure CosmosDB - SQL API Demo

## Concepts

- Core Concepts
  - Database
  - Collection
  - Scale by Request Units - RUs
  - Partition Key
  - Document - JSON, id
  - Indexing
  - Transactions
  - SDKs

- Distributed Concepts
  - Azure Regions
  - Replication
  - Single vs Multi-Master

- Server-Side Programming
  - Stored Procedure
  - Triggers; pre and post
  - UDF

- Interesting Features
  - Change Feed
  - TTL
  - Spatial Queries and GeoJSON

## Links

- Request Units: https://docs.microsoft.com/en-us/azure/cosmos-db/request-units
- Change Feed: https://docs.microsoft.com/en-us/azure/cosmos-db/change-feed
- Server Side: https://docs.microsoft.com/en-us/azure/cosmos-db/stored-procedures-triggers-udfs
- Common Use-Cases: https://docs.microsoft.com/en-us/azure/cosmos-db/use-cases

## pydocumentdb SDK in-a-nutshell

```
import pydocumentdb.document_client as document_client

client = document_client.DocumentClient(host, {'masterKey': key})
client.default_headers['x-ms-documentdb-query-enablecrosspartition'] = True

coll_link = ''dbs/dev/colls/map_points'

client.UpsertDocument(coll_link, some_json_doc)
```

## CosmosDB, Azure Maps, and Spatial Queries demonstration

See https://github.com/cjoakim/azure-web-services/blob/master/maps/readme_v2.md
