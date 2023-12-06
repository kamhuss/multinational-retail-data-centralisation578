#Step 6: Create a method clean_user_data in the DataCleaning class

import pandas as pd
from data_extraction import DataExtractor


class DataCleaning:
    def clean_user_data(df):
        db_datacleaning= DataExtractor()
        # Implement cleaning logic. e.g. handling NULL values, fixing date errors, etc.
        
        return df

# ms2 task 4 step 3
import pandas as pd
from data_extraction import DataExtractor

class DataCleaning:
    def clean_card_data(df):
        # Implement cleaning logic. e.g. handling NULL values, fixing date errors, etc.

        return(df)

# ms2 task 5 step 4-5
class DataCleaning:
    def __init__(self):
        pass

    def clean_store_data(self, raw_data):
        # Implement data cleaning
        df = pd.DataFrame(raw_data)

        return df

    def upload_to_db(self, df, table_name):
        
        pass

# ms2 task 6 step 2-4

class DataCleaning:
    def __init__(self):
        pass

    def convert_product_weights(self, products_df):
        products_df['weight'] = products_df['weight'].apply(self.convert_weight)
        return products_df

    def convert_weight(self, weight):
        
        if 'g' in weight:
            return float(weight.replace('g', '').strip()) / 1000
        elif 'ml' in weight:
            return float(weight.replace('ml', '').strip()) / 1000
        else:
            return float(weight)

    def clean_products_data(self, products_df):
        cleaned_df = products_df.dropna()
        return cleaned_df


# ms2 task 7

class DataCleaning:
    def __init__(self):
        pass

    def clean_orders_data(self, orders_df):
        orders_df = orders_df.drop(['first_name', 'last_name', '1'], axis=1)
        return orders_df

