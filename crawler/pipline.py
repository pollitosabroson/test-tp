import argparse
import json
import logging
import pprint
import random

from config import config
from pages_crawler import CrawlerPage

logger = logging.getLogger(__name__)

PLATFORM_PARSE = 'github'
CONFIG = config


def get_random_proxie(proxies=None):
    """Randomly get a proxy to use in execution.

    Args:
        proxies(proxies, Optional): List of proxies
    Return:
    """
    i_proxies = proxies or []
    if i_proxies:
        return random.choice(proxies or [])
    return None


def get_params():
    """."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        '--params',
        help='crawler configuration',
        type=json.loads,
    )

    args = parser.parse_args()
    # Get paramas
    params = args.params
    return params


def initial_crawler():
    """."""
    config = CONFIG()
    params = get_params()
    # Get proxie
    proxie = get_random_proxie(
        params.pop('proxies', [])
    )
    # crawler for page
    results = CrawlerPage(
        config=config[PLATFORM_PARSE],
        params=params,
        proxie=proxie
    )
    # Parse Value
    list_link = results.parse_results()

    # Show values
    pprint.pprint(list_link)


if __name__ == '__main__':
    initial_crawler()
