class EntityCrawler:
    """Entity for crawler."""

    @staticmethod
    def to_public_representation(site, values=None):
        """We create the structure that we are going to return.
        Args:
            site(str:)
        Return:
        """
        link_list = []
        append_link = link_list.append
        i_values = values or []
        for link in i_values:
            if link and link.has_attr('href'):
                append_link(
                    {
                        'url': f'{site}{link["href"]}'
                    }
                )
        return link_list

    @staticmethod
    def to_representation_proxie(http_proxie, https_proxie):
        """Get representation from proxie.

        Args:
            http_proxie(str): Url or ip from http proxie
            https_proxie(str): Url or ip from https proxie
        Return:
            Dict: Formatted Dict to apply a request
        """
        # User representation from here
        # https://2.python-requests.org/en/master/user/advanced/#id10
        return {
            'http': f'http://{http_proxie}',
            'https': f'https://{https_proxie}',
        }
