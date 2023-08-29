# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from schematic_api.models.base_model_ import Model
from schematic_api.models.file import File
from schematic_api import util

from schematic_api.models.file import File  # noqa: E501

class FilesPage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, number=None, size=None, total_elements=None, total_pages=None, has_next=None, has_previous=None, files=None):  # noqa: E501
        """FilesPage - a model defined in OpenAPI

        :param number: The number of this FilesPage.  # noqa: E501
        :type number: int
        :param size: The size of this FilesPage.  # noqa: E501
        :type size: int
        :param total_elements: The total_elements of this FilesPage.  # noqa: E501
        :type total_elements: int
        :param total_pages: The total_pages of this FilesPage.  # noqa: E501
        :type total_pages: int
        :param has_next: The has_next of this FilesPage.  # noqa: E501
        :type has_next: bool
        :param has_previous: The has_previous of this FilesPage.  # noqa: E501
        :type has_previous: bool
        :param files: The files of this FilesPage.  # noqa: E501
        :type files: List[File]
        """
        self.openapi_types = {
            'number': int,
            'size': int,
            'total_elements': int,
            'total_pages': int,
            'has_next': bool,
            'has_previous': bool,
            'files': List[File]
        }

        self.attribute_map = {
            'number': 'number',
            'size': 'size',
            'total_elements': 'totalElements',
            'total_pages': 'totalPages',
            'has_next': 'hasNext',
            'has_previous': 'hasPrevious',
            'files': 'files'
        }

        self._number = number
        self._size = size
        self._total_elements = total_elements
        self._total_pages = total_pages
        self._has_next = has_next
        self._has_previous = has_previous
        self._files = files

    @classmethod
    def from_dict(cls, dikt) -> 'FilesPage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FilesPage of this FilesPage.  # noqa: E501
        :rtype: FilesPage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def number(self):
        """Gets the number of this FilesPage.

        The page number.  # noqa: E501

        :return: The number of this FilesPage.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this FilesPage.

        The page number.  # noqa: E501

        :param number: The number of this FilesPage.
        :type number: int
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def size(self):
        """Gets the size of this FilesPage.

        The number of items in a single page.  # noqa: E501

        :return: The size of this FilesPage.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FilesPage.

        The number of items in a single page.  # noqa: E501

        :param size: The size of this FilesPage.
        :type size: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def total_elements(self):
        """Gets the total_elements of this FilesPage.

        Total number of elements in the result set.  # noqa: E501

        :return: The total_elements of this FilesPage.
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """Sets the total_elements of this FilesPage.

        Total number of elements in the result set.  # noqa: E501

        :param total_elements: The total_elements of this FilesPage.
        :type total_elements: int
        """
        if total_elements is None:
            raise ValueError("Invalid value for `total_elements`, must not be `None`")  # noqa: E501

        self._total_elements = total_elements

    @property
    def total_pages(self):
        """Gets the total_pages of this FilesPage.

        Total number of pages in the result set.  # noqa: E501

        :return: The total_pages of this FilesPage.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this FilesPage.

        Total number of pages in the result set.  # noqa: E501

        :param total_pages: The total_pages of this FilesPage.
        :type total_pages: int
        """
        if total_pages is None:
            raise ValueError("Invalid value for `total_pages`, must not be `None`")  # noqa: E501

        self._total_pages = total_pages

    @property
    def has_next(self):
        """Gets the has_next of this FilesPage.

        Returns if there is a next page.  # noqa: E501

        :return: The has_next of this FilesPage.
        :rtype: bool
        """
        return self._has_next

    @has_next.setter
    def has_next(self, has_next):
        """Sets the has_next of this FilesPage.

        Returns if there is a next page.  # noqa: E501

        :param has_next: The has_next of this FilesPage.
        :type has_next: bool
        """
        if has_next is None:
            raise ValueError("Invalid value for `has_next`, must not be `None`")  # noqa: E501

        self._has_next = has_next

    @property
    def has_previous(self):
        """Gets the has_previous of this FilesPage.

        Returns if there is a previous page.  # noqa: E501

        :return: The has_previous of this FilesPage.
        :rtype: bool
        """
        return self._has_previous

    @has_previous.setter
    def has_previous(self, has_previous):
        """Sets the has_previous of this FilesPage.

        Returns if there is a previous page.  # noqa: E501

        :param has_previous: The has_previous of this FilesPage.
        :type has_previous: bool
        """
        if has_previous is None:
            raise ValueError("Invalid value for `has_previous`, must not be `None`")  # noqa: E501

        self._has_previous = has_previous

    @property
    def files(self):
        """Gets the files of this FilesPage.

        A list of files.  # noqa: E501

        :return: The files of this FilesPage.
        :rtype: List[File]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this FilesPage.

        A list of files.  # noqa: E501

        :param files: The files of this FilesPage.
        :type files: List[File]
        """
        if files is None:
            raise ValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = files
