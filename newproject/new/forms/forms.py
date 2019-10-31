from django import forms

from .models import Forms

class Formform(forms.ModelForm):
    title = forms.CharField(label='',
                widget=forms.TextInput(attrs={ "placeholder": "your title"}))
    class Meta:
        model = Forms
        fields = [
            'title',
            'description',
            'price',
        ]
class RawFormform(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={ "placeholder": "your title"}))
    description=forms.CharField(required=False,
                                widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "your description",
                                        "class": "new-class-name two",
                                        "id": "my_id_for_textarea",
                                        "rows": 20,
                                        "cols": 120
                                    }
                                )
                            )
    price=forms.CharField(initial=199.990)
