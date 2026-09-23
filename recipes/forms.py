from django import forms


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    ingredients = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(widget=forms.Textarea)
