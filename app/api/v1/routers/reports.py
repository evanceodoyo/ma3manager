from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.api import deps
from datetime import date

router = APIRouter()


@router.get("/monthly-earnings-vs-expenses",
            response_model=schemas.MonthlyReport)
def get_monthly_earnings_vs_expenses(
    year: int,
    month: int,
    db: Session = Depends(
        deps.get_db)):
    earnings = crud.remittance.get_total_earnings(db, year=year, month=month)
    expenses = crud.maintenance.get_total_expenses(db, year=year, month=month)
    return {
        "year": year,
        "month": month,
        "total_earnings": earnings,
        "total_expenses": expenses}
