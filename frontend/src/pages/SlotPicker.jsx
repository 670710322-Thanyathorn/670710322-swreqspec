import { useEffect, useState } from 'react'

import { api } from '../api/client.js'

const PACKAGE_OPTIONS = [
  { code: 'GENERAL', label: 'ทั่วไป' },
  { code: 'PREMIUM', label: 'พรีเมียม' },
]

function formatDate(dateString) {
  const date = new Date(dateString)
  return new Intl.DateTimeFormat('th-TH', {
    day: '2-digit',
    month: 'short',
    year: 'numeric',
  }).format(date)
}

function formatTime(timeString) {
  return timeString.slice(0, 5)
}

export default function SlotPicker() {
  const [selectedPackage, setSelectedPackage] = useState(PACKAGE_OPTIONS[0].code)
  const [slots, setSlots] = useState([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    async function loadSlots() {
      setLoading(true)
      setError('')
      try {
        const today = new Date().toISOString().slice(0, 10)
        const response = await api.getSlots({ dateFrom: today, packageCode: selectedPackage })
        const items = Array.isArray(response) ? response : response?.slots ?? []
        setSlots(items)
      } catch (err) {
        setError('ไม่สามารถโหลดช่วงเวลาว่างได้ในขณะนี้')
        setSlots([])
      } finally {
        setLoading(false)
      }
    }

    loadSlots()
  }, [selectedPackage])

  return (
    <section className="mt-8 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm">
      <div className="flex items-center justify-between gap-4">
        <div>
          <p className="text-sm font-medium uppercase tracking-[0.2em] text-teal-700">Booking</p>
          <h2 className="mt-1 text-2xl font-bold text-slate-900">เลือกแพ็กเกจและช่วงเวลา</h2>
        </div>
      </div>

      <div className="mt-5 flex flex-wrap gap-3">
        {PACKAGE_OPTIONS.map((option) => (
          <button
            key={option.code}
            type="button"
            onClick={() => setSelectedPackage(option.code)}
            className={[
              'rounded-full border px-4 py-2 text-sm font-medium transition',
              selectedPackage === option.code
                ? 'border-teal-700 bg-teal-700 text-white shadow-sm'
                : 'border-slate-300 bg-white text-slate-700 hover:border-slate-400',
            ].join(' ')}
          >
            {option.label}
          </button>
        ))}
      </div>

      {error ? <p className="mt-4 text-sm text-red-600">{error}</p> : null}

      <div className="mt-6 space-y-3">
        {loading ? (
          <p className="text-sm text-slate-500">กำลังโหลดช่วงเวลาว่าง…</p>
        ) : slots.length === 0 ? (
          <p className="rounded-xl border border-dashed border-slate-300 bg-slate-50 p-4 text-sm text-slate-500">
            ไม่มีช่วงเวลาว่างสำหรับแพ็กเกจที่เลือก
          </p>
        ) : (
          slots.map((slot) => (
            <button
              key={`${slot.date ?? slot.slot_date}-${slot.start_time ?? slot.startTime}`}
              type="button"
              className="flex w-full items-center justify-between gap-4 rounded-xl border border-slate-200 bg-slate-50 p-4 text-left transition hover:border-teal-300 hover:bg-teal-50"
            >
              <div>
                <p className="text-base font-semibold text-slate-900">
                  {formatDate(slot.date ?? slot.slot_date)} • {formatTime(slot.start_time ?? slot.startTime)}
                </p>
                <p className="text-sm text-slate-500">แพ็กเกจ {selectedPackage}</p>
              </div>
              <div className="rounded-full bg-white px-3 py-1 text-sm font-medium text-teal-700 shadow-sm">
                คงเหลือ {slot.remaining ?? slot.remaining_slots ?? 0} ที่
              </div>
            </button>
          ))
        )}
      </div>
    </section>
  )
}
