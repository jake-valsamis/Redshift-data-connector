import boto3
import os
import pandas as pd
import redshift_connector
import sys

if (len(sys.argv) >= 4):
    query = sys.argv[1]
    database = sys.argv[2]
    host = sys.argv[3]
    port = int(sys.argv[4])
    file_name = sys.argv[5]
    output_format = sys.argv[6]
else:
    query = "SELECT * FROM tickit.users"
    database = "sample_data_dev"
    host = "acmecorp-cfn-demo-endpoint-endpoint-tvuxknj0hc5lueze2pff.147080935342.us-east-1.redshift-serverless.amazonaws.com"
    port = 5439
    file_name = "users_table"
    output_format = "csv"

if host == "Default Host":
    host = "acmecorp-cfn-demo-endpoint-endpoint-tvuxknj0hc5lueze2pff.147080935342.us-east-1.redshift-serverless.amazonaws.com"
    
#set up and establish connection
client = boto3.client('redshift-serverless')

#if database secrets exist use them, otherwise use an assumed role
if "DATABASE_USERNAME" in os.environ:
    user=os.environ['DATABASE_USERNAME']
    password=os.environ['DATABASE_PASSWORD']
else:
    creds = client.get_credentials(
        workgroupName='default'
    )
    user=creds['dbUser']
    password=creds['dbPassword']

conn = redshift_connector.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)
cursor = conn.cursor()

#fetch table as dataframe
cursor.execute(query)
df = cursor.fetch_dataframe()

#preview table and save it as a csv
print(df.head())
# df.to_csv(f"../results/{file_name}.csv")  
match output_format: 
    case 'tsv': 
        print("I'm a tsv")
        df.to_csv(f"../results/{file_name}.tsv", sep='\t')
    case 'csv': 
        print("I'm a csv")
        df.to_csv(f"../results/{file_name}.csv")
    case 'parquet': 
        print("I'm a parquet")
        df.to_parquet(f"../results/{file_name}.parquet")
    case 'json': 
        print("I'm a json")
        df.to_json(f"../results/{file_name}.json")

#close connection
conn.close()