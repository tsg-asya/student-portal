<p align="center"><img src="logo.jpg" height="140" alt="logo"/></p>
<h1 align="center">Student Portal 📚</h1>
<p align="center">Unofficial Student Portal for University until Approved!</p>
<p align="center">
<img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/AnimeshRy/gymrocket">
<a href="https://img.shields.io/github/issues/tsg-asya/portal-backend"><img alt="GitHub issues" src="https://img.shields.io/github/issues/tsg-asya/portal-backend"></a>
<a href="https://img.shields.io/github/issues/tsg-asya/portal-backend/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/tsg-asya/portal-backend"></a>

## ⚡ Features

🎯 **Multiple User Authentication** - Access to Create a Teacher and a Student Account

🎯 **Course Creation and Enrollment** - Teacher's Create Courses and Student Enroll, there's more too

🎯 **Notices/Results Creation** - Seperate Staff only access to CRUD Notices and Results

🎯 **Quizzes** - Teacher's Create Multiple Choice Quizzes and Students can take them

> Many more features that you can explore yourself

## 🚀 Setup

These instructions will get you a copy of the project up and running on your local machine for deployement and development.

You'll need [Git](https://git-scm.com) and [Python 3.8+](https://www.python.org/downloads/) installed on your local computer.

```
python@3.8 or higher
git@2.17.1 or higher
```

You can also use the [Zip](https://github.com/tsg-asya/portal-backend/archive/refs/heads/main.zip) file and extract the folder.

## 🔧 How To Use

From your command line, clone and deploy:

```bash
# Clone this repository
$ git clone https://github.com/tsg-asya/portal-backend

# Go into the repository
$ cd portal-backend

# Install dependencies
# if Pipenv available ? run
$ pipenv install

# Else
$ pip install -r requirements.txt

```

## 📨 Environment Setup

```bash
# You'll need some environment variables
touch .env
# replace string with a random string
SECRET_KEY={string}
DEBUG=True
```

## 🛠️ Django Setup

After installing the requirements, we'll need to setup some Django commands.

### Perform database migration:

```bash
python manage.py check
python manage.py migrate
```

### Create Admin Account

> This is the admin account and only this user can login.

```bash
python manage.py createsuperuser
# follow instruction
```

### Create Staff Account

> You can create a group inside admin and make new staff users members in it. Not giving permissions by default is a security feature.

### Run Development Server

```bash
python manage.py runserver
```

Navigate to [http://localhost:8000/](http://localhost:8000/) endpoint in your browser.

Admin endpoint is at http://127.0.0.1:8000/admin/

## Important

This is a part of a **project for my university** and is still **in development** and the README isn't complete yet.

## 📄 License

This project is licensed under the GPL3 License - see the [LICENSE.md](./LICENSE) file for details


#### Designed & Developed with 💙 by [Animesh Singh](https://www.github.com/AnimeshRy)
