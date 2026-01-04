import { useEffect, useState } from "react";
import type { ReactNode } from "react";
import axios from "axios";

import keycloak from "./keycloak";
import { startTokenRefresh, stopTokenRefresh } from "./tokenRefresh";
import { AuthContext } from "./AuthContext";
import type { User } from "./AuthContext";

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initAuth = async () => {
      try {
        const authenticated = await keycloak.init({
          onLoad: "login-required",
          pkceMethod: "S256",
          checkLoginIframe: false,
          flow: "standard",
          responseMode: "query",
        });

        if (!authenticated) return;

        const t = keycloak.token;
        if (!t) return;

        setToken(t);
        axios.defaults.headers.common.Authorization = `Bearer ${t}`;

        const res = await axios.get<User>("/api/me");
        setUser(res.data);

        startTokenRefresh();
        setLoading(false);
      } catch {
        setLoading(false);
      }
    };

    initAuth();

    return () => {
      stopTokenRefresh();
    };
  }, []);

  const login = () =>
    keycloak.login({ redirectUri: window.location.origin + "/admin" });

  const logout = () =>
    keycloak.logout({ redirectUri: window.location.origin });

  const hasRole = (roles: string[]) =>
    roles.some((r) => user?.roles?.includes(r));

  if (loading) return <div>Cargando autenticación…</div>;

  return (
    <AuthContext.Provider value={{ user, token, login, logout, hasRole }}>
      {children}
    </AuthContext.Provider>
  );
}
