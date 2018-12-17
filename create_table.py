import pandas as pd
from odo import odo
import sqlalchemy
from db_creds import *
from sqlalchemy import String, Integer, BigInteger, VARCHAR, \
        DateTime, Table, Column, Date, Boolean, FLOAT
from sqlalchemy.dialects.postgresql import UUID


def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return url, con, meta


url, con, meta = connect(USER, PASSWORD, DATABASE)

transactions = Table('transactions', meta,
    Column('currency', String, nullable = False),
    Column('amount', BigInteger, nullable=False),
    Column('state', VARCHAR(25), nullable=False),
    Column('created_date', DateTime, nullable=False),
    Column('merchant_category', VARCHAR(100)),
    Column('merchant_country', VARCHAR(3)),
    Column('entry_method', VARCHAR(4), nullable=False),
    Column('user_id', UUID, nullable=False),
    Column('type', VARCHAR(20), nullable=False),
    Column('source', VARCHAR(20), nullable=False),
    Column('id', UUID, primary_key=True),
)

users = Table("users", meta, 
    Column("id", UUID, primary_key = True),
    Column("has_email", Boolean, nullable=False),
    Column("phone_country", VARCHAR(300)),
    Column("terms_version", Date),
    Column("created_date", DateTime, nullable=False),
    Column("state", VARCHAR(25), nullable=False),
    Column("country", VARCHAR(2)),
    Column("birth_year", Integer),
    Column("kyc", VARCHAR(20),),
    Column("failed_sign_in_attempts", Integer)
)

fx_rates = Table("fx_rates", meta,
    Column("base_ccy", VARCHAR(3)),
    Column("ccy", VARCHAR(10)),
    Column("rate", FLOAT(precision = 2))
)

currency_details = Table("currency_details", meta,
    Column("ccy", VARCHAR(10), primary_key=True),
    Column("iso_code", Integer),
    Column("exponent", Integer),
    Column("is_crypto", Boolean, nullable=False)
)

meta.create_all(con)
