import boto3
import urllib
import logging
from botocore.exceptions import ClientError

s3 = boto3.client('s3', region_name='us-east-1')

# Part 1 #
# Fetch a PDF (the Challenger disaster Rogers 
# Commission Report) from the internet
url = "https://sma.nasa.gov/SignificantIncidents/assets/rogers_commission_report.pdf"
output_file = "rogers_commission_report.pdf"

# Download the PDF file
urllib.request.urlretrieve(url, output_file)

print('Part 1: Success!')

# Part 2 #
# Upload the PDF to a bucket in S3
bucket = 'ds2002-ked6na'
local_file = 'rogers_commission_report.pdf'

# Open and read the file
with open(local_file, 'rb') as file:
    # Upload the file to the bucket
    resp = s3.put_object(
        Body=file.read(),
        Bucket=bucket,
        Key=local_file
    )

print('Part 2: Success!')

# Part 3 #
# Presign a URL for the file w/ an expiration time
expiration = 60   # The expiration time in sec

# Use a try-catch statement to generate a URL 
# for the file with an expiration time.
try:
    response = s3.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': local_file}, ExpiresIn=expiration)

except ClientError as e:
    logging.error(e)

print('Part 3: Success!')

# Part 4 #
# Output the presigned URL
print('URL: ', response)
print('Expires in: ', expiration)

print('Part 4: Success!')