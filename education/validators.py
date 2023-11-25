from rest_framework.serializers import ValidationError


class LinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        link = 'youtube.com'
        tmp_val = dict(value).get(self.field)
        if link not in tmp_val:
            raise ValidationError("Only links from youtube.com are allowed")
