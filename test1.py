
import json


V2_SCHEMA_JSON = """

{
  "title": "Identity V2.0 Service Catalog",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
        "type": {"type": "string"},
        "name": {"type": "string"},
        "endpoints_links": {"type": "array"},
        "endpoints": {"type": "array"}
    }
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
                    "id": "0e0b3d009aa04da0aee163e034dd6190",
                    "adminURL": "http://192.168.122.239:35357/v3",
                    "internalURL": "http://192.168.122.239:5000/v3",
                    "publicURL": "http://192.168.122.239:5000/v3",
                    "region": "RegionOne"
                }
            ]
        }
    ]
}

"""

SAMPLE_V2_CATALOG = json.loads(SAMPLE_V2_CATALOG_JSON)

