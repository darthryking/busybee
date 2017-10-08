# busybee

a simple lil todo list app, meant for personal use.

## Models

* Project
* Task
* Tag
* plus anything you need for authentication/user accounts

### Project

* Tied to a user account
* Name (text field, not optional)
* Description (can be long, text field, can be empty)
* Flag for marking it active/inactive

### Task

* Tied to a project (not optional, many to one)
* Name (text field, not optional)
* Description (can be long, text field, can be empty)
* Flag for marking complete/incomplete
* Due date (optional)

### Tag

* Tied to Task (many-to-many)
* Name

AND THAT'S IT!

## Views and Controllers

* Home page

### Authentication

* Login page
* Logout page
* Register page

Authentication will be SUPER simple. Each user must provide username, password, and email. These three fields are NOT optional. However that's all they need, there is no other user info.

### Main Page Views

These pages will be where the user lands and where things happen. However the actual functionality will be done through Ajax calls on these pages, to like... other pages.

* Dashboard (Home page when you are logged in)
* Project view (Home page for a Project)
* Tags view (Home page for searching through tags)

You can make these empty for now, because they are 100% front-end things.

### Main Controllers for functionality

These will all be called through Ajax only, and will return JSON results rather than a webpage. You can decide what to name stuff in this API, basically just... do whatever works, just document it so I know how to call it.

#### POST - things that change state

* Create new Project
* Create new Task
* Edit Task:
	- Name
	- Description
	- Due date
	- Mark complete/incomplete
* Edit Project: 
	- Name
	- Description
	- Mark active/inactive

#### GET - for viewing data

* View Project
* View Task
* View all Tasks within specific constraints
	* Constraint: can specify multiple tags
	* Constraint: can specify a project, or "all projects"
	* Constraint: can specify up to two dates: 
		* "Before" date - view all projects due before this date
		* "After" date - view all projects due after this date
	* Constraint: Complete/incomplete/both
	* Constraint: Option to show tasks in inactive projects; by default they are not shown

## That's all for now