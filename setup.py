########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

__author__ = 'elip'

from setuptools import setup

PLUGINS_COMMON_VERSION = '3.0'
PLUGINS_COMMON_BRANCH = "develop"
PLUGINS_COMMON = 'https://github.com/cloudify-cosmo/cloudify-plugins-common' \
    '/tarball/{0}'.format(PLUGINS_COMMON_BRANCH)

# Replace the place holders with values for your project

setup(

    # Do not use underscores in the plugin name.
    name='${PLUGIN_NAME}',

    version='${VERSION}',
    author='${AUTHOR}',
    author_email='${AUTHOR_EMAIL}',

    # This must correspond to the actual packages in the plugin.
    # It will also serve as the plugin prefix for mapping operations to tasks.
    packages=['plugin'],

    license='LICENSE',
    description='${DESCRIPTION}',
    zip_safe=False,
    install_requires=[
        # Necessary dependency for developing plugins, do not remove!
        "cloudify-plugins-common"
    ],
    test_requires=[
        "nose"
    ],

    # Necessary dependency for developing plugins, do not remove!
    dependency_links=["{0}#egg=cloudify-plugins-common-{1}"
                      .format(PLUGINS_COMMON, PLUGINS_COMMON_VERSION)]
)
