from schema import And, Regex, Schema

VALIDATION_URL_HTTP = r'^http?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
VALIDATION_URL_HTTPS = r'^https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
VALID_LINK = r'^https?://.+/.+$'

proxie_schema = Schema(
    {
        'http': And(
            str,
            Regex(VALIDATION_URL_HTTP)
        ),
        'https': And(
            str,
            Regex(VALIDATION_URL_HTTPS)
        )
    }
)


links_schema = Schema(
    [
        {
            'url': And(
                str,
                Regex(VALID_LINK)
            )
        }
    ]
)
