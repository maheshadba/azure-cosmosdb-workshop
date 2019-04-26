

# Chris Joakim, Microsoft, 2019/04/25

import csv, json, math, os, random, sys, time, ssl, traceback

from decimal import *
from faker import Faker

getcontext().prec = 6

class Main:

    def __init__(self):
        self.fake = Faker()
        self.fake.seed(4321)
        self.line_item_count_tup = (1,2,3,4,5,6,7,8,1,10)
        self.line_item_qty_tup = (1,2,3,4,5,6)
        self.price_tup = (0.99, 1.99, 2.99, 3.99, 4.99, 5.99, 9.99, 19.99, 49.99)
        self.order_lines = list()
        self.line_item_lines = list()
        self.delivery_lines = list()

    def order_fields(self):
        return 'Id,Date,StoreNumber,PaymentType,CreditCardNumber,SalesTax,OrderTotal'.split('.')

    def line_item_fields(self):
        return 'Id,OrderId,LineItem,SKU,Quantity,UnitPrice,SalesTax,ItemTotal'.split('.')

    def delivery_fields(self):
        return 'Id,OrderId,LineNumber,RequestedDate,ActualDate,Address,City,State,Zipcode'.split('.')

    def execute(self):
        if len(sys.argv) > 0:
            func = sys.argv[1].lower()
            print('function: {}'.format(func))

            if func == 'generate_csv':
                self.generate_csv()

            elif func == 'csv_to_documents':
                self.csv_to_documents()

            else:
                print('Error: invalid function: {}'.format(func))
        else:
            print('Error: no function argument provided.')

    def generate_csv(self):
        for order_number in range(1,11):
            li_count = random.choice(self.line_item_count_tup)
            print('order_number: {} li_count: {}'.format(order_number, li_count))
            for line_item_number in range(1, li_count+1):
                self.generate_random_line_item(order_number, line_item_number)

    def generate_random_line_item(self, order_number, line_item_number):
        # Id,OrderId,LineItem,SKU,Quantity,UnitPrice,SalesTax,ItemTotal
        qty = random.choice(self.line_item_qty_tup)
        up  = random.choice(self.price_tup)
        qxp = Decimal(qty * up) 
        tax = qxp * Decimal(0.05).quantize(Decimal('.01'), rounding=ROUND_DOWN)
        tax = Decimal(tax).quantize(Decimal('.01'), rounding=ROUND_DOWN)
        tot = Decimal(qxp + tax).quantize(Decimal('.01'), rounding=ROUND_DOWN)
        row = list()
        row.append(order_number)
        row.append(line_item_number)
        row.append(self.fake.license_plate().replace(' ','-').replace('•','-'))
        row.append(qty)
        row.append(up)
        row.append(str(tax))
        row.append(str(tot))
        print(row)
        self.line_item_lines.append(row)


    def csv_to_documents(self):
        pass



Main().execute()
