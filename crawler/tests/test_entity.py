from crawler.pages_crawler.entity import EntityCrawler
from crawler.pipline import CONFIG, PLATFORM_PARSE

from .schema import links_schema, proxie_schema


def test_to_representation_proxie():
    """Test to representation proxie."""
    proxie = EntityCrawler.to_representation_proxie(
        '13.78.125.167:8080', '13.78.125.167:8080'
    )

    proxie_schema.validate(proxie)
    assert proxie_schema.is_valid(proxie)


def test_to_public_representation_empyt_values():
    """Test public representation values."""
    config = CONFIG()
    list_link = EntityCrawler.to_public_representation(
        config[PLATFORM_PARSE]['url'],
        []
    )

    assert list_link == []


def test_to_public_representation_list_values():
    """Test public representation values."""
    config = CONFIG()
    from bs4 import BeautifulSoup
    a = [
        '<a href="/diegohaz/rest">diegohaz/<em>rest</em></a>',
        '<a href="/OKCoin/rest">OKCoin/<em>OKCoin</em></a>',
        '<a href="/cujojs/rest">OKCoin/<cujojs>cujojs</em></a>',
        '<a href="/Respect/Rest">Respect/<em>Respect</em></a>'
    ]

    list_link = []
    for link in a:
        soup = BeautifulSoup(link)
        list_link.append(soup.find('a'))
    list_link = EntityCrawler.to_public_representation(
        config[PLATFORM_PARSE]['url'],
        list_link
    )

    assert links_schema.is_valid(list_link)
