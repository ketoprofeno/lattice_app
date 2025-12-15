from __future__ import annotations

import json
from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    env: str = Field(default="dev", alias="ENV")

    # OIDC / JWT
    oidc_issuer: str = Field(alias="OIDC_ISSUER")
    oidc_audience: str = Field(alias="OIDC_AUDIENCE")
    oidc_jwks_url: AnyHttpUrl = Field(alias="OIDC_JWKS_URL")
    oidc_algorithms: str = Field(default="RS256", alias="OIDC_ALGORITHMS")

    # Claims / RBAC
    auth_groups_claim: str = Field(default="groups", alias="AUTH_GROUPS_CLAIM")
    rbac_group_role_map_raw: str = Field(
        default='{"admin-app-admin":"ADMIN"}',
        alias="RBAC_GROUP_ROLE_MAP",
    )

    # CORS
    cors_origins: str = Field(default="http://localhost:3000", alias="CORS_ORIGINS")

    @property
    def oidc_algorithms_list(self) -> list[str]:
        return [a.strip() for a in self.oidc_algorithms.split(",") if a.strip()]

    @property
    def rbac_group_role_map(self) -> dict[str, str]:
        return json.loads(self.rbac_group_role_map_raw)

    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


settings = Settings()
