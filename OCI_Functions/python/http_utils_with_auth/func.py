import io
import json
import requests
import ads
import logging
from urllib.parse import urlparse, parse_qs

def handler(ctx, data: io.BytesIO = None):
    logger = logging.getLogger()
    logger.info("Begin to invoke the function")
    try:
        method = ctx.Method()
        logger.info(f"method: {method}")
        if "POST".lower() == method.lower():
            return http_post(ctx, data, logger)
        elif "GET".lower() == method.lower():
            return http_get(ctx, data, logger)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return {"error": f"Unexpected error: {e}"}

def http_post(ctx, data, logger):
    logger.info("process post method request")

    ads.set_auth('resource_principal')
    endpoint = ctx.Headers()["model_deployment"]
    logger.info(f"endpoint: {endpoint}")

    body = json.loads(data.getvalue())
    logger.info(f"input body: {body}")
    return requests.post(endpoint, json=body, auth=ads.common.auth.default_signer()['signer']).json()

def http_get(ctx, data, logger):
    logger.info("process get method request")
    ads.set_auth('resource_principal')
        
    request_url = ctx.RequestURL()
    logger.info(f"Request URL: {request_url}")

    parsed_url = urlparse(request_url)
    query_params = parse_qs(parsed_url.query)
    logger.info(f"Query parameters: {query_params}")

    endpoint = ctx.Headers()["model_deployment"]
    logger.info(f"endpoint: {endpoint}")

    return requests.get(endpoint, params=query_params, auth=ads.common.auth.default_signer()['signer']).json()
