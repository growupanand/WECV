# WECV

WEVC is a python module, which can be used to read Whatsapp Export Chat file `_chat.txt`.

## Installation

copy `wevc.py` file into your python project folder.

## Usage

```python
import wevc

chats = wevc.get_chats("Path\_chat.txt")

```

## Example
Print in simple json format

### _chat.txt
```text
[08/02/18, 1:57:28 PM] Santa: ‎Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them.
[08/02/18, 1:57:28 PM] Banta: Hi Banta this side.
[08/02/18, 1:58:11 PM] Banta: Do you know we can use wecv to export chats in json.
[08/02/18, 2:02:43 PM] Santa: Good, can we show attachements also like below.
‎[08/02/18, 2:45:08 PM] Santa: ‎<attached: 00000006-PHOTO-2018-02-08-14-45-07.jpg>
[08/02/18, 4:47:09 PM] Banta: Yes above msg will give additional field name {"attachment":{"name":"00000006-PHOTO-2018-02-08-14-45-07.jpg","type":".jpg"}}
[14/02/18, 4:41:42 PM] Santa: Great.

```

### run.py
```python
import wevc

chats = wevc.get_chats("Path\_chat.txt")

if chats['result']:
    print(chats)
else:
    print('File does not  exist')

    
```

### Output
```python
{
  "result": True,
  'chats': [
    {
      'date': '[08/02/18, 1:57:28 PM]',
      'name': 'Santa',
      'message': ' Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them.',
      'attachment': None
    },
    {
      'date': '[08/02/18, 1:57:28 PM]',
      'name': 'Banta',
      'message': ' Hi Banta this side.',
      'attachment': None
    },
    {
      'date': '[08/02/18, 1:58:11 PM]',
      'name': 'Banta',
      'message': ' Do you know we can use wecv to export chats in json.',
      'attachment': None
    },
    {
      'date': '[08/02/18, 2:02:43 PM]',
      'name': 'Santa',
      'message': ' Good, can we show attachments also like below.',
      'attachment': None
    },
    {
      'date': '[08/02/18, 2:45:08 PM]',
      'name': 'Santa',
      'message': ' <attached: 00000006-PHOTO-2018-02-08-14-45-07.jpg>',
      'attachment': {
        'name': '00000006-PHOTO-2018-02-08-14-45-07.jpg',
        'type': '.jpg'
      }
    },
    {
      'date': '[08/02/18, 4:47:09 PM]',
      'name': 'Banta',
      'message': ' Yes above msg will give additional field name {"attachment":{"name":"00000006-PHOTO-2018-02-08-14-45-07.jpg","type":".jpg"}}',
      'attachment': None
    },
    {
      'date': '[14/02/18, 4:41:42 PM]',
      'name': 'Santa',
      'message': ' Great.',
      'attachment': None
    }
  ],
  'users': [
    'Santa',
    'Banta'
  ]
}
```

## Example 2
You can create something looks good like this.

![Example](Example.png)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
