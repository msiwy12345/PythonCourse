from datetime import datetime

def generate(name): 
    if name == 's':
        sec = 60
    if name == 'm':
        sec = 3600
    if name == 'h':
        sec=86400
    source = '''
def f(start, end):
    duration = end - start
    duration_s = duration.total_seconds()
    return divmod(duration_s, {})
'''.format(sec)
    exec(source, globals())
    return f


f_minutes = generate('m')
f_seconds = generate('s')
f_hours = generate('h')
 
start = datetime(2019, 1, 1, 0, 0, 0)  
end  = datetime.now()

print(f_seconds(start, end))
print(f_minutes(start, end))
print(f_hours(start, end))