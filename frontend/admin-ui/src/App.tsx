import { BrowserRouter, Routes, Route } from "react-router-dom";

import { AuthProvider } from "./auth/AuthProvider";
import { ProtectedRoute } from "./routes/ProtectedRoute";
import { AdminLayout } from "./layouts/AdminLayout";
import { Home } from "./pages/Home";
import Admin from "./pages/Admin";


export default function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <AdminLayout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route
              path="/admin"
              element={
                <ProtectedRoute roles={["ADMIN"]}>
                  <Admin />
                </ProtectedRoute>
              }
            />
          </Routes>
        </AdminLayout>
      </BrowserRouter>
    </AuthProvider>
  );
}
