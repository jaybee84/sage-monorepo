"""Implementation of all endpoints"""
import os
from typing import Optional, Union, Callable, Any


import pandas as pd
from schematic.store.synapse import SynapseStorage, ManifestDownload, load_df  # type: ignore
from schematic import CONFIG  # type: ignore

from schematic_api.models.basic_error import BasicError
from schematic_api.models.dataset import Dataset
from schematic_api.models.datasets_page import DatasetsPage
from schematic_api.models.manifests_page import ManifestsPage
from schematic_api.models.manifest import Manifest
from schematic_api.models.project import Project
from schematic_api.models.projects_page import ProjectsPage
from schematic_api.models.file import File
from schematic_api.models.files_page import FilesPage
from schematic_api.controllers.utils import handle_exceptions, get_access_token


def get_asset_storage_class(asset_type: str) -> Callable:
    """Returns the class associated with the asset type.

    Args:
        asset_type (str): An asset type, such as "synapse".

    Raises:
        ValueError: When the asset_type isn't in the asst_type dictionary

    Returns:
        Callable: A class that has
        - access_token parameter
        - getStorageDatasetsInProject method
        - getProjectManifests method
    """
    asset_type_dict = {"synapse": SynapseStorage}
    asset_type_object = asset_type_dict.get(asset_type)
    if asset_type_object is None:
        msg = f"{asset_type} is not an allowed value: [{list(asset_type_dict.keys())}]"
        raise ValueError(msg)
    return asset_type_object


def get_asset_view_from_schematic(
    asset_type: str,  # pylint: disable=unused-argument
) -> pd.DataFrame:
    """Gets the asset view in pandas.Dataframe form

    Args:
        asset_view_id (str): The d of the asset view
        asset_type (str): The type of asset, ie "synapse"

     Returns:
        pandas.DataFrame: The asset view
    """
    access_token = get_access_token()
    store = SynapseStorage(access_token=access_token)  # type: ignore
    return store.getStorageFileviewTable()


@handle_exceptions
def get_asset_view_json(
    asset_view_id: str, asset_type: str
) -> tuple[Union[str, BasicError], int]:
    """Gets the asset view in json form

    Args:
        asset_view_id (str): The d of the asset view
        asset_type (str): The type of asset, ie "synapse"

    Returns:
        tuple[Union[str, BasicError], int]: A tuple
          The first item is either the fileview or an error object
          The second item is the response status
    """
    CONFIG.synapse_master_fileview_id = asset_view_id
    asset_view = get_asset_view_from_schematic(asset_type)
    result: Union[str, BasicError] = asset_view.to_json()
    status = 200
    return result, status


def get_dataset_files_from_schematic(
    dataset_id: str,
    asset_type: str,  # pylint: disable=unused-argument
    file_names: Optional[list[str]],
    use_full_file_path: bool,
) -> list[tuple[str, str]]:
    """Gets a list of datasets from the project

    Args:
        project_id (str): The id for the project
        asset_type (str): The type of asset, ie "synapse"

    Returns:
        list[tuple(str, str)]: A list of files in tuple form
    """
    access_token = get_access_token()
    store = SynapseStorage(access_token=access_token)  # type: ignore
    return store.getFilesInStorageDataset(
        datasetId=dataset_id,
        fileNames=file_names,  # type: ignore
        fullpath=use_full_file_path,
    )


@handle_exceptions
def get_dataset_files(
    dataset_id: str,
    asset_type: str,
    asset_view_id: str,
    file_names: Optional[list[str]] = None,
    use_full_file_path: bool = False,
) -> tuple[Union[FilesPage, BasicError], int]:
    """Attempts to get a list of files associated with a dataset

    Args:
        dataset_id (str): The Id for the dataset to get the files from
        asset_view_id (str): The id for the asset view of the project
        asset_type (str): The type of asset, ie "synapse"
        file_names (Optional[list[str]]): An optional list of file names to filter the output by
        use_full_file_path: Whether or not to return the full file path of each file

    Returns:
        tuple[Union[FilesPage, BasicError], int]: A tuple
          The first item is either the datasets or an error object
          The second item is the response status
    """
    CONFIG.synapse_master_fileview_id = asset_view_id
    file_tuples = get_dataset_files_from_schematic(
        dataset_id, asset_type, file_names, use_full_file_path
    )
    files = [File(id=item[0], name=item[1]) for item in file_tuples]

    page = FilesPage(
        number=0,
        size=100,
        total_elements=len(files),
        total_pages=1,
        has_next=False,
        has_previous=False,
        files=files,
    )
    result: Union[FilesPage, BasicError] = page
    status = 200

    return result, status


def load_manifest_from_synapse_metadata(manifest_data: Any) -> pd.DataFrame:
    """Loads a manifest from a csv file

    Args:
        manifest_data (Any): Manifest metadata from doing syanpseclient.get on a file entity

    Returns:
        pandas.DataFrame: The manifest

    """
    manifest_local_file_path = manifest_data["path"]
    manifest = load_df(manifest_local_file_path)
    os.remove(manifest_local_file_path)
    return manifest


def get_dataset_manifest_from_schematic(
    asset_type: str, dataset_id: str  # pylint: disable=unused-argument
) -> pd.DataFrame:
    """Gets a manifest in pandas.Dataframe format

    Args:
        asset_type (str): The type of asset, ie "synapse"
        manifest_id (str): The unique id for the manifest file
        dataset_id (str): The id of the dataset the manifest is in

    Returns:
        pandas.DataFrame: The manifest
    """
    access_token = get_access_token()
    store = SynapseStorage(access_token=access_token)  # type: ignore
    manifest_data = store.getDatasetManifest(
        datasetId=dataset_id, downloadFile=True, newManifestName="manifest.csv"
    )
    return load_manifest_from_synapse_metadata(manifest_data)


@handle_exceptions
def get_dataset_manifest_json(
    asset_type: str,
    dataset_id: str,
    asset_view_id: str,
) -> tuple[Union[str, BasicError], int]:
    """Gets a manifest in json form

    Args:
        asset_type (str): The type of asset, ie "synapse"
        asset_view_id (str): The id of the asst view the dataset is in
        dataset_id (str): The id of the dataset the manifest is in

    Returns:
        tuple[Union[str, BasicError], int]: A tuple
          The first item is either the manifest or an error object
          The second item is the response status
    """
    CONFIG.synapse_master_fileview_id = asset_view_id
    manifest = get_dataset_manifest_from_schematic(asset_type, dataset_id)
    result: Union[str, BasicError] = manifest.to_json()
    status = 200

    return result, status


def get_manifest_from_schematic(
    asset_type: str, manifest_id: str  # pylint: disable=unused-argument
) -> pd.DataFrame:
    """Gets a manifest in pandas.Dataframe format

    Args:
        asset_type (str): The type of asset, ie "synapse"
        manifest_id (str): The unique id for the manifest file

    Returns:
        pandas.DataFrame: The manifest
    """
    access_token = get_access_token()
    store = SynapseStorage.login(access_token=access_token)
    manifest_download = ManifestDownload(store, manifest_id)
    manifest_data = ManifestDownload.download_manifest(
        manifest_download, "manifest.csv"
    )
    return load_manifest_from_synapse_metadata(manifest_data)


@handle_exceptions
def get_manifest_json(
    asset_type: str, manifest_id: str
) -> tuple[Union[str, BasicError], int]:
    """Gets a manifest in json form

    Args:
        asset_type (str): The type of asset, ie "synapse"
        manifest_id (str): The unique id for the manifest file

    Returns:
        tuple[Union[str, BasicError], int]: A tuple
          The first item is either the manifest or an error object
          The second item is the response status
    """
    manifest = get_manifest_from_schematic(asset_type, manifest_id)
    result: Union[str, BasicError] = manifest.to_json()
    status = 200

    return result, status


def get_project_datasets_from_schematic(
    project_id: str, asset_type: str  # pylint: disable=unused-argument
) -> list[tuple[str, str]]:
    """Gets a list of datasets from the project

    Args:
        project_id (str): The id for the project
        asset_type (str): The type of asset, ie "synapse"

    Returns:
        list[tuple(str, str)]: A list of datasets in tuple form
    """
    access_token = get_access_token()
    store = SynapseStorage(access_token=access_token)  # type: ignore
    return store.getStorageDatasetsInProject(projectId=project_id)  # type: ignore


@handle_exceptions
def get_project_datasets(
    project_id: str, asset_type: str, asset_view_id: str
) -> tuple[Union[DatasetsPage, BasicError], int]:
    """Attempts to get a list of datasets from a Synapse project

    Args:
        project_id (str): The Id for the project to get datasets from
        asset_view_id (str): The id for the asset view of the project
        asset_type (str): The type of asset, ie "synapse"

    Returns:
        tuple[Union[DatasetsPage, BasicError], int]: A tuple
          The first item is either the datasets or an error object
          The second item is the response status
    """

    CONFIG.synapse_master_fileview_id = asset_view_id
    dataset_tuples = get_project_datasets_from_schematic(project_id, asset_type)
    datasets = [Dataset(id=item[0], name=item[1]) for item in dataset_tuples]

    page = DatasetsPage(
        number=0,
        size=100,
        total_elements=len(datasets),
        total_pages=1,
        has_next=False,
        has_previous=False,
        datasets=datasets,
    )
    result: Union[DatasetsPage, BasicError] = page
    status = 200

    return result, status


def get_project_manifests_from_schematic(
    project_id: str,
    asset_type: str,  # pylint: disable=unused-argument
) -> list[tuple[tuple[str, str], tuple[str, str], tuple[str, str]]]:
    """Gets a list of manifests from the project

    Args:
        project_id (str): The id for the project
        asset_type (str): The type of asset, ie "synapse"

    Returns:
        list[tuple[tuple[str, str], tuple[str, str], tuple[str, str]]]: A list of manifests
    """
    access_token = get_access_token()
    store = SynapseStorage(access_token=access_token)  # type: ignore
    return store.getProjectManifests(projectId=project_id)  # type: ignore


@handle_exceptions
def get_project_manifests(
    project_id: str, asset_type: str, asset_view_id: str
) -> tuple[Union[ManifestsPage, BasicError], int]:
    """Attempts to get a list of manifests from a Synapse project

    Args:
        project_id (str): A Synapse id
        asset_view_id (str): A Synapse id
        asset_type (str): The type of asset, ie "synapse"

    Returns:
        tuple[Union[ManifestsPage, BasicError], int]: A tuple
          The first item is either the manifests or an error object
          The second item is the response status
    """
    # load config
    CONFIG.synapse_master_fileview_id = asset_view_id
    project_manifests = get_project_manifests_from_schematic(project_id, asset_type)
    manifests = [
        Manifest(
            name=item[1][1],
            id=item[1][0],
            dataset_name=item[0][1],
            dataset_id=item[0][0],
            component_name=item[2][0],
        )
        for item in project_manifests
    ]

    page = ManifestsPage(
        number=0,
        size=100,
        total_elements=len(manifests),
        total_pages=1,
        has_next=False,
        has_previous=False,
        manifests=manifests,
    )
    result: Union[ManifestsPage, BasicError] = page
    status = 200

    return result, status


def get_projects_from_schematic(
    asset_type: str,  # pylint: disable=unused-argument
) -> list[tuple[str, str]]:
    """Gets a list of projects

    Args:
        asset_type (str): The type of asset, ie "synapse"

    Returns:
        list[tuple(str, str)]: A list of projects in tuple form
    """
    access_token = get_access_token()
    store = SynapseStorage(access_token=access_token)  # type: ignore
    return store.getStorageProjects()  # type: ignore


@handle_exceptions
def get_projects(
    asset_view_id: str, asset_type: str
) -> tuple[Union[ProjectsPage, BasicError], int]:
    """Attempts to get a list of projects the user has access to

    Args:
        asset_view_id (str): The id for the asset view of the project
        asset_type (str): The type of asset, ie "synapse"

    Returns:
        tuple[Union[ProjectsPage, BasicError], int]: A tuple
          The first item is either the projects or an error object
          The second item is the response status
    """

    CONFIG.synapse_master_fileview_id = asset_view_id
    project_tuples = get_projects_from_schematic(asset_type)
    projects = [Project(id=item[0], name=item[1]) for item in project_tuples]

    page = ProjectsPage(
        number=0,
        size=100,
        total_elements=len(projects),
        total_pages=1,
        has_next=False,
        has_previous=False,
        projects=projects,
    )
    result: Union[ProjectsPage, BasicError] = page
    status = 200

    return result, status
