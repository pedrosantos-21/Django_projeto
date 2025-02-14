from django.shortcuts import get_object_or_404, render, redirect
from .models import Pessoa
from .forms import PessoaForm

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'secretaria/home.html', {'pessoas': pessoas})

def add_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PessoaForm()
    return render(request, 'secretaria/add_pessoa.html', {'form': form})

def delete_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('home')
    return render(request, 'secretaria/delete_pessoa.html', {'pessoa': pessoa})
