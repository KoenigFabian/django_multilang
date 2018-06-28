# django_multilang
django multilanguage example

setup up multilang follow this link
http://levipy.com/django-internationalization/

install gnu text editor on mac / ubuntu<p>

- mac:<br>
Install Homebrew : /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"<br>
Install GNU gettext : brew install gettext<br>
Create symlink : brew link gettext --force<p>
- ubuntu:<br>
sudo apt-get install gettext<br><p>


delete everything that has to do with git in folder<br>
- rm -rf .git*<p>


./manage.py makemessages -l en (create all messages to be translated)<br>
django-admin compilemessages (compile translation file to be used with django)
