

def _recursive_step_failer(step):
    for nested_step in step.steps:
        _recursive_step_failer(nested_step)
        if nested_step.status == 'failed':
            step.status = 'failed'


def pytest_runtest_makereport(item, call):
    plugin = item.config.pluginmanager.get_plugin('allure_listener')
    test_result = plugin.allure_logger.get_test(None)

    if call.when == 'call':
        _recursive_step_failer(test_result)

