# azure-cosmosdb-workshop

## Modeling: Relational to Document 

A Retail Order with two Line Items

### CSV / Relational Data 

Order Table:
```
order_id,date,payment_type,credit_card_num,tax,total
8,2019/04/27,ccard,377743182720649,1.63,34.59
```

Line Items Table:
```
order_id,line_num,sku,quantity,price,tax,total
8,1,834DB,3,9.99,1.49,31.46
8,2,IDG-8746,1,2.99,0.14,3.13
```

### Single Document 

```
{
    "pk": 8,
    "order_id": 8,
    "date": "2019/04/27",
    "pmt_type": "ccard",
    "ccard": "377743182720649",
    "tax": "1.63",
    "total": "34.59",
    "items": [
        {
            "order_id": 8,
            "line_num": 1,
            "sku": "834DB",
            "qty": 3,
            "unit": 9.99,
            "tax": "1.49",
            "total": "31.46"
        },
        {
            "order_id": 8,
            "line_num": 2,
            "sku": "IDG-8746",
            "qty": 1,
            "unit": 2.99,
            "tax": "0.14",
            "total": "3.13"
        }
    ]
}
```

### Multiple Documents

```
{
    "doctype": "order",
    "pk": 8,
    "order_id": 8,
    "date": "2019/04/27",
    "pmt_type": "ccard",
    "ccard": "377743182720649",
    "tax": "1.63",
    "total": "34.59",
}

{
    "doctype": "item",
    "pk": 8,
    "order_id": 8,
    "line_num": 1,
    "sku": "834DB",
    "qty": 3,
    "unit": 9.99,
    "tax": "1.49",
    "total": "31.46"
}

{
    "doctype": "item",
    "pk": 8,
    "order_id": 8,
    "line_num": 2,
    "sku": "IDG-8746",
    "qty": 1,
    "unit": 2.99,
    "tax": "0.14",
    "total": "3.13"
}
```