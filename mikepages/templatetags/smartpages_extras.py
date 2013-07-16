__author__ = 'mike'
"""
contain

{% smartblock_url %} - bind on url
{% smartblock key=3 %} - bind on url
{% smartblock_url key="bottom" %} - bind on url

{% smartblock_url key="bottom" filter="textonly"%} - bind on url
{% smartblock_url key="bottom" filter="html_only"%} - bind on url
{% smartblock_url key="bottom" filter=""%} - bind on url
    filters:
        - full_html
        -
        - detect_contain
        - embeded_html "a,h2,h3,h4,h5,h6,strong,i" with class and id
        - simple_html "a,h2,h3,h4,h5,h6,strong,i" without class and ids

        tags = "a,h1,p,h2,h3"






"""

