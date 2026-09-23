from datetime import date, datetime, time

from sqlalchemy import Date, DateTime, ForeignKey, Integer, String, Time, UniqueConstraint, Column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Slot(Base):
    """รองรับ FR-BKG-01, FR-BKG-06, CON-TECH-01"""

    __tablename__ = "slots"

    id = Column(Integer, primary_key=True)
    slot_date = Column(Date, nullable=False, index=True)
    start_time = Column(Time, nullable=False)
    package_code = Column(String(50), nullable=False)
    capacity = Column(Integer, nullable=False)
    remaining = Column(Integer, nullable=False, default=0)

    __table_args__ = (
        UniqueConstraint("slot_date", "start_time", "package_code", name="uq_slots_day_time_package"),
    )


class Booking(Base):
    """รองรับ FR-BKG-02, FR-BKG-04, IF-HIS-01"""

    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    hn = Column(String(50), nullable=False, index=True)
    slot_id = Column(Integer, ForeignKey("slots.id"), nullable=False, index=True)
    booking_date = Column(Date, nullable=False, index=True)
    queue_no = Column(String(50), nullable=True)
    status = Column(String(20), nullable=False, default="confirmed")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)


class AuditLog(Base):
    """รองรับ DOM-PDPA-01"""

    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True)
    actor_id = Column(String(100), nullable=False)
    action = Column(String(100), nullable=False)
    hn = Column(String(50), nullable=False, index=True)
    accessed_at = Column(DateTime, nullable=False, default=datetime.utcnow)
