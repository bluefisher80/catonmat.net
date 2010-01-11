#!/usr/bin/python
#
# Peteris Krumins (peter@catonmat.net)
# http://www.catonmat.net  --  good coders code, great reuse
#
# The new catonmat.net website. See this post for more info:
# http://www.catonmat.net/blog/50-ideas-for-the-new-catonmat-website/
#
# Code is licensed under GNU GPL license.
#

from werkzeug.exceptions    import NotFound

from catonmat.views.utils   import render_template_with_quote
from catonmat.quotes        import get_random_quote
from catonmat.parser        import parse
from catonmat.comments      import add_comment, get_comment, CommentError
from catonmat.urls          import get_page_from_request_path

def main(request, map):
    comment_error = ""
    form = request.form

    if request.method == "POST":
        # TODO: if request.form.get('ajax')
        try:
            add_comment(request)
            form = dict()
            # TODO: after adding comment, redirect to this comment's page
        except CommentError, e:
            comment_error = e.message

    template_data = {
        'page':             map.page,
        'page_path':        map.request_path,
        'display_comments': True,
        'comment_error':    comment_error,
        'form':             form,
        'comments':         map.page.comments.all()
    }
    map.page.content = parse(map.page.content)
    return render_template_with_quote("page", template_data)


def comment(request, path, id):
    # Look-up the path in the UrlMap table to find the matching page
    path = '/' + path
    map = get_page_from_request_path(path)
    if not map:
        raise NotFound() # TODO: this exception gets caught by `application`,
                         # which results in getpfrp being called again

    comment = get_comment(id)
    if not comment:
        raise NotFound()

    template_data = {
        'comment':   comment,
        'page':      map.page,
        'page_path': path
    }

    return render_template_with_quote("individual_comment", template_data)
