import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '491916172:AAFmAKK7qOpFfiHbJ5yNHFCK60Y58tCmUn8'
WEBHOOK_URL ='https://d0181d9c.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'which',
        'horoscope',
        'horoquery',
        'divination',
        '2018',
        '2018query'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'which',
            'dest': 'which',
            'conditions': 'which_to_which'
        },
        {
            'trigger': 'advance',
            'source': 'which',
            'dest': 'horoscope',
            'conditions': 'is_going_to_horoscope'
        },
        {
            'trigger': 'advance',
            'source': 'horoscope',
            'dest': 'horoquery',
            'conditions': 'is_going_to_horoquery'
        },

        {
            'trigger': 'advance',
            'source': 'which',
            'dest': 'divination',
            'conditions': 'is_going_to_divination'
        },
        {
            'trigger': 'advance',
            'source': 'which',
            'dest': '2018',
            'conditions': 'is_going_to_2018'
        },
        {
            'trigger': 'advance',
            'source': '2018',
            'dest': '2018query',
            'conditions': 'is_going_to_2018query'
        },

        {
            'trigger': 'go_back',
            'source': [
                'horoscope',
                'divination',
                '2018query',
                'horoquery'
            ],
            'dest': 'which'
        }
    ],
    initial='which',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
