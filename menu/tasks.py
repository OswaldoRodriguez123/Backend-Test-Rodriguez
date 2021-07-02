import os
from celery import shared_task
from slack import WebClient

@shared_task
def send_menu(options,uuid):
    wc = WebClient(os.environ['TOKEN_SLACK'])
    menu_url = "http://127.0.0.1:8000/menu/%s" % str(uuid);
    
    wc.chat_postMessage(
        channel="#lunch",
        text=("Hello!\n"
              "I share with you today's menu :) \n\n"
              + options + "\n"
              "Make your order here: "+ menu_url +" \n\n"
              "Have a nice day!")
    )