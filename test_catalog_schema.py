# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json

import jsonschema


V2_SCHEMA = json.load(open('schemas/v2.json'))
SAMPLE_v2_CATALOGS = [
    'devstack',
    'keystone',
    'rackspace',
    'rdo',
    'auro',
    'datacentred',
    'dreamhost',
]

for s in SAMPLE_v2_CATALOGS:
    fn = 'samples/v2/%s.json' % s
    sample = json.load(open(fn))
    jsonschema.validate(sample['serviceCatalog'], V2_SCHEMA)


V3_SCHEMA = json.load(open('schemas/v3.json'))
SAMPLE_V3_CATALOGS = [
    'keystone',
    'mirantis',
    'citycloud',
]

for s in SAMPLE_V3_CATALOGS:
    fn = 'samples/v3/%s.json' % s
    sample = json.load(open(fn))
    jsonschema.validate(sample['catalog'], V3_SCHEMA)


NG_SCHEMA = json.load(open('schemas/ng.json'))
SAMPLE_NG_CATALOGS = [
    'simple',
]

for s in SAMPLE_NG_CATALOGS:
    fn = 'samples/ng/%s.json' % s
    sample = json.load(open(fn))
    jsonschema.validate(sample['catalog'], NG_SCHEMA)
