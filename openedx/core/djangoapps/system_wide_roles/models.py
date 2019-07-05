"""
Django models for system wide roles.
"""
from __future__ import unicode_literals

from edx_rbac.models import UserRole, UserRoleAssignment


class SystemWideRole(UserRole):  # pylint: disable=model-missing-unicode
    """
    User role definitions to govern non-enterprise system wide roles.
     .. no_pii:
    """


class SystemWideRoleAssignment(UserRoleAssignment):  # pylint: disable=model-missing-unicode
    """
    Model to map users to a SystemWideRole.
     .. no_pii:
    """

    role_class = SystemWideRole
