import logging
from websocket_server import WebsocketServer

# dictionary of clients
dict_of_clients = {}


# Called when client sending a message
def send_message(object_ws, receiver, message):
    print(f'send message {message} to client {receiver["id"]}')
    object_ws.send_message(receiver, message)


# Called for every client connecting
def new_client(client, object_ws):
    print('a new client join us ')


# Called when a client sends a message
def message_received(client, object_ws, message):
    # decode string to dictionary
    message_after_decode = eval(message)
    if message_after_decode['type'] == 'subscribe' and message_after_decode['receiver_id']:
        dict_of_clients[message_after_decode['receiver_id']] = client
        print('getting subscribe')
        # TODO
    else:
        print(f"dict_of_clients[message_after_decode['receiver_id']] == {dict_of_clients[message_after_decode['receiver_id']]} ")
        print(f"message_after_decode['message'] == {message_after_decode['message']}")
        send_message(object_ws=object_ws, receiver=dict_of_clients[message_after_decode['receiver_id']],
                     message=message_after_decode['message'])


# Called for every client disconnecting
# def client_left(client, object_ws):
#     # if client disconnected delete from the dictionary of the clients
#     dict_of_clients.pop(client['id'])


PORT = 1111
HOST = "localhost"
# create a object websocket
server = WebsocketServer(port=PORT, host=HOST, loglevel=logging.INFO)
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
# server.set_fn_client_left(client_left)
# server.send_message()
server.run_forever()
