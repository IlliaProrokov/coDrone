from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()
drone.hover(1)

# 1. Політ на 1.5 метра вперед
drone.move_forward(1.5, "m", 2.0)
drone.hover(1)

# --- ТРЮК ---
drone.flip("front")  # Сальто вперед
drone.hover(2)     # Час на стабілізацію після трюку

# 2. Поворот на 90 градусів праворуч
drone.turn_right(90)
drone.hover(1)

# 3. Політ на 0.5 метра вперед
drone.move_forward(0.5, "m", 2.0)
drone.hover(1)

# 4. Поворот на 90 градусів ліворуч
drone.turn_left(90)
drone.hover(1)

# 5. Політ на 1.5 метра вперед
drone.move_forward(1.5, "m", 2.0)
drone.hover(1)

# 6. Поворот на 90 градусів праворуч
drone.turn_right(90)
drone.hover(1)

# 7. Політ на 1.6 метра вперед
drone.move_forward(1.6, "m", 2.0)
drone.hover(1)

drone.land()
drone.close()