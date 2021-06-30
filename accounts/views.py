from django.shortcuts import render

from accounts.forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'accounts/register_done.html', {'user': user})
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
