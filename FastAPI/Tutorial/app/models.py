from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    Enum, Boolean,
)
from database.connection import Base
from sqlalchemy.orm import Session

class BaseMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=func.utc_timestamp())
    updated_at = Column(DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())

    def all_columns(self):
        return [c for c in self.__table__.columns if c.primary_key is False and c.name != "created_at"]

    @classmethod
    def create(cls, session: Session, auto_commit=False, **kwargs):
        """
        테이블 데이터 적재 전용 함수
        :param session:
        :param auto_commit: 자동 커밋 여부
        :param kwargs: 적재 할 데이터
        :return:
        """
        obj = cls()
        for col in obj.all_columns():
            col_name = col.name
            if col_name in kwargs:
                setattr(obj, col_name, kwargs.get(col_name))
        session.add(obj)
        session.flush()
        if auto_commit:
            session.commit()
        return obj


class CompanyTable(Base, BaseMixin):
    __tablename__ = 'company'
    company_name_ko = Column(String(length=300), nullable=True, default="")
    company_name_en = Column(String(length=300), nullable=True, default="")
    company_name_ja = Column(String(length=300), nullable=True, default="")



