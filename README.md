# GroceryList

<h2>Distributed Grocery list</h2>
<h3> Version Used </h3>
<ol>
	<li> python 3.7.2 </li>
	<li> Django==3.0.4 </li>
</ol>

<h3>UI:</h3>
<ol>
	<li> <br>SignUp <br><img src = "https://github.com/SanjayChandak95/GroceryList/blob/master/Output_Screen/SignUp.PNG">  </li>
	<li> <br>Login<br><img src = "https://github.com/SanjayChandak95/GroceryList/blob/master/Output_Screen/Login.PNG"> 	</li>
	<li> <br>Welcome Page<br><img src = "https://github.com/SanjayChandak95/GroceryList/blob/master/Output_Screen/Welcome.PNG"></li>
	<li> <br>create Grocery Title<br><img src = "https://github.com/SanjayChandak95/GroceryList/blob/master/Output_Screen/create_new_grocery_list_title.PNG"></li>
	<li> <br>create Content in the Grocery and share it with other<br><img src = "https://github.com/SanjayChandak95/GroceryList/blob/master/Output_Screen/Application_page.PNG"></li>
</ol>
If user click on any grocery list, then on second page the content of list will display and on third page the other users detail will display with the authority. 

Only whoever have edit property can add list. 
And whoever have admin property can remove, add and delete any list. 

<h3>Data base:</h3>
<ol>
	<li>	User table : email and password and security question and answer, confirmation link </li>
	<li>	Grocery list : grocery list name </li>
	<li>	ContentInList : content and foreign key to Grocery list </li>
	<li>	UsersAndGrocery : groceryListId ,UserId , canEdit, canView, isAdmin, isCreator </li>
</ol>

<h3> Method: </h3>
<ol>
	<li>	Signup </li>
	<li>	Login	</li>
	<li>	CreateGroceryList	</li>
	<li>	DeleteGroceryList	</li>
	<li>	CreateContentInList	</li>
	<li>	DeleteContentInList	</li>
	<li>	AddUserToGrocery	</li>
</ol> 

