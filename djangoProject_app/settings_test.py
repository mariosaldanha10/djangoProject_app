import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject_app.settings_test')

DEBUG = False

DATABASES = {
    'test': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pollsdjango_',
        'USER': 'root',
        'PASSWORD': 'admin100190',
        'HOST': 'localhost',
    }
}

# this is to specify the test runner to use when running Django tests. 'CA3'
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

""" 'CA3'
This line of code assigns a string value 'djangoProject_app.test_settings' to a variable named test. 
This string is likely used as a reference to a Django test settings module that defines the settings 
required to run tests for the project.
"""
test = 'djangoProject_app.test_settings'


