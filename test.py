from pg.pg import Pg
pg = Db(dbname='postgres', user='postgres', password='admin', host='localhost', port='5432')

#create schema
pg.create_schema('name', db'sdss')