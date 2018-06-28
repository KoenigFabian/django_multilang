# django_multilang
django multilanguage example

setup up multilang follow this link
http://levipy.com/django-internationalization/

install gnu text editor on mac / ubuntu

- mac:
Install Homebrew : /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
Install GNU gettext : brew install gettext
Create symlink : brew link gettext --force
- ubuntu:
sudo apt-get install gettext


delete everything that has to do with git in folder
- rm -rf .git*


./manage.py makemessages -l en (create all messages to be translated)
django-admin compilemessages (compile translation file to be used with django)
