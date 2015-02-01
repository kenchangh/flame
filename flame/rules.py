# -*- coding: utf-8 -*-
import json
import requests

{% macro get(item, url) -%}
def get_{{ item }}():
    api_url = '{{ url }}'
    req = requests.get(api_url)
    assert req.status_code == 200
    return json.loads(req.text)
{% endmacro %}


{% macro post(item, url, obj) -%}
def post_{{ item }}():
    api_url = '{{ url }}'
    headers = {'Content-type': 'application/json'}
    obj = {{ obj }}

    req = requests.post(api_url,
        data=json.dumps(obj), headers=headers)
    assert req.status_code == 200
    return json.loads(req.text)
{% endmacro %}
