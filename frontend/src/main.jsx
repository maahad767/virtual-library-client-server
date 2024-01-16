import React from "react";
import ReactDOM from "react-dom/client";
import { Spin } from "antd";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { AuthProvider } from "./contexts/AuthContext";
import AppLayout from "./layouts/AppLayout";
import Root from "./Root";
import Login from "./pages/login/Login";
import "./index.css";

const router = createBrowserRouter([
  {
    path: "/",
    loader: () => <Spin />,
    element: (
      <AppLayout>
        <Root />
      </AppLayout>
    ),
    children: [
      {
        path: "/login",
        element: <Login />,
      },
    ],
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <AuthProvider>
      <RouterProvider router={router} />
    </AuthProvider>
  </React.StrictMode>
);
