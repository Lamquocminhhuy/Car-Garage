from garage.models import Booking
import datetime

def generate_daylist():
    daylist = []
    today = datetime.date.today()
    map = {
    "MONDAY": "THỨ HAI",
    "TUESDAY": "THỨ BA",
    "WEDNESDAY": "THỨ TƯ",
    "THURSDAY": "THỨ NĂM",
    "FRIDAY": "THỨ SÁU",
    "SATURDAY": "THỨ BẢY",
    "SUNDAY": "CHỦ NHẬT"
    }
    for i in range(7):
        day = {}
        curr_day = today + datetime.timedelta(days=i)
        weekday = curr_day.strftime("%A").upper()

        day["date"] = str(curr_day)
        day['day'] = map[weekday]

        day["A_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="8:00").exclude(status="Đã hủy").exists()
        )
        day["B_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="9:00").exclude(status="Đã hủy").exists()
        )
        day["C_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="10:00").exclude(status="Đã hủy").exists()
        )
        day["D_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="11:00").exclude(status="Đã hủy").exists()
        )
        day["E_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="01:00").exclude(status="Đã hủy").exists()
        )
        day["F_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="02:00").exclude(status="Đã hủy").exists()
        )
        day["G_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="03:00").exclude(status="Đã hủy").exists()
        )
        day["H_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="04:00").exclude(status="Đã hủy").exists()
        )
        day["I_booked"] = (
            Booking.objects.filter(date=str(curr_day)).filter(timeblock="05:00").exists()
        )
        if day["day"] != "SATURDAY":  
            daylist.append(day)
    return daylist