# coding: utf-8

"""
    Marketing API v.1.0

    IMPORTANT: This swagger links to Criteo production environment. Any test applied here will thus impact real campaigns.  # noqa: E501

    The version of the OpenAPI document: v.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ProductShippingDimensionV3(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'value': 'float',
        'unit': 'str'
    }

    attribute_map = {
        'value': 'value',
        'unit': 'unit'
    }

    def __init__(self, value=None, unit=None):  # noqa: E501
        """ProductShippingDimensionV3 - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._unit = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if unit is not None:
            self.unit = unit

    @property
    def value(self):
        """Gets the value of this ProductShippingDimensionV3.  # noqa: E501

        The dimension of the product used to calculate the shipping cost of the item.  # noqa: E501

        :return: The value of this ProductShippingDimensionV3.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ProductShippingDimensionV3.

        The dimension of the product used to calculate the shipping cost of the item.  # noqa: E501

        :param value: The value of this ProductShippingDimensionV3.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def unit(self):
        """Gets the unit of this ProductShippingDimensionV3.  # noqa: E501

        The unit of value.  # noqa: E501

        :return: The unit of this ProductShippingDimensionV3.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ProductShippingDimensionV3.

        The unit of value.  # noqa: E501

        :param unit: The unit of this ProductShippingDimensionV3.  # noqa: E501
        :type: str
        """

        self._unit = unit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProductShippingDimensionV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
