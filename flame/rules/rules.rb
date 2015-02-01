require 'rubygems'
require 'json'
require 'net/http'

{% macro get(item, url, obj={}) -%}
def get_{{ item }}
  url = URI.parse('{{ url }}')
  req = Net::HTTP::Get.new(url.to_s)
  res = Net::HTTP.start(url.host, url.port) {|http|
    http.request(req)
  }
  raise 'ResponseError' unless res.code == 200
  return JSON.parse(res.body)
end
{% endmacro %}

{% macro post(item, url, obj) -%}
def post
  url = URI.parse('{{ url }}')
  headers = {'Content-Type' =>'application/json'}
  req = Net::HTTP::Post.new(url, initheader = headers)
  req.body = {{ obj }}
  res = Net::HTTP.new(url.host, url.port).start {|http|
    http.request(req)
  }
  raise 'ResponseError' unless res.code == 200
  return JSON.parse(res.body)
end
{% endmacro %}
