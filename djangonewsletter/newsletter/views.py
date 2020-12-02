from django.shortcuts import render, redirect, reverse
from .forms import NewsletterSignupForm
from .models import NewsletterSignup


# Create your views here.
def newsletter(request):
    """A view to subscribe to the newsletter"""
    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'postcode': request.POST['postcode'],
        }

        request_form = NewsletterSignupForm(form_data)
        if request_form.is_valid():
            request_form = request_form.save(commit=False)
            request_form.save()
            return redirect(reverse('newsletter'))

    else:
        request_form = NewsletterSignupForm()
        template = 'newsletter/newsletter_form.html'
        context = {
            'request_form': request_form,
        }
        return render(request, template, context)


def unsubscribe(request):
    """A view to unsubscribe to the newsletter"""
    if NewsletterSignup.objects.get(full_name=request.POST['full_name']):
        if NewsletterSignup.objects.get(email=request.POST['email']):
            if NewsletterSignup.objects.get(postcode=request.POST['postcode']):
                NewsletterSignup.objects.filter(email=request.POST['email']).delete()
                return redirect(reverse('newsletter'))
