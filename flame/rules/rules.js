
{% macro get(item, url, obj={}) -%}
function get{{ item|title }}(cb) {
  var apiUrl = '{{ url }}';
  $.get(apiUrl, function(json) {
    var obj = JSON.parse(json);
    cb(obj);
  });
}
{% endmacro %}


{% macro post(item, url, obj) -%}
function post{{ item|title }}(cb) {
  var apiUrl = '{{ url }}';
  var obj = {{ obj }};
  $.post(apiUrl, obj, function(json) {
    var returnedObj = JSON.parse(json);
    cb(returnedObj);
  });
}
{% endmacro %}
