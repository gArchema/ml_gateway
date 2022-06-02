import sagemaker

from src.aws.base import *

sagemaker_session = sagemaker.session.Session(session)

serializer = sagemaker.serializers.JSONSerializer()
deserializer = sagemaker.deserializers.JSONDeserializer()

predictor = sagemaker.predictor.Predictor(endpoint_name='semantic-search-generate-embeddings',
                                          sagemaker_session=sagemaker_session,
                                          serializer=serializer,
                                          deserializer=deserializer)
