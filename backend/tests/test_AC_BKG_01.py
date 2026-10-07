# test ของ T-03: จองคิวสำเร็จ
# AC-BKG-01 (FR-BKG-04)
from app.db.models import Booking, Slot
from tests.conftest import AUTH


def test_AC_BKG_01_booking_success(client, make_slot, db):
    """AC-BKG-01: ยืนยันตัวตนแล้ว และช่วง 09.00 น. มีที่นั่งว่าง 1 ที่"""
    # Given
    slot = make_slot(start="09:00", remaining=1)

    # When
    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    # Then
    assert res.status_code == 201
    payload = res.json()
    assert payload["slot_id"] == slot.id
    assert isinstance(payload["queue_no"], str) and payload["queue_no"]
    assert db.get(Slot, slot.id).remaining == 0
    assert db.query(Booking).filter_by(slot_id=slot.id).count() == 1


def test_AC_BKG_01_last_seat_booking_reduces_remaining_to_zero(client, make_slot, db):
    """AC-BKG-01: เมื่อใช้ที่นั่งสุดท้ายแล้ว ช่องว่างต้องลดจาก 1 เป็น 0"""
    # Given
    slot = make_slot(start="09:00", remaining=1)

    # When
    res = client.post("/bookings", json={"slot_id": slot.id}, headers=AUTH)

    # Then
    assert res.status_code == 201
    payload = res.json()
    assert payload["queue_no"]
    assert db.get(Slot, slot.id).remaining == 0
    assert db.query(Booking).filter_by(slot_id=slot.id).count() == 1


def test_AC_BKG_01_rejects_unverified_user(client, make_slot, db):
    """AC-BKG-01: ผู้ใช้ที่ยังไม่ยืนยันตัวตนต้องถูกปฏิเสธและไม่ลดที่นั่ง"""
    # Given
    slot = make_slot(start="09:00", remaining=1)

    # When
    res = client.post("/bookings", json={"slot_id": slot.id})

    # Then
    assert res.status_code == 401
    assert res.json()["detail"] == "ยังไม่ได้ยืนยันตัวตน"
    assert db.get(Slot, slot.id).remaining == 1
    assert db.query(Booking).count() == 0
