[![Code Ocean Logo](images/CO_logo_135x72.png)](http://codeocean.com/product)

<hr>

# Redshift Data connector

This is a generic Redshift connector which will query a Redshift database and save the result as a csv file. 

## Secrets

This capsule requires one of two secret types which grant access to the database. 

1. An assumable role configured by your admin.
2. Database Credentials created in the User Secrets section of the Account page. 

## Input Data

None

## Output Data

**output**: Stderr output

**output_file_name.csv**: csv file containing the output for the query where output_file_name will be based on the "Output File Name" parameter. 

## App Panel Parameters

### Query Parameters

SQL Query
- Query to execute 

### Redshift Parameters

Database
- The Redshift database to query. 

Host
- Hostname address in the form [name].[id].[region].redshift.amazonaws.com or [name].[id].[region].redshift-serverless.amazonaws.com

Port
- Port number for your Redshift endpoint (usually 5439). 

### Output Parameters

Output File Name
- File name to use for the query output. Note that this should not include the file extension or any special characters. 

<hr>

[Code Ocean](https://codeocean.com/) is a cloud-based computational platform that aims to make it easy for researchers to share, discover, and run code.<br /><br />
[![Code Ocean Logo](images/CO_logo_68x36.png)](https://www.codeocean.com)


