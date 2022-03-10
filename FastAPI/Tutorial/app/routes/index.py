from datetime import datetime

from fastapi import APIRouter, Depends
from starlette.responses import Response
from database import schemas
from database.connection import db
from sqlalchemy.orm import Session
import models
from typing import Optional

router = APIRouter()


@router.get("/")
async def index(db: Session = Depends(db.session)):
    """
    `회사 List Get API`\n
    return:
    """
    # current_time = datetime.utcnow()
    company_list = db.query(models.CompanyTable).all()
    return company_list

@router.post("/")
async def create(company_name_ko: str = None, company_name_en: str = None, company_name_ja: str = None, db: Session = Depends(db.session)):
    """
    `회사 생성 API`\n
    param company_name_ko: 국문 회사\n
    param company_name_en: 영문 회사\n
    param company_name_ja: 일문 회사\n
    param db:
    return:
    """

    new_company = models.CompanyTable()
    new_company.company_name_ko = company_name_ko
    new_company.company_name_en = company_name_en
    new_company.company_name_ja = company_name_ja
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

