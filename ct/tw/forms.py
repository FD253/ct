from django import forms
from tw.models import Tweet
from tastypie.validation import Validation

class AwesomeValidation(Validation):
    def is_valid(self, bundle, request=None):
        if not bundle.data:
            return {'__all__': 'Not quite what I had in mind.'}

        errors = {}

        for key, value in bundle.data.items():
            if key.startswith('image'):
                print(value)
                if value.file.size > 5*1024*1024:
                    errors[key] = ['IMAGE TOO BIG']

class TweetForm(forms.Form):
    class Meta:
        model = Tweet
        validation = AwesomeValidation()
        resource_name = 'tw/tweet'

