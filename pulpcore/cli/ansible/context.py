import gettext

from pulpcore.cli.common.context import (
    PulpEntityContext,
    PulpRepositoryContext,
    PulpRepositoryVersionContext,
)

_ = gettext.gettext

# TODO Add Role and Collection Content contexts


class PulpAnsibleDistributionContext(PulpEntityContext):
    ENTITY = "distribution"
    HREF = "ansible_ansible_distribution_href"
    LIST_ID = "list"
    READ_ID = "read"
    CREATE_ID = "create"
    UPDATE_ID = "partial_update"
    DELETE_ID = "delete"


class PulpAnsibleRoleRemoteContext(PulpEntityContext):
    ENTITY = "role remote"
    HREF = "ansible_role_remote_href"
    LIST_ID = "list"
    READ_ID = "read"
    CREATE_ID = "create"
    UPDATE_ID = "partial_update"
    DELETE_ID = "delete"


class PulpAnsibleCollectionRemoteContext(PulpEntityContext):
    ENTITY = "collection remote"
    HREF = "ansible_collection_remote_href"
    LIST_ID = "list"
    READ_ID = "read"
    CREATE_ID = "create"
    UPDATE_ID = "partial_update"
    DELETE_ID = "delete"


class PulpAnsibleRepositoryVersionContext(PulpRepositoryVersionContext):
    HREF = "ansible_ansible_repository_version_href"
    REPOSITORY_HREF = "ansible_ansible_repository_href"
    LIST_ID = "list"
    READ_ID = "read"
    DELETE_ID = "delete"
    REPAIR_ID = "repair"


class PulpAnsibleRepositoryContext(PulpRepositoryContext):
    HREF = "ansible_ansible_repository_href"
    LIST_ID = "list"
    READ_ID = "read"
    CREATE_ID = "create"
    UPDATE_ID = "partial_update"
    DELETE_ID = "delete"
    SYNC_ID = "sync"
    MODIFY_ID = "modify"
    VERSION_CONTEXT = PulpAnsibleRepositoryVersionContext
