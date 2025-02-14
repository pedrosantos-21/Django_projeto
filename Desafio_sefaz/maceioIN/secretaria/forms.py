from django import forms
from .models import Pessoa
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'setor', 'email']

    def __init__(self, *args, **kwargs):
        super(PessoaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Adicionar'))