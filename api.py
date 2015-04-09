import json
from decimal import Decimal
import llapi
import datetime


def _parse_response(api_response, data):
    res = json.loads(data)
    return res['data']


class OrderBookEntry(object):
    amount = 0
    price = 0
    trade_type = None

    def __init__(self, amount, price, trade_type):
        self.amount = amount
        self.price = price
        self.trade_type = trade_type

    def __repr__(self):
        return "OBook[V:%f, $:%f, %s]" % (self.amount,
                                          self.price,
                                          self.trade_type)


class Trade(object):
    tid = None
    amount = 0
    price = 0
    trade_type = None
    issued = None

    def __init__(self, tid, amount, price, trade_type, issued):
        self.tid = tid
        self.amount = amount
        self.price = price
        self.trade_type = trade_type
        self.issued = issued

    def __repr__(self):
        return "Trade[ID:%s, V:%f, $:%f, %s, %s]" % (self.tid,
                                                     self.amount,
                                                     self.price,
                                                     self.trade_type,
                                                     self.issued)


class Offer(object):
    issued = 0
    volume = 0
    currency = None
    limit = 0
    offer_type = None
    offer_id = None

    def __init__(self, issued, volume, currency, limit, offer_type, offer_id):
        self.issued = issued
        self.volume = volume
        self.currency = currency
        self.limit = limit
        self.offer_type = offer_type
        self.offer_id = offer_id


class Wallet(object):

    market = None
    balance = 0

    def __init__(self, market, value):
        self.market = market
        self.value = value

    def __repr__(self):
        return "[M:%s, V:%f]" % (self.market, self.value)


class Ticker(object):
    low_tx = 0
    high_tx = 0
    last_tx = 0
    avg = 0
    ask = 0
    bid = 0
    market = None

    def __init__(self, market, low_tx, high_tx, last_tx, avg, ask, bid):
        self.market = market
        self.low_tx = low_tx
        self.high_tx = high_tx
        self.last_tx = last_tx
        self.avg = avg
        self.ask = ask
        self.bid = bid

    def __repr__(self):
        return "M:%s LOW:%f, HIGH:%f, LAST:%f, AVG:%f, ASK:%f, BID:%f" % (
            self.market,
            self.low_tx,
            self.high_tx,
            self.last_tx,
            self.avg,
            self.ask,
            self.bid
        )


def get_ticker(market):
    res = llapi.get_ticker(market)
    ticker = Ticker(
        res['curr'],
        Decimal(res['lowest_tx_price_h']),
        Decimal(res['highest_tx_price_h']),
        Decimal(res['last_tx_price_h']),
        Decimal(res['average_price_h']),
        Decimal(res['best_ask_h']),
        Decimal(res['best_bid_h'])
    )
    return ticker


def get_wallets():
    res = _parse_response(*llapi.get_balance())
    balances = {}
    for market, value in res.items():
        balances[market] = Wallet(market, Decimal(value))
    return balances


def get_my_offers(market):
    res = _parse_response(*llapi.get_my_offers(market))
    offers = []
    for raw_offer in res:
        offers.append(Offer(res['issued'],
                            Decimal(res['volume']),
                            res['currency'],
                            Decimal(res['limit']),
                            res['offer_type'],
                            res['offer_id']))
    return offers


def get_all_offers(market):
    res = _parse_response(*llapi.get_all_offers(market))
    offers = []
    print res
    for raw_offer in res:
        offers.append(Offer(datetime.datetime.fromtimestamp(res['issued']),
                            Decimal(res['volume']),
                            res['currency'],
                            Decimal(res['limit']),
                            res['offer_type'],
                            res['offer_id']))
    return offers


def get_my_trades(market):
    res = _parse_response(*llapi.get_my_trades(market))
    trades = []
    for trade in res['trades']:
        trades.append(Trade(trade['tid'],
                            Decimal(trade['amount']),
                            Decimal(trade['price']),
                            trade['type'],
                            datetime.datetime.fromtimestamp(trade['ts'])
                        ))
    return trades


def get_trades(market, fromts):
    res = _parse_response(*llapi.get_trades(market, fromts=fromts))
    trades = []
    for trade in res['trades']:
        trades.append(Trade(trade['tid'],
                            Decimal(trade['amount']),
                            Decimal(trade['price']),
                            trade['type'],
                            datetime.datetime.fromtimestamp(trade['ts'])
                        ))
    return trades


def get_orderbook(market, depth):
    _, res = llapi.get_orderbook(market, depth=depth)
    res = json.loads(res)
    orderbook = []
    for bid in res['bids']:
        orderbook.append(OrderBookEntry(bid[1], bid[0], 'bid'))
    for bid in res['asks']:
        orderbook.append(OrderBookEntry(bid[1], bid[0], 'ask'))
    return orderbook


def cancel_offer(offer):
    res = _parse_response(*llapi.cancel_offer(offer.offer_id))
    print res


def make_offer(market, price, volume, offer_type=llapi.ASK):
    res = _parse_response(*llapi.new_offer(market, price, volume, offer_type))
    new_id = res['id']
    return new_id



