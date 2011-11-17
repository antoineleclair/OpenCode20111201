# OpenCode 2011/12/01 presentation

This project will be used for my presentation about tests at OpenCode 2011/12/01 in Quebec City.

The content of this readme is not final yet. Please come back later for up-to-date content.

## Reason I use Python and Pyramid instead of X

Because it's easy to write tests and there is practically no boilerplate code. Pretty much everything is exposed so it's ideal in the context of my presentation.

## Preparation

To participate in the presentation and/or the workshop after, you will need some stuff installed on your computer. I use Ubuntu 11.10, but you can use anything you want. The content of the presentation should work equally on OS X or Windows. I provide command lines for Ubuntu, but you can follow the links for other OSes.

### Python

First, you will need [Python](http://python.org/). I use 2.7 during the presentation, and I'm pretty sure 2.6 would be OK. Don't use &lt;2.6 or 3.x.

Python 2.7 comes pre-installed with ubuntu 11.10.

### Virtualenv

[Virtualenv](http://pypi.python.org/pypi/virtualenv) allows you to isolate every Python environments for each of your apps. It's much like Bundle in Ruby. You can install it with

    $ sudo apt-get install python-virtualenv

### Create a directory to work in and a virtualenv
    $ cd /home/yourname/src
    $ mkdir opencode-tests
    $ cd opencode-tests
    $ virtualenv --no-site-packages env

The last line will create a virtualenv in the folder `env`.

### Clone this project
    $ git clone git://github.com/antoineleclair/OpenCode20111201.git

### Activate the virtualenv
From now on, each time you want to work with this virtualenv, you activate it with this command

    $ source env/bin/activate

And you can deactivate it with

    $ deactivate

When a virtualenv is activated you should have the name of the virtualenv in your prompt. E.g.: `(env)$`

### Install the project dependencies
    (env)$ cd cody
    (env)$ python setup.py develop
This will install all the dependencies listed in the project in your virtualenv. That's about it for the code.

### Firefox
I use Chrome most of the time, but you need Firefox for Selenium.

### Selenium
Install Selunium plugin. TODO how-to

### qunit
We will make some JavaScript tests with [qunit](https://github.com/jquery/qunit). TODO how-to.

