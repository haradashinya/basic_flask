#!/usr/bin/env python
from basic_app import create_app
from basic_app.tasks.models import Task
from basic_app.users.models import User








create_app().run(host="0.0.0.0",debug=True)




