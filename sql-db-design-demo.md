# Azure CosmosDB - SQL API Design

## Concepts

- Core Concepts
  - Database
  - Collection
  - [Scale by Request Units](https://docs.microsoft.com/en-us/azure/cosmos-db/request-units)
  - Partition Key
  - Document - JSON, id
  - Indexing
  - Transactions
  - SDKs

## Design Thoughts

- Don't Port Relational Designs
- It's Schemaless
- Think first of how your data will be queried, not what it looks like
- Use a Generic Partition Key name
- Prototype designs with YOUR data and observe the RU costs
- Use the Metrics information in Azure Portal
- https://docs.microsoft.com/en-us/azure/cosmos-db/modeling-data
- https://devblogs.microsoft.com/premier-developer/designing-a-cosmos-db-database/

## Use-Case Discussions

- Regional Data and Partition Keys
- Retail example: Order, Line Items, Deliveries, Service
- Duplication: Not necessarily bad as in Relational DBs
  - Product Catalog and Store Inventory example
