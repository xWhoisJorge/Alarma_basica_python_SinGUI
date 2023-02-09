import time

print("Bienvenido al programa de alarma")
print("Ingrese la hora en formato hh:mm:ss")
alarm_time = input()

current_time = time.strftime("%H:%M:%S")
print("La hora actual es: " + current_time)
print("La alarma está programada para sonar a las " + alarm_time)

while current_time != alarm_time:
    current_time = time.strftime("%H:%M:%S")
    time.sleep(1)

print("¡Alarma!")
