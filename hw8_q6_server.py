#!/usr/bin/env python3

import socket
import translators as trans

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 6000        # Port to listen on (non-privileged ports are > 1023)


class Translator:
    def __init__(self, to_lang='fa', from_lang='auto', provider='bing'):
        self.to_lang = to_lang
        self.from_lang, self.provider = from_lang, provider

    def translate_text(self, text):
        return eval(f"trans.{self.provider}(text, '{self.from_lang}', '{self.to_lang}')")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            data_ls = data.decode().split("/")
            print(data_ls)
            from_lang = data_ls[0]
            to_lang = data_ls[1]
            text  = data_ls[2]
            try:
                t = Translator(to_lang=to_lang, from_lang=from_lang)
                translated : str = t.translate_text(text)
                print(translated)
                conn.send(translated.encode())
            except:
                raise Exception("inputs are invalid")

