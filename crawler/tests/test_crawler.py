from crawler.pipline import get_random_proxie


def test_get_random_proxie():
    """Test for validation select proxie."""
    demo_proxies = [
        '161.202.226.194:8123',
        '64.4.94.129:80',
        '13.92.119.142:80'
    ]
    proxie = get_random_proxie(demo_proxies)

    assert proxie in demo_proxies
