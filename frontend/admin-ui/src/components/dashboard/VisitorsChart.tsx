import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts"

export function VisitorsChart() {
  const data = [
    { month: "Ene", visitors: 120 },
    { month: "Feb", visitors: 210 },
    { month: "Mar", visitors: 180 },
    { month: "Abr", visitors: 260 },
    { month: "May", visitors: 300 },
    { month: "Jun", visitors: 280 },
  ]

  return (
    <div className="h-[300px] w-full">
      <ResponsiveContainer width="100%" height="100%">
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" className="stroke-muted" />
          <XAxis
            dataKey="month"
            stroke="hsl(var(--muted-foreground))"
          />
          <YAxis stroke="hsl(var(--muted-foreground))" />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="visitors"
            stroke="hsl(var(--primary))"
            strokeWidth={2}
            dot={{ r: 4 }}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  )
}
