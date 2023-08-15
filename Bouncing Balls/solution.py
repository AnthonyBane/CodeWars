def bouncing_ball(h, bounce, window):
    if (h <= 0) or (bounce >= 1) or (bounce <= 0) or (window >= h):
        return -1
    
    bounce_height = h
    count = 0
    
    while bounce_height > window:
        count += 1
        bounce_height = bounce_height * bounce
        if bounce_height > window:
            count += 1
              
    return count