from http.cookies import SimpleCookie


def parse_cookie(query: str) -> dict:
    """
    Parsing cookie-string for purpose to extract values of cookie-parameters
    Works via standard python lib http.cookies

    :param query:
    :return: dict {cookies_param: value}
    """
    cookie = SimpleCookie()
    cookie.load(query)
    cookies = {k: v.value for k, v in cookie.items()}

    return cookies


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}

    assert parse_cookie('session_id=abc123; user_id=987654; auth_token=xyz789') == \
           {'session_id': 'abc123', 'user_id': '987654', 'auth_token': 'xyz789'}
    assert parse_cookie('language=en; theme=dark; logged_in=true') == \
           {'language': 'en', 'theme': 'dark', 'logged_in': 'true'}
    assert parse_cookie('cart_id=12345; currency=USD; promo_code=SALE50') == \
           {'cart_id': '12345', 'currency': 'USD', 'promo_code': 'SALE50'}
    assert parse_cookie('visitor_id=54321; last_visit=2023-05-18; viewed_pages=10') == \
           {'visitor_id': '54321', 'last_visit': '2023-05-18', 'viewed_pages': '10'}
    assert parse_cookie('access_token=abcdef; user_role=admin; preferences=""') == \
           {'access_token': 'abcdef', 'user_role': 'admin', 'preferences': ''}
    assert parse_cookie('tracking_id=xyz987; source=google; landing_page=https://example.com') == \
           {'tracking_id': 'xyz987', 'source': 'google', 'landing_page': 'https://example.com'}
    assert parse_cookie('session_id=qwerty; user_id=543210') == {'session_id': 'qwerty', 'user_id': '543210'}
    assert parse_cookie('language=fr; timezone=Europe/Paris; visited_countries=France,Italy,Spain') == \
           {'language': 'fr', 'timezone': 'Europe/Paris', 'visited_countries': 'France,Italy,Spain'}
    assert parse_cookie('session_id=1234567890; user_id=98765; referral_source=partner') == \
           {'session_id': '1234567890', 'user_id': '98765', 'referral_source': 'partner'}
    assert parse_cookie('remember_me=true; user_mode=dark; font_size=16') == \
           {'remember_me': 'true', 'user_mode': 'dark', 'font_size': '16'}
