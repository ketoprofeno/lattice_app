import { NavLink } from "react-router-dom";

const linkClass =
  "block rounded-md px-3 py-2 text-sm font-medium hover:bg-muted";

export function Sidebar() {
  return (
    <aside className="w-64 border-r bg-background p-4">
      <h2 className="mb-6 text-lg font-semibold">Lattice Admin</h2>

      <nav className="space-y-1">
        <NavLink to="/" className={linkClass}>
          Home
        </NavLink>

        <NavLink to="/admin" className={linkClass}>
          Admin
        </NavLink>
      </nav>
    </aside>
  );
}
