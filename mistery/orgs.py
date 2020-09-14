# -*- coding: utf-8 -*-
"""Define the mistery.orgs.Orgs class."""

import logging

from ._endpoint import Endpoint

LOGGER = logging.getLogger(__name__)


class Organization(Endpoint):
    """Query the MIST REST API for Organization data."""

    def __init__(self, client, org_id, api_version="v1"):
        """Initialize the class.

        Note: The *all* method will be run on object instantiation to fetch all organizations

        :param object client: An instantiated cert_manager.Client object
        :param string org_id: The organization ID to query
        :param string api_version: The API version to use; the default is "v1"
        """
        super().__init__(client=client, endpoint="/orgs", api_version=api_version)
        self._org_id = org_id

        self.__orgs = None
