import { createContext, useContext } from "react";

export type User = {
  sub: string;
  email?: string;
  name?: string;
  roles: string[];
};

export type AuthContextType = {
  user: User | null;
  token: string | null;
  login: () => void;
  logout: () => void;
  hasRole: (roles: string[]) => boolean;
};

export const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const useAuth = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
};
