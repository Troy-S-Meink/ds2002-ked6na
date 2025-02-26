#!/bin/bash
set -e

## Part i #
## Assign a variable to the image URL
#curl https://www.freepnglogos.com/uploads/dog-png/bow-wow-gourmet-dog-treats-are-healthy-natural-low-4.png > dog.png
#
## Upload the image to the bucket
#aws s3 cp dog.png s3://ds2002-ked6na/
#
## Part ii #
## Pre-sign a 1 minute url
#aws s3 presign --expires-in 60 s3://ds2002-ked6na/dog.png



# Part iii #
# Modify the code above to take positional arguments
# Pass argument 1 as the file
upload_file=$1
# Pass argument 2 as the bucket
aws_bucket=$2
# Pass argument 3 as the timer
timer=$3

# Add the file to the bucket
aws s3 cp $upload_file $aws_bucket

# Generate the URL
aws s3 presign --expires-in $timer $aws_bucket$upload_file