import io
import logging

import torch
from botocore.exceptions import ClientError

from src.aws.base import *


s3_client = session.client('s3')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def upload_torch_file(embeddings,
                      bucket,
                      file_path,
                      object_name=None):
    try:
        buffer = io.BytesIO()
        torch.save(embeddings, buffer)
        buffer.seek(0)
        response_to_upload = s3_client.put_object(Bucket=bucket,
                                                  Key=file_path,
                                                  Body=buffer.getvalue())
    except ClientError as e:
        logging.error(e)
        return False
    return True


def get_torch_file(bucket, file_path):
    response = s3_client.get_object(Bucket=bucket,
                                    Key=file_path)
    body = response['Body']
    buffer = io.BytesIO(body.read())
    return torch.load(buffer).to(device)
