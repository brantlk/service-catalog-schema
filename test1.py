
import json

import jsonschema


V2_SCHEMA_JSON = """
{
  "title": "Identity V2.0 Service Catalog",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
        "type": {"type": "string", "minlength": 1},
        "name": {"type": "string", "minlength": 1},
        "endpoints_links": {"type": "array", "maxItems": 0},
        "endpoints": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "adminURL": {"type": "string"},
              "internalURL": {"type": "string"},
              "publicURL": {"type": "string"},
              "region": {"type": "string"},
              "id": {"type": "string"}
            },
            "required": [
              "adminURL", "internalURL", "publicURL", "region", "id"]
          }
        }
    },
    "required": ["type", "name", "endpoints_links", "endpoints"]
  }
}
"""


V2_SCHEMA = json.loads(V2_SCHEMA_JSON)


SAMPLE_V2_CATALOG_JSON = """
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


V3_SCHEMA_JSON = """
{
   "title": "Identity V3 Service Catalog"
}
"""

V3_SCHEMA = json.loads(V3_SCHEMA_JSON)


SAMPLE_V3_CATALOG_JSON = """
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
