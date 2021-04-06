import time

from loguru import logger
from flask import Flask, request, Response

app = Flask(__name__)

PORT = 1234


@app.errorhandler(500)
def error_handler(error):
    logger.info(f'error_handler {error}')
    return 'ERROR PAGE'
