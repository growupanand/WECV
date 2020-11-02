import os
import re

def get_chats(file):
    if os.path.exists(file):
        chats = []
        users = []
        chats_file = open(file, 'r', encoding='utf-8').read()
        for i in ('\u200e', '\ufeff'):
            chats_file = chats_file.replace(i,'')
        r = re.compile(r'(?P<date>\[.*\])\s(?P<name>[\w\s]+):(?P<message>[^\[]*)[\n]')
        for m in r.finditer(chats_file):
            chat = m.groupdict()
            #add name to users
            if not chat['name'] in users:
                users.append(chat['name'])
            #add attachment field
            chat['attachment'] = None
            is_attachment = re.search('<attached: (?P<filename>.*)>', chat['message'])
            if is_attachment:
                chat['attachment'] = {}
                chat['attachment']['name'] = is_attachment.groupdict()['filename']
                chat['attachment']['type'] = re.search('[\.][\w]*$', chat['attachment']['name']).group()
                chat['attachment']['url'] = os.getcwd()+"\\"+chat['attachment']['name']
            chats.append(chat)
        return {'result':True, 'chats':chats, 'users':users}
    else:
        return {'result':False, 'msg':'File not found'}