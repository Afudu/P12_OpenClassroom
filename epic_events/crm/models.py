from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('role', 'ADMIN')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model extending the default Django User, for creating users.
    AbstractBaseUser by default contains password, last_login and is_active.
    Adding additional fields:  roles for Management, Sales, and Support.
    """

    ROLE_CHOICES = [('SALES', 'Sales'),
                    ('SUPPORT', 'Support'),
                    ('MANAGEMENT', 'Management'),
                    ('ADMIN', 'Admin')
                    ]

    username = None
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=20,
                            choices=ROLE_CHOICES,
                            null=True,
                            blank=True,
                            help_text="Role of the user in the system",
                            )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # users log in using their email addresses
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        ordering = ('first_name', 'last_name')

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    def save(self, *args, **kwargs):
        if self.role == 'MANAGEMENT':
            self.is_admin = True
            self.is_staff = True

        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.email}"

    def __repr__(self):
        return f"{self.first_name} {self.last_name} - Role : {self.role}"


class Client(models.Model):
    """Represents a client, either potential or existing."""

    objects = None
    STATUS_CHOICES = [('POTENTIAL', 'Potential'),
                      ('EXISTING', 'Existing')]

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20, blank=True)
    address = models.TextField(null=True, blank=True)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(User,
                                      on_delete=models.SET_NULL,
                                      related_name="clients",
                                      null=True,
                                      limit_choices_to={'role': 'SALES'}
                                      )
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, default='Potential')

    def __str__(self):
        return f"Client - {self.company_name}"


class Contract(models.Model):
    """ Model for creating contracts signed by clients."""
    objects = None
    STATUS_CHOICES = [('SIGNED', 'Signed'),
                      ('OPEN', 'Open')]
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               related_name="contract_assigned_to")
    amount = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_signed = models.DateField(blank=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=True, default='Open')

    def __str__(self):
        return f"Contract for {self.client}"


class Event(models.Model):
    """Represents events for signed contracts."""
    objects = None
    STATUS_CHOICES = [('UPCOMING', 'Upcoming'),
                      ('ONGOING', 'Ongoing'),
                      ('CANCELLED', 'Cancelled'),
                      ('COMPLETED', 'Completed')
                      ]
    name = models.CharField(max_length=255)
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, related_name="events", null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(User,
                                        on_delete=models.SET_NULL,
                                        related_name="events",
                                        limit_choices_to={'role': 'SUPPORT'},
                                        null=True,
                                        blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(max_length=500)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"Event: {self.name} - Date : {self.start_date}"
