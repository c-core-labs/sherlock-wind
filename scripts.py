# Temporary workaround until Poetry supports scripts
# https://github.com/sdispater/poetry/issues/241
from subprocess import check_call


def format() -> None:
    check_call(["black", "river_ice_ingester/", "tests/"])


def start() -> None:
    check_call(["python", "-m", "river_ice_ingester.main"])


def test() -> None:
    check_call(["pytest", "tests/"])


def freeze() -> None:
    with open("requirements.txt", "w") as file:
        check_call(["poetry", "export", "--without-hashes", "-f", "requirements.txt"], stdout=file)


def docker_build() -> None:
    freeze()
    check_call(
        [
            "docker",
            "build",
            "-t",
            "gcr.io/iceberg-detection-suite/iceberg-detection-api:latest",
            ".",
        ]
    )


def docker_run() -> None:
    check_call(
        [
            "docker",
            "run",
            "--rm",
            "-it",
            "-p",
            "8080:8080",
            "-t",
            "gcr.io/iceberg-detection-suite/iceberg-detection-api:latest",
        ]
    )
