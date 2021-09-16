from django.forms import forms

from mylap.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('ISBN',)
