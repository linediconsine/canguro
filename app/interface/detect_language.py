from pydantic import BaseModel, constr
from typing import Any, List, Optional


class SourceText(BaseModel):
    text: constr(curtail_length=80)


class LangProbability(BaseModel):
    lang: str
    prob: float


class Response(BaseModel):
    lang: List[LangProbability]
