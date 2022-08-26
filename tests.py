from django.test import TestCase

# Create your tests here.
from django.test import TransactionTestCase
from django.test import TransactionTestCase
from django.test.runner import DiscoverRunner
from unittest.suite import TestSuite

class UnitTestRunner(DiscoverRunner):
def setup_databases(self, **kwargs):
pass
def teardown_databases(self, old_config, **kwargs):
pass
def build_suite(self, **kwargs):
suite = super().build_suite(**kwargs)
tests = [t for t in suite._tests if self.is_unittest(t)]
return TestSuite(tests=tests)
def is_unittest(self, test):
return not issubclass(test.class, TransactionTestCase)
# unittest.py
from django.core.management.commands.test import Command as TCommand

class Command(TCommand):

def execute(self, *args, **options):
    test_class = 'oncokdm_api.runner.unittest.UnitTestRunner'
    options['testrunner'] = test_class
    super().execute(*args, **options)
