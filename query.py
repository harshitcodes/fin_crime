from connection import connect
from db_creds import *

url, con, meta = connect(USER, PASSWORD, DATABASE)

query1 = con.execute("""WITH processed_users AS (
SELECT left(u.phone_country, 2) AS short_phone_country, u.id 
FROM users u
)
SELECT t.user_id, 
t.merchant_country,
sum(t.amount / fx.rate / power(10, cd.exponent)) AS amount 
FROM transactions t
JOIN fx_rates fx ON (fx.ccy = t.currency AND fx.base_ccy = 'EUR')
JOIN currency_details cd ON cd.currency = t.currency
JOIN processed_users pu ON pu.id = t.user_id
WHERE t.source = 'GAIA'
AND pu.short_phone_country = t.merchant_country
GROUP BY t.user_id, t.merchant_country
ORDER BY amount DESC;"""
)

query2 = con.execute("""
With cash_amt AS (
    select user_id,
    created_date,
    state,
    type,
    txn.amount / fx.rate / power(10, cd.exponent) AS cash_amount
    from transactions txn
    JOIN fx_rates fx ON (fx.ccy = txn.currency AND fx.ccy = 'USD')
    JOIN currency_details cd ON cd.currency = txn.currency
)
select cash_amt.user_id, cash_amt.created_date, cash_amt.cash_amount
from (select user_id, MIN(created_date) AS first
    from cash_amt
    group by user_id) first_txn
JOIN cash_amt ON first_txn.user_id = cash_amt.user_id and first_txn.first = cash_amt.created_date
where cash_amt.cash_amount > 10 and state = 'COMPLETED' and type = 'CARD_PAYMENT'
;
"""
)

for i in query2:
    print(i)
print(query2.rowcount)

# results = meta.tables['transactions']
# print(results.c)

# columns = meta.tables['users']
# # print(columns.c)
# for i in query1:
#     print(i)

# print(query1.rowcount)