# Telegram Notifier

...

## Requirements

  * [Python 3.6+](https://www.python.org/)

> This code makes use of the `f'...'` or [f-string syntax](https://www.python.org/dev/peps/pep-0498/). This syntax was
> introduced in Python 3.6.

  * [Poetry](https://python-poetry.org/)

OR 

* [Docker](https://docs.docker.com/)


## Getting started

### Setup

To start the project, you will need to create and fill in the following `.env` file:

```
TOKEN_ID=<token_id>
CHAT_IDS=<some_id>,<other_id>
```

The very example of the file and how the variables should look can be found in `.env.example` file.

The environment variables themselves are:

* `TOKEN_ID` - bot token, which can be obtained by creating your own using [@BotFather](https://t.me/botfather);
* `CHAT_IDS` - can be found if you write something to the bot and send a GET request to
https://api.telegram.org/bot<TOKEN_ID>/getUpdates, in the response you can find the chat id.

### On your machine

1. Make sure **Python** and **Poetry** of the correct versions are installed:
    ```bash
   python3 --version                   
   ```
   ```bash
   poetry --version
   ```
2. Install dependencies:
   ```bash
   poetry config virtualenvs.create false && poetry install --no-dev
   ```
3. Run example:
   ```bash
   python3 example.py
   ```

### Using Docker

1. Make sure that **Docker** is installed and running (Linux):
    ```bash
   docker --version                   
   ```
   ```bash
   systemctl status docker
   ```
2. Run following:
    ```bash
   docker build . -t telegram-notifier
   ```
3. Run following:
   ```bash
   docker run --env-file=.env telegram-notifier
   ```
