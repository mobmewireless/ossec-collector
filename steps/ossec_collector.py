import os

import union.ossec_collector as collector


def test_file_path(logfile):
    return os.path.dirname(os.path.abspath(__file__)) + '/alerts/' + logfile + '.log'

@given('collect method is called')
def step_impl(context):
    context.response = collector.collect(test_file_path('alerts'))

@given('collect method is called for non-existent log file')
def step_impl(context):
    context.response = collector.collect('/tmp/non_existent_file')

@then('returns all alerts')
def step_impl(context):
    assert len(context.response) is 4
    assert len(context.response['1392807321.42985']) is 8

@then('returns entry indicating absence of log file')
def step_impl(context):
    assert len(context.response) is 1
    assert context.response.values()[0][0] == 'OSSEC alerts log file is missing.'
