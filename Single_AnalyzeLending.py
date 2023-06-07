#Import Required Python Packages
import boto3
from textractcaller import call_textract_lending
from textractprettyprinter.t_pretty_print import convert_lending_from_trp2
import trp.trp2_lending as tl

input_file = "s3://BUCKET_NAME/FILENAME.pdf"
textract_client = boto3.client('textract', region_name='us-east-1')
textract_json = call_textract_lending(input_document=input_file, boto3_textract_client=textract_client)
print(textract_json)
