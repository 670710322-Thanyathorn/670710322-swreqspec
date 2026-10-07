# RTM: จองคิวตรวจสุขภาพ (Booking)
อ้างอิง: spec.md SPEC-BKG-001 Draft v2 | tasks.md | test-cases.md
สร้างด้วย /verify เมื่อ 2569-10-07 08:30 | test: 7 ผ่าน 0 ไม่ผ่าน

## 1. ตามรอยไปข้างหน้า (requirement ไป โค้ด ไป test)
| ID | AC | task | โค้ด (ไฟล์: ฟังก์ชัน) | test (ผล) | สถานะ |
|---|---|---|---|---|---|
| FR-BKG-01 | AC-BKG-05 (ไม่ตรงเรื่อง) | T-02 | backend/app/slots/service.py:list_available_slots; backend/app/slots/router.py:get_slots | backend/tests/test_AC_BKG_05.py::test_AC_BKG_05 (PASS) | ช่องโหว่ |
| FR-BKG-02 | AC-BKG-02 | T-04 | ไม่มีการตรวจสอบใน backend/app/booking/service.py:create_booking | ไม่มี | ยังไม่ถึง |
| FR-BKG-03 | AC-BKG-03 | T-05, T-11, T-12 | ไม่มี implementation | ไม่มี | ยังไม่ถึง |
| FR-BKG-04 | AC-BKG-01 | T-03, T-06 | backend/app/booking/service.py:create_booking; backend/app/booking/router.py:create_booking | backend/tests/test_AC_BKG_01.py::test_AC_BKG_01_booking_success (PASS), test_AC_BKG_01_last_seat_booking_reduces_remaining_to_zero (PASS), test_AC_BKG_01_rejects_unverified_user (PASS) | รอ Q-02 |
| FR-BKG-05 | AC-BKG-04 | T-07 | ไม่มีคิวส่งซ้ำ / retry queue | ไม่มี | ยังไม่ถึง |
| FR-BKG-06 | ไม่มี AC | T-10 | backend/app/slots/service.py:list_available_slots | ไม่มี | ช่องโหว่ |
| NFR-PERF-01 | AC-BKG-05 | T-02 | backend/app/slots/service.py:list_available_slots | backend/tests/test_AC_BKG_05.py::test_AC_BKG_05 (PASS) | ครบ |
| NFR-SEC-01 | ไม่มี AC | - | ไม่มี TLS/HTTPS setup ใน code | ไม่มี | ยังไม่ถึง |
| NFR-REL-02 | AC-BKG-04 | T-07 | ไม่มี retry queue | ไม่มี | ยังไม่ถึง |
| NFR-USE-01 | ไม่มี AC | - | ไม่มี flow/UI test | ไม่มี | ยังไม่ถึง |
| CON-TECH-01 | - | T-01 | backend/app/config.py:DATABASE_URL; backend/app/db/session.py:engine | backend/tests/test_T01_schema.py::test_T01_tables_created (PASS) | ครบ |
| DOM-PDPA-01 | AC-BKG-06 | T-08 | backend/app/db/models.py:AuditLog; ไม่มี middleware | ไม่มี | ยังไม่ถึง |
| IF-IDP-01 | - | T-03 | backend/app/auth/idp.py:get_verified_hn | backend/tests/test_AC_BKG_01.py::test_AC_BKG_01_rejects_unverified_user (PASS) | ครบ |
| IF-HIS-01 | - | T-09 | ไม่มี HIS client lookup | ไม่มี | ยังไม่ถึง |
| IF-NOT-01 | AC-BKG-04 | T-07 | ไม่มี async notification queue | ไม่มี | ยังไม่ถึง |

