example_stac_item = {
      "type": "Feature",
      "geometry": {
        "coordinates": [
          [
            [
              -137.954361,
              68.606705
            ],
            [
              -139.232834,
              70.1577
            ],
            [
              -132.518936,
              70.689018
            ],
            [
              -131.700699,
              69.112328
            ],
            [
              -137.954361,
              68.606705
            ]
          ]
        ],
        "type": "Polygon"
      },
      "properties": {
        "created": "2021-02-26T09:34:08Z",
        "updated": "2021-02-26T09:34:08Z",
        "platform": "Sentinel 1",
        "datetime": "2021-02-26T02:24:54Z",
        "sar:instrument_mode": "IW",
        "sar:polarizations": [
          "VV",
          "VH"
        ],
        "sar:product_type": "GRD"
      },
      # "id": "S1A_IW_GRDH_1SDV_20210226T022454_20210226T022521_036755_045213_F5FD",
      "id": "S1A_IW_GRDH_1SDV_20190811T212221_20190811T212246_028527_0339B5_B0AF",
      # "bbox": [
      #   -139.232834,
      #   68.606705,
      #   -131.700699,
      #   70.689018
      # ],
      "bbox": [
        -139.232834,
        68.606705,
        -131.700699,
        70.689018
      ],
      "stac_version": "1.0.0-beta.2",
      "assets": {
        "VH": {
          "title": "VH",
          "href": "s3://sentinel-s1-l1c/GRD/2021/2/26/IW/DV/S1A_IW_GRDH_1SDV_20210226T022454_20210226T022521_036755_045213_F5FD/measurement/iw-vh.tiff",
          "roles": [
            "data"
          ]
        },
        "VV": {
          "title": "VV",
          "href": "s3://sentinel-s1-l1c/GRD/2021/2/26/IW/DV/S1A_IW_GRDH_1SDV_20210226T022454_20210226T022521_036755_045213_F5FD/measurement/iw-vv.tiff",
          "roles": [
            "data"
          ]
        },
        "thumbnail": {
          "title": "thumbnail",
          "href": "s3://sentinel-s1-l1c/GRD/2021/2/26/IW/DV/S1A_IW_GRDH_1SDV_20210226T022454_20210226T022521_036755_045213_F5FD/preview/quick-look.png",
          "roles": [
            "thumbnail"
          ]
        },
        "VH-METADATA": {
          "title": "VH-METADATA",
          "href": "s3://sentinel-s1-l1c/GRD/2021/2/26/IW/DV/S1A_IW_GRDH_1SDV_20210226T022454_20210226T022521_036755_045213_F5FD/annotation/iw-vh.xml",
          "roles": [
            "metadata"
          ]
        },
        "VV-METADATA": {
          "title": "VV-METADATA",
          "href": "s3://sentinel-s1-l1c/GRD/2021/2/26/IW/DV/S1A_IW_GRDH_1SDV_20210226T022454_20210226T022521_036755_045213_F5FD/annotation/iw-vv.xml",
          "roles": [
            "metadata"
          ]
        },
        "product-info": {
          "title": "product-info",
          "href": "s3://sentinel-s1-l1c/GRD/2021/2/26/IW/DV/S1A_IW_GRDH_1SDV_20210226T022454_20210226T022521_036755_045213_F5FD/productInfo.json",
          "roles": [
            "metadata"
          ]
        }
      },
      "links": [
        {
          "href": "http://stac-api.c-core.app/collections/s1-l1c-grd/items/S1A_IW_GRDH_1SDV_20210226T022454_20210226T022521_036755_045213_F5FD",
          "rel": "self",
          "type": "application/geo+json"
        },
        {
          "href": "http://stac-api.c-core.app/collections/s1-l1c-grd",
          "rel": "parent",
          "type": "application/json"
        },
        {
          "href": "http://stac-api.c-core.app/collections/s1-l1c-grd",
          "rel": "collection",
          "type": "application/json"
        },
        {
          "href": "http://stac-api.c-core.app/",
          "rel": "root",
          "type": "application/json"
        },
        {
          "href": "http://stac-api.c-core.app/collections/s1-l1c-grd/items/S1A_IW_GRDH_1SDV_20210226T022454_20210226T022521_036755_045213_F5FD/tiles",
          "rel": "alternate",
          "type": "application/json",
          "title": "tiles"
        }
      ],
      "stac_extensions": [
        "sar"
      ],
      "collection": "s1-l1c-grd"
    }
