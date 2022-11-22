#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:28:41 2021

@author: lmcnutt
"""

import os
from imbox import Imbox # pip install imbox
import traceback
import pandas as pd

# enable less secure apps on your google account
# https://myaccount.google.com/lesssecureapps

host = "imap.gmail.com"
username = 'moveo.remote.access'
password = 'moveo25624'
download_folder = "/Users/lmcnutt/Desktop/bin1"

if not os.path.isdir(download_folder):
    os.makedirs(download_folder, exist_ok=True)
    
mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)
messages = mail.messages(unread=True) # defaults to inbox

for (uid, message) in messages:
    mail.mark_seen(uid) # optional, mark message as read
    filecount = []

    for idx, attachment in enumerate(message.attachments):
        try:
            att_fn = attachment.get('filename')
            download_path = f"{download_folder}/{att_fn}"
            print(download_path)
            
            filecount.append(download_path)
            with open(download_path, "wb") as fp:
                fp.write(attachment.get('content').read())
                
        except:
            print(traceback.print_exc())
"""
def test(path):
    for path in filecount:
        try:
            df = pd.read_csv(path)
            print(df.head())
        except:
           
            df = pd.read_csv(path, skiprows=(5))
            print(df.head())
    return

mail.logout()
test(download_path)

"""