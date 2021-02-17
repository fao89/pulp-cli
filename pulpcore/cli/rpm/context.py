import gettext

from pulpcore.cli.common.context import (
    EntityDefinition,
    PulpEntityContext,
    PulpRepositoryContext,
    PulpRepositoryVersionContext,
)

_ = gettext.gettext


class PulpRpmDistributionContext(PulpEntityContext):
    ENTITY = "distribution"
    HREF = "rpm_rpm_distribution_href"
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


class PulpRpmPublicationContext(PulpEntityContext):
    ENTITY = "publication"
    HREF = "rpm_rpm_publication_href"
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


class PulpRpmRemoteContext(PulpEntityContext):
    ENTITY = "remote"
    HREF = "rpm_rpm_remote_href"
    LIST_ID = "list"
    READ_ID = "read"
    CREATE_ID = "create"
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


class PulpRpmRepositoryVersionContext(PulpRepositoryVersionContext):
    HREF = "rpm_rpm_repository_version_href"
    REPOSITORY_HREF = "rpm_rpm_repository_href"
    LIST_ID = "list"
    READ_ID = "read"
    DELETE_ID = "delete"
    REPAIR_ID = "repair"


class PulpRpmRepositoryContext(PulpRepositoryContext):
    HREF = "rpm_rpm_repository_href"
    LIST_ID = "list"
    READ_ID = "read"
    CREATE_ID = "create"
    UPDATE_ID = "partial_update"
    DELETE_ID = "delete"
    SYNC_ID = "sync"
    VERSION_CONTEXT = PulpRpmRepositoryVersionContext

    def preprocess_body(self, body: EntityDefinition) -> EntityDefinition:
        body = super().preprocess_body(body)
        if body.get("description") == "":
            body["description"] = None
        return body
