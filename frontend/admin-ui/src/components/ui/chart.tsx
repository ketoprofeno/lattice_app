import { ResponsiveContainer } from "recharts"

export function ChartContainer({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <div className="rounded-xl bg-card p-4 shadow-sm">
      <ResponsiveContainer width="100%" height={300}>
        {children}
      </ResponsiveContainer>
    </div>
  )
}
