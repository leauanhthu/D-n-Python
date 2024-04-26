from django import forms
from .models import Publisher, Review
from django.views.generic import DetailView
from .models import Book

class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(choices=[('title', 'Title'), ('contributor', 'Contributor')], required=True)
class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'website', 'email']
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 0, 'max': 5})
        }
