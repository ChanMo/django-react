import json
import logging
from django import template
from django.core.cache import cache
from django.conf import settings
from django.utils.html import format_html, format_html_join

register = template.Library()
logger = logging.getLogger(__name__)


@register.simple_tag
def react_static(filename):
    cache_res = cache.get(filename)
    if cache_res:
        return cache_res

    if settings.DEBUG:
        domain = 'localhost'
        host = f'http://{domain}:5173/'
        res = format_html('''
  <script type="module">
   import RefreshRuntime from "http://{}:5173/@react-refresh"
   RefreshRuntime.injectIntoGlobalHook(window)
   window.$RefreshReg$ = () => {{}}
   window.$RefreshSig$ = () => (type) => type
   window.__vite_plugin_react_preamble_installed__ = true
  </script>
  <script>global = window</script>
  <script type="module" src="{}@vite/client" ></script>
  <script type="module" src="{}{}"></script>
''', domain, host, host, filename)
        return res

    manifest_file = settings.BASE_DIR / 'static/dist/manifest.json'
    with open(manifest_file, 'r') as f:
        res = json.loads(f.read())

    base_url = f'{settings.STATIC_URL}dist/'
    html_string = format_html('<script type="module" src="{}{}"></script>',
                     base_url, res[filename]['file'])


    if 'css' in res[filename].keys():
        css = format_html_join(
            '\n', '<link rel="stylesheet" type="text/css" href="{}{}">',
            ((base_url, i) for i in res[filename]['css'])
        )
        html_string = format_html('{}\n{}', html_string, css)

    cache.set(filename, html_string, 60)
    return html_string


