# busybee

a simple lil todo list app, meant for personal use.

## Local Setup Instructions
This only works with Python 3. If you try to use Python 2, you will be very sad.

You should create a venv dedicated to this project. Then, activate the venv and run:

```
pip install -r requirements.txt
```

Then, run `python runserver.py`.

Visit `http://127.0.0.1:8000/`.


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

For all endpoints, only data that is associated in some way with the current user is displayed.

* List Projects
    * Endpoint: `/api/projects/`
* View Project
    * Endpoint: `/api/projects/<projectid>/`
* View Task
    * Endpoint: `/api/tasks/<taskid>/`
* View all Tasks within specific constraints
    * Endpoint: `/api/tasks/`
    * Parameters (all are optional):
        * `?tags=1,2,3`
            * Comma-separated list of Tag IDs to filter by.
        * `?project=<projectid>`
            * Project ID to filter by.
        * `?before=YYYY-MM-DD`
            * Filter by all tasks that are due before the given date.
        * `?after=YYYY-MM-DD`
            * Filter by all tasks that are due after the given date.
        * `?complete=<bool>`
            * Include completed tasks (default `true`)
        * `?incomplete=<bool>`
            * Include incomplete tasks (default `true`)
        * `?inactive=<bool>` 
            * Include tasks that are part of inactive projects (default `false`)
* View Tags
    * Endpoint: `/api/tags/`

## That's all for now
