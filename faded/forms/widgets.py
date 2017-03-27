# from django.conf import settings
# from django.forms.widgets import Media, Widget
# from django.forms.utils import flatatt
# from django.utils.encoding import force_text
# from django.utils.html import format_html
#
#
# class RichText(Widget):
#     def __init__(self, attrs=None):
#         default_attrs = {'cols': '40', 'rows': '10', 'class': 'tinymce'}
#         if attrs:
#             default_attrs.update(attrs)
#         super(RichText, self).__init__(default_attrs)
#
#     @property
#     def media(self):
#         root = settings.STATIC_URL + 'faded/widgets/'
#         editor = root + 'tinymce/tinymce.min.js'
#         setup = root + 'tinymce/tinymce_setup.js'
#         return Media(js=(editor, setup))
#
#     def render(self, name, value, attrs=None):
#         if value is None:
#             value = ''
#         final_attrs = self.build_attrs(attrs, name=name)
#         return format_html('<textarea{}>\r\n{}</textarea>', flatatt(final_attrs), force_text(value))
