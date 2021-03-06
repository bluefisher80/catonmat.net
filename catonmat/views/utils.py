#!/usr/bin/python
#
# Peteris Krumins (peter@catonmat.net)
# http://www.catonmat.net  --  good coders code, great reuse
#
# The new catonmat.net website.
#
# Code is licensed under GNU GPL license.
#

from werkzeug               import import_string, Response

from mako.template          import Template
from mako.lookup            import TemplateLookup

from catonmat.config        import config
from catonmat.cache         import from_cache_or_compute
from catonmat.quotes        import get_random_quote

import re

# ----------------------------------------------------------------------------

class MakoDict(object):
    """
    Given a dict d, MakoDict makes its keys accessible via dot.
    It also returns None if the key doesn't exist.
    >>> d = DotDict({'apple': 5, 'peach': { 'kiwi': 9 } })
    >>> d.apple
    5
    >>> d.peach.kiwi
    9
    >>> d.coco
    None
    """
    def __init__(self, d, exclude=None):
        if exclude is None:
            exclude = []

        for k, v in d.items():
            if isinstance(v, dict) and k not in exclude:
                v = MakoDict(v)
            self.__dict__[k] = v

    def __getitem__(self, k):
        return self.__dict__[k]

    def __getattr__(self, name):
        if name.startswith('__'):
            return object.__getattr__(self, name)
        return None

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __setitem__(self, name, value):
        self.__dict__[name] = value


def number_to_us(num):
    return (','.join(re.findall(r'\d{1,3}', str(num)[::-1])))[::-1]


mako_lookup = TemplateLookup(
    directories=['catonmat/templates'],
    module_directory=config.mako_modules,
    output_encoding='utf-8'
)

def template_response(rendered_template):
    return Response(
        rendered_template,
        mimetype='text/html'
    )


def cached_template_response(computef, cache_key, duration, *args, **kw):
    return template_response(from_cache_or_compute(computef, cache_key, duration, *args, **kw))


def display_template(template, **template_args):
    rendered_template = render_template(template, **template_args)
    return template_response(rendered_template)


def display_plain_template(template, **template_args):
    rendered_template = render_plain_template(template, **template_args);
    return template_response(rendered_template)


def render_template(template_name, **template_args):
    quote = get_random_quote()
    top_pages = get_most_popular_pages()
    top_downloads = get_most_downloads()
    recent_pages = get_recent_pages()
    categories = session.query(Category).order_by(Category.name.asc()).all()
    post_archive = get_post_archive()
    return render_plain_template(
             template_name, 
             quote=quote,
             top_pages=top_pages,
             top_downloads=top_downloads,
             recent_pages = recent_pages,
             categories = categories,
             post_archive = post_archive,
             **template_args)


def render_plain_template(template_name, **template_args):
    template = get_template(template_name)
    return template.render(**template_args)


def get_template(name):
    file = name + ".tmpl.html"
    template = mako_lookup.get_template(file)
    return template


def get_view(endpoint):
  try:
    return import_string('catonmat.views.' + endpoint)
  except (ImportError, AttributeError):
    try:
      return import_string(endpoint)
    except (ImportError, AttributeError):
      raise RuntimeError('Could not locate view for %r' % endpoint)


from catonmat.models        import Category, session
from catonmat.statistics    import (
    get_most_popular_pages, get_most_downloads, get_recent_pages, get_post_archive
)

