# HomeTask2
HMO = Health maintenance organization
This is a system for managing a health insurance fund during the Corona period.
The system holds the data of the insured and employees, personal details and corona information for each employee.
we start with MainPage.html page
In the first step, the system allows you to perform 3 different actions:
1. Get the data of all users
2. Get user data by name
3. Create a new user

![image](https://github.com/MYHINDA/HomeTask2/assets/40015918/8e4444b9-c549-45ad-ac7b-2b53a51b9323)

When choosing the first option, a GET request is sent to the server, the server goes to the DB where all the data is stored and fetches it.
![image](https://github.com/MYHINDA/HomeTask2/assets/40015918/2fc6b29f-a79c-4249-9479-df29f4928bef)

When choosing the second option, a POST request is sent with the search string, the server addresses the DB with the string and fetches the appropriate information from there. The reason that the request is sent in the POST method and not GET is, among other things, the security of the information, when sending a GET request, the information is saved in the URL and remains exposed.
![image](https://github.com/MYHINDA/HomeTask2/assets/40015918/14b197a4-a059-4b11-afcc-8be35750ffdf)

When choosing the third option, the system makes a reference to a form document, where the details must be filled in, some details are mandatory (such as name, ID number, phone, etc.) and there are details that are not mandatory (such as corona vaccinations, photo, etc.)
After filling out the form, the information is sent to the server via a POST request, the server processes the request and creates a new record in the DB with all the appropriate details.

![image](https://github.com/MYHINDA/HomeTask2/assets/40015918/58b2c4c5-4fc3-4018-8eb1-3cd6ce5bf333)

After creating the new record, a success message appears on the screen with the employee's name

*welcome Israel Israeli*
 
OS: Windows 10
Workspace: vscode, localhost:5000
Language: Python 3.10.7, HTML5
Modules: flask, bson, json, markupsafe
DB: mongoDB
Plugins: MongoDB for VS Code
Note
There is an option to import a file or export a file of all users, the option is accessible only to those who have access to the source files



