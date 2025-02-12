"""Globals and pytest fixtures for testing"""
from typing import Generator
import pytest

import pandas as pd


def csv_to_bytes(path: str) -> str:
    """reads in a csv file and returns as bytes"""
    dataframe = pd.read_csv(path)
    csv_string = dataframe.to_csv(line_terminator="\r\n", index=False)
    return bytes(csv_string, encoding="utf-8")


def csv_to_json_str(path: str) -> str:
    """reads in a csv file and returns as json string"""
    dataframe = pd.read_csv(path)
    return dataframe.to_json()


EXAMPLE_MANIFEST_METADATA = [
    (("dataset_id1", "dataset_name1"), ("syn1", "name1"), ("component1", "component1")),
    (("dataset_id2", "dataset_name2"), ("syn2", "name2"), ("component2", "component2")),
]


@pytest.fixture(scope="session", name="example_manifest_metadata")
def fixture_example_manifest_metadata() -> Generator:
    """
    Yields an example of a list of manifest metadata
    """
    yield EXAMPLE_MANIFEST_METADATA


TEST_SCHEMA_URL = "https://raw.githubusercontent.com/Sage-Bionetworks/schematic/develop/tests/data/example.model.jsonld"  # pylint: disable=line-too-long


@pytest.fixture(scope="session", name="test_schema_url")
def fixture_test_schema_url() -> Generator:
    """
    Yields an the URL of the test schema
    """
    yield TEST_SCHEMA_URL


CORRECT_MANIFEST_PATH = "schematic_api/test/data/manifests/biospecimen.csv"


@pytest.fixture(scope="session", name="correct_manifest_path")
def fixture_correct_manifest() -> Generator:
    """
    Yields the path to biospecimen manifest csv
    """
    yield CORRECT_MANIFEST_PATH


INCORRECT_MANIFEST_PATH = "schematic_api/test/data/manifests/biospecimen_incorrect.csv"


@pytest.fixture(scope="session", name="incorrect_manifest_path")
def fixture_incorrect_manifest_dataframe() -> Generator:
    """
    Yields the path to biospecimen manifest csv
    """
    yield INCORRECT_MANIFEST_PATH


@pytest.fixture(scope="session", name="incorrect_manifest_errors")
def fixture_incorrect_manifest_errors() -> Generator:
    """
    Yields the expected errors from the incorrect manifest
    """
    yield [
        [
            "2",
            "Wrong schema",
            "'Tissue Status' is a required property",
            "Wrong schema",
        ]
    ]
