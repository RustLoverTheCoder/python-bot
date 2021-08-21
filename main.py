# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import websocket


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def on_open(ws):
    print(ws)
    print(f'connect success')

def on_message(ws,message):
    print('received message')
    print(message)

def on_close(ws):
    print('close')


socket = 'wss://alpha.shuoapi.com/websocket?token=eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMjMiLCJjbGllbnRfaWQiOiI1NzU2MDgxMy04M2VkLTRiODMtODhlNS0yNWUzNjAwY2NkZmEiLCJleHBpcmVzX2F0IjoxNjMxNDk3MDgyLCJ0eXBlIjoiYWNjZXNzIn0.vP4RQ_-Kyj2Bo5zs9YlwTo_skkNn6mKbvt5OSjX2TmkGSXWbBbr-TWSx_hPaq2ZWivAPMz2HEJHIh9RrWzwauQ&request_id=70bd7806-d4ae-4bc3-a581-b2aa386cb310'

if __name__ == '__main__':
  ws = websocket.WebSocketApp(socket, on_open=on_open,on_close=on_close,on_message=on_message)
  ws.run_forever()
# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
