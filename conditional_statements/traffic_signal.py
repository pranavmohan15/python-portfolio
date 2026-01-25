color=str(input("Enter the color of traffic signal(red,yellow,green): "))
if color=='red':
    print("stop")
elif color=='yellow':
    print("ready")
elif color=='green':    
    print("go")
else:
    print("invalid color")