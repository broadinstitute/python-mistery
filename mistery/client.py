# -*- coding: utf-8 -*-
"""Define the mistery.client.Client class."""

import logging
import sys

import requests

LOGGER = logging.getLogger(__name__)


class Client(object):
    """Make HTTP calls to the MIST REST API."""

    def __init__(
        self, username, password, base_url="https://api.mist.com/api", api_version="v1", verify_ssl=True
    ):
        """Initialize the class.

        :param string username: The username with which to login
        :param string password: The password with which to login
        :param string base_url: The base URL of the API (default: https://api.mist.com/api)
        :param string api_version: The API version (default: v1)
        :param bool verify_ssl: Verify the certificate on the API (default: True)
        """
        self.__username = username
        self.__password = password
        self.__base_url = base_url
        self.__api_version = api_version
        self.__verify_ssl = verify_ssl

        # Create a new Requests Session
        self.__session = requests.Session()

        # Set the default HTTP headers
        self.__headers = {
            "Accept": "application/json",
            # "User-Agent": self.user_agent,
        }
        self.__session.headers.update(self.__headers)

        # Setup the authentication
        self.__authstring = requests.auth.HTTPBasicAuth(self.__username, self.__password)

        # Manually build the base URL to find any errors
        url = urlparse(base_url)
        self.__base_url = url.scheme
        self.__base_url += "://" + url.netloc
        self.__base_url += "/config"

        if url.scheme == "https":
            # If verify_ssl is False, also disable the urllib3 warnings
            if not self.__verify_ssl:
                requests.packages.urllib3.disable_warnings()  # pylint: disable=no-member
        else:
            # If not using https, force SSL verification to False
            self.__verify_ssl = False

    # @property
    # def user_agent(self):
    #     """Return a user-agent string including the module version and Python version."""
    #     ver_info = list(map(str, sys.version_info))
    #     pyver = ".".join(ver_info[:3])
    #     useragent = "cert_manager/%s (Python %s)" % (__version__.__version__, pyver)

    #     return useragent

    @property
    def api_version(self):
        """Return the internal __api_version value."""
        return self.__api_version

    @property
    def base_url(self):
        """Return the internal __base_url value."""
        return self.__base_url

    @property
    def headers(self):
        """Return the internal __headers value."""
        return self.__headers

    @property
    def session(self):
        """Return the setup internal __session requests.Session object."""
        return self.__session

    def get(self, url, headers=None):
        """Submit a GET request to the provided URL.

        :param str url: A URL to query
        :param dict headers: A dictionary with any extra headers to add to the request
        :return obj: A requests.Response object received as a response
        """
        result = self.__session.get(url, headers=headers)
        # Raise an exception if the return code is in an error range
        result.raise_for_status()

        return result

    def post(self, url, headers=None, data=None):
        """Submit a POST request to the provided URL and data.

        :param str url: A URL to query
        :param dict headers: A dictionary with any extra headers to add to the request
        :param dict data: A dictionary with the data to use for the body of the POST
        :return obj: A requests.Response object received as a response
        """
        result = self.__session.post(url, json=data, headers=headers)
        # Raise an exception if the return code is in an error range
        result.raise_for_status()

        return result

    def put(self, url, headers=None, data=None):
        """Submit a PUT request to the provided URL and data.

        :param str url: A URL to query
        :param dict headers: A dictionary with any extra headers to add to the request
        :param dict data: A dictionary with the data to use for the body of the PUT
        :return obj: A requests.Response object received as a response
        """
        result = self.__session.put(url, data=data, headers=headers)
        # Raise an exception if the return code is in an error range
        result.raise_for_status()

        return result

    def delete(self, url, headers=None):
        """Submit a DELETE request to the provided URL.

        :param str url: A URL to query
        :param dict headers: A dictionary with any extra headers to add to the request
        :return obj: A requests.Response object received as a response
        """
        result = self.__session.delete(url, headers=headers)
        # Raise an exception if the return code is in an error range
        result.raise_for_status()

        return result
