# GroceryList

<h2>Distributed Grocery list</h2>

<h3>UI:</h3>
	1. SignUp <br>
	2. Login
	3. Welcome Page (login required)
	4. create Grocery Title
	5. create Content in the Grocery
	6. Other can also share it to whom creator or admin share the list. 
	(Refer Output Screen Folder for browser data)

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

Validation (still need to be implemented) : 
	1.	Unique email
	2.	Password will be complex
	3.	Every 30 days password need to be change

————-
