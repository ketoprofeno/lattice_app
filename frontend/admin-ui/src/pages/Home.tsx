import { VisitorsChart } from "@/components/dashboard/VisitorsChart"

export function Home() {
  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <p className="text-muted-foreground">
          Bienvenido a Lattice Admin
        </p>
      </div>

      {/* Cards métricas */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        {/* decirme si quieres que te deje estas cards listas */}
      </div>

      {/* Chart */}
      <div>
        <h2 className="mb-2 text-lg font-semibold">Total Visitors</h2>
        <p className="mb-4 text-sm text-muted-foreground">
          Últimos 7 días
        </p>

        <VisitorsChart />
      </div>
    </div>
  )
}
