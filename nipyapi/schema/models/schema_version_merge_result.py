# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SchemaVersionMergeResult(object):
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
        'schema_id_version': 'SchemaIdVersion',
        'merge_message': 'str'
    }

    attribute_map = {
        'schema_id_version': 'schemaIdVersion',
        'merge_message': 'mergeMessage'
    }

    def __init__(self, schema_id_version=None, merge_message=None):
        """
        SchemaVersionMergeResult - a model defined in Swagger
        """

        self._schema_id_version = None
        self._merge_message = None

        if schema_id_version is not None:
          self.schema_id_version = schema_id_version
        if merge_message is not None:
          self.merge_message = merge_message

    @property
    def schema_id_version(self):
        """
        Gets the schema_id_version of this SchemaVersionMergeResult.

        :return: The schema_id_version of this SchemaVersionMergeResult.
        :rtype: SchemaIdVersion
        """
        return self._schema_id_version

    @schema_id_version.setter
    def schema_id_version(self, schema_id_version):
        """
        Sets the schema_id_version of this SchemaVersionMergeResult.

        :param schema_id_version: The schema_id_version of this SchemaVersionMergeResult.
        :type: SchemaIdVersion
        """

        self._schema_id_version = schema_id_version

    @property
    def merge_message(self):
        """
        Gets the merge_message of this SchemaVersionMergeResult.

        :return: The merge_message of this SchemaVersionMergeResult.
        :rtype: str
        """
        return self._merge_message

    @merge_message.setter
    def merge_message(self, merge_message):
        """
        Sets the merge_message of this SchemaVersionMergeResult.

        :param merge_message: The merge_message of this SchemaVersionMergeResult.
        :type: str
        """

        self._merge_message = merge_message

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
        if not isinstance(other, SchemaVersionMergeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other