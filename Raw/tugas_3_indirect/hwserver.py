import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://192.168.43.129:5555")

while True:

    message = socket.recv()
    print("Received request: %s" % message)

	# do some work
    time.sleep(1)


    socket.send(b"Hello Herpoes")
