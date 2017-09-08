from behave import *
from main import Calculator
from nose import *

# use_step_matcher(parse)
#
# @parse.with_pattern(r"\d+")
# def parse_number(text):
#     return int(text)
#
# register_type(Number=parse_number)
obj = Calculator()


@given("nothing")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("inputs {x} and {y} are passed")
def step_impl(context, x, y):
    """
    :type context: behave.runner.Context
    """
    obj.a = int(x)
    obj.b = int(y)


@then("output is {z}")
def step_impl(context, z):
    """
    :type context: behave.runner.Context
    """
    obj.operate()
    obj.showResult()
    assert (int(z) == obj.sum)


@given("specified {op}")
def step_impl(context, op):
    """
    :type context: behave.runner.Context
    :type op: str
    """
    obj.sign = op
