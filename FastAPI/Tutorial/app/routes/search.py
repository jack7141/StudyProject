from fastapi import APIRouter, Depends
from database.connection import db
from sqlalchemy.orm import Session
import models

router = APIRouter()

@router.get("/company_name_ko/{name}")
async def company_name_ko_search(name, db: Session = Depends(db.session)):
    """
    `한국 회사 이름 검색`\n
    param name: 입력값\n
    param db:\n
    return: 회사[상호]에 입력 단어가 하나라도 포함되어 있을 경우 return
    """
    # models.CompanyTable.company_name_ko
    model_column = getattr(models.CompanyTable, 'company_name_ko')
    icontain = db.query(models.CompanyTable).filter(model_column.contains(f'{name}')).all()
    return icontain

@router.get("/company_name_en/{name}")
async def company_name_en_search(name, db: Session = Depends(db.session)):
    """
    `영어 회사 이름 검색`\n
    param name: 입력값\n
    param db:\n
    return: 회사[상호]에 입력 단어가 하나라도 포함되어 있을 경우 return
    """
    # models.CompanyTable.company_name_en
    model_column = getattr(models.CompanyTable, 'company_name_en')
    icontain = db.query(models.CompanyTable).filter(model_column.contains(f'{name}')).all()
    return icontain

@router.get("/company_name_ja/{name}")
async def company_name_ja_search(name, db: Session = Depends(db.session)):
    """
    `일본 회사 이름 검색`\n
    param name: 입력값\n
    param db:\n
    return: 회사[상호]에 입력 단어가 하나라도 포함되어 있을 경우 return
    """
    # models.CompanyTable.company_name_ja
    model_column = getattr(models.CompanyTable, 'company_name_ja')
    icontain = db.query(models.CompanyTable).filter(model_column.contains(f'{name}')).all()
    return icontain