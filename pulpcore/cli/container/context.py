import gettext

from pulpcore.cli.common.context import (
    PulpEntityContext,
    PulpRepositoryContext,
    PulpRepositoryVersionContext,
)

_ = gettext.gettext


class PulpContainerDistributionContext(PulpEntityContext):
    ENTITY = "distribution"
    HREF = "container_container_distribution_href"
    LIST_ID = "list"
    READ_ID = "read"
    CREATE_ID = "create"
    UPDATE_ID = "partial_update"
    DELETE_ID = "delete"


class PulpContainerRemoteContext(PulpEntityContext):
    ENTITY = "remote"
    HREF = "container_container_remote_href"
    LIST_ID = "list"
    CREATE_ID = "create"
    UPDATE_ID = "partial_update"
    DELETE_ID = "delete"


class PulpContainerRepositoryVersionContext(PulpRepositoryVersionContext):
    HREF = "container_container_repository_version_href"
    REPOSITORY_HREF = "container_container_repository_href"
    LIST_ID = "list"
    READ_ID = "read"
    DELETE_ID = "delete"


class PulpContainerPushRepositoryVersionContext(PulpRepositoryVersionContext):
    HREF = "container_container_push_repository_version_href"
    REPOSITORY_HREF = "container_container_push_repository_href"
    LIST_ID = "list"
    READ_ID = "read"
    DELETE_ID = "delete"


class PulpContainerRepositoryContext(PulpRepositoryContext):
    HREF = "container_container_repository_href"
    LIST_ID = "list"
    READ_ID = "read"
    CREATE_ID = "create"
    UPDATE_ID = "partial_update"
    DELETE_ID = "delete"
    SYNC_ID = "sync"
    VERSION_CONTEXT = PulpContainerRepositoryVersionContext


class PulpContainerPushRepositoryContext(PulpRepositoryContext):
    HREF = "container_container_push_repository_href"
    LIST_ID = "push_list"
    READ_ID = "push_read"
    # CREATE_ID = "push_create"
    # UPDATE_ID = "push_update"
    # DELETE_ID = "push_delete"
    # Cannot sync a push type repository
    # TODO Incorporate into capabilities
    # SYNC_ID = "push_sync"
    VERSION_CONTEXT = PulpContainerPushRepositoryVersionContext
