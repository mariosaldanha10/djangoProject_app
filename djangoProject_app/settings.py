from pathlib import Path
import export as export
from django.conf import settings
from djangoProject_app import settings_dev
from djangoProject_app import settings_test

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings_base - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"

WSGI_APPLICATION = 'djangoProject_app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pollsdjango',
        'USER': 'root',
        'PASSWORD': 'admin100190',
        'HOST': 'localhost',
    },
    # 'CA3' This is a database configuration dictionary for the Django project's test settings module.
    'test': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pollsdjango_',
        'USER': 'root',
        'PASSWORD': 'admin100190',
        'HOST': 'localhost',
    }
}
"""
# this is to specify the test runner to use when running Django tests. 'CA3'
#TEST_RUNNER = 'django.test.runner.DiscoverRunner'

""" 'CA3'
This line of code assigns a string value 'djangoProject_app.test_settings' to a variable named test. 
This string is likely used as a reference to a Django test settings module that defines the settings 
required to run tests for the project.
"""
#test = 'djangoProject_app.test_settings'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




EMAIL_FILE_PATH = BASE_DIR / "sent_emails"

