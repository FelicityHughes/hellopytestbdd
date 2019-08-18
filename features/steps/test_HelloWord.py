from hamcrest import assert_that, equal_to
from pytest_bdd import scenarios, given, when, then

import pytest

from hello.HelloWorld import HelloWorld


@pytest.fixture(scope="module")
def greeter():
    return HelloWorld()


scenarios("../")


#
# 'Then' step, which asserts the output of
# {@link HelloWorld#printGreeting()} equals the supplied value.
#
# @param greeting The expected greeting from the {@link HelloWorld} class.
#
@then('should result in "<greeting>"')
def check_greeting(greeter, greeting):
    assert_that(greeter.print_greeting(), equal_to(greeting))


#
# Given' step, which asserts the {@link HelloWorld#setName(String)}
# method properly saves the supplied name.
#
# @param name The name to set in the {@link HelloWorld} class.
#
@given('the name "<name>"')
def set_name(greeter, name):
    greeter.name = name
    assert_that(greeter.name, equal_to(name))


#
# 'When' step, which asserts the {@link HelloWorld#setSalutation(String)}
# method properly saves the supplied salutation.
#
# @param salutation The salutation to set in the {@link HelloWorld} class.
#
@when('combined with "<salutation>"')
def set_salutation(greeter, salutation):
    greeter.salutation = salutation
    assert_that(greeter.salutation, equal_to(salutation))
