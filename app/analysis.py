from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from app.models import Remittance, Maintenance


def get_monthly_earnings(db: Session, year: int, month: int):
    earnings = (
        db.query(func.sum(Remittance.amount))
        .filter(
            extract('year', Remittance.created_at) == year,
            extract('month', Remittance.created_at) == month
        )
        .scalar()
    )
    return earnings or 0.0


def get_monthly_maintenance_expenses(db: Session, year: int, month: int):
    expenses = (
        db.query(func.sum(Maintenance.cost))
        .filter(
            extract('year', Maintenance.date) == year,
            extract('month', Maintenance.date) == month
        )
        .scalar()
    )
    return expenses or 0.0


def get_monthly_earnings_vs_expenses(db: Session, year: int, month: int):
    earnings = get_monthly_earnings(db, year, month)
    expenses = get_monthly_maintenance_expenses(db, year, month)
    return {
        'year': year,
        'month': month,
        'earnings': earnings,
        'maintenance_expenses': expenses,
        'net_earnings': earnings - expenses
    }
