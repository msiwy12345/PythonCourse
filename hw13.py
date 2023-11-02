def show_progress(count, character = '*'):
    for i in range(count):
        print(character)

show_progress(10)
show_progress(20)

show_progress(10,'x')