projects=['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Vladimir Putin', 'Donald Trump and Bill Clinton']

array=list(zip(projects, leaders))

for i,j in array:
    print('project',i,'leader',j)

dates = ['2016-06-23', '2016-08-29', '1994-01-01']


for i,j,k in (zip(projects, dates, leaders)):
    print('project',i,'date',j,'leader',k)