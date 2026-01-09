from datetime import date,time,datetime,timedelta

hoy= date.today()
print(hoy)
ahora=datetime.now()
print(ahora)
print()
hora=time(7,22,15)
fecha=date(2020,12,31)
momento=datetime(1968,10,8,18,15)
print(fecha)
print(hora)
print(momento)

formateo=momento.strftime("%A %d %B %m %y")
print(formateo)

texto="2025-01-03 14:30"
formato="%Y-%m-%d %H:%M"
objeto=datetime.strptime(texto,formato)
print(objeto)

fechafutura=objeto+timedelta(days=3527,hours=5,weeks=12)
print(fechafutura)