#
# generator.py
#
# Written by John Sowell
#
# Written 7/10/2023 - 7/19/2023
#
# The main window (subclassed from jss_win), in this case, is the main
# screen to the Flask Website Generator project.
#
import os

from tkinter import *
from tkinter import messagebox

from jss_cons import *

from jss_button import jss_button
from jss_label import jss_label
from jss_text_box import jss_text_box
from jss_win import jss_win

# $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $

class generator(jss_win):

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # constructor function
    def __init__(self, master, t, w=500, h=375, m=GRID_MODE, b='#cccccc', f='#000000', r=7, c=4, sx=550, sy=0, ff='System', fs=8):
        super(generator, self).__init__(master, t, w, h, m, b, f, r, c, sx, sy, ff, fs)

        master.iconbitmap("JSS2.ico")

        self.banner = jss_label(self, 1, 1,"        FLASK WEBSITE GENERATOR        ", 2, None, "#cccccc", "#000000", "Times New Roman", 18, "center")

        self.lbl_start_folder = jss_label(self, 1, 2, "Starting Folder:",1,None, "#cccccc", "#000000","",8 ,'nw')
        self.txt_start_folder = jss_text_box(self, 2, 2, 40, 1, False, "", 1, self.update_start_folder)

        self.lbl_app_name = jss_label(self, 1, 3, "App Name:",1,None, "#cccccc", "#000000","",8, 'nw')
        self.txt_app_name = jss_text_box(self, 2, 3, 40, 1, False, "", 1, self.update_app_name)

        self.btn_generate = jss_button(self, 1, 4, 60, "GENERATE WEBSITE", 2, None, self.generate_website)

        self.btn_generate.disable()

        self.start_folder = ""
        self.app_name = ""

        self.txt_start_folder.widget.focus()

    # *************************************************************************
    # checks the two text boxes -- if both text boxes have something in them, enable generate button, else, disable it
    def check_strings(self):
        if len(self.app_name) > 0 and len(self.start_folder) > 0:
            self.btn_generate.enable()
        else:
            self.btn_generate.disable()

    # *************************************************************************
    # this is where the magic really occurs -- the start-up flask website is generated here
    def generate_website(self):
        # these four lines ensure all characters in the text boxes are accounted for (the fext change functions by themselves don't completely do it)
        self.start_folder = self.txt_start_folder.get_text()
        self.check_strings()
        self.app_name = self.txt_app_name.get_text()
        self.check_strings()

        # creates the base folder
        base_dir = self.slashify(self.start_folder) + "\\" + self.lower_space(self.app_name)
        cmd = "mkdir " + base_dir
        os.system(cmd)

        # creates the website folder
        web_dir = base_dir + "\\" + "website"
        cmd = "mkdir " + web_dir
        os.system(cmd)

        # creates the main.py file. When you create your website, type python main.py in your base folder, then copy and
        # paste the resulting URL to your browser to see your start-up flask website
        outfile = open(base_dir + "\\" + "main.py", "w")
        outfile.write("from website import create_app\n\n")
        outfile.write("app = create_app()\n\n")
        outfile.write("if __name__ == '__main__':\n")
        outfile.write("\tapp.run(debug=True)")
        outfile.close()

        # creates the static folder -- to house javascript and stylesheet files
        static_dir = web_dir + "\\static"
        cmd = "mkdir " + static_dir
        os.system(cmd)

        # creates the templates folder to house the HTML files, including the ones that use and access the base template
        templates_dir = web_dir + "\\templates"
        cmd = "mkdir " + templates_dir
        os.system(cmd)

        # creates the __init__.py file
        outfile = open(web_dir + "\\" + "__init__.py", "w")
        outfile.write("from flask import Flask\n\n")
        outfile.write("def create_app():\n")
        outfile.write("\tapp = Flask(__name__)\n")
        outfile.write("\tapp.config['SECRET_KEY'] = 'KEY'\n\n")
        outfile.write("\tfrom .views import views\n")
        outfile.write("\tfrom .auth import auth\n")
        outfile.write("\tapp.register_blueprint(views, url_prefix='/')\n")
        outfile.write("\tapp.register_blueprint(auth, url_prefix='/')\n\n")
        outfile.write("\treturn app")
        outfile.close()

        # creates the auth.py file -- rendering the login page
        outfile = open(web_dir + "\\" + "auth.py","w")
        outfile.write("from flask import Blueprint, render_template\n\n")
        outfile.write("auth = Blueprint('auth', __name__)\n\n")
        outfile.write("@auth.route('/login')\n")
        outfile.write("def login():\n")
        outfile.write("\treturn render_template('login.html')")
        outfile.close()

        # generates the models.py, for data models -- empty by default
        outfile = open(web_dir + "\\" + "models.py","w")
        outfile.close()

        # generates the views.py file, for rendering the home page, and other pages not related to authentication
        outfile = open(web_dir + "\\" + "views.py","w")
        outfile.write("from flask import Blueprint, render_template\n\n")
        outfile.write("views = Blueprint('views', __name__)\n\n")
        outfile.write("@views.route('/')\n")
        outfile.write("def home():\n")
        outfile.write("\treturn render_template('home.html')")
        outfile.close()

        # generates a default javascript file, which is empty to start
        outfile = open(static_dir + "\\" + "index.js", "w")
        outfile.close()

        # generates the base template file (base.html)
        outfile = open(templates_dir + "\\" + "base.html","w")
        outfile.write("<html>\n")
        outfile.write("\t<head>\n")
        outfile.write('\t\t<meta charset = "UTF-8">\n')
        outfile.write('\t\t<meta name = "viewport"content = "width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">\n')
        outfile.write('\t\t<meta name = "viewport" content = "width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">\n')
        outfile.write('\t\t<meta http - equiv = "X-UA-Compatible" content = "ie=edge">\n')
        outfile.write('\t\t<link rel = "stylesheet" href = "https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" /\n')
        outfile.write("\t\t<title> {% block title %} Home {% endblock %} </title>\n")
        outfile.write('\t\t<nav class ="navbar navbar-expand-lg navbar-dark bg-dark">\n')
        outfile.write('\t\t\t<button class ="navbar-toggle" type="button" data-toggle="collapse" data-target="#navbar" >')
        outfile.write('<span class="navbar-toggler-icon"> </span></button>\n')
        outfile.write('\t\t\t<div class ="collapse navbar-collapse" id="navbar" >\n')
        outfile.write('\t\t\t\t<div class ="navbar-nav">\n')
        outfile.write('\t\t\t\t\t<a class ="nav-item nav-link" id="login" href="/login" > Login </a>\n')
        outfile.write('\t\t\t\t\t<a class ="nav-item nav-link" id="home" href="/" > Home </a>\n')
        outfile.write('\t\t\t\t</div>\n\t\t\t</div>\n')
        outfile.write('\t\t</nav>\n\t</head >\n')
        outfile.write('\t<body style = "background-color: black; color: white;" >\n')
        outfile.write('\t\t<div class ="container" style="background-color: #000040; color: gold;">\n')
        outfile.write('\t\t\t{% block content %}{% endblock %}\n')
        outfile.write('\t\t</div>\n\t\t<script type="text/javascript" src="{{ url_for(')
        outfile.write("'static', filename='index.js') }}")
        outfile.write('"></script>\n\t</body>\n</html>')
        outfile.close()

        # generates the home page (home.html)
        outfile = open(templates_dir + "\\" + "home.html","w")
        outfile.write('{% extends "base.html" %}\n')
        outfile.write('{% block title %}Home Page {% endblock %}\n')
        outfile.write('{% block content %}\n')
        outfile.write('<h1> This Is The Home Page!</h1>\n')
        outfile.write('{% endblock %}')
        outfile.close()

        # generates the login page (login.html)
        outfile = open(templates_dir + "\\" + "login.html","w")
        outfile.write('{% extends "base.html" %}\n')
        outfile.write('{% block title %}Login Page{% endblock %}\n')
        outfile.write('{% block content %}\n')
        outfile.write('<form method = "POST">\n')
        outfile.write('<h1>This Is The Login Page!</h1>\n')
        outfile.write('</form>\n')
        outfile.write('{% endblock %}')
        outfile.close()

        messagebox.showinfo("ALL DONE", "Website Generated!")

    ###########################################################################

    def lower_space(self, str):
        # converts strings to lower case, and converts spaces to underlines (for creating folders)
        low_str = str.lower()
        new_str = ""
        for i in range(0,len(str)):
            if low_str[i] != ' ':
                new_str += low_str[i]
            else:
                new_str += '_'

        return new_str

    ###########################################################################

    def slashify(self, str):
        # creates extra slashes when necessary (for creating folders)
        new_str = ""
        for i in range(0,len(str)):
            new_str += str[i]
            if str[i] == '\\':
                new_str += '\\'

        return new_str

    # *************************************************************************

    def update_app_name(self, e):
        # updates the app name by keystroke (doesn't take care of the last character)
        self.app_name = self.txt_app_name.get_text()
        self.check_strings()

    # *************************************************************************

    def update_start_folder(self, e):
        # updates the start folder string (doesn't account for the last character)
        self.start_folder = self.txt_start_folder.get_text()
        self.check_strings()