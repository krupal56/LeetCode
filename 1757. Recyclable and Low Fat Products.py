import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    temp = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return temp[['product_id']]