from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Member, Borrow, Reservation, Fine
from core.models import UserProfile
from room_management.models import Room, RoomBooking
from django.utils import timezone

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone_number', 'address', 'gender', 'age', 'date_of_birth']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['notes']
        widgets = {
            'notes': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Optional notes about this borrowing...'
            })
        }

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['notes']
        widgets = {
            'notes': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Optional notes about this reservation...'
            })
        }

class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = ['booking_date', 'start_time', 'end_time', 'purpose', 'attendees_count', 'special_requirements', 'notes']
        widgets = {
            'booking_date': forms.DateInput(attrs={
                'class': 'form-control', 
                'type': 'date',
                'min': timezone.now().date().strftime('%Y-%m-%d')
            }),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control'}),
            'attendees_count': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'special_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')
        booking_date = cleaned_data.get('booking_date')
        
        if start_time and end_time:
            if start_time >= end_time:
                raise forms.ValidationError("End time must be after start time.")
        
        if booking_date:
            if booking_date < timezone.now().date():
                raise forms.ValidationError("Booking date cannot be in the past.")
        
        return cleaned_data

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'phone_number', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class BookSearchForm(forms.Form):
    query = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search books by title, author, or ISBN...'
        })
    )
    category = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    available_only = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

class ReturnBookForm(forms.Form):
    CONDITION_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('damaged', 'Damaged'),
    ]
    
    condition = forms.ChoiceField(
        choices=CONDITION_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='good'
    )
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 3, 
            'placeholder': 'Any notes about the book condition...'
        })
    )

class FinePaymentForm(forms.Form):
    payment_method = forms.ChoiceField(
        choices=[
            ('cash', 'Cash'),
            ('card', 'Credit/Debit Card'),
            ('online', 'Online Payment'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 2, 
            'placeholder': 'Payment notes...'
        })
    )

class RenewBookForm(forms.Form):
    notes = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 2, 
            'placeholder': 'Reason for renewal...'
        })
    )

class StudentRegistrationForm(forms.Form):
    # User account fields
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your desired username'
        }),
        help_text='Letters, digits and @/./+/-/_ only. 150 characters or fewer.'
    )
    first_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your first name'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your last name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        }),
        help_text='Your password must be at least 8 characters long and not entirely numeric.'
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm your password'
        }),
        help_text='Enter the same password as before, for verification.'
    )    # Member profile fields
    phone_number = forms.CharField(
        max_length=15,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+1 (555) 123-4567',
            'autocomplete': 'tel'
        })
    )
    address = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Enter your full address',
            'autocomplete': 'street-address'
        })
    )
    gender = forms.ChoiceField(
        choices=Member.GENDER_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'autocomplete': 'off'
        })
    )
    age = forms.IntegerField(
        min_value=16,
        max_value=100,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your age',
            'autocomplete': 'off'
        })
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'autocomplete': 'off'
        })
    )
    
    # Terms and conditions
    terms_accepted = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='I agree to the Terms and Conditions and Privacy Policy'
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('A user with this username already exists.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('A user with this email address already exists.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('The two password fields didn\'t match.')
            if len(password1) < 8:
                raise forms.ValidationError('Password must be at least 8 characters long.')
            if password1.isdigit():
                raise forms.ValidationError('Password cannot be entirely numeric.')
        return password2

    def clean_age(self):
        age = self.cleaned_data.get('age')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        
        if age and date_of_birth:
            from datetime import date
            today = date.today()
            calculated_age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            
            if abs(calculated_age - age) > 1:  # Allow 1 year difference for upcoming birthdays
                raise forms.ValidationError('Age doesn\'t match the date of birth.')
        return age

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError('Phone number is required.')
        if len(phone_number.strip()) < 8:
            raise forms.ValidationError('Phone number must be at least 8 digits.')
        return phone_number.strip()

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address:
            raise forms.ValidationError('Address is required.')
        if len(address.strip()) < 10:
            raise forms.ValidationError('Please provide a complete address (at least 10 characters).')
        return address.strip()      
    def save(self):
        """Create user and member profile"""
        # Create User
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        
        # UserProfile is automatically created by signals, just update the role if needed
        from core.models import UserProfile
        profile, created = UserProfile.objects.get_or_create(
            user=user,
            defaults={'role': 'student'}
        )
        if not created:
            profile.role = 'student'
            profile.save()
        
        # Member is also created by signals with default values, update with actual data
        member_id = f"STU{user.id:05d}"
        full_name = f"{self.cleaned_data['first_name']} {self.cleaned_data['last_name']}"
        
        # Get or create member and update with form data
        member, created = Member.objects.get_or_create(
            user=user,
            defaults={
                'member_id': member_id,
                'name': full_name,
                'email': self.cleaned_data['email'],
                'phone_number': self.cleaned_data['phone_number'],
                'address': self.cleaned_data['address'],
                'gender': self.cleaned_data['gender'],
                'age': self.cleaned_data['age'],
                'date_of_birth': self.cleaned_data['date_of_birth']
            }
        )
        
        # If member already exists (created by signal), update with form data
        if not created:
            member.member_id = member_id
            member.name = full_name
            member.email = self.cleaned_data['email']
            member.phone_number = self.cleaned_data['phone_number']
            member.address = self.cleaned_data['address']
            member.gender = self.cleaned_data['gender']
            member.age = self.cleaned_data['age']
            member.date_of_birth = self.cleaned_data['date_of_birth']
            member.save()
        
        return user