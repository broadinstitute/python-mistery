# -*- coding: utf-8 -*-
"""Define the mistery._endpoint.Endpoint base class."""

import logging

LOGGER = logging.getLogger(__name__)


class Endpoint(object):
    """Act as a superclass for all API endpoints."""

    def __init__(self, client, endpoint, api_version=None):
        """Initialize the class.

        :param object client: An instantiated mistery.Client object
        :param string endpoint: The API endpoint you are accessing (for example: "/sites")
        :param string api_version: The API version to use; the default is inherited from the client
        """
        self._client = client
        self._api_version = api_version
        if not api_version:
            self._api_version = client.api_version
        self._api_url = self.create_api_url(client.base_url, endpoint, self._api_version)

    @property
    def api_version(self):
        """Return the internal _api_version value."""
        return self._api_version

    @property
    def api_url(self):
        """Return the internal _api_url value."""
        return self._api_url

    @staticmethod
    def create_api_url(base_url, service, version):
        """Build the entire MIST API URL for the service and version.

        :param str base_url: The base URL you have i.e. for https://api.mist.com/api/v1/sites the base URL
            would be https://api.mist.com/api
        :param str service: The API service to use i.e. for https://api.mist.com/api/v1/sites the service would
            be sites
        :param str version: The API version to use i.e. for https://api.mist.com/api/v1/sites the version would
            be v1
        :return: The full URL
        :rtype: str
        """
        url = base_url.rstrip("/")
        url = f"{url}/{version.strip('/')}"
        url = f"{url}/{service.strip('/')}"
        LOGGER.debug("URL created: %s", url)

        return url

    def _url(self, suffix):
        """Build the endpoint URL based on the API URL inside this object.

        :param str suffix: The suffix of the URL you wish to create i.e. for
            https://api.mist.com/api/v1/sites/:site_id/wlans the suffix would be :site_id/wlans
        :return str: The full URL
        """
        url = self._api_url.rstrip("/")
        url = f"{url}/{suffix.strip('/')}"
        LOGGER.debug("URL created: %s", url)

        return url
