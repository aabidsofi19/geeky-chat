import socketio
import os
import sys
from socketio.client import Client
import typer
from typer.main import Typer

app = typer.Typer()
sender_ = None
reciever_ = None
stop = False

messages = [

]


sio = socketio.Client()


def print_decoration():
    decor = "❄️ "*5
    s = typer.style(sender_, fg="green")
    r = typer.style(reciever_, fg="red")
    typer.echo(f"{decor}   Chat {s} with {r}  {decor}")


@sio.event
def connect():
    print('connection established')


def print_messages(messages):
    indent = " "*30
    print_decoration()
    # s = typer.stule(sender_, fg="green")
    # r = typer.stule(reciever_, fg="red")
    for m in messages:

        if m["sent"]:

            n = m["message"]
            typer.secho(f"{n}{indent}", fg="green")
        else:
            n = m["message"]

            typer.secho(f"{indent}{n}", fg="red")


@sio.event
def chat(data):

    messages.append({"message": data, "sent": False})
    os.system('cls||clear')
    print_messages(messages)


@sio.event
def disconnect():

    pass


def start_chat():

    os.system('cls||clear')
    print_decoration()
    while True:

        message = input()

        messages.append({"message": message, "sent": True})
        os.system('cls||clear')
        print_messages(messages)
        sio.emit("chat", message)

    sys.sxit()

    # asyncio.sleep(1)


def start_client():

    start_chat()
    # await start_chat()
    sio.wait()


@app.command()
def start_chatting(sender: str = None, reciever: str = None):

    global sender_
    global reciever_
    sender_ = sender
    reciever_ = reciever

    typer.echo(f"connecting to {reciever}")
    indent = " "*20
    sio.connect('http://localhost:8080',
                auth={"to": reciever, "from": sender}, headers={"to": reciever, "from": sender})

    start_chat()

    quit()


app()
