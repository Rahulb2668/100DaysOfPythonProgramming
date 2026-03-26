from PIL import ImageGrab 
import time 
import pyautogui 

print("Switch to the game now! Starting in 3 seconds...")
time.sleep(3) 
pyautogui.press("space")  

start_time = time.time()

while True:
    time_played = time.time() - start_time
    
    extra_reach = int(time_played * 1.5) 
    
    if extra_reach > 100: 
        extra_reach = 100
        
    box_width = 20 + extra_reach
    
    box = (700, 300, 700 + box_width, 361)
    
    image = ImageGrab.grab(box)
    gray_image = image.convert("L")    
    action = None 
    
  
    for x in range(box_width): 
        for y in range(36, 61):
            if gray_image.getpixel((x, y)) < 100: 
                action = "jump"
                break
        if action == "jump":
            break

    if not action: 
        for x in range(box_width):
            for y in range(0, 36):
                if gray_image.getpixel((x, y)) < 100:
                    action = "duck"
                    break
            if action == "duck":
                break
            
    if action == "jump":
        pyautogui.press("up")
        time.sleep(0.05) 
    elif action == "duck":
        pyautogui.keyDown("down")
        time.sleep(0.1)
        pyautogui.keyUp("down")
        
    time.sleep(0.001)
