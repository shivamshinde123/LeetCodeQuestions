import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    
    users['name'] = users['name'].str.capitalize()
    users.sort_values('user_id', ascending=True, inplace=True)

    return users