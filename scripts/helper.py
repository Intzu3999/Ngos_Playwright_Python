
from datetime import datetime
import random

def generate_random_four_digit():
    return str(random.randint(1000, 9999))

def generate_random_nric():
    now = datetime.now()
    
    yy = "88"
    mm = f"{now.month:02d}"
    dd = f"{now.day:02d}" 
    xx = "14"
    last_four_digit = f"{now.strftime('%H%M%S')[-4:]}" 

    return yy + mm + dd + xx + last_four_digit

def mouse_scroll(page, direction="down", distance=100):
    if direction == "down":
        page.mouse.wheel(0, distance)
    elif direction == "up":
        page.mouse.wheel(0, -distance)
    else:
        raise ValueError("Direction must be 'down' or 'up'.")
    page.wait_for_timeout(500)