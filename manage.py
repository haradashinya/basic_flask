#!/usr/bin/env python
from basic_app import create_app
from basic_app.tasks.models import Task






create_app().run(host="0.0.0.0",debug=True)




