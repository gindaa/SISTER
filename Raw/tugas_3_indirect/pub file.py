import zmq
import time
import os

context = zmq.Context()

sock = context.socket(zmq.PUB)
sock.bind("tcp://*:5680")
id = 0

while True:
    time.sleep(1)
    id, now = id+1, time.ctime()

    message = "1-Update! >> #{id} >> {time} waktu 1".format(id=id, time=now)
    filename = 'hitagi.png'
    size = os.stat(filename).st_size
    print ("file size",size)
    file = open(filename,'rb')
    sock.send(message.encode('ascii'))
    if file:
        sock.send(file.encode('ascii'))
    
    message = "2-Update! >> #{id} >> {time} waktu 2".format(id=id, time=now) 
    sock.send(message.encode('ascii'))

    id += 1
