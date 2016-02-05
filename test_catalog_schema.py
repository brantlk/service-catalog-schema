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
SAMPLE_V2_CATALOG = json.load(open('samples/v2/keystone.json'))


jsonschema.validate(SAMPLE_V2_CATALOG['serviceCatalog'], V2_SCHEMA)


V3_SCHEMA = json.load(open('schemas/v3.json'))
SAMPLE_V3_CATALOG = json.load(open('samples/v3/keystone.json'))


jsonschema.validate(SAMPLE_V3_CATALOG['catalog'], V3_SCHEMA)


NG_SCHEMA = json.load(open('schemas/ng.json'))
SAMPLE_NG_CATALOG = json.load(open('samples/ng/simple.json'))


jsonschema.validate(SAMPLE_NG_CATALOG['catalog'], NG_SCHEMA)
