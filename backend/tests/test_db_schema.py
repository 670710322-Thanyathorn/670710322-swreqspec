from sqlalchemy import inspect

from app.db.models import Base
from app.db.session import engine


def test_db_schema_has_required_tables_and_no_national_id_column():
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)

    tables = set(inspector.get_table_names())
    assert {"slots", "bookings", "audit_logs"}.issubset(tables)

    booking_columns = {column["name"] for column in inspector.get_columns("bookings")}
    assert "hn" in booking_columns
    assert "national_id" not in booking_columns
