import gettext

from pulpcore.cli.common.context import (
    EntityDefinition,
    PulpEntityContext,
    PulpRepositoryContext,
    PulpRepositoryVersionContext,
)

_ = gettext.gettext


class PulpFileContentContext(PulpEntityContext):
    ENTITY = "file content"
    ENTITIES = "file content"
    HREF = "file_file_content_href"
    LIST_ID = "list"
    READ_ID = "read"
    CREATE_ID = "create"


class PulpFileDistributionContext(PulpEntityContext):
    ENTITY = "file distribution"
    ENTITIES = "file distributions"
    HREF = "file_file_distribution_href"
    LIST_ID = "list"
    READ_ID = "read"
    CREATE_ID = "create"
    UPDATE_ID = "partial_update"
    DELETE_ID = "delete"

    def preprocess_body(self, body: EntityDefinition) -> EntityDefinition:
        body = super().preprocess_body(body)
        for nullable in [
            "publication",
        ]:
            if body.get(nullable) == "":
                body[nullable] = None
        return body


class PulpFilePublicationContext(PulpEntityContext):
    ENTITY = "file publication"
    ENTITIES = "file publications"
    HREF = "file_file_publication_href"
    LIST_ID = "list"
    READ_ID = "read"
    CREATE_ID = "create"
    DELETE_ID = "delete"

    def preprocess_body(self, body: EntityDefinition) -> EntityDefinition:
        body = super().preprocess_body(body)
        version = body.pop("version", None)
        if version is not None:
            repository_href = body.pop("repository")
            body["repository_version"] = f"{repository_href}versions/{version}/"
        return body


class PulpFileRemoteContext(PulpEntityContext):
    ENTITY = "file remote"
    ENTITIES = "file remotes"
    HREF = "file_file_remote_href"
    LIST_ID = "list"
    CREATE_ID = "create"
    READ_ID = "read"
    UPDATE_ID = "partial_update"
    DELETE_ID = "delete"

    def preprocess_body(self, body: EntityDefinition) -> EntityDefinition:
        body = super().preprocess_body(body)
        for nullable in [
            "ca_cert",
            "client_cert",
            "client_key",
            "password",
            "proxy_url",
            "username",
        ]:
            if body.get(nullable) == "":
                body[nullable] = None
        return body


class PulpFileRepositoryVersionContext(PulpRepositoryVersionContext):
    HREF = "file_file_repository_version_href"
    REPOSITORY_HREF = "file_file_repository_href"
    LIST_ID = "list"
    READ_ID = "read"
    DELETE_ID = "delete"
    REPAIR_ID = "repair"


class PulpFileRepositoryContext(PulpRepositoryContext):
    HREF = "file_file_repository_href"
    LIST_ID = "list"
    READ_ID = "read"
    CREATE_ID = "create"
    UPDATE_ID = "partial_update"
    DELETE_ID = "delete"
    SYNC_ID = "sync"
    MODIFY_ID = "modify"
    VERSION_CONTEXT = PulpFileRepositoryVersionContext

    def preprocess_body(self, body: EntityDefinition) -> EntityDefinition:
        body = super().preprocess_body(body)
        if body.get("description") == "":
            body["description"] = None
        return body
