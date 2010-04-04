#!/usr/bin/python
#
# Peteris Krumins (peter@catonmat.net)
# http://www.catonmat.net  --  good coders code, great reuse
#
# The new catonmat.net website.
#
# Code is licensed under GNU GPL license.
#

from catonmat.views.utils       import display_template
from catonmat.models            import Feedback

from urlparse                   import urlparse

import re

# ----------------------------------------------------------------------------

def main(request):
    if request.method == "POST":
        return handle_feedback_post(request)
    return handle_feedback_get(request)


class FeedbackError(Exception):
    pass


email_rx = re.compile(r'^.+@.+\..+$')


def validate_feedback(request):
    def validate_name(name):
        if not name:
            raise FeedbackError, "You forgot to specify your name!"
        if len(name) > 64:
            raise FeedbackError, "Your name is too long. Maximum length is 64 characters."

    def validate_email(email):
        if not email:
            raise FeedbackError, "You forgot to specify your e-mail!"
        if len(email) > 128:
            raise FeedbackError, "Your e-mail is too long. Maximum length is 128 characters."
        if not email_rx.match(email):
            raise FeedbackError, "Sorry, your e-mail address is not valid!"

    def validate_website(website):
        if website:
            if len(website) > 256:
                raise FeedbackError, "Your website address is too long. Maximum length is 256 characters."
            if '.' not in website:
                raise FeedbackError, "Your website address is invalid!"

            url = urlparse(website)
            if url.scheme:
                if url.scheme not in ('http', 'https', 'ftp'):
                    raise FeedbackError, "The only allowed website schemes are http://, https:// and ftp://"

    def validate_subject(subject):
        if not subject:
            raise FeedbackError, "You didn't write the subject of the message!"

    def validate_message(message):
        if not message:
            raise FeedbackError, "You didn't type the message!"

    validate_name(request.form['name'].strip())
    validate_email(request.form['email'].strip())
    validate_website(request.form['website'].strip())
    validate_subject(request.form['subject'].strip())
    validate_message(request.form['message'].strip())


def handle_feedback_post(request):
    thank_you = False
    try:
        validate_feedback(request)
        Feedback(
          request.form['name'].strip(), 
          request.form['email'].strip(),
          request.form['subject'].strip(),
          request.form['message'].strip(),
          request.form['website'].strip()
        ).save()
        thank_you = True
    except FeedbackError, e:
        return display_template("feedback", form=request.form, error=e.message)

    if thank_you:
        form = dict()
    else:
        form = request.form
    return display_template("feedback", form=form, thank_you=thank_you)


def handle_feedback_get(request):
    return display_template("feedback", form=dict())

