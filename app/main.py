from fastapi import (
    FastAPI
)
import logging
from langdetect import detect_langs

from app.interface import SourceText, Response, HealthStatus

app = FastAPI(redoc_url="/", docs_url=None)

logging.basicConfig(filename="production.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


@app.post('/detect_language',
          responses={200: {'model': Response}},
          description="Detect language used, return \n supports 55 languages, response is in (ISO 639-1 codes):",
          tags=[])
def detect_language(data: SourceText):
    detected_lang = detect_langs(data.text)
    logger.info(f"Detected {detected_lang[0]} on  '{data.text[:40]}'")
    return detected_lang


@app.get('/health',
         responses={200: {'model': HealthStatus}},
         description="Microservice heality check",
         tags=["utility"])
def health():
    if detect_langs("Campa cavallo che l erba cresce")[0].lang == 'it':
        return {"status": True}
    return {"status": False}
