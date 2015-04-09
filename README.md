# Bitcurex Api V2

Prod url = https://api.bitcurex.com/v2/

changelog:

11:16:39 PM11/24/14 : added informations about ticker, added symbol to orderbook and trades
09:09:27 PM12/01/14 : added new method, and some update

get user balances

Params:
hash = hmac(key=secret, message="nonce=1416526812", sha512)
nonce = timestamp

URL:
GET /balance/api_key/hash/?nonce=1416526812

Example request:
200 GET
/balance/069199d0190c9845691dfd5922abd7dafd40d3fc0d8229aaba9bbb79e486a9542cfa55a38d68a1ed6a52a178e8ce9f6335727590c714056424a437/b7579a90244d9b2e52fa9733c056d3dc5e713cfaa8e1ce0647dc56bdb0011b7868a0e2fb14b7b6fca1a5f67feac41a019b4a04def553f80a026ae6655a8d44d7/?nonce=1416526812

Example response:
{"status": "ok", "data": {"pln": "999555.1225", "usd": "1248705.0000", "btc": "75.00000000", "eur":"1246843.0000"}}


get user offers

Params:
hash = hmac(key=secret, message="market=pln&nonce=1416526813", sha512)
market = pln / eur / usd
nonce = timestamp

URL:
GET /offers/market/api_key/hash/?nonce

example request:
GET
/offers/pln/069199d0190c9845691dfd5922abd7dafd40d3fc0d8229aaba9bbb79e486a9542cfa55a38d68a1ed6a52a178e8ce9f6335727590c714056424a437/b1c00483a06b1805168a153d1d0276b9f22d90acec6eb70fbe48919ac0ce517b01464bfa665f56c0bcd18193a5aa199ae8c9ee9d3d615c4c71986c597d2a131b/?nonce=1416526813

example response:
{"status": "ok", "data": [{"issued": 1415892208581, "volume": "10.00000000", "currency": "pln",
"limit": "12.0000", "type": "bid", "id": "2014/11/13/143/3097"}, {"issued": 1415892602667, "volume":"12.00000000", "currency": "pln", "limit": "12.0000", "type": "bid", "id": "2014/11/13/145/5788"},{"issued": 1415892858632, "volume": "12.00000000", "currency": "pln", "limit": "12.0000", "type":"bid", "id": "2014/11/13/148/1837"}, {"issued": 1415896356191, "volume": "1.00000000", "currency":"pln", "limit": "12.0000", "type": "bid", "id": "2014/11/13/165/6669"}, {"issued": 1416311876879,"volume": "12.00000000", "currency": "pln", "limit": "12.0000", "type": "bid", "id":"2014/11/18/200/4436"}, {"issued": 1416347036503, "volume": "13.00000000", "currency": "pln","limit": "12.0000", "type": "bid", "id": "2014/11/18/203/5015"}, {"issued": 1416577455599, "volume":"2.00000000", "currency": "pln", "limit": "200.0000", "type": "ask", "id": "2014/11/21/233/5015"},{"issued": 1416577592508, "volume": "2.00000000", "currency": "pln", "limit": "200.0000", "type":"ask", "id": "2014/11/21/234/3113"}, {"issued": 1416591190887, "volume": "2.00000000", "currency":
"pln", "limit": "200.0000", "type": "ask", "id": "2014/11/21/236/9156"}, {"issued": 1416818729472,"volume": "2.00000000", "currency": "pln", "limit": "200.0000", "type": "ask", "id":"2014/11/24/237/6669"}, {"issued": 1416311889649, "volume": "1.75161290", "currency": "pln","limit": "234.0000", "type": "ask", "id": "2014/11/18/202/9458"}, {"issued": 1416347125677,"volume": "3.00000000", "currency": "pln", "limit": "345.0000", "type": "ask", "id":"2014/11/18/208/4771"}]}


get all offers

Params:
hash = hmac(key=secret, message="market=pln&nonce=1416526814", sha512)
market = pln / eur / usd
nonce = timestamp

URL:
GET /all/offers/market/api_key/hash/?nonce

Example request:
GET
/all/offers/pln/069199d0190c9845691dfd5922abd7dafd40d3fc0d8229aaba9bbb79e486a9542cfa55a38d68a1ed6a52a178e8ce9f6335727590c714056424a437/b3d7678bbf8a56fc5d7a1168b8ea5e609924a6f3c8be2f2ec07ea04b85dd2b25185e9d8933888dd1dd3f6348a01e05f7b30ae6adbe390c5faa707ba45e92eb7f/?nonce=1416526814

Example response:
{"status": "ok", "data": [{"issued": 1416394737431, "volume": "0.50000000", "currency": "pln",
"limit": "22.0000", "type": "bid", "id": "2014/11/19/211/2095"}, {"issued": 1416394523699, "volume":"1.00000000", "currency": "pln", "limit": "20.0000", "type": "bid", "id": "2014/11/19/210/1421"},{"issued": 1415892208581, "volume": "60.00000000", "currency": "pln", "limit": "12.0000", "type":"bid", "id": "aggregated"}, {"issued": 1416577455599, "volume": "8.00000000", "currency": "pln","limit": "200.0000", "type": "ask", "id": "aggregated"}, {"issued": 1416311889649, "volume":"1.75161290", "currency": "pln", "limit": "234.0000", "type": "ask", "id": "2014/11/18/202/9458"},{"issued": 1416347125677, "volume": "3.00000000", "currency": "pln", "limit": "345.0000", "type":"ask", "id": "2014/11/18/208/4771"}, {"issued": 1416394949663, "volume": "0.30000000", "currency":"pln", "limit": "500.0000", "type": "ask", "id": "2014/11/19/213/1598"}]}


