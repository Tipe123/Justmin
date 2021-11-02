from django.db import models
from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin , BaseUserManager, User 



    

class UserAccountManager(BaseUserManager):
    def create_user(self , email, first_name , last_name , cellphone  , password =None):
        if not email:
            raise ValueError("User must have email address")

        email =self.normalize_email(email)
        user = self.model(email = email , first_name = first_name , last_name = last_name , cellphone = cellphone )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self,first_name, last_name,cellphone,email, password):
        user = self.create_user(email, first_name , last_name , cellphone , password)

        user.is_staff = True
        user.is_superuser = True

        user.save()

        return user

class UserAccount(AbstractBaseUser , PermissionsMixin):

    email           = models.EmailField(max_length=255, unique = True)
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50) 
    cellphone       = models.CharField(max_length=15, unique = True)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','cellphone']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email


class Profile(models.Model):
    staff = models.OneToOneField(UserAccount , on_delete=models.CASCADE , null=True)
    bio = models.TextField(max_length=200)
    main_picture = models.ImageField(default= 'avatar.jpg' , upload_to= "Main_Images")
    profile_picture = models.ImageField(default = 'avatar.jpg' , upload_to = "Proile_Images")
    

    class Meta:
        verbose_name_plural = "User Profile Picture"
    
    def __str__(self):
        return f'{self.staff.first_name} {self.staff.last_name}- Profile'

# For Advertisement


ROOM__TYPE = (
    ("Sharing","Sharing"),
    ("Single","Single"),
    )

# Create your models here.
class House(models.Model):
    house_name = models.CharField(max_length=50)
    number_of_rooms = models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    suburb = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    stree_name = models.CharField(max_length=50)
    picture_main = models.ImageField(upload_to="Houses",blank=True)
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.house_name

class Room(models.Model):
    price = models.PositiveIntegerField()
    house = models.ForeignKey(House,on_delete=models.CASCADE)
    type_of_room = models.CharField(max_length=50, choices=ROOM__TYPE, default="Single")
    
    picture_main = models.ImageField(upload_to='Rooms',blank=True)
    picture_sub1 = models.ImageField(upload_to='Rooms',blank=True)
    picture_sub2 = models.ImageField(upload_to='Rooms',blank=True)
    
    def __str__(self):
        return f'{self.house.house_name} - {self.house.stree_name} price : {self.price}'

# In this model we want to assign a user a type of room
class Occupation(models.Model):
    owner = models.OneToOneField(UserAccount , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    set_move_in_date = models.DateTimeField()
    taken = models.BooleanField( default = False)
    room = models.OneToOneField(Room , on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Users Occupations"

    def __str__(self):
        return f'{self.owner.email}s room' 


class Location(models.Model):

    house = models.OneToOneField(House , on_delete=models.CASCADE)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)
    