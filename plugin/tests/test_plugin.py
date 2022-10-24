import unittest

from uuid import uuid1

# you can use the cloudify mocks package
from cloudify.state import current_ctx
from cloudify.mocks import MockCloudifyContext

from cloudify.exceptions import NonRecoverableError

from plugin.tasks import my_task


class TestPlugin(unittest.TestCase):

    def setUp(self):
        super(TestPlugin, self).setUp()

    def get_host_conf_props(self):
        return {
            "host_config": {
                "mock_host": "localhost",
                "mock_username": "myuser",
                "mock_password": "super-secret",
            }
        }

    def mock_ctx(self,
                 test_name,
                 test_properties,
                 test_runtime_properties=None):
        test_node_id = uuid1()
        ctx = MockCloudifyContext(
                node_id=test_node_id,
                properties=test_properties,
                runtime_properties=test_runtime_properties,
        )
        return ctx

    def test_my_task_success(self):
        node_props = self.get_host_conf_props()
        ctx = self.mock_ctx('test_my_task', node_props)
        current_ctx.set(ctx=ctx)
        kwargs = {
            'ctx': ctx
        }
        expected_result = {
            "connection_status": "Connection Established"
        }
        my_task(**kwargs)
        self.assertEqual(
            ctx.instance.runtime_properties,
            expected_result)

    def test_my_task_failure(self):
        node_props = self.get_host_conf_props()
        # make one of the values empty to trigger raise NonRecoverable
        node_props['host_config']['mock_host'] = ''
        ctx = self.mock_ctx('test_my_task', node_props)
        current_ctx.set(ctx=ctx)
        kwargs = {
            'ctx': ctx
        }
        with self.assertRaises(NonRecoverableError):
            my_task(**kwargs)
