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


V2_SCHEMA_JSON = r"""
{
  "title": "Identity V2.0 Service Catalog",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
        "type": {
          "description": "Service type, may use non-standard naming: identity, volume, compute",
          "type": "string",
          "minlength": 1
        },
        "name": {"type": "string", "minlength": 1},
        "endpoints_links": {
          "description": "This is not present in the HP public cloud catalog.",
          "type": "array",
          "maxItems": 0
        },
        "endpoints": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "publicURL": {
                "description": "The URL may contain the version, project (tenant) ID, or account ID.",
                "type": "string"
               },
              "adminURL": {
                "description": "The URL may contain the version, project (tenant) ID, or account ID.",
                "type": "string"
              },
              "internalURL": {
                "description": "The URL may contain the version, project (tenant) ID, or account ID.",
                "type": "string"
              },
              "region": {"type": "string"},
              "id": {
                "description": "This is present in Keystone, but not in HP public cloud or Internap. An ID.",
                "type": "string"
              },
              "publicURL2": {
                "description": "This is present in HP public cloud catalog. A URL.",
                "type": "string"
              },
              "tenantId": {
                "description": "This is present in HP, RAX public cloud catalog. An ID.",
                "type": "string"
              },
              "versionID": {
                "description": "This is present in HP, RAX public cloud catalog, like 2.0.",
                "type": "string"
              },
              "versionInfo": {
                "description": "This is present in HP, RAX public cloud catalog. A URL.",
                "type": "string"
              },
              "versionList": {
                "description": "This is present in HP, RAX public cloud catalog. A URL.",
                "type": "string"
              }
            },
            "required": ["publicURL", "region"],
            "optional": [
              "id",
              "adminURL", "internalURL", "publicURL2", "tenantId",
              "versionID", "versionInfo", "versionList"],
            "additionalProperties": true
          }
        }
    },
    "required": ["type", "name", "endpoints"],
    "optional": ["endpoints_links"],
    "additionalProperties": false
  }
}
"""


V2_SCHEMA = json.loads(V2_SCHEMA_JSON)


SAMPLE_V2_CATALOG_JSON = r"""
{
  "serviceCatalog": [
    {
      "type": "identity",
      "name": "keystone",
      "endpoints_links": [],
      "endpoints": [
        {
          "adminURL": "http://192.168.122.239:35357/v3",
          "internalURL": "http://192.168.122.239:5000/v3",
          "publicURL": "http://192.168.122.239:5000/v3",
          "region": "RegionOne",
          "id": "0e0b3d009aa04da0aee163e034dd6190"
        }
      ]
    }
  ]
}
"""

SAMPLE_V2_CATALOG = json.loads(SAMPLE_V2_CATALOG_JSON)


jsonschema.validate(SAMPLE_V2_CATALOG['serviceCatalog'], V2_SCHEMA)


V3_SCHEMA_JSON = r"""
{
  "title": "Identity V3 Service Catalog",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "type": {
        "description": "Service type, may use non-standard naming: identity, volume, compute",
        "type": "string",
        "minLength": 1
      },
      "name": {"type": "string", "minLength": 1},
      "id": {"type": "string", "minLength": 1},
      "endpoints": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "interface": {
              "type": "string",
              "enum": ["public", "admin", "internal"]
            },
            "region": {
              "description": "This is being changed to region_id.",
              "type": "string"
            },
            "region_id": {
              "description": "newer, so not all clouds report this.",
              "type": "string"
            },
            "url": {
              "description": "The URL may contain the version, project (tenant) ID, or account ID.",
              "type": "string"
            },
            "id": {
              "description": "Not present on UnitedStack cloud. An ID.",
              "type": "string"
            }
          },
          "required": ["interface", "region", "url"],
          "optional": ["region_id", "id"],
          "additionalProperties": false
        }
      }
    },
    "required": ["type", "name", "id", "endpoints"],
    "additionalProperties": false
  }
}
"""

