from typing import Optional, List
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tempfile import NamedTemporaryFile, TemporaryDirectory
import logging

from .wind import wind_speed
from .example import example_stac_item
from .storage import move_file, convert_uri_to_url, move_directory
from .format import convert_to_zarr


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

app = FastAPI(title="Sherlock Wind")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


class StacItemRequest(BaseModel):
    id: str
    bbox: List

    class Config:
        schema_extra = {
            "example": example_stac_item
        }


@app.get("/")
async def health_check():
    return {
        "status": "ok"
    }


@app.post("/item")
def process_wind_speed(body: StacItemRequest):
    """
    Process wind speed
    """
    zarr = False
    sink_path = f"gs://spill-sight-public/sherlock_wind/{body.id}.nc"
    with NamedTemporaryFile() as netcdf_file:
        source_path = wind_speed(body.id, body.bbox, netcdf_file.name)
        if zarr:
            with TemporaryDirectory() as zarr_directory:
                source_path = convert_to_zarr(source_path, zarr_directory)
                sink_path = f"gs://spill-sight-public/sherlock_wind/{body.id}.zarr"
                move_directory(source_path, sink_path)
        else:
            move_file(source_path, sink_path)

    url = convert_uri_to_url(sink_path)
    result = {
        "uri": sink_path,
        "url": url
    }

    return result



if __name__ == "__main__":
    # Entry point for development
    # Production containers call `uvicorn` from bash shell (see Dockerfile)
    import uvicorn

    uvicorn.run(
        "sherlock_wind.main:app", host="0.0.0.0", port=8080, log_level="info", reload=True,
    )
