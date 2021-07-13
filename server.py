from aiohttp import web
import socketio
import asyncio

app = web.Application()
sio = socketio.AsyncServer()
sio.attach(app)

connection_session = {
    "aabid": None,
    "umar": None,
}


@sio.event
async def connect(sid, environ, auth=None, headers=None):
    print(environ)

    if auth["to"] in connection_session and auth["from"] in connection_session:
        connection_session[auth["from"]] = sid
        await sio.save_session(sid, {"to": auth["to"]})

    print(connection_session)


@sio.event
async def chat(sid, data):
    print("message recieved", data)
    to = await sio.get_session(sid)
    print(to)
    to = connection_session[to["to"]]
    await sio.emit("chat", data, to=to)
    return "oK"


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    web.run_app(app)