V3_SCHEMA = json.loads(V3_SCHEMA_JSON)


SAMPLE_V3_CATALOG_JSON = r"""
{"catalog": [
  {
    "type": "identity",
    "name": "keystone",
    "id": "cdc3ae8870af44698e722547d660355b",
    "endpoints": [
      {
        "interface": "internal",
        "region": "RegionOne",
        "region_id": "RegionOne",
        "url": "http://192.168.122.239:5000/v3",
        "id": "0e0b3d009aa04da0aee163e034dd6190"
      },
      {
        "interface": "admin",
        "region": "RegionOne",
        "region_id": "RegionOne",
        "url": "http://192.168.122.239:35357/v3",
        "id": "1024e233d9a4460d83292f151b405cf5"
      },
      {
        "interface": "public",
        "region": "RegionOne",
        "region_id": "RegionOne",
        "url": "http://192.168.122.239:5000/v3",
        "id": "1b4b82bb39b6487b8265748a6142104f"
      }
    ]
  }
] }
"""

SAMPLE_V3_CATALOG = json.loads(SAMPLE_V3_CATALOG_JSON)


jsonschema.validate(SAMPLE_V3_CATALOG['catalog'], V3_SCHEMA)


NG_SCHEMA_JSON = r"""
{
  "title": "Next-Generation Service Catalog",
  "type": "array",
  "items": {
    "description": "Additional properties are allowed for backwards-compatibility as deployments move to the new format.",
    "type": "object",
    "properties": {
      "type": {
        "description": "Allowed service type values are defined in projects.yaml in the openstack/governance repository. Examples are: identity, compute, volume",
        "type": "string",
        "minLength": 1
      },
      "name": {"type": "string", "minLength": 1},
      "id": {"type": "string", "minLength": 1},
      "endpoints": {
        "type": "array",
        "items": {
          "description": "Additional properties are allowed for backwards-compatibility as deployments move to the new format.",
          "type": "object",
          "properties": {
            "interface": {
              "type": "string",
              "enum": ["public", "admin", "internal"]
            },
            "region": {
              "description": "This is being changed to region_id, but may still be present.",
              "type": "string"
            },
            "region_id": {
              "description": "newer, so not all clouds even report this.",
              "type": "string"
            },
            "url": {
              "description": "The URL does not contain the version, project (tenant) ID, or account ID.",
              "type": "string"
            },
            "id": {"type": "string"}
          },
          "required": ["interface", "region", "url", "id"],
          "optional": ["region_id"],
          "additionalProperties": true
        }
      }
    },
    "required": ["type", "id", "endpoints"],
    "optional": ["name"],
    "additionalProperties": true
  }
}
"""

NG_SCHEMA = json.loads(NG_SCHEMA_JSON)


SAMPLE_NG_CATALOG_JSON = r"""
{"catalog": [
  {
    "type": "identity",
    "id": "cdc3ae8870af44698e722547d660355b",
    "endpoints": [
      {
        "interface": "internal",
        "region": "RegionOne",
        "region_id": "RegionOne",
        "url": "https://server/openstack/identity",
        "id": "0e0b3d009aa04da0aee163e034dd6190"
      },
      {
        "interface": "admin",
        "region": "RegionOne",
        "region_id": "RegionOne",
        "url": "https://server/openstack/identity_admin",
        "id": "1024e233d9a4460d83292f151b405cf5"
      },
      {
        "interface": "public",
        "region": "RegionOne",
        "region_id": "RegionOne",
        "url": "https://server/openstack/identity",
        "id": "1b4b82bb39b6487b8265748a6142104f"
      }
    ]
  }
] }
"""

SAMPLE_NG_CATALOG = json.loads(SAMPLE_NG_CATALOG_JSON)


jsonschema.validate(SAMPLE_NG_CATALOG['catalog'], NG_SCHEMA)
