import xarray as xr
import pydap
import scipy
import zarr


def convert_to_zarr(source_path, sink_path):
    """
    Convert data to zarr
    """
    data = xr.open_dataset(source_path)

    data.to_zarr(sink_path)

    return sink_path
