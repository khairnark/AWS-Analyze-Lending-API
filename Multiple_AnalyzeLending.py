#Import Python Packages
import boto3
from textractcaller import call_textract_lending
from textractprettyprinter.t_pretty_print import convert_lending_from_trp2
import trp.trp2_lending as tl
import csv

s3=boto3.resource('s3')
BUCKET_NAME = 'bucketname'
allFiles = s3.Bucket(BUCKET_NAME).objects.all()

for file in allFiles:
    if file.key.endswith('pdf'):
        s3uri = 's3://'+BUCKET_NAME+'/'+ file.key
        print(s3uri)
        print("===============")
        textract_client = boto3.client('textract', region_name='us-east-1')
        textract_json = call_textract_lending(input_document=s3uri, boto3_textract_client=textract_client)
        print(textract_json)
        trp2_doc: tl.TFullLendingDocument = tl.TFullLendingDocumentSchema().load(textract_json)
        lending_array = convert_lending_from_trp2(trp2_doc)
         for row in lending_array:
             print(row)
        with open("file.csv", "a", newline ="") as output_f:
            csv_writer = csv.writer(output_f)
             csv_writer.writerows(lending_array)
