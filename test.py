from pg.pg import Pg
pg = Pg(dbname='sdss', user='postgres',
        password='gicait123', host='localhost', port='5432')

# create schema
pg.get_all_values('auth_user', "public")
print(pg.get_columns_names('auth_user'))
