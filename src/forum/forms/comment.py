from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(max_length=15000, 
                           required=True, 
                           widget=forms.Textarea(), 
                           label="Сообщение")