## 2. ตามรอยย้อนกลับ (โค้ด ไป requirement)
| โค้ด (ไฟล์: ฟังก์ชัน หรือ endpoint) | อ้าง ID | ตรงกับข้อความใน spec ไหม | หมายเหตุ |
|---|---|---|---|
| backend/app/slots/service.py:list_available_slots | FR-BKG-01, FR-BKG-06 | ไม่ตรง | กำหนดวันล่วงหน้าเป็น 14 วัน (`DAYS_AHEAD = 14`) แต่ spec ระบุภายใน 30 วันข้างหน้า; filter package_code ทำงานแต่ไม่ครบ 30 วัน |
| backend/app/booking/service.py:create_booking | FR-BKG-02, FR-BKG-04 | ไม่ครบ | ไม่มีการป้องกันการจองซ้ำวันเดียวกันตาม HN และตรวจ `slot.remaining < 0` จึงอนุญาตค่า 0 เป็นจุดเริ่มให้ติดลบ |
| backend/app/booking/service.py:next_queue_no | FR-BKG-04, Q-02 | ไม่ตรง | ดีไซน์ queue number แบบ `A001` กับรีเซ็ตทุกวันเป็นการเดาเรื่อง Q-02 ก่อนได้รับคำตอบจริง |
| backend/app/auth/idp.py:get_verified_hn | IF-IDP-01 | ใช่ | ตรวจ Authorization header และปฏิเสธการเข้าถึงเมื่อยังไม่ยืนยันตัวตน |
| backend/app/db/models.py:Booking | IF-HIS-01 | ไม่ครบ | เก็บเฉพาะ HN ตามข้อกำหนด แต่ไม่มีขั้นตอนค้นข้อมูลจาก HIS ด้วยเลขบัตรประชาชนก่อนบันทึกการจอง |
| backend/app/config.py:DATABASE_URL | CON-TECH-01 | ค่อนข้างตรง | ตั้งค่า PostgreSQL ในสภาพแวดล้อมจริง และ test ใช้ SQLite อย่างชัดเจนเพื่อจำลองฐานข้อมูลเป็นสภาพแวดล้อม dev |

## 3. ข้อค้นพบ
ชนิด: AC ไม่มี test / test อ่อน / โค้ดไม่มี FR / FR ไม่มี AC / เดา Q-xx / ละเมิด Constraint / ตัวเลขไม่ตรง spec / อ้าง ID ผิดเรื่อง
ทีมตัดสิน: แก้โค้ด / แก้ spec / เพิ่ม Q-xx / ไม่ใช่ปัญหา (พร้อมเหตุผล 1 บรรทัด)

| F-ID | ชนิด | อยู่ที่ | ขัดกับ | รายละเอียด | ทีมตัดสิน |
|---|---|---|---|---|---|
| F-BKG-01 | ตัวเลขไม่ตรง spec | backend/app/slots/service.py:list_available_slots | FR-BKG-01 | มีค่า `DAYS_AHEAD = 14` แต่ spec ระบุภายใน 30 วันข้างหน้า จึงไม่ตรงกับข้อกำหนดและไม่แสดงช่วงเวลาเต็ม 30 วัน |  |
| F-BKG-02 | เดา Q-xx | backend/app/booking/service.py:next_queue_no | FR-BKG-04, Q-02 | โค้ดกำหนดรูปแบบ `A001` และรีเซ็ตทุกวันก่อนได้รับคำตอบจากเจ้าหน้าที่เวชระเบียน จึงเป็นการเดาแทน Q-02 |  |
| F-BKG-03 | โค้ดไม่มี FR | backend/app/booking/service.py:create_booking | FR-BKG-02 | ไม่มีการตรวจว่าผู้รับบริการมีคิวที่ยังไม่ได้ใช้ในวันเดียวกัน จึงอาจสร้างคิวซ้ำในวันเดียวกัน |  |
| F-BKG-04 | ตัวเลข/กฎไม่ตรง spec | backend/app/booking/service.py:create_booking | FR-BKG-04 | เงื่อนไข `if slot.remaining < 0` ทำให้ `remaining == 0` ยังคงผ่านและลดลงเป็น -1 ได้ ส่งผลให้ที่นั่งติดลบ |  |
| F-BKG-05 | FR ไม่มี AC | backend/app/slots/service.py:list_available_slots | FR-BKG-06 | มีการกรองตาม package_code ใน code แล้ว แต่ไม่มี AC ใน spec ให้ตรวจความถูกต้องโดยตรง จึงเป็นช่องว่างของ traceability |  |

## 4. แก้แล้ว
| F-ID | แก้อย่างไร | รู้ได้อย่างไร |
|---|---|---|
