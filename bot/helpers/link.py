from html import escape


def create_link(url: str, text: str):
    return f'<a href="{url}">{escape(text)}</a>'
