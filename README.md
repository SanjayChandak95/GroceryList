# GroceryList

Distributed Grocery list

Sign up and login

After login user will create grocery list and add different user to edit or view or both. 

Ui:
First login and then,
Three part. 
	1.	All different type of grocery list
	2.	Blank page
	3.	Blank

Forget password: question answer
Change Password : 

If user click on any grocery list, then on second page the content of list will display and on third page the other users detail will display with the authority. 

Only whoever have edit property can add list. 
And whoever have admin property can remove, add and delete any list. 

Data base:
	1.	User table : email and password and security question and answer
	2.	Grocery list : grocery list name
	3.	ContentInList : content and foreign key to Grocery list
	4.	UsersAndGrocery : groceryListId ,UserId , canEdit, canView, isAdmin, isCreator

Method:
	1.	Signup
	2.	Login
	3.	CreateGroceryList
	4.	DeleteGroceryList
	5.	CreateContentInList
	6.	DeleteContentInList
	7.	AddUserToGrocery

Require: python and django for backend, basic HTML in frontend. 

Validation : 
	1.	Unique email
	2.	Password will be complex
	3.	Every 30 days password need to be change

————-
