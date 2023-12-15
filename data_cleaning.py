#Step 6: Create a method clean_user_data in the DataCleaning class

import pandas as pd
from data_extraction import DataExtractor

class DataCleaning:
         
    def clean_user_data(self,df):
        df = self.clean_invalid_date(df,'date_of_birth')
        df = self.clean_invalid_date(df,'join_date')        
        df = self.clean_NaNs_Nulls_misses(df)
        df.drop(columns='1',inplace=True)
        return df

# ms2 task 4 step 3
    
    def clean_card_data(self,df):
        df['card_number'] = df['card_number'].apply(str)
        df['card_number'] = df['card_number'].str.replace('?','')
        df = self.clean_invalid_date(df,'date_payment_confirmed')  
        df.dropna(how='any',inplace= True)
        return df

# ms2 task 5 step 4-5
    def __init__(self):
        pass
      
    def called_clean_store_data(self,df):
        df.drop(columns='lat',inplace=True)
        df = self.clean_invalid_date(df,'opening_date')                     
        df['staff_numbers'] =  pd.to_numeric( df['staff_numbers'].apply(self.remove_char_from_string),errors='coerce', downcast="integer") 
        df.dropna(subset = ['staff_numbers'],how='any',inplace= True)
        return df

    def upload_to_db(self, df, table_name):
        
        pass

# ms2 task 6 step 2-4
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
    def __init__(self):
        pass
    
    def clean_orders_data(self,df):
        df.drop(columns='1',inplace=True)
        df.drop(columns='first_name',inplace=True)
        df.drop(columns='last_name',inplace=True)
        df.drop(columns='level_0',inplace=True)
        df['card_number'] = df['card_number'].apply(self.isDigits)
        df.dropna(how='any',inplace= True)
        return df

