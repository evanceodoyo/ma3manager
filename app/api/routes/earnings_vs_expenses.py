from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.analysis import get_monthly_earnings_vs_expenses

router = APIRouter()


@router.get("/earnings_vs_expenses/{year}/{month}")
def read_monthly_earnings_vs_expenses(
        year: int,
        month: int,
        db: Session = Depends(get_db)):
    return get_monthly_earnings_vs_expenses(db, year, month)
