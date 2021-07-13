import asyncio
import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def chat(data):
    print('message received with ', data)
    # await sio.emit('chat', {'response': 'my response'})


@sio.event
def disconnect():

    print('disconnected from server')


def start_chat():
    while True:
        message = input("message")
        sio.emit("chat", message)
        # asyncio.sleep(1)


def start_client():
    sio.connect('http://localhost:8080',)
    start_chat()
    # await start_chat()
    sio.wait()


# if __name__ == '__main__':

#     asyncio.run(main())
