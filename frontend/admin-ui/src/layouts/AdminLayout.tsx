import type { ReactNode } from "react";
import { useAuth } from "../auth/AuthContext";
import { Link } from "react-router-dom";

export function AdminLayout({ children }: { children: ReactNode }) {
  const { user, logout, hasRole } = useAuth();

  return (
    <div style={{ display: "flex", height: "100vh" }}>
      {/* Sidebar */}
      <aside style={{ width: 220, background: "#111", color: "#fff", padding: 16 }}>
        <h3>Lattice Admin</h3>
        <nav>
          <ul>
            <li><Link to="/" style={{ color: "#fff" }}>Home</Link></li>
            {hasRole(["ADMIN"]) && (
              <li><Link to="/admin" style={{ color: "#fff" }}>Admin</Link></li>
            )}
          </ul>
        </nav>
      </aside>

      {/* Main */}
      <div style={{ flex: 1 }}>
        {/* Topbar */}
        <header style={{ padding: 12, borderBottom: "1px solid #ddd" }}>
          {user?.email} ({user?.roles.join(", ")})
          <button style={{ float: "right" }} onClick={logout}>
            Logout
          </button>
        </header>

        <main style={{ padding: 16 }}>{children}</main>
      </div>
    </div>
  );
}
