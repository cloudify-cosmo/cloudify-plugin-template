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

import os
from setuptools import setup
from setuptools import find_packages


# Get the plugin version from the yaml , so you would have one source of truth 
def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_file='plugin.yaml'):
    lines = read(rel_file)
    for line in lines.splitlines():
        if 'package_version' in line:
            split_line = line.split(':')
            line_no_space = split_line[-1].replace(' ', '')
            line_no_quotes = line_no_space.replace('\'', '')
            return line_no_quotes.strip('\n')
    raise RuntimeError('Unable to find version string.')


# Replace the place holders with values for your project

setup(

    # Do not use underscores in the plugin name.
    name='ENTER-PLUGIN-NAME-HERE',

    version=get_version(),
    author='ENTER-AUTHOR-HERE',
    author_email='ENTER-AUTHOR-EMAIL-HERE',
    description='ENTER-DESCRIPTION-HERE',

    # This must correspond to the actual packages in the plugin.
    packages=find_packages(exclude=['tests*']),

    license='LICENSE',
    zip_safe=False,
    install_requires=[
        # Necessary dependency for developing plugins, do not remove!
        "cloudify-common>=7.0.0.dev1"
    ],
    test_requires=[
        "cloudify-common>=7.0.0.dev1",
        "nose"
    ]
)
