from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length = 254) # max length required
    password = models.CharField(max_length = 200)
    securityQuestion = models.CharField(max_length = 200)
    securityQuesAnswer = models.CharField(max_length = 200)
    confirmationLink = models.CharField(max_length = 200)
    auth = models.BooleanField(default = False)

    def __str__(self):
        return self.email

class GroceryList(models.Model):
    title = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 254,default = "test@test.com") #just for distinguish
    def __str__(self):
        return self.title

class GrocerListContent(models.Model):
    item = models.CharField(max_length = 200)
    groceryListId = models.ForeignKey(GroceryList, on_delete=models.CASCADE)
    def __str__(self):
        return self.item

class UsersAndGrocery(models.Model):
    groceryListId = models.ForeignKey(GroceryList, on_delete=models.CASCADE)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    canEdit = models.BooleanField(default = False)
    canView = models.BooleanField(default = False)
    isAdmin = models.BooleanField(default = False)
    isCreator = models.BooleanField(default = False)
