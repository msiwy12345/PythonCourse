def calculate_paint(litres, *room):
    total=0
    for i in room:
        total=total + i
    print(total)
    print(litres*total)

calculate_paint(3, 21, 2, 13)

rooms = [21, 2, 13]
calculate_paint(3, *rooms)

