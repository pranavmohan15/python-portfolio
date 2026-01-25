def signal(color):
    if color=='red':
        return "STOP"
    elif color=='yellow':
        return "READY"
    elif color=='green':
        return "GO"
color=input("enter the colour:")
print(signal(color))