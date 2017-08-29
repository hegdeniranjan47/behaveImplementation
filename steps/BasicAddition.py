from behave import *
from main import Calculator
from nose import *
import parse
import parse_type

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
    print 'a= '+str(x)+'\nb= '+str(y)+'\n'


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
    print op+' sign\n'
    obj.sign = op
