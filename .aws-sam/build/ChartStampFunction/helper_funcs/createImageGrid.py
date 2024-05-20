from PIL import Image
from aws_jserver import upload_object_to_s3, generate_presigned_url
import io
from datetime import datetime

bucket_name = "chart-stamp"

def createImage(chart_1h, chart_4h, chart_1d, chart_1w, ticker):
    img_01 = Image.open(io.BytesIO(chart_1w))
    img_02 = Image.open(io.BytesIO(chart_1d))
    img_03 = Image.open(io.BytesIO(chart_4h))
    img_04 = Image.open(io.BytesIO(chart_1h))

    img_01_size = img_01.size

    pad = 1 # Thickness of divider line
    new_im = Image.new('RGB', (2*img_01_size[0]+pad,2*img_01_size[1]+pad), (0,0,0))
    
    new_im.paste(img_01, (0,0))
    new_im.paste(img_02, (img_01_size[0]+pad,0))
    new_im.paste(img_03, (0,img_01_size[1]+pad))
    new_im.paste(img_04, (img_01_size[0]+pad,img_01_size[1]+pad))

    img_byte_arr = io.BytesIO()
    new_im.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()  

    # Generate a timestamp in the format: YYYYMMDD_HHMMSS
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    object_name = f"{ticker}_{timestamp}.png"
    upload_object_to_s3(img_byte_arr, bucket_name, object_name)
    info = {
        "presigned_image_download_url": generate_presigned_url(bucket_name, object_name),
        "object_name": object_name
    }
    return info
    