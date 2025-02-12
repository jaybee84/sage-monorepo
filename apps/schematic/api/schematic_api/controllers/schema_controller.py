import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from schematic_api.models.basic_error import BasicError  # noqa: E501
from schematic_api.models.connected_nodes_page import ConnectedNodesPage  # noqa: E501
from schematic_api.models.node_properties_page import NodePropertiesPage  # noqa: E501
from schematic_api.models.nodes_page import NodesPage  # noqa: E501
from schematic_api.models.validation_rules_page import ValidationRulesPage  # noqa: E501
from schematic_api import util
from schematic_api.controllers import schema_controller_impl


def get_component(component_label, schema_url, include_index=None):  # noqa: E501
    """Get all the attributes associated with a specific data model component formatted as a dataframe (stored as a JSON String).

    Get all the attributes associated with a specific data model component formatted as a dataframe (stored as a JSON String). # noqa: E501

    :param component_label: The label of a component in a schema
    :type component_label: str
    :param schema_url: The URL of a schema in jsonld form
    :type schema_url: str
    :param include_index: Whether to include the indexes of the dataframe in the returned JSON string.
    :type include_index: bool

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    return schema_controller_impl.get_component(
        component_label, schema_url, include_index
    )


def get_connected_nodes(schema_url, relationship_type):  # noqa: E501
    """Gets a list of connected node pairs

    Gets a list of connected node pairs # noqa: E501

    :param schema_url: The URL of a schema in jsonld form
    :type schema_url: str
    :param relationship_type: Type of relationship in a schema, such as requiresDependency
    :type relationship_type: str

    :rtype: Union[ConnectedNodesPage, Tuple[ConnectedNodesPage, int], Tuple[ConnectedNodesPage, int, Dict[str, str]]
    """
    return schema_controller_impl.get_connected_nodes(schema_url, relationship_type)


def get_node_is_required(node_display, schema_url):  # noqa: E501
    """Gets whether or not the node is required in the schema

    Gets whether or not the node is required in the schema # noqa: E501

    :param node_display: The display name of the node in a schema
    :type node_display: str
    :param schema_url: The URL of a schema in jsonld form
    :type schema_url: str

    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """
    return schema_controller_impl.get_node_is_required(node_display, schema_url)


def get_node_properties(node_label, schema_url):  # noqa: E501
    """Gets properties associated with a given node

    Gets properties associated with a given node # noqa: E501

    :param node_label: The label of the source node in a schema to get the dependencies of
    :type node_label: str
    :param schema_url: The URL of a schema in jsonld form
    :type schema_url: str

    :rtype: Union[NodePropertiesPage, Tuple[NodePropertiesPage, int], Tuple[NodePropertiesPage, int, Dict[str, str]]
    """
    return schema_controller_impl.get_node_properties(node_label, schema_url)


def get_property_label(
    node_display, schema_url, use_strict_camel_case=None
):  # noqa: E501
    """Gets the property label of the node

    Gets the property label of the node # noqa: E501

    :param node_display: The display name of the node in a schema
    :type node_display: str
    :param schema_url: The URL of a schema in jsonld form
    :type schema_url: str
    :param use_strict_camel_case: Whether or not to use the more strict way of converting to camel case
    :type use_strict_camel_case: bool

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    return schema_controller_impl.get_property_label(
        node_display, schema_url, use_strict_camel_case
    )


def get_schema_attributes(schema_url):  # noqa: E501
    """Get all the attributes associated with a data model formatted as a dataframe (stored as a JSON String).

    Get all the attributes associated with a data model formatted as a dataframe (stored as a JSON String). # noqa: E501

    :param schema_url: The URL of a schema in jsonld form
    :type schema_url: str

    :rtype: Union[str, Tuple[str, int], Tuple[str, int, Dict[str, str]]
    """
    return schema_controller_impl.get_schema_attributes(schema_url)


def list_node_dependencies(
    node_label, schema_url, return_display_names=None, return_ordered_by_schema=None
):  # noqa: E501
    """Gets the immediate dependencies that are related to the given source node

    Gets the immediate dependencies that are related to the given source node # noqa: E501

    :param node_label: The label of the source node in a schema to get the dependencies of
    :type node_label: str
    :param schema_url: The URL of a schema in jsonld form
    :type schema_url: str
    :param return_display_names: Whether or not to return the display names of the component, otherwise the label
    :type return_display_names: bool
    :param return_ordered_by_schema: Whether or not to order the components by their order in the schema, otherwise random
    :type return_ordered_by_schema: bool

    :rtype: Union[NodesPage, Tuple[NodesPage, int], Tuple[NodesPage, int, Dict[str, str]]
    """
    return schema_controller_impl.list_node_dependencies(
        node_label, schema_url, return_display_names, return_ordered_by_schema
    )


def list_node_validation_rules(node_display, schema_url):  # noqa: E501
    """Gets the validation rules, along with the arguments for each given rule associated with a given node

    Gets the validation rules, along with the arguments for each given rule associated with a given node # noqa: E501

    :param node_display: The display name of the node in a schema
    :type node_display: str
    :param schema_url: The URL of a schema in jsonld form
    :type schema_url: str

    :rtype: Union[ValidationRulesPage, Tuple[ValidationRulesPage, int], Tuple[ValidationRulesPage, int, Dict[str, str]]
    """
    return schema_controller_impl.list_node_validation_rules(node_display, schema_url)
