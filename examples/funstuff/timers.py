from machine import Timer

index = 0

def ReadThing(t):
    global index    
    print('Print out some number')
    print(index)

def DoThing(t):
    global index
    print('Do a thing with number')
    index = index + 1    

tim0 = Timer(0)
tim0.init(period=3000, mode=Timer.PERIODIC, callback=ReadThing)

tim1 = Timer(1)
tim1.init(period=2000, mode=Timer.PERIODIC, callback=DoThing)
