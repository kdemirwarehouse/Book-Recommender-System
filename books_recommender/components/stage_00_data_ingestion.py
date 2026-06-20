import os
import sys
from six.moves import urllib
import zipfile
from books_recommender.logger.log import logging
from books_recommender.exception.exception_handler import AppException
from books_recommender.config.configuration import AppConfiguration

class DataIngestion:
    def __init__(self):
        self.config = AppConfiguration().get_data_ingestion_config()

    def initiate_data_ingestion(self):
        pass
    