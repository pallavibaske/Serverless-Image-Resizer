import boto3
import os
from PIL import Image
from urllib.parse import unquote_plus

s3 = boto3.client('s3')

def lambda_handler(event, context):

    print("Lambda Triggered")

    # Get bucket name
    bucket_name = event['Records'][0]['s3']['bucket']['name']

    # Get uploaded file name
    object_key = unquote_plus(
        event['Records'][0]['s3']['object']['key']
    )

    print("Uploaded File:", object_key)

    # Temporary file paths
    download_path = "/tmp/input-image"
    upload_path = "/tmp/output-image.jpg"

    # Download image
    print("Downloading image...")
    s3.download_file(
        bucket_name,
        object_key,
        download_path
    )
    print("Image downloaded successfully")

    # Open image
    image = Image.open(download_path)

    print("Original Mode:", image.mode)
    print("Original Size:", image.size)

    # Resize image
    image = image.resize((300, 300))

    print("Image resized")

    # Convert image to RGB if needed
    if image.mode != "RGB":
        image = image.convert("RGB")
        print("Converted image to RGB")

    # Save as JPEG
    image.save(
        upload_path,
        "JPEG",
        optimize=True,
        quality=50
    )

    print("Compressed image saved")

    # Create output filename
    filename = os.path.splitext(os.path.basename(object_key))[0]
    output_key = f"output/{filename}.jpg"

    # Upload resized image
    s3.upload_file(
        upload_path,
        bucket_name,
        output_key
    )

    print("Output uploaded successfully")

    return {
        "statusCode": 200,
        "body": f"Image processed successfully: {output_key}"
    }
