import os
from pathlib import Path
from urllib.parse import urlparse
from smart_open import open
from google.cloud.storage import Client
# import geopandas as gpd
# from fiona.session import GSSession
# import fiona
import shutil
import zipfile
# import httpx
import logging


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
logging.getLogger("smart_open").setLevel(logging.WARNING)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(
    Path("./cloud_storage.json").absolute()
)
client = Client()


def move_file(source_path: str, sink_path: str):
    """
    Copy cloud storage file to local path
    """
    with open(source_path, "rb") as source:
        with open(sink_path, "wb") as sink:
            sink.write(source.read())


def move_directory(source_directory: str, sink_directory: str):
    results = []
    for file in Path(source_directory).rglob("*"):
        if file.is_file():
            sink_path = f"{sink_directory}/{file.name}"
            source_path = str(file)
            log.info("source_path")
            log.info(source_path)
            log.info("sink_path")
            log.info(sink_path)

            move_file(source_path, sink_path)
            result = {"uri": sink_path, "url": convert_uri_to_url(sink_path)}
            results.append(result)

    return results


def zip_directory(source, sink):
    shutil.make_archive(sink, "zip", source)

    return f"{sink}.zip"


def download_directory(
    bucket_name="spill-sight-public",
    prefix="labrador/S1A_IW_GRDH_1SDV_20190507T212420_20190507T212448_027127_030EC1_DF1D.SAFE",
    storage_client=client,
):

    # storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_or_name=bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)  # Get list of files
    for blob in blobs:
        # filename = blob.name.replace('/', '_')
        filename = blob.name
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        # directory = '/'.join(blob.name.split('/')[:-1])
        log.info(blob.name)
        # print(filename)
        # print(dl_dir+filename)
        blob.download_to_filename(filename)  # Download


def make_archive(source, destination):
    """
    Source: http://www.seanbehan.com/how-to-use-python-shutil-make_archive-to-zip-up-a-directory-recursively-including-the-root-folder/
    :param source:
    :param destination:
    :return:
    """
    base = os.path.basename(destination)
    name = base.split(".")[0]
    format_file = base.split(".")[1]
    archive_from = os.path.dirname(source)
    archive_to = os.path.basename(source.strip(os.sep))
    shutil.make_archive(name, format_file, archive_from, archive_to)
    shutil.move("%s.%s" % (name, format_file), destination)

    return destination


def download_and_zip_directory(bucket_name, prefix, id):
    download_directory(bucket_name, prefix)
    file_name = make_archive(prefix, f"{id}.zip")

    return file_name


def convert_uri_to_url(uri: str):
    parsed_uri = urlparse(uri)
    bucket = parsed_uri.netloc
    path = parsed_uri.path

    url = f"https://storage.cloud.google.com/{bucket}{path}"

    return url


# def read_cloud_storage_file(uri, zip=False):
#     with fiona.Env(session=GSSession(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])):
#         if zip:
#             gdf = gpd.read_file(f"zip+{uri}")
#         else:
#             gdf = gpd.read_file(uri)

#         return gdf


def archive_shapefile(shp_path):
    extensions = [".shp", ".cpg", ".dbf", ".shx"]
    files = []
    path = Path(shp_path)
    stem = path.stem
    root = str(Path(path.parent, path.stem))
    zip_path = f"{shp_path}/{stem}.zip"

    for extension in extensions:
        file = f"{shp_path}/{stem}{extension}"
        files.append(file)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip:
        for file in files:
            print(file)
            zip.write(file, Path(file).name)
    print(f"zip_path: {zip_path}")
    return zip_path


def save_as_shapefile(
    data_frame, output_path="gs://spill-sight/spill-sight-features.zip"
):
    with TemporaryDirectory() as directory:
        data_frame.to_file(directory)

        zip_path = archive_shapefile(directory)

        move_file(zip_path, "gs://spill-sight/spill-sight-features.zip")

    return output_path


def format_date(string: str):
    date = f"{string[0:4]}-{string[4:6]}-{string[6:11]}:{string[11:13]}:{string[13:15]}UTC"

    return date


def format_url(id):
    orbit = id.split("_")[6]
    start = format_date(id.split("_")[4])
    end = format_date(id.split("_")[5])

    url = f"https://api.daac.asf.alaska.edu/services/search/param?platform=S1&absoluteOrbit={orbit}&output=json&start={start}&end={end}"

    return url


def format_start_time(string: str):
    start_time = f"{string[0:4]}-{string[4:6]}-{string[6:11]}:{string[11:13]}:{string[13:15]}.000000"

    return start_time



if __name__ == "__main__":
    pass
