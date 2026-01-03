import keycloak from "./keycloak";

const REFRESH_INTERVAL_MS = 60_000; // cada 60s
const MIN_VALIDITY = 60; // renovar si expira en <60s

let intervalId: number | null = null;

export function startTokenRefresh() {
  if (intervalId) return;

  console.debug("[auth] start token refresh loop");

  intervalId = window.setInterval(async () => {
    try {
      if (!keycloak.authenticated) {
        console.debug("[auth] not authenticated, skip refresh");
        return;
      }

      const refreshed = await keycloak.updateToken(MIN_VALIDITY);

      console.debug("[auth] token check", {
        refreshed,
        exp: keycloak.tokenParsed?.exp,
        now: Math.floor(Date.now() / 1000),
      });
    } catch (err) {
      console.error("[auth] token refresh failed", err);
      keycloak.logout();
    }
  }, REFRESH_INTERVAL_MS);
}

export function stopTokenRefresh() {
  if (intervalId) {
    console.debug("[auth] stop token refresh loop");
    clearInterval(intervalId);
    intervalId = null;
  }
}
