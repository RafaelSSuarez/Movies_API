import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
# API metadata
    WEB_APP_TITLE: str = 'Movies API'
    WEB_APP_DESCRIPTION: str = ''
    WEB_APP_VERSION: str = '0.0.1'
    OPENAPI_SERVER: str = ''
# Path to csv file
    CSV_FILE_PATH: str = os.path.realpath(
                            os.path.join(
                                os.getcwd(),
                                'files',
                                'movie_metadata.csv'
                            )
                        )
    
settings = Settings()