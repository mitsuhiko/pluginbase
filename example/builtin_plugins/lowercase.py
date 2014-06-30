def make_lowercase(s):
    return s.lower()


def setup(app):
    app.register_formatter('lowercase', make_lowercase)
