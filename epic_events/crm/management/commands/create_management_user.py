from django.core.management.base import BaseCommand
from crm.models import User


class Command(BaseCommand):
    help = "Create a new management user"

    def handle(self, *args, **kwargs):
        self.stdout.write("Enter details for the new management user:")
        email = input("Email: ")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        password = input("Password: ")

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.ERROR("A user with this email already exists."))
            return

        User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role='MANAGEMENT',
            password=password,
        )
        self.stdout.write(self.style.SUCCESS(f"Management user {email} created successfully."))
