import zmq
import time

context = zmq.Context()

sock = context.socket(zmq.PUSH)
sock.bind("tcp://192.168.43.129:5690")

id = 0

while True:
    time.sleep(1)
    id, now = id+1, time.ctime()
    message = "{id} - {time} Aing pen balik mau main life is strange :(".format(id=id, time=now)
    sock.send(message.encode())
    print ("Sent: {msg} ".format(msg=message))