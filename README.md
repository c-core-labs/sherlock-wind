# Sherlock Wind 🌬️
Process wind speed and direction data for Sentinel 1 scenes using Sherlock.

---

## Features

- Input
  - STAC item, or
  - Sherlock unique identifier
- Output
  - NetCDF file with wind vector data
- Retrieves wind data from [ERA5 reanalysis](https://www.ecmwf.int/en/forecasts/datasets/reanalysis-datasets/era5)
- Retrieves data from the European Union's [Climate Data Store](https://cds.climate.copernicus.eu/) (CDS)

## Installation

``` shell
$ git clone https://github.com/c-core-labs/sherlock-wind.git
$ cd sherlock-wind && pip install -r requirements.txt
```

## Environment variables

Sherlock Wind expects a (CDS API)[https://cds.climate.copernicus.eu/api-how-to] url and key to access data from the Climate Data Store.

``` shell
$ export CDS_API_URL=https://cds.climate.copernicus.eu/api/v2
$ export CDS_API_KEY=insert_cds_api_key_here
```

## Start Sherlock Wind

With local Python environment
``` shell
$ python -m sherlock_wind.main
```

Or with Docker

``` shell
$ docker build -t sherlock-wind .
$ docker run --rm -it -p 8080:8080 sherlock-wind
```

## Examples
View `notebooks` for examples.
