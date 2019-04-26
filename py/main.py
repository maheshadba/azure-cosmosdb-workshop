

# Chris Joakim, Microsoft, 2019/04/25

import csv, json, math, os, random, sys, time, ssl, traceback

from decimal import *
from faker import Faker

import arrow

getcontext().prec = 6

class Order:

    def __init__(self, id):
        self.id = id
        self.fields = list()

class LineItem:

    def __init__(self, order_id, id):
        self.order_id = id
        self.id = id
        self.fields = list()

class Main:

    def __init__(self):
        self.fake = Faker()
        self.fake.seed(4321)
        self.line_item_count_tup = (1,2,3,4,5,6,7,8,1,10)
        self.line_item_qty_tup = (1,2,3)
        self.price_tup = (0.99, 1.99, 2.99, 3.99, 4.99, 5.99, 9.99, 19.99, 49.99, 999.99)
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

    def generate_csv_orig(self):
        for order_number in range(1,11):
            li_count = random.choice(self.line_item_count_tup)
            print('order_number: {} li_count: {}'.format(order_number, li_count))
            for line_item_number in range(1, li_count+1):
                self.generate_random_line_item(order_number, line_item_number)


    def generate_csv_orig(self):

        date = arrow.utcnow().format('YYYY-MM-DD')
        curr_order_num, curr_order = -1, list()
        curr_order_tax, curr_order_tot = Decimal(0), Decimal(0)

        for order_number in range(1,11):
            li_count = random.choice(self.line_item_count_tup)
            print('order_number: {} li_count: {}'.format(order_number, li_count))
            for line_item_number in range(1, li_count+1):
                self.generate_random_line_item(order_number, line_item_number)

        for line_item in self.line_item_lines:
            onum = line_item[0]
            if onum == curr_order_num:
                item_tax, item_tot = line_item[-2], line_item[-1]
                curr_order_tax = curr_order_tax + Decimal(item_tax)
                curr_order_tot = curr_order_tot + Decimal(item_tot)
            else:
                if len(curr_order) > 0:
                    curr_order.append(str(curr_order_tax))
                    curr_order.append(str(curr_order_tot))
                    self.order_lines.append(curr_order)
                    curr_order_tax, curr_order_tot = Decimal(0), Decimal(0)
                
                # Id,Date,StoreNumber,PaymentType,CreditCardNumber,SalesTax,OrderTotal
                curr_order_num = onum
                curr_order = list()
                curr_order.append(onum)
                curr_order.append(date)
                curr_order.append(random.randint(1,1000))
                curr_order.append(self.fake.credit_card_number(card_type=None))

        if len(curr_order) > 0:
            curr_order.append(str(curr_order_tax))
            curr_order.append(str(curr_order_tot))
            self.order_lines.append(curr_order)
            curr_order_tax, curr_order_tot = Decimal(0), Decimal(0)

        for line_item in self.line_item_lines:
            item_tot = Decimal(line_item[-1])
            if item_tot > 999:
                print('delivery: {}'.format(line_item))

        for line_item in self.line_item_lines:
            print('line_item: {}'.format(line_item))
        for order in self.order_lines:
            print('order: {}'.format(line_item))
        for delivery in self.delivery_lines:
            print('delivery: {}'.format(line_item))

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
        self.line_item_lines.append(row)


    def csv_to_documents(self):
        pass



Main().execute()
