import aws
import gvision_settings as settings
from urllib import quote_plus
import pickle

uri = "https://dlcs-ida.org/iiif-img/2/1/M-1304_R-13_0175"
s3 = aws.get_s3_resource()
response = aws.get_s3_object(s3, settings.RAW_OCR_BUCKET, quote_plus(uri))
body = response['Body'].read()
item = pickle.loads(body)
print(item)  # set breakpoint

