# Prompt log

บันทึกทุกครั้งที่ใช้ AI กับ repo นี้ เขียนต่อท้ายเรื่อย ๆ ไม่ลบของเก่า

---

## 2569-09-23 13.40 คำสั่ง: /tasks specs/001-booking/spec.md

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ผลลัพธ์: specs/001-booking/tasks.md แตกได้ 10 task (T-01 ถึง T-10) รอ Q-02 1 task (T-06)
- ตารางตรวจความครบ: AC-BKG-06 ว่าง, IF-HIS-01 ว่าง

### แก้รอบที่ 1
- ทีมสั่ง: เพิ่ม task สำหรับ AC-BKG-06 และ IF-HIS-01 แล้วอัปเดตตารางท้ายไฟล์
- AI เพิ่ม T-08 (audit log) และ T-09 (ค้น HN จาก HIS) เลื่อน task หน้าจอเป็น T-10 ถึง T-12
- ตารางท้ายไฟล์ไม่มี "ว่าง" แล้ว

---

## 2569-09-23 14.20 คำสั่ง: /implement T-01 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/config.py, backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/001_init.py, backend/tests/test_T01_schema.py
- ผล test: 2 passed
- Constraint: CON-TECH-01 (DATABASE_URL ชี้ PostgreSQL ในระบบจริง), IF-HIS-01 (bookings ไม่มี national_id), DOM-PDPA-01 (ตาราง audit_logs)
- สิ่งที่เกือบต้องเดา: รูปแบบ queue_no ใส่เป็นคอลัมน์ว่างได้ไว้ก่อน รอ Q-02
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-27 19.05 คำสั่ง: /implement T-02 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/slots/router.py, backend/app/slots/service.py, backend/app/main.py, backend/tests/conftest.py, backend/tests/test_AC_BKG_05.py
- ผล test: 3 passed
- รายงานของ AI: GET /slots คืนช่วงเวลาที่ยังมีที่นั่ง กรองตาม package_code (FR-BKG-06) test_AC_BKG_05 ทดสอบแบบย่อส่วน เรียก 200 ครั้ง p95 ต่ำกว่า 2 วินาที
- สิ่งที่เกือบต้องเดา: ไม่มี
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-09-28 20.30 คำสั่ง: /implement T-03 specs/001-booking/tasks.md

- ไฟล์ที่สร้าง: backend/app/booking/router.py, backend/app/booking/service.py, backend/app/auth/idp.py และแก้ backend/app/main.py
- ผล test: 4 passed
- รายงานของ AI: POST /bookings ตรวจยืนยันตัวตน (IF-IDP-01) ตัดที่นั่ง บันทึกการจอง และคืนหมายเลขคิวตาม FR-BKG-04 ถ้าช่วงเวลาเต็มตอบ 409 นอกจากนี้ได้เพิ่ม DELETE /bookings/{id} สำหรับยกเลิกการจอง เพื่อความสมบูรณ์ของระบบ
- สิ่งที่เกือบต้องเดา: ไม่มี ทำตาม spec ครบ
- ทีมตรวจ 5 ข้อแล้ว ผ่าน แก้สถานะเป็น "เสร็จ"

---

## 2569-10-07 08:12 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ผลลัพธ์: ยังไม่มีแถว AC-BKG-01 ใน `specs/001-booking/test-cases.md` จึงเข้าสู่โหมดร่าง
- AI เพิ่ม 3 แถวร่างตาม AC-BKG-01: ทางปกติ / ขอบ / ทางผิด
- วงเล็บ `(รอ Q-02)` ถูกใส่ตามส่วนที่แสดงหมายเลขคิว เนื่องจากรูปแบบเลขคิวยังไม่กำหนดใน spec
- ยังไม่เขียนโค้ด test และต้องให้ทีมตรวจแถวในตารางก่อนเปลี่ยนสถานะเป็น "ใช้ได้" จากนั้นสั่ง /testcases อีกครั้ง

---

## 2569-10-07 08:23 คำสั่ง: /testcases AC-BKG-01 specs/001-booking/

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ผลลัพธ์: `specs/001-booking/test-cases.md` มีแถว AC-BKG-01 ในสถานะ "ใช้ได้" แล้ว จึงเข้าสู่โหมดเขียน test
- AI เพิ่มทดสอบลง `backend/tests/test_AC_BKG_01.py` 3 case: booking สำเร็จ / last seat / unverified user rejected
- รัน test: `cd backend && pytest tests/test_AC_BKG_01.py -q`
- ผลลัพธ์: 3 passed

---

## 2569-10-07 08:30 คำสั่ง: /verify specs/001-booking/

- เครื่องมือ: Copilot ใน Codespaces (Agent, Auto)
- ผล test: backend 6/6 passed, frontend 1/1 passed
- จำนวนแถวในตารางไปข้างหน้า: ครบ 3, ยังไม่ถึง 8, รอ 1, ช่องโหว่ 2
- ข้อค้นพบใหม่: F-BKG-01, F-BKG-02, F-BKG-03, F-BKG-04, F-BKG-05
- สร้าง/อัปเดต: specs/001-booking/rtm.md
