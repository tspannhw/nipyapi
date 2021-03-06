# coding: utf-8

"""
    NiFi Rest Api



    OpenAPI spec version: 1.2.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProcessGroupStatusSnapshotEntity(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'can_read': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'can_read': 'canRead'
    }

    def __init__(self, id=None, can_read=False):
        """
        ProcessGroupStatusSnapshotEntity - a model defined in Swagger
        """

        self._id = None
        self._can_read = None

        if id is not None:
          self.id = id
        if can_read is not None:
          self.can_read = can_read

    @property
    def id(self):
        """
        Gets the id of this ProcessGroupStatusSnapshotEntity.
        The id of the process group.

        :return: The id of this ProcessGroupStatusSnapshotEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProcessGroupStatusSnapshotEntity.
        The id of the process group.

        :param id: The id of this ProcessGroupStatusSnapshotEntity.
        :type: str
        """

        self._id = id

    @property
    def can_read(self):
        """
        Gets the can_read of this ProcessGroupStatusSnapshotEntity.
        Indicates whether the user can read a given resource.

        :return: The can_read of this ProcessGroupStatusSnapshotEntity.
        :rtype: bool
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read):
        """
        Sets the can_read of this ProcessGroupStatusSnapshotEntity.
        Indicates whether the user can read a given resource.

        :param can_read: The can_read of this ProcessGroupStatusSnapshotEntity.
        :type: bool
        """

        self._can_read = can_read

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ProcessGroupStatusSnapshotEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
