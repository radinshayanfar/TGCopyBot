# Telegram Copy Bot


## What it does
This bot copies (not forward) messages from a source channel (which doesn't have administrator privileges on it) to a destination chat (simple user, channel, etc.).

## How to use
1. Copy `.env.example` to `.env`.
    ```
    cp .env.example .env
    ```
2. Obtain `api_id` and `api_hash` from [this link](https://my.telegram.org/apps) and fill it inside `Telegram Configuration` section of the `.env` file alongside other configurations (such as phone number of your user, which acts as your bot).
3. Run the project via Docker and login to Telegram:
    ```
    docker run -it \
        --env-file=.env \
        -v td-data:/tmp/.tdlib_files \
        radinshayanfar/tgcopybot
    ```
4. After logging in, you will see your chat names and their chat id. Copy chat ids of source and destination chats and put them inside `App Configuration` section of the `.env` file.
5. Run the container in detached mode and it will do the job:
     ```
     docker run -d \
        --env-file=.env \
        -v td-data:/tmp/.tdlib_files \
        radinshayanfar/tgcopybot
    ```

