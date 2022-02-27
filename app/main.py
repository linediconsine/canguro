import pathlib

from langdetect import detect_langs
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import (
    FastAPI,
    Request,
)

from app.interface import SourceText, Response

BASE_DIR = pathlib.Path(__file__).parent

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


app = FastAPI(redoc_url="/", docs_url=None)


@app.post('/detect_language',
          responses={200: {'model': Response}},
          description="Detect language used, return \n  supports 55 languages, response is in (ISO 639-1 codes):",
          tags=[])
def detect_language(data: SourceText):
    return detect_langs(data.text)
