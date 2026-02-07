interface Props {
  status: string;
  isLoading: boolean;
  error: string | null;
}

const statusColor: Record<string, string> = {
  ok: 'badge--success',
  unreachable: 'badge--error',
  unknown: 'badge--muted',
};

export default function HealthStatus({ status, isLoading, error }: Props) {
  const normalized = status?.toLowerCase();
  const badgeClass = statusColor[normalized] ?? 'badge--muted';

  return (
    <div className="health">
      <div className={`badge ${badgeClass}`}>
        {isLoading ? 'Checking…' : status}
      </div>
      {error && <p className="error-text">{error}</p>}
      {!error && !isLoading && (
        <p className="muted">Health is pulled from `/health` on the FastAPI backend.</p>
      )}
    </div>
  );
}

