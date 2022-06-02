#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""
secret = ""
client = Client(key, secret)

logger = logging.getLogger(__name__)

response = client.gift_card_redeem_code("<the_code_to_redeem>")
logger.info(response)
