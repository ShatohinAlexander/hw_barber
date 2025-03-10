from django import forms

from main.models import Review, Visit


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ["name", "phone", "comment", "master", "services"]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш телефон'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий',
                'rows': 4
            }),
            "master": forms.Select(attrs={"class": "form-select text-center"}),
            "services": forms.SelectMultiple(attrs={"class": "form-select text-center text-dark" , "style": "margin-top: 10px; color:black;"})
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'text', 'master', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш отзыв (минимум 30 символов)',
                'rows': 4
            }),
            'master': forms.Select(attrs={
                'class': 'form-control'
            }),
            'rating': forms.Select(attrs={
                'class': 'form-control'
            })
        }