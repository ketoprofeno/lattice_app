import type { ReactNode } from "react";
import { Navigate } from "react-router-dom";
import { useAuth } from "../auth/AuthContext";

export type ProtectedRouteProps = {
  roles?: string[];
  children: ReactNode;
};

export function ProtectedRoute({ roles, children }: ProtectedRouteProps) {
  const { user, hasRole } = useAuth();

  if (!user) return <Navigate to="/" replace />;

  if (roles && !hasRole(roles)) {
    return <div>No autorizado</div>;
  }

  return <>{children}</>;
}
