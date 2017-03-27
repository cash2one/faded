# from django.db import models
#
# class RichTextField(models.TextField):
#     def __init__(self, *args, **kwargs):
#         super(RichTextField, self).__init__(*args, **kwargs)
#
#     def formfield(self, **kwargs):
#         kwargs['widget'] = TinyMCE(attrs={'cols': 80, 'rows': 30})
#         return super(RichTextField, self).formfield(**kwargs)