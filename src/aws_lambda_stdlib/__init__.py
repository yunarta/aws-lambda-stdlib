import json

import boto3
from botocore.exceptions import ClientError


def get_secrets(secret_name) -> (str, str, str):
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name='us-east-1'
    )

    try:
        secret_value = client.get_secret_value(SecretId=secret_name)
        if 'SecretString' in secret_value:
            secrets = json.loads(secret_value['SecretString'])
            return secrets['root-ca'], secrets['certificate'], secrets['private-key'],
    except ClientError as e:
        raise e

    return None
