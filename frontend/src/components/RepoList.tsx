import { Repo } from '../types/github';

interface Props {
  repos: Repo[];
  isLoading: boolean;
  error: string | null;
}

export default function RepoList({ repos, isLoading, error }: Props) {
  if (isLoading) {
    return <p className="muted">Loading repositories…</p>;
  }

  if (error) {
    return <p className="error-text">{error}</p>;
  }

  if (!repos.length) {
    return <p className="muted">No repositories loaded yet.</p>;
  }

  return (
    <div className="table">
      <div className="table__head">
        <div>Name</div>
        <div>Language</div>
        <div>Stars</div>
        <div>Forks</div>
        <div>Description</div>
      </div>
      <div className="table__body">
        {repos.map((repo) => (
          <div className="table__row" key={repo.name}>
            <div>
              <a href={repo.url} target="_blank" rel="noreferrer" className="repo-link">
                {repo.name}
              </a>
            </div>
            <div>{repo.language ?? '—'}</div>
            <div>{repo.stars ?? '—'}</div>
            <div>{repo.forks ?? '—'}</div>
            <div className="muted truncate">{repo.description ?? '—'}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

