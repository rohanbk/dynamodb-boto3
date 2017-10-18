import boto3
import json
import decimal
import os

dynamodb = boto3.resource('dynamodb')
tableName = ''
rootdir = ''

if rootdir == '':
    rootdir = input('What is the root-dir of the JSON files you wish to upload to DynamoDB? ')
if tableName == '':
    tableName = input('What is the name of the table you wish to upload the JSON into? ')

table = dynamodb.Table(tableName)

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        selected = subdir + file
        try:
            with open(selected, encoding="UTF-8") as json_file:
                rows = json.load(json_file, parse_float=decimal.Decimal)

                for row in rows:
                    row['id'] = str(row['id'])

                    table.put_item(Item=row)
        except Exception as e:
            print("error: " + e)

print('Script finished...')