import logging

import bs4
from requests.exceptions import ConnectionError, HTTPError
from urllib3.exceptions import MaxRetryError

from .entity import EntityCrawler
from .repository import RepositoryCrawler

logger = logging.getLogger(__name__)


class CrawlerPage:
    """Get Info Pages."""

    def __init__(self, config, params, proxie):
        """Init for CrawlerPage."""
        self.config = config
        self._html = None
        self._proxie = proxie

        self.visit(
            **{
                'params': params
            }
        )

    def _select(self, query_string):
        """Select vale from html.

        Args:
            query_string(str): Query that we are going to execute on the html
        Return:
            list: List with found values
        """
        return self._html.select(query_string)

    def get_info_repo(self, path):
        """Get info by repo.

        Args:
            path(str): path from url
        Return:
            str: url to visit
        """
        return self.build_url(
            path=path
        )

    def build_url(self, path):
        """Build url.

        Args:
            path(str): path from url
        Return:
            str: Url to which we are going to attack
        """
        return f"{self.config['url']}/{path}"

    def build_params(self, params):
        """.

        Args:
            params(dict): Dict whit params to apply
        Return:
            str: Url to which we are going to attack
        """
        return {
            self.config['params']['keywords']: "+".join(
                params.get('keywords', [])
            ),
            self.config['params']['type']: params.get('type')
        }

    def visit(self, **kwargs):
        """Visit site."""
        try:
            response = RepositoryCrawler.make_filter_search(
                url=self.build_url(
                    path=self.config['prefix_search']
                ),
                params=self.build_params(kwargs.get('params')),
                proxies=self._proxie
            )
            self._html = bs4.BeautifulSoup(response.text, 'html.parser')
        except (HTTPError, ConnectionError, MaxRetryError):
            logger.warning(
                f'Error while fechting {self.config["url"]}',
                exc_info=False
            )

    def parse_results(self):
        """Parse result.

        Return:
            List: List of all filtered values
        """
        if self._html is not None:
            results = self._select(
                self.config['queries']['search_repo_links']
            )
            return EntityCrawler.to_public_representation(
                self.config['url'], results
            )
        return []
