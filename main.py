from telegram.client import Telegram

######################
# App Configurations #
######################

channel_id = 0
user_id = 0

###########################
# Telegram Configurations #
###########################

# Proxy settings (if needed)
proxy_type = {
   '@type': 'proxyTypeSocks5',  # 'proxyTypeMtproto', 'proxyTypeHttp'
}
proxy_port = 39159
proxy_server = 'localhost'

tg = Telegram(
    # Your app_id and api_hash obtained from my.telegram.org/apps
    api_id='XXXXXXX',
    api_hash='XXXXXXX',

    # Your user phone number
    phone='+989XXXXXXXXX',

    # An arbitrary key for app datebase
    database_encryption_key='myverysecretpassword',

    # You can change messages database with this line: (default to /tmp/.tdlib_files/...)
    # files_directory='path/to/your/directory',

    # If you need proxy:
    # proxy_server=proxy_server,
    # proxy_port=proxy_port,
    # proxy_type=proxy_type,
)

###############
# App methods #
###############

def copy_message(from_chat_id: int, message_id: int, send_copy: bool = True) -> None:
    data = {
            'chat_id': user_id,
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
    if message_chat_id != channel_id:
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

    tg.add_message_handler(new_message_handler)
    tg.idle()
