
# Multinational retail data centralisation Project
- This is my seconf project in the AiCore course
- In this project, we create a local PostgreSQL database. We upload data from various sources, process it, create a database schema and run SQL queries. 

# Installation instructions
Used Postgres, AWS (s3), boto3, rest-API, csv, Python (Pandas).

# Installation instructions
- Python programming

# Usage instructions
- Create a local PostgreSQL database. We upload data from various sources, process it, create a database schema and run SQL queries

# File structure of the project
- Data extraction. In "data_extraction.py" we store methods responsible for the upload of data into pandas data frame from different sources.
- Data cleaning. In "data_cleaning.py" we develop the class DataCleaning that clean different tables, which we uploaded in "data_extraction.py".
- Uploading data into the database. We write DatabaseConnector class "database_utils.py", which initiates the database engine based on credentials provided in ".yml" file.
- "main.py" contains methods, which allow uploading data directly into the local database. 

# License information
- Non required. Public repository.
