import requests

from .entity import EntityCrawler


class RepositoryCrawler:
    """Repository Crawler."""

    @classmethod
    def make_filter_search(cls, url, params=None, proxies=None):
        """Make a request to the search engine of the page that we are doing
        the scrapping.

        Args:
            url(str): Url to which we are going to attack
            params(dict, Optional): Paramas to add
            proxies(list, Optional): List of proxies
            Return:
                response: Reponse
        """
        return cls._make_get_petition(
            url=url,
            params=params or {},
            proxies=proxies
        )

    @staticmethod
    def _make_get_petition(url, params=None, proxies=None):
        """Make petion with method GET.

        Args:
            url(str): Url to which we are going to attack
            params(dict, Optional): Paramas to add
            proxies(dict, Optional): dict of proxies
        Return:
            response: Reponse
        """
        if proxies:
            proxies = EntityCrawler.to_representation_proxie(
                http_proxie=proxies,
                https_proxie=proxies
            )
        response = requests.get(
            url,
            params=params or {},
            proxies=proxies or {}
        )
        response.raise_for_status()
        return response
