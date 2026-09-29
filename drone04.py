import time
from codrone_edu.drone import *

drone = Drone()
drone.pair()

# --- 1. БАТАРЕЯ (Розділ 2) ---
battery = drone.get_battery()
print("Battery:", battery, "%")
print("Flights left, roughly:", battery // 15)
print()

# --- 2. ДАТЧИК ВИСОТИ / НИЖНІЙ ДАЛЕКОМІР (Розділ 3) ---
height_cm = drone.get_height("cm")
height_in = drone.get_height("in")
print(f"Height on desk: {height_cm} cm ({height_in} in)")
print()

# --- 3. ПЕРЕДНІЙ ДАТЧИК ВІДСТАНІ (Розділ 4) ---
front_dist = drone.get_front_range("cm")
print(f"Front distance: {front_dist} cm")
if drone.detect_wall(50):
    print("Wall detected closer than 50 cm!")
print()

# --- 4. ДАТЧИКИ КОЛЬОРУ (Розділ 5) ---
colors = drone.get_colors()
print("Front color:", colors[0])
print("Back color:", colors[1])
print()

# --- 5. ТЕСТИ У ПОЛЬОТІ (Розділи 6 та 7) ---
input("Press Enter to start the flight test (make sure the surrounding area is clear)...")

drone.takeoff()
drone.hover(1)

# Позиція та кути (Розділ 6)
print("Start position (X, Y):", drone.get_pos_x(), drone.get_pos_y())

drone.move_forward(50, "cm", 1)
drone.hover(1)
print("After 50cm forward (X, Y):", drone.get_pos_x(), drone.get_pos_y())

drone.move_left(30, "cm", 1)
drone.hover(1)
print("After 30cm left (X, Y):", drone.get_pos_x(), drone.get_pos_y())
print()

# Шум датчика висоти під час зависання (Розділ 7)
for i in range(10):
    print(f"Reading {i+1}: {drone.get_height()} cm")
    time.sleep(1)

drone.land()
drone.close()