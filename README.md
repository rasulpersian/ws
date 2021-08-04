WebsocketServer by Python
=====
***
Description
---
A minimal websocket project by Python 3.5+. 

The server can be used for a simple messaging application and monitoring the status 
of various services in large projects. 

Installation
---
Project can be used by the link:
```
tttt
```

Message
---

Client message have the next structure:
```
{
    'action_type' : 'subscribe (or publish)',
    'id' : 'client_id (int)'
    'message' : 'text message (string)' 
}
```
Where 'action_type' is which client want to do, 'id' is client id (if action_type publish then 
'id' is receiver id, else own id), 'message' is just a text send message (if 'action_type' is 
'subscribe' then this field is empty (None)).
