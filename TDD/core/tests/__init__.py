"""
Command Line
# Run all the tests in the core.tests module
$ python manage.py test core.tests

# Run all the tests found within the 'core' package
$ python manage.py test core

# Run just one test case
$ python manage.py test core.tests.test_admin

# Run just one test method
$ python manage.py test core.tests.test_models.ModelTests.test_create_user_with_email_successful({app_name}.{tests}.{module_name}.{class_name}.{method})
"""
