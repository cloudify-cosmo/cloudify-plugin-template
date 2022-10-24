# you can use the decorators that gives the ability
# to mark the task as resumable or not
from cloudify.decorators import operation
# you can use the exeption logic to mark the operation final status
# [ as it will affect the workflow execution] you can raise according
# to your logic could be `RecoverableError` if you want you code to do retries
# and wait for a certian period of time or `NonRecoverableError`
# which means mark this operation as failure and stop the flow right there
# unless you set ignore_failure flag as true on the workflow trigger
from cloudify.exceptions import NonRecoverableError

# 'ctx' is always passed as a keyword argument to operations, so
# your operation implementation must either specify it in the arguments
# list, or accept '**kwargs'. Both are shown here.


@operation
def my_task(ctx, **kwargs):
    # getting some values from passed properties
    host_config = ctx.node.properties.get('host_config', {})
    mock_host = host_config.get('mock_host', '')
    mock_user = host_config.get('mock_username', '')
    mock_pass = host_config.get('mock_password', '')

    # you can use the cloudify context logger
    ctx.logger.info('Got these values for host {0} , user {1} , '
                    'password {2}'.format(mock_host, mock_user, mock_pass))

    # you can put here what is the actual task defintion
    # that you want to implement
    if mock_host and mock_host and mock_pass:
        # do something useful with that properties values
        ctx.instance.runtime_properties['connection_status'] = \
                'Connection Established'
    else:
        ctx.instance.runtime_properties['connection_status'] = \
            'Connection Failed'
        ctx.instance.runtime_properties['failure_reason'] = \
            'invalid or empty inputs'
        # or raise an error that will stop the workflow due to failure
        raise NonRecoverableError('Invalid inputs were passed '
                                  'to this operation')
