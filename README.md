Niak in your browser

The server has a some dependency that need to be instaled before it can run smoothly.

We recommand instaling a python3 virtual env to make it run in `./python_virtual` with the following command

```virtualenv -p /path/to/python3``` path/to/web_nial/venv_niak`

then

```source path/to/web_nial/venv_niak/bin/activate```

this makes ``path/to/web_nial/venv_niak/bin the "default python path" is your terminal, this means that pip an easy_install are also called from there.

Some library are needed to have the server running they are include in the setup.py file
Runnig `python setup.py develop` should install all that you need in your virtual environement
Do not forget to add the package you add for additional developpement in the setup.py file 


