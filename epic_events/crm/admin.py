from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User, Client, Contract, Event


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ("email", "role", "is_admin")
    list_filter = ["role"]
    fields = (("first_name", "last_name"), "email", "role", "password", "is_active", "is_staff")

    def save_model(self, request, obj, form, change):
        if change:
            if form.cleaned_data['password']:
                obj.set_password(form.cleaned_data['password'])
            else:
                existing_user = User.objects.get(pk=obj.pk)
                obj.password = existing_user.password
        else:
            obj.set_password(form.cleaned_data['password'])
        obj.save()


# register the new UserAdmin
admin.site.register(User, UserAdmin)

# unregister the Group model from admin.
admin.site.unregister(Group)

admin.site.register(Client)
admin.site.register(Contract)
admin.site.register(Event)
