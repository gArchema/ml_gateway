from typing import List

import torch
from pydantic import BaseModel
from fastapi import APIRouter, File, HTTPException, Query

from src.aws import *

semantic_search_router = APIRouter(prefix='/semantic_search', tags=['semantic_search'])

bucket = 'sagemaker-eu-west-1-494948610654'
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


class GenerateEmbeddingsRequest(BaseModel):
    embedding_name: str = None
    paragraphs: List[str]


@semantic_search_router.post('/generate_embeddings')
async def generate_embeddings(request: GenerateEmbeddingsRequest):
    file_path = f'generated_embeddings/{request.embedding_name}.pt'
    data = {
        'inputs': request.paragraphs
    }

    predicted_res = predictor.predict(data=data)

    tensor_to_be_uploaded = torch.Tensor(predicted_res['vectors']).to(device)
    return {
        'uploaded_status': upload_torch_file(tensor_to_be_uploaded, bucket, file_path),
        'embedded_file_name': request.embedding_name
    }
