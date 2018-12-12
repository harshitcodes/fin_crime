import pandas as pd
import os
from .create_table import connect

dir_path = os.path.abspath(os.path.dirname(__file__))


currency_df = pd.read_csv(os.path.join(dir_path, './fct_data/currency_details.csv'))
fx_df = pd.read_csv(os.path.join(dir_path, './fct_data/fx_rates.csv'))
# trans_df = pd.read_csv(os.path.join(dir_path, './fct_data/transactions.csv'))
users_df = pd.read_csv(os.path.join(dir_path, './fct_data/users.csv'))


