#Step 8: Upload the cleaned data to the database

from data_cleaning import DataCleaning
from data_extraction import DataExtractor
from database_utils import DatabaseConnector

if __name__ == "__main__":
    data_extractor = DataExtractor()
    table_name = data_extractor.list_db_tables()[0]  
    user_data = data_extractor.read_rds_table(table_name)

    data_cleaner = DataCleaning()
    cleaned_user_data = data_cleaner.clean_user_data(user_data)

    db_connector = DatabaseConnector()
    db_connector.upload_to_db(cleaned_user_data, 'dim_users')


# ms2 task 4 step 4

if __name__ == "__main__":

    pdf_link = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
    data_extractor = DataExtractor()
    pdf_data = data_extractor.retrieve_pdf_data(pdf_link)

    data_cleaner = DataCleaning()
    cleaned_card_data = data_cleaner.clean_card_data(pdf_data)

    db_connector = DatabaseConnector()
    db_connector.upload_to_db(cleaned_card_data, 'dim_card_details')
