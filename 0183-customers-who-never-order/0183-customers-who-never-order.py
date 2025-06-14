import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    # Approach 1
    # df = pd.merge(customers, orders, how='left', left_on='id', right_on='customerId', indicator=True)
    # df = df[df['_merge'] == 'left_only']

    # return df[['name']].rename(columns={'name':'Customers'})

    # Approach 2
    df = customers[~customers['id'].isin(orders['customerId'])]

    return df[['name']].rename(columns={'name': 'Customers'})