#   $$Author1$:Nick Larsson, Researcher, Dep. of Computer Science and Information Systems at Birkbeck University, London, England, email:nick@dcs.bbk.ac.uk, License:GNU GPLv3
#
#we acknowledge the use of the following software under the terms of the specified licences:
#
#Bootstrap - https://getbootstrap.com/docs/4.0/about/license/
#
#
#
#
#!/usr/bin/env python
import os

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from app import create_app
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
#manager.add_command("debug", Server(host='0.0.0.0', port=7777))


@app.before_first_request
def before_first_request():
    with app.app_context():
 	from app.main.models import initmodels
	initmodels()


if __name__ == '__main__':
    manager.run()
