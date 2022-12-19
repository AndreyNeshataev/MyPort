from django.shortcuts import render, redirect
from django.contrib.auth import login  # authenticate,
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# from app_users.models import Profile, PurchaseHistory
from django.http import HttpResponseRedirect
from .forms import *


# class RegisterUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = 'users/register.html'
#     success_url = reverse_lazy('login_url')

    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         user = form.save()
    #         city = form.cleaned_data.get('city')
    #         date_of_birth = form.cleaned_data.get('date_of_birth')
    #         number_phone = form.cleaned_data.get('number_phone')
    #         profile = Profile.objects.create(user=user,
    #                                          city=city,
    #                                          date_of_birth=date_of_birth,
    #                                          number_phone=number_phone,
    #                                          )
    #         profile.save()
    #         login(self.request, user)
    #         return redirect(self.success_url)
    #     return render(request, 'users/register.html', {'form': form})


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


    # def form_valid(self, form):
    #     """Security check complete. Log the user in."""
    #     login(self.request, form.get_user())
    #     logger.info(f'Пользователь: {self.request.user.username}, ID: {self.request.user.id} прошел аутентификацию')
    #     return HttpResponseRedirect(self.get_success_url())


# class LogoutUser(LogoutView):
#     pass
#
#
# class MyUser(ListView):
#     model = User
#     template_name = 'users/account.html'
#
#
# class ChangeUser(UpdateView):
#     success_url = reverse_lazy('home')
#
#     def get(self, request, *args, **kwargs):
#         my_profile = Profile.objects.get(user_id=self.request.user.id)
#         my_user = User.objects.get(id=self.request.user.id)
#         profile_form = ChangeProfileForm(instance=my_profile)
#         user_form = ChangeUserForm(instance=my_user)
#         return render(request, 'users/change_user.html', {'profile_form': profile_form,
#                                                           'user_form': user_form})
#
#     def post(self, request, *args, **kwargs):
#         my_profile = Profile.objects.get(user_id=self.request.user.id)
#         my_user = User.objects.get(id=self.request.user.id)
#         profile_form = ChangeProfileForm(request.POST, instance=my_profile)
#         user_form = ChangeUserForm(request.POST, instance=my_user)
#         if user_form.is_valid() and profile_form.is_valid():
#             my_user.first_name = user_form.cleaned_data.get('first_name')
#             my_user.last_name = user_form.cleaned_data.get('last_name')
#             my_user.save()
#             my_profile.city = profile_form.cleaned_data['city']
#             my_profile.number_phone = profile_form.cleaned_data['number_phone']
#             my_profile.save()
#             return redirect(self.success_url)
#         return render(request, 'users/change_user.html', {'profile_form': profile_form,
#                                                           'user_form': user_form})
#
#
# class ReplenishmentBalance(ListView):
#     success_url = reverse_lazy('home')
#
#     def get(self, request, *args, **kwargs):
#         form = ReplenishmentBalanceForm()
#         return render(request, 'users/replenishment_balance.html', {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         my_profile = Profile.objects.get(user_id=request.user.id)
#         form = ReplenishmentBalanceForm(request.POST)
#         if form.is_valid():
#             my_profile.balance = float(my_profile.balance) + float(form.cleaned_data['amount_balance'])
#             my_profile.save()
#             logger.info(f'Пользователь: {request.user}, ID: {request.user.id}'
#                         f' пополнил баланс на сумму: {form.cleaned_data["amount_balance"]} руб')
#             return redirect(self.success_url)
#         return render(request, 'users/replenishment_balance.html', {'form': form})
#
#
# def purchase_history(request, *args, **kwargs):
#     history_list = PurchaseHistory.objects.filter(user_id=request.user.id)
#     return render(request, 'users/history.html', {'history_list': history_list})
