import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    customers.rename(columns={'id':'customerId', 'name':'Customers'}, inplace=True)
    df = pd.merge(customers, orders, how='left', on='customerId', indicator=True)
    df = df[df['_merge'] == 'left_only']

    return df[['Customers']]
