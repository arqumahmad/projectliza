def command(data):
    b=data
    if (b.find('weather')>-1):
        print "weather"
    elif (b.find('temperature')>-1):
        print 'temp'
    



def obj(a):
    a = a.lower()
    print a
    if (a.find('hello')>-1 or a.find('ok')>-1 or a.find('hey')>-1)  and a.find('alpha')>-1:
        command(a)
