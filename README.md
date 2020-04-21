# Telegram Copy Bot


## What it does
This bot can copy (not forward) messages from a channel (which doesn't have administrator privileges on it) to another chat (simple user, channel, etc)

## How to use
1. Copy `.env.example` to `.env`.
    ```
    cp .env.example .env
    ```
2. Obtain `api_id` and `api_hash` from [this link](https://my.telegram.org/apps) and fill it inside Telegram Configuration section of `.env` alongside other configurations (such as phone number of your user which acts as your bot)
3. Run it and login to telegram (may take some minutes to build image for the first time):
    ```
    sudo docker-compose run bot
    ```
4. After logging in you will see your chat names and their chat id. Just copy chat id of source and destination chats and put them inside App Configuration section of `.env`.
5. Rebuild the docker image:
    ```
    sudo docker-compose build
    ```
6. Run the script as a daemon:
     ```
    sudo docker-comose up -d
    ```

