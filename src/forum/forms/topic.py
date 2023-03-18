from django import forms


class TopicForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Название темы")
    text = forms.CharField(max_length=15000, 
                           required=True, 
                           widget=forms.Textarea(),
                           label="Сообщение")
