
## Agenda

  - https://github.com/cjoakim/azure-cosmosdb-workshop/blob/master/agenda.md

## What is NoSQL?

  - https://github.com/cjoakim/azure-cosmosdb-workshop/blob/master/what-is-nosql.md

## What is CosmosDB?

  - https://github.com/cjoakim/azure-cosmosdb-workshop/blob/master/what-is-cosmosdb.md 
  - Use-Cases

## Demo 1 - Azure Maps w/SQL API

  - https://github.com/cjoakim/azure-cosmosdb-workshop/blob/master/sql-api-demo.md
  - https://github.com/cjoakim/azure-web-services/blob/master/maps/readme_v2.md

|DB|Collection|Partition Key|RU|
|--- |--- |--- |--- |
|dev|map_points|/pk|10,000|
|dev|map_points_live|/pk|10,000|


#### Invoke the Maps API, Write to CosmosDB, Gen HTML

Show the locations.csv file

See Route API:
https://docs.microsoft.com/en-us/rest/api/maps/route/getroutedirections


```
cd ~/github/azure-web-services/maps/python
sba
./get_routes_v2.sh  ( gets 3 routes per locations.csv )
```

See a new Document in Azure Portal, with GeoJSON

#### Start the Py Webserver

```
~/github/azure-web-services/maps/python
./webserver.sh
```

Visit http://localhost:3000/web/animated_path_1_2.html
Or http://localhost:3000/web_bak/animated_path_1_2.html

#### Query CosmosDB 

See **Query Explorer** in Azure Portal

Count the points on Route1: Microsoft Charlotte to Davidson College
```
SELECT VALUE COUNT(1) FROM c where c.pk = 1   (487)
```

Closest point to SouthPark mall along the route?
```
SELECT * FROM c WHERE ST_DISTANCE(c.location, {'type': 'Point', 'coordinates':[-80.832353, 35.151622]}) < 7092 
and c.pk = 1
```

---

## Demo 2 - 6-Degrees of Kevin Bacon w/Graph API

- https://github.com/cjoakim/azure-cosmosdb-workshop/blob/master/gremlin-graph-demo.md

- https://github.com/cjoakim/azure-cosmosdb-graph-node

- https://www.imdb.com/interfaces/

#### Webserver

In another Terminal
```
./webserver.sh
```

#### Queries

```
node main.js dev movies query path lori_singer charlotte_rampling
node main.js dev movies query path lori_singer bradley_cooper
node main.js dev movies query path lori_singer keanu_reeves
```