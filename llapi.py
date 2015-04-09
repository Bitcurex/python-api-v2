import requests
import json
import hmac
import hashlib
import time
from config import API_KEY, API_SECRET

CONFIG = {
    'api_key': API_KEY,
    'secret': API_SECRET,
    'main_api_url': 'https://api.bitcurex.com/v2',
    }

ASK = 'ask'
BID = 'bid'

def cancel_offer(offer_id, config=CONFIG):

    send_data = {
        'offer_id': offer_id,
        'nonce': int(time.time()),

    }

    msg = '&'.join([str(q) + '=' + str(send_data[q]) for
                    q in sorted(send_data)])
    config['_hash'] = hmac.new(config['secret'],
                               msg=msg,
                               digestmod=hashlib.sha512).digest().encode('hex')

    full_url = '%(main_api_url)s/offer/del/%(api_key)s/' \
               '%(_hash)s' % (config)

    headers = {
        'content-type': 'application/json',
        'accept': 'application/json'
    }

    api_response = requests.delete(
        full_url,
        data=json.dumps(send_data),
        headers=headers
    )

    return (api_response, api_response.text)


def get_all_offers(market, config=CONFIG):
    config['market'] = market
    send_data = {
        'nonce': int(time.time()),
        'market': config['market'],
    }

    msg = '&'.join([str(q) + '=' + str(send_data[q]) for
                    q in sorted(send_data)])
    config['_hash'] = hmac.new(config['secret'],
                               msg=msg,
                               digestmod=hashlib.sha512).digest().encode('hex')

    full_url = '%(main_api_url)s/offers/all/%(market)s/' \
               '%(api_key)s/%(_hash)s/' % (config)

    api_response = requests.get(full_url, params=send_data)
    print api_response, api_response.text
    return (api_response, api_response.text)


def get_balance(config=CONFIG):

    send_data = {
        'nonce': int(time.time()),
    }

    msg = '&'.join([str(q) + '=' + str(send_data[q]) for
                    q in sorted(send_data)])
    config['_hash'] = hmac.new(config['secret'],
                               msg=msg,
                               digestmod=hashlib.sha512).digest().encode('hex')

    full_url = '%(main_api_url)s/balance/' \
               '%(api_key)s/%(_hash)s/' % (config)
    api_response = requests.get(full_url, params=send_data)
    return (api_response, api_response.text)


def get_my_offers(market, config=CONFIG):
    config['market'] = market
    send_data = {
        'nonce': int(time.time()),
        'market': config['market']
    }

    msg = '&'.join([str(q) + '=' + str(send_data[q]) for
                    q in sorted(send_data)])
    config['_hash'] = hmac.new(config['secret'],
                               msg=msg,
                               digestmod=hashlib.sha512).digest().encode('hex')

    full_url = '%(main_api_url)s/offers/%(market)s/%(api_key)s/' \
               '%(_hash)s/' % (config)

    api_response = requests.get(full_url, params=send_data)
    return (api_response, api_response.text)


def get_my_trades(market, config=CONFIG):
    config['market'] = market
    config['txid'] = 0
    send_data = {
        'nonce': int(time.time()),
        'market': config['market'],
        'txid': config['txid'],
    }

    msg = '&'.join([str(q) + '=' + str(send_data[q]) for
                    q in sorted(send_data)])
    config['_hash'] = hmac.new(config['secret'],
                               msg=msg,
                               digestmod=hashlib.sha512).digest().encode('hex')

    full_url = '%(main_api_url)s/trades/%(market)s/%(txid)s/%(api_key)s/' \
               '%(_hash)s/' % (config)
    api_response = requests.get(full_url, params=send_data)
    return (api_response, api_response.text)


def get_trades(market, fromts=0, config=CONFIG):
    config['market'] = market
    config['fromts'] = fromts
    send_data = {
        'nonce': int(time.time()),
        'market': config['market'],
        'fromts': config['fromts'],
    }

    full_url = '%(main_api_url)s/%(market)s/%(fromts)s/trades' % (config)
    api_response = requests.get(full_url, params=send_data)
    return (api_response, api_response.text)


def get_orderbook(market, depth=0, config=CONFIG):
    config['market'] = market
    config['depth'] = depth
    send_data = {
        'nonce': int(time.time()),
        'market': config['market'],
        'depth': config['depth']
    }

    full_url = '%(main_api_url)s/%(market)s/%(depth)s/orderbook' % (config)
    api_response = requests.get(full_url, params=send_data)
    return (api_response, api_response.text)


def new_offer(market, price, volume, offer_type, config=CONFIG):
    config['price'] = price
    config['volume'] = volume
    config['offer_type'] = offer_type
    config['market'] = market

    send_data = {
        'limit': config['price'],
        'volume': config['volume'],
        'offer_type': CONFIG['offer_type'],
        'nonce': int(time.time()),
        'market': config['market']
    }

    msg = '&'.join([str(q) + '=' + str(send_data[q]) for
                    q in sorted(send_data)])
    config['_hash'] = hmac.new(config['secret'],
                               msg=msg,
                               digestmod=hashlib.sha512).digest().encode('hex')
    full_url = '%(main_api_url)s/offer/%(market)s/' \
               '%(api_key)s/%(_hash)s/' % (config)

    headers = {
        'content-type': 'application/json',
        'accept': 'application/json'
    }
    api_response = requests.post(
        full_url,
        data=json.dumps(send_data),
        headers=headers
    )
    return (api_response, api_response.text)


def get_ticker(market):
    res = requests.get("http://bitcurex.com/api/%s/ticker.json" % market)
    return res.json()
