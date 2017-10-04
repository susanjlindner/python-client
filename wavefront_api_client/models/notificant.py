# coding: utf-8

"""
    Wavefront Public API

    <p>The Wavefront public API enables you to interact with Wavefront servers using standard web service API tools. You can use the API to automate commonly executed operations such as automatically tagging sources.</p><p>When you make API calls outside the Wavefront API documentation you must add the header \"Authorization: Bearer &lt;&lt;API-TOKEN&gt;&gt;\" to your HTTP requests.</p><p>For legacy versions of the Wavefront API, see the <a href=\"/api-docs/ui/deprecated\">legacy API documentation</a>.</p>

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Notificant(object):
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
        'method': 'str',
        'content_type': 'str',
        'id': 'str',
        'description': 'str',
        'customer_id': 'str',
        'title': 'str',
        'creator_id': 'str',
        'created_epoch_millis': 'int',
        'updated_epoch_millis': 'int',
        'updater_id': 'str',
        'template': 'str',
        'triggers': 'list[str]',
        'custom_http_headers': 'dict(str, str)',
        'recipient': 'str',
        'email_subject': 'str'
    }

    attribute_map = {
        'method': 'method',
        'content_type': 'contentType',
        'id': 'id',
        'description': 'description',
        'customer_id': 'customerId',
        'title': 'title',
        'creator_id': 'creatorId',
        'created_epoch_millis': 'createdEpochMillis',
        'updated_epoch_millis': 'updatedEpochMillis',
        'updater_id': 'updaterId',
        'template': 'template',
        'triggers': 'triggers',
        'custom_http_headers': 'customHttpHeaders',
        'recipient': 'recipient',
        'email_subject': 'emailSubject'
    }

    def __init__(self, method=None, content_type=None, id=None, description=None, customer_id=None, title=None, creator_id=None, created_epoch_millis=None, updated_epoch_millis=None, updater_id=None, template=None, triggers=None, custom_http_headers=None, recipient=None, email_subject=None):
        """
        Notificant - a model defined in Swagger
        """

        self._method = None
        self._content_type = None
        self._id = None
        self._description = None
        self._customer_id = None
        self._title = None
        self._creator_id = None
        self._created_epoch_millis = None
        self._updated_epoch_millis = None
        self._updater_id = None
        self._template = None
        self._triggers = None
        self._custom_http_headers = None
        self._recipient = None
        self._email_subject = None
        self.discriminator = None

        self.method = method
        if content_type is not None:
          self.content_type = content_type
        if id is not None:
          self.id = id
        self.description = description
        if customer_id is not None:
          self.customer_id = customer_id
        self.title = title
        if creator_id is not None:
          self.creator_id = creator_id
        if created_epoch_millis is not None:
          self.created_epoch_millis = created_epoch_millis
        if updated_epoch_millis is not None:
          self.updated_epoch_millis = updated_epoch_millis
        if updater_id is not None:
          self.updater_id = updater_id
        self.template = template
        self.triggers = triggers
        if custom_http_headers is not None:
          self.custom_http_headers = custom_http_headers
        self.recipient = recipient
        if email_subject is not None:
          self.email_subject = email_subject

    @property
    def method(self):
        """
        Gets the method of this Notificant.
        The notification method used for notification target.

        :return: The method of this Notificant.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this Notificant.
        The notification method used for notification target.

        :param method: The method of this Notificant.
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")
        allowed_values = ["WEBHOOK", "EMAIL", "PAGERDUTY"]
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def content_type(self):
        """
        Gets the content_type of this Notificant.
        The value of the Content-Type header of the webhook POST request.

        :return: The content_type of this Notificant.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this Notificant.
        The value of the Content-Type header of the webhook POST request.

        :param content_type: The content_type of this Notificant.
        :type: str
        """
        allowed_values = ["application/json", "text/html", "text/plain", "application/x-www-form-urlencoded"]
        if content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def id(self):
        """
        Gets the id of this Notificant.

        :return: The id of this Notificant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Notificant.

        :param id: The id of this Notificant.
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """
        Gets the description of this Notificant.
        Description

        :return: The description of this Notificant.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Notificant.
        Description

        :param description: The description of this Notificant.
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def customer_id(self):
        """
        Gets the customer_id of this Notificant.

        :return: The customer_id of this Notificant.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this Notificant.

        :param customer_id: The customer_id of this Notificant.
        :type: str
        """

        self._customer_id = customer_id

    @property
    def title(self):
        """
        Gets the title of this Notificant.
        Title

        :return: The title of this Notificant.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Notificant.
        Title

        :param title: The title of this Notificant.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def creator_id(self):
        """
        Gets the creator_id of this Notificant.

        :return: The creator_id of this Notificant.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """
        Sets the creator_id of this Notificant.

        :param creator_id: The creator_id of this Notificant.
        :type: str
        """

        self._creator_id = creator_id

    @property
    def created_epoch_millis(self):
        """
        Gets the created_epoch_millis of this Notificant.

        :return: The created_epoch_millis of this Notificant.
        :rtype: int
        """
        return self._created_epoch_millis

    @created_epoch_millis.setter
    def created_epoch_millis(self, created_epoch_millis):
        """
        Sets the created_epoch_millis of this Notificant.

        :param created_epoch_millis: The created_epoch_millis of this Notificant.
        :type: int
        """

        self._created_epoch_millis = created_epoch_millis

    @property
    def updated_epoch_millis(self):
        """
        Gets the updated_epoch_millis of this Notificant.

        :return: The updated_epoch_millis of this Notificant.
        :rtype: int
        """
        return self._updated_epoch_millis

    @updated_epoch_millis.setter
    def updated_epoch_millis(self, updated_epoch_millis):
        """
        Sets the updated_epoch_millis of this Notificant.

        :param updated_epoch_millis: The updated_epoch_millis of this Notificant.
        :type: int
        """

        self._updated_epoch_millis = updated_epoch_millis

    @property
    def updater_id(self):
        """
        Gets the updater_id of this Notificant.

        :return: The updater_id of this Notificant.
        :rtype: str
        """
        return self._updater_id

    @updater_id.setter
    def updater_id(self, updater_id):
        """
        Sets the updater_id of this Notificant.

        :param updater_id: The updater_id of this Notificant.
        :type: str
        """

        self._updater_id = updater_id

    @property
    def template(self):
        """
        Gets the template of this Notificant.
        A mustache template that will form the body of the POST request, email and summary of the PagerDuty.

        :return: The template of this Notificant.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this Notificant.
        A mustache template that will form the body of the POST request, email and summary of the PagerDuty.

        :param template: The template of this Notificant.
        :type: str
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")

        self._template = template

    @property
    def triggers(self):
        """
        Gets the triggers of this Notificant.
        A list of occurrences on which this webhook will be fired.  Valid values are ALERT_OPENED, ALERT_UPDATED, ALERT_RESOLVED, ALERT_MAINTENANCE, ALERT_SNOOZED

        :return: The triggers of this Notificant.
        :rtype: list[str]
        """
        return self._triggers

    @triggers.setter
    def triggers(self, triggers):
        """
        Sets the triggers of this Notificant.
        A list of occurrences on which this webhook will be fired.  Valid values are ALERT_OPENED, ALERT_UPDATED, ALERT_RESOLVED, ALERT_MAINTENANCE, ALERT_SNOOZED

        :param triggers: The triggers of this Notificant.
        :type: list[str]
        """
        if triggers is None:
            raise ValueError("Invalid value for `triggers`, must not be `None`")
        allowed_values = ["ALERT_OPENED", "ALERT_UPDATED", "ALERT_RESOLVED", "ALERT_MAINTENANCE", "ALERT_SNOOZED", "ALERT_INVALID", "ALERT_NO_LONGER_INVALID", "ALERT_TESTING", "ALERT_RETRIGGERED", "ALERT_NO_DATA", "ALERT_NO_DATA_RESOLVED", "ALERT_NO_DATA_MAINTENANCE"]
        if not set(triggers).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `triggers` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(triggers)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._triggers = triggers

    @property
    def custom_http_headers(self):
        """
        Gets the custom_http_headers of this Notificant.
        A string->string map specifying the custom HTTP header key / value pairs that will be sent in the requests of this web hook

        :return: The custom_http_headers of this Notificant.
        :rtype: dict(str, str)
        """
        return self._custom_http_headers

    @custom_http_headers.setter
    def custom_http_headers(self, custom_http_headers):
        """
        Sets the custom_http_headers of this Notificant.
        A string->string map specifying the custom HTTP header key / value pairs that will be sent in the requests of this web hook

        :param custom_http_headers: The custom_http_headers of this Notificant.
        :type: dict(str, str)
        """

        self._custom_http_headers = custom_http_headers

    @property
    def recipient(self):
        """
        Gets the recipient of this Notificant.
        The end point for the notification target.EMAIL: email address.  PAGERDUTY: PagerDuty routing Key.  WEBHOOK: URL end point

        :return: The recipient of this Notificant.
        :rtype: str
        """
        return self._recipient

    @recipient.setter
    def recipient(self, recipient):
        """
        Sets the recipient of this Notificant.
        The end point for the notification target.EMAIL: email address.  PAGERDUTY: PagerDuty routing Key.  WEBHOOK: URL end point

        :param recipient: The recipient of this Notificant.
        :type: str
        """
        if recipient is None:
            raise ValueError("Invalid value for `recipient`, must not be `None`")

        self._recipient = recipient

    @property
    def email_subject(self):
        """
        Gets the email_subject of this Notificant.
        The subject title of an email notification target

        :return: The email_subject of this Notificant.
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """
        Sets the email_subject of this Notificant.
        The subject title of an email notification target

        :param email_subject: The email_subject of this Notificant.
        :type: str
        """

        self._email_subject = email_subject

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
        if not isinstance(other, Notificant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other