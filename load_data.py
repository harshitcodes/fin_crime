import pandas as pd
import os
from create_table import connect
from db_creds import *

dir_path = os.path.abspath(os.path.dirname(__file__))


currency_df = pd.read_csv(os.path.join(dir_path, './fct_data/currency_details.csv'))
fx_df = pd.read_csv(os.path.join(dir_path, './fct_data/fx_rates.csv'))
trans_df = pd.read_csv(os.path.join(dir_path, './fct_data/transactions.csv'))
users_df = pd.read_csv(os.path.join(dir_path, './fct_data/users.csv'))

url, con, meta = connect(USER, PASSWORD, DATABASE)

currency_df.to_sql('currency_details', con=con, if_exists = 'replace', index=False)
fx_df.to_sql('fx_rates', con=con, if_exists = 'replace', index=False)
users_df.to_sql('users', con=con, if_exists = 'replace', index=False)
currency_df.to_sql('transactions', con=con, if_exists = 'replace', index=False)