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


class CampaignReportQueryMessage(object):
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
        'advertiser_ids': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'dimensions': 'list[str]',
        'metrics': 'list[str]',
        'format': 'str',
        'currency': 'str',
        'timezone': 'str'
    }

    attribute_map = {
        'advertiser_ids': 'advertiserIds',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'dimensions': 'dimensions',
        'metrics': 'metrics',
        'format': 'format',
        'currency': 'currency',
        'timezone': 'timezone'
    }

    def __init__(self, advertiser_ids=None, start_date=None, end_date=None, dimensions=None, metrics=None, format=None, currency=None, timezone=None):  # noqa: E501
        """CampaignReportQueryMessage - a model defined in OpenAPI"""  # noqa: E501

        self._advertiser_ids = None
        self._start_date = None
        self._end_date = None
        self._dimensions = None
        self._metrics = None
        self._format = None
        self._currency = None
        self._timezone = None
        self.discriminator = None

        if advertiser_ids is not None:
            self.advertiser_ids = advertiser_ids
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if dimensions is not None:
            self.dimensions = dimensions
        if metrics is not None:
            self.metrics = metrics
        if format is not None:
            self.format = format
        if currency is not None:
            self.currency = currency
        if timezone is not None:
            self.timezone = timezone

    @property
    def advertiser_ids(self):
        """Gets the advertiser_ids of this CampaignReportQueryMessage.  # noqa: E501


        :return: The advertiser_ids of this CampaignReportQueryMessage.  # noqa: E501
        :rtype: str
        """
        return self._advertiser_ids

    @advertiser_ids.setter
    def advertiser_ids(self, advertiser_ids):
        """Sets the advertiser_ids of this CampaignReportQueryMessage.


        :param advertiser_ids: The advertiser_ids of this CampaignReportQueryMessage.  # noqa: E501
        :type: str
        """

        self._advertiser_ids = advertiser_ids

    @property
    def start_date(self):
        """Gets the start_date of this CampaignReportQueryMessage.  # noqa: E501


        :return: The start_date of this CampaignReportQueryMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CampaignReportQueryMessage.


        :param start_date: The start_date of this CampaignReportQueryMessage.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CampaignReportQueryMessage.  # noqa: E501


        :return: The end_date of this CampaignReportQueryMessage.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CampaignReportQueryMessage.


        :param end_date: The end_date of this CampaignReportQueryMessage.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def dimensions(self):
        """Gets the dimensions of this CampaignReportQueryMessage.  # noqa: E501


        :return: The dimensions of this CampaignReportQueryMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this CampaignReportQueryMessage.


        :param dimensions: The dimensions of this CampaignReportQueryMessage.  # noqa: E501
        :type: list[str]
        """

        self._dimensions = dimensions

    @property
    def metrics(self):
        """Gets the metrics of this CampaignReportQueryMessage.  # noqa: E501


        :return: The metrics of this CampaignReportQueryMessage.  # noqa: E501
        :rtype: list[str]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this CampaignReportQueryMessage.


        :param metrics: The metrics of this CampaignReportQueryMessage.  # noqa: E501
        :type: list[str]
        """

        self._metrics = metrics

    @property
    def format(self):
        """Gets the format of this CampaignReportQueryMessage.  # noqa: E501


        :return: The format of this CampaignReportQueryMessage.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this CampaignReportQueryMessage.


        :param format: The format of this CampaignReportQueryMessage.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def currency(self):
        """Gets the currency of this CampaignReportQueryMessage.  # noqa: E501


        :return: The currency of this CampaignReportQueryMessage.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CampaignReportQueryMessage.


        :param currency: The currency of this CampaignReportQueryMessage.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def timezone(self):
        """Gets the timezone of this CampaignReportQueryMessage.  # noqa: E501


        :return: The timezone of this CampaignReportQueryMessage.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this CampaignReportQueryMessage.


        :param timezone: The timezone of this CampaignReportQueryMessage.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

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
        if not isinstance(other, CampaignReportQueryMessage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
