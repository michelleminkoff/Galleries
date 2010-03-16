from django import forms

TOPIC_CHOICES = (
    ('closed', 'Closed'),
    ('same location', 'Same location'),
    ('moved in Chicago', 'Moved in Chicago'),
    ('moved out of Chicago', 'Moved out of Chicago'),
)


class SearchForm(forms.Form):
    name = forms.CharField(initial='a')
    zipcode = forms.CharField(initial='60605')
    outcome=forms.ChoiceField(choices=TOPIC_CHOICES, initial='all')
    
