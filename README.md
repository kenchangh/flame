flame
=====

Generating API functions using command line.

Use this:

`flame py get comments http://example.com/comments`

To get this:

```
def get_comments():
    api_url = 'http://example.com/comments'
    req = requests.get(api_url)
    assert req.status_code == 200
    return json.loads(req.text)
```

Then just convert `py` to `js` or `rb`.

Client-side JavaScript with jQuery:

```
function getComments(cb) {
  var apiUrl = 'http://example.com/comments';
  $.get(apiUrl, function(json) {
    var obj = JSON.parse(json);
    cb(obj);
  });
}
```

Ruby:

```
def get_comments
  url = URI.parse(http://example.com/comments)
  req = Net::HTTP::Get.new(url.to_s)
  res = Net::HTTP.start(url.host, url.port) {|http|
    http.request(req)
  }
  raise 'ResponseError' unless res.code == 200
  return JSON.parse(res.body)
end
```

Writing rules
-------------

Refer to the existing rules for Python, JavaScript and Ruby. Write it in (Jinja2)[http://jinja.pocoo.org/docs/dev/].

