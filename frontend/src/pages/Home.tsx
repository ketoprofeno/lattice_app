import { useEffect, useState } from "react";
import { getHealth } from "../services/api";

export function Home() {
  const [status, setStatus] = useState("loading");

  useEffect(() => {
    getHealth().then(r => setStatus(r.status));
  }, []);

  return <div>Backend status: {status}</div>;
}
