from dotenv import load_dotenv, find_dotenv
from os import getenv
from sys import exit
from telegram.client import Telegram

load_dotenv(find_dotenv())

######################
# App Configurations #
######################

src_chat = getenv("SOURCE") or None
dst_chat = getenv("DESTINATION") or None

###########################
# Telegram Configurations #
###########################

tg = Telegram(
    api_id=getenv("API_ID"),
    api_hash=getenv("API_HASH"),

    phone=getenv("PHONE"),

    database_encryption_key=getenv("DB_PASSWORD"),
    files_directory=getenv("FILES_DIRECTORY"),

    proxy_server=getenv("PROXY_SERVER"),
    proxy_port=getenv("PROXY_PORT"),
    proxy_type={
          # 'proxyTypeSocks5', 'proxyTypeMtproto', 'proxyTypeHttp'
          '@type': getenv("PROXY_TYPE"),
    },
)

###############
# App methods #
###############

def copy_message(from_chat_id: int, message_id: int, send_copy: bool = True) -> None:
    data = {
        'chat_id': dst_chat,
        'input_message_content': {
            '@type': 'inputMessageForwarded',
            'from_chat_id': from_chat_id,
            'message_id': message_id,
            'send_copy': send_copy,
        },
    }
    result = tg.call_method(method_name='sendMessage', params=data, block=True)
    # print(result.update)


def new_message_handler(update):
    # To print every update:
    # print(update)

    # We want to process only new messages
    if 'sending_state' in update['message']:
        return

    message_chat_id = update['message']['chat_id']
    message_id = update['message']['id']

    # We want to process only messages from specific channel
    if message_chat_id != src_chat:
        return

    # Check if message is forwarded
    if 'forward_info' in update['message']:
        copy_message(message_chat_id, message_id, False)
    else:
        copy_message(message_chat_id, message_id)


if __name__ == "__main__":
    tg.login()
    result = tg.get_chats()

    result = tg.get_chats(9223372036854775807)  # const 2^62-1: from the first
    result.wait()
    chats = result.update['chat_ids']
    for chat_id in chats:
        r = tg.get_chat(chat_id)
        r.wait()
        title = r.update['title']
        print(f"{chat_id}, {title}")

    if (src_chat is None or dst_chat is None):
        print("\nPlease enter SOURCE and DESTINATION in .env file")
        exit(1)
    else:
        src_chat = int(src_chat)
        dst_chat = int(dst_chat)

    tg.add_message_handler(new_message_handler)
    tg.idle()
