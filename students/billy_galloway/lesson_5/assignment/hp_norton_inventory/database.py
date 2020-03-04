'''
Database 
interacts with the database via files formatted from csv files
'''
import sys
sys.path.append("./hp_norton_inventory")
import json
import logging
import csv_handler as csvh
from mongo_connect import *

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def import_data(directory_name, customer_file, product_file, rentals_file):
    ''' import data from csv files into database to be used in functions '''
    mongo = MongoDBConnection()
    csv_handler = csvh.CsvHandler()

    ERROR_COUNT = {
        'CUSTOMER_ERROR': 0,
        'PRODUCT_ERROR': 0,
        'RENTALS_ERROR': 0
    }

    INVENTORY_COUNT = {
        'customer_totals': 0,
        'product_totals': 0,
        'rental_totals': 0
    }

    customer_file = f'{directory_name}/{customer_file}'
    product_file = f'{directory_name}/{product_file}'
    rentals_file = f'{directory_name}/{rentals_file}'

    with mongo:
        # generate hpnorton_db
        hpnorton_db = mongo.connection.hpnorton_db

        # collections in database
        customers = hpnorton_db['customers']
        rentals = hpnorton_db['rentals']
        products = hpnorton_db['products']

        try:
            customer = csv_handler.generate_document_list(customer_file, "customer")
        except FileNotFoundError as error:
            logger.info(f' File not found {error}')
            ERROR_COUNT['CUSTOMER_ERROR']+=1

        try:
            product = csv_handler.generate_document_list(product_file, "product")
        except FileNotFoundError as error:
            logger.info(f' File not found {error}')
            ERROR_COUNT['PRODUCT_ERROR']+=1

        try:
            rental = csv_handler.generate_document_list(rentals_file, "rentals")
        except FileNotFoundError as error:
            logger.info(f' File not found {error}')
            ERROR_COUNT['RENTALS_ERROR']+=1
    
        # write to database
        try:
            customers.insert_many(customer)
            customer_totals = [customer_id for customer_id in customers.find()]
            INVENTORY_COUNT['customer_totals'] = len(customer_totals)
        except UnboundLocalError as error:
            logger.info(f' {error}')
            logger.info(ERROR_COUNT['CUSTOMER_ERROR'])
            ERROR_COUNT['CUSTOMER_ERROR']+=1

        try:
            products.insert_many(product)
            product_totals = [product_id for product_id in products.find()]
            INVENTORY_COUNT['product_totals'] = len(product_totals)
        except UnboundLocalError as error:
            logger.info(f' {error}')
            ERROR_COUNT['PRODUCT_ERROR']+=1

        try:
            rentals.insert_many(rental)
            rental_totals = [rental_id for rental_id in rentals.find()]
            INVENTORY_COUNT['rental_totals'] = len(rental_totals)
        except UnboundLocalError as error:
            logger.info(f' {error}')
            ERROR_COUNT['RENTALS_ERROR']+=1

        inventory_count = [INVENTORY_COUNT['customer_totals'],
                           INVENTORY_COUNT['product_totals'],
                           INVENTORY_COUNT['rental_totals']]

        error_count = [ERROR_COUNT['CUSTOMER_ERROR'],
                       ERROR_COUNT['PRODUCT_ERROR'],
                       ERROR_COUNT['RENTALS_ERROR']]

        return [tuple(inventory_count), tuple(error_count)]

def show_available_products():
    mongo = MongoDBConnection()

    with mongo:
        hpnorton_db = mongo.connection.hpnorton_db
        product_totals = [product for product in hpnorton_db.products.find()]
        available = [product_totals[i]['description'] for i in range(len(product_totals)) if int(product_totals[i]['quantity_available']) > 0]
        
        return available

def show_rentals(product_id):
    mongo = MongoDBConnection()

    with mongo:
        hpnorton_db = mongo.connection.hpnorton_db
        rental_totals = [rental for rental in hpnorton_db.rentals.find()]
        rented_unit = [rental_totals[i] for i in range(len(rental_totals)) if rental_totals[i]['product_id'] == product_id]
        
        return rented_unit

def main():
    ''' main method to interact with mongodb '''
    mongo = MongoDBConnection()

    output = import_data('old_database', 'customer.csv', 'product.csv', 'rentals.csv')
    logger.info(f' Total number of invetory and errors {output}')
    
    available = show_available_products()
    logger.info(f' Current list of available items: {available}')

    rentals = show_rentals('prd006')
    logger.info(f'{rentals}')
    with mongo:
        database = mongo.connection.hpnorton_db
        yorn = input("Drop data?")
        if yorn.upper() == 'Y':
            database['customers'].drop()
            database['rentals'].drop()
            database['products'].drop()

if __name__ == "__main__":
    main()
