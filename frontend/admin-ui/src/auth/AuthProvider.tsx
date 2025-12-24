import { useEffect, useState } from "react";
import type { ReactNode } from "react";
import axios from "axios";

import keycloak from "./keycloak";
import { AuthContext } from "./AuthContext";
import type { User } from "./AuthContext";

const API_URL = import.meta.env.VITE_API_URL;

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    keycloak
      .init({ onLoad: "login-required", pkceMethod: "S256" })
      .then(async (authenticated: boolean) => {
        if (!authenticated) {
          keycloak.login();
          return;
        }

        const t = keycloak.token!;
        setToken(t);
        axios.defaults.headers.common["Authorization"] = `Bearer ${t}`;

        const res = await axios.get(`${API_URL}/me`);
        setUser(res.data);
        setLoading(false);
      })
      .catch(() => keycloak.login());
  }, []);

  const login = () => keycloak.login();
  const logout = () =>
    keycloak.logout({ redirectUri: window.location.origin });

  const hasRole = (roles: string[]) =>
    !!user && roles.some((r) => user.roles.includes(r));

  if (loading) return <div>Cargando...</div>;

  return (
    <AuthContext.Provider value={{ user, token, login, logout, hasRole }}>
      {children}
    </AuthContext.Provider>
  );
}
