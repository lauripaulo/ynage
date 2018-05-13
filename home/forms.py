from django import forms


class SearchForm(forms.Form):
    languages = (
        (1, 'Java'),
        (2, 'C'),
        (3, 'Javascript'),
        (4, 'Ruby'),
        (5, 'Dart')
    )
    keyword = forms.CharField(label='Keyword', max_length=100,
                              widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                            'placeholder': 'Type something you want to search'}))
    language = forms.ChoiceField(label='Choose a programming language:', choices=languages,
                                 widget=forms.RadioSelect)
