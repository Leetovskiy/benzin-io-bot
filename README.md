<div align="center">
  <h1> Benzin IO bot</h1>
</div>

Benzin-io is a small, asynchronous application that removes the background of the image.
It uses a [third-party API](https://benzin.io/) to process the photos and
the [Telegram Bot API](https://core.telegram.org/bots/api) to implement the user
interface.

It also uses _aiogram_ to implement fast and async Telegram bots, _aiohttp_ to send async
requests, and _loguru_ for logging.

## Installation

Firstly, you should create your Telegram bot and get its
token ([read more](https://core.telegram.org/bots#how-do-i-create-a-bot)). Also, you have
to create a Benzin.io account and take their API key
too ([read more](https://benzin.io/integration/api-docs/)). Finally, if you're done, you
can start an installation.

Clone the repository and go into it:

```shell
git clone https://github.com/Leetovskiy/benzin-io-bot.git
cd benzin-io-bot
```

In this step, you have two options: use `pipenv` or `pip`. If you choose `pip` you should
manually create a virtual environment to avoid conflicts with the system environment.
`pipenv` does it by itself, so you do not need to do anything.

```shell
# For pip users
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# For pipenv users
pipenv install
```

Next, you should pass your Telegram bot token and Benzin.io API key to environment
variables. You may also want to create an.env file and store this information in it if you
use `pipenv`.

```shell
# For pip users
export BOT_TOKEN="<your_token>"
export BENZIN_TOKEN="<your_key>"
```

```dotenv
# .env file (for pipenv users)
BOT_TOKEN=<your_token>
BENZIN_TOKEN=<your_key>
```

All right, that's it. Try running `main.py` and sending the `/start` command to chat.

```shell
python main.py
```

## License

The Apache 2.0 license applies to the project's sources. For further details, refer to
the [LICENSE.txt](https://github.com/Leetovskiy/benzin-io-bot/blob/master/LICENSE.txt)
file.

## Contribution

Feel free to make a pull request and contribute if you accept the Apache 2.0 license. I'm
also open to discussing any suggestions you may have regarding this project.

---

<div align="right">
  Telegram: <a href="https://t.me/leetovskiy">@leetovskiy</a><br>
  Email: <a href="mailto:dev.zaitsev@gmail.com">dev.zaitsev@gmail.com</a>
</div>
