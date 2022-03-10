from pydantic import BaseModel
from typing import Optional

class Company(BaseModel):
    company_name_ko: Optional[str] = None
    company_name_en: Optional[str] = None
    company_name_ja: Optional[str] = None