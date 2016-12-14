########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
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


from setuptools import setup

# Replace the place holders with values for your project

setup(

    # Do not use underscores in the plugin name.
    name='ENTER-PLUGIN-NAME-HERE',

    version='0.1',
    author='ENTER-AUTHOR-HERE',
    author_email='ENTER-AUTHOR-EMAIL-HERE',
    description='ENTER-DESCRIPTION-HERE',

    # This must correspond to the actual packages in the plugin.
    packages=['plugin'],

    license='LICENSE',
    zip_safe=False,
    install_requires=[
        # Necessary dependency for developing plugins, do not remove!
        "cloudify-plugins-common>=4.0a10"
    ],
    test_requires=[
        "cloudify-dsl-parser>=4.0a10"
        "nose"
    ]
)