create offer

Params:
hash = hmac(key=secret,message="limit=200&market=pln&nonce=1416526815&offer_type=bid &volume=2",sha512)
market = pln / eur / usd
nonce = timestamp
limit = price (integer or float)
volume = how many btc user want to buy/sell
offer_type = 'ask' / 'buy'

URL:
POST /offer/market/api_key/hash

Headers:
'content-type': 'application/json',
'accept': 'application/json'

Request Data:
{
'limit': 200,
'volume': 2,
'offer_type': 'bid', // or ask
'nonce': 1416526815,
}

Example request:
POST
/offer/pln/069199d0190c9845691dfd5922abd7dafd40d3fc0d8229aaba9bbb79e486a9542cfa55a38d68a1ed6a52a178e8ce9f6335727590c714056424a437/415f274a15dcbce5f92b0d62cd1a6979294ac6f7b9a829445cd66eafc2fc98fc8e3d4ed066c211aa736e8e43bf92dc463ed925c7ad7c0cb21121c1d11272e024/

Example response:
{"status": "ok", "data": {"offer_status": "open", "id": "2014/11/24/238/4771"}}



delete offer

Params:
hash = hmac(key=secret,message="nonce=1416526815&offer_id=2014/11/24/238/4771",sha512)
nonce = timestamp
offer_id = offer identyfication

URL:
DELETE /offer/del/api_key/hash

Headers:
'content-type': 'application/json',
'accept': 'application/json'

Request Data:
{
'offer_id': '2014/11/24/238/4771',
'nonce': 1416526816,
}

example request:
DELETE
/offer/del/069199d0190c9845691dfd5922abd7dafd40d3fc0d8229aaba9bbb79e486a9542cfa55a38d68a1ed6a52a178e8ce9f6335727590c714056424a437/6966975f0b8e491c4c482554bdea4d324ea2960d36d6b390f24894b1b09a3786bdcee1fbf4ff9c46d633dea3196a55ccf843500ce561defe0d16669bf6b176d9

example response:
{"status": "ok", "data": [{"orig_limit": 2000000, "orig_volume": 200000000, "volume": 200000000,"limit": 2000000, "issued": 1416821170199, "expiry": "infinity", "type": "bid", "id":
"2014/11/24/238/4771", "market": "btcpln"}]}


order book

Params:
depth = integer (limit to number of entries)
market = pln / eur / usd

URL:
GET /market/depth/orderbook

Example request:
GET
/pln/5/orderbook

Example response:
{"symbol": "btcpln", "bids": [[22.0, 0.5], [20.0, 1.0], [12.0, 10.0], [12.0, 12.0], [12.0, 12.0]],
"asks": [[200.0, 1.0], [200.0, 2.0], [200.0, 2.0], [200.0, 2.0], [234.0, 1.7516129]]}


traders

Params:
market = pln / eur / usd
fromts = limiting timestamp

URL:
GET /market/fromts/trades

example request:
GET
/pln/0/trades – get all trades
/pln/1416394861/trades – get trades newer then given timestamp

example response:
{"status": "ok", "data": {"symbol": "btcpln", "trades": [{"tid": "2014/11/19/101/6971", "amount":0.0483871, "price": 234.0, "type": "ask", "ts": 1416398073}, {"tid": "2014/11/24/102/1598","amount": 1.0, "price": 200.0, "type": "ask", "ts": 1416826175}]}}


ticker

Params:
market = pln / eur / usd

URL:
GET /api/market/ticker

Example request:
GET
/api/pln/ticker

Example response:
{"lowest_tx_price_h": "200.0000", "curr": "pln", "currency": "pln", "total_volume_h": "1.0000","highest_tx_price": 0, "average_price_h": "200.0000", "market": "btcpln", "total_volume": 100000000,"best_bid": 220000, "last24_volume_h": 0.0, "total_spent_h": "200.0000", "total_spent": 2000000,"best_bid_h": "22.0000", "lowest_tx_price": 2000000, "highest_tx_price_h": "0.0000","last_tx_price": 2000000, "last24_volume": 0, "price_change": 14.529914529914533,"best_ask":2000000, "lowest_tx_spread": 0.0, "last_tx_price_h": "200.0000", "highest_tx_spread": 100.0,"best_ask_h": "200.0000", "average_price": 2000000}


get user transactions

Params:
market = pln / eur / usd
txid = limiting txid
hash = hmac(key=secret, message="txid=0&market=pln&nonce=1416527003", sha512)
nonce = timestamp

URL:
GET /trades/market/txid/api_key/hash/?nonce=1416527003

Example request:
GET
trades/pln/0/069199d0190c9845691dfd5922abd7dafd40d3fc0d8229aaba9bbb79e486a9542cfa55a38d68a1ed6a52a178e8ce9f6335727590c714056424a437/a09b29a8907039547129fa45ceb5fc51669eb5d40f148838dba6a4c4a900f3698dc6e9320902fe963bb5c6ccba42d4f0d77a6e961188aba0d79ab82cd9c6a4ce/?nonce=1416527003

Example response:
{"status": "ok", "data": {"symbol": "btcpln", "trades": [{"tid": "2014/11/19/101/6971", "amount":
0.0483871, "price": 234.0, "type": "ask", "ts": 1416398073}, {"tid": "2014/11/24/102/1598",
"amount": 1.0, "price": 200.0, "type": "ask", "ts": 1416826175}]}}
