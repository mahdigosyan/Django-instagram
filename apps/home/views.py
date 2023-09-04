from apps.accounts.forms import UserRegisterForm

from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User


class HomeView(FormView):
    form_class = UserRegisterForm
    template_name = 'home/home.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        cd = self.form_class.cleaned_data
        User.objects.create_user(cd['username'], cd['email'], cd['password'])
        messages.success(self.request, 'Successfully created account')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Invalid data')
        return self.render_to_response(self.get_context_data(form=form))