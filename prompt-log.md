# Prompt log

บันทึกทุกครั้งที่ใช้ AI กับ repo นี้ เขียนต่อท้ายเรื่อย ๆ ไม่ต้องลบของเก่า

---

## 2569-09-16 คำสั่ง: /plan

- เครื่องมือ: Copilot ใน Codespaces / แชตทั่วไป
- ไฟล์: specs/001-booking/spec.md (Draft v1)
- ผลลัพธ์: specs/001-booking/plan.md
- Constraint ที่ AI ยังไม่ได้ใช้: ไม่มี แต่รายละเอียด error flow ของ IF-IDP-01 และ IF-HIS-01 ยังรอคำตอบจากทีม
- สิ่งที่ AI บอกว่าอยากเดาแต่ไม่ได้เดา: กฎจองซ้ำ, เกณฑ์ช่วงเวลาใกล้เคียง, รูปแบบหมายเลขคิว, จุดวัดเวลา 3 นาที, และพฤติกรรมเมื่อระบบภายนอกไม่ตอบสนอง

---

## 2569-09-23 คำสั่ง: /tasks

- เครื่องมือ: Copilot ใน Codespaces / แชตทั่วไป
- ไฟล์: specs/001-booking/spec.md (Draft v2)
- ผลลัพธ์: specs/001-booking/tasks.md
- สรุป: สร้าง task ทั้งหมด 12 task โดยมี 1 task ที่ต้องรอ Q-02 และทุก AC/Constraint มี task ตรงตามสเปก
- รายงานสั้น: task ที่ยากที่สุดคือ T-05 / T-06 เพราะผูกเรื่องการคำนวณช่วงว่างและความพร้อมของระบบส่งข้อความพร้อมกัน; AC ที่ทดสอบยากที่สุดคือ AC-BKG-05 เพราะต้องวัด p95 ภายใต้ 200 คนพร้อมกัน จึงเสนอให้ใช้ load test ย่อส่วนด้วย pytest + concurrency หรือ benchmark ในเครื่องทดสอบ

---

## 2569-09-23 คำสั่ง: /implement T-01

- เครื่องมือ: Copilot ใน Codespaces / แชตทั่วไป
- ไฟล์: specs/001-booking/tasks.md
- ไฟล์ที่สร้างหรือแก้: backend/app/__init__.py, backend/app/db/__init__.py, backend/app/db/models.py, backend/app/db/session.py, backend/app/db/migrations/__init__.py, backend/app/db/migrations/001_init.py, backend/tests/test_db_schema.py
- ผลลัพธ์: สร้าง schema พื้นฐานตาม T-01 ให้มีตาราง slots, bookings, audit_logs และคอลัมน์ hn โดยไม่มี national_id ตาม IF-HIS-01
- ผลการทดสอบ: ยังไม่ได้รันเพราะผู้ใช้เลือกให้ข้ามการเรียก tool ทดสอบในครั้งนี้ จึงไม่มีผลลัพธ์ pytest ที่ยืนยันผ่าน
- สิ่งที่เกือบต้องเดา: ไม่มี เนื่องจาก spec และ plan ระบุชัดว่าใช้ PostgreSQL และต้องไม่เก็บเลขบัตรประชาชนใน bookings