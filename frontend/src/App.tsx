import { useEffect, useState } from 'react';
import { fetchHealth } from './services/healthService';
import { fetchRepos } from './services/githubService';
import { Repo } from './types/github';
import HealthStatus from './components/HealthStatus';
import RepoSearch from './components/RepoSearch';
import RepoList from './components/RepoList';

function App() {
  const [healthStatus, setHealthStatus] = useState<string>('unknown');
  const [isHealthLoading, setIsHealthLoading] = useState<boolean>(false);
  const [healthError, setHealthError] = useState<string | null>(null);

  const [username, setUsername] = useState<string>('');
  const [repos, setRepos] = useState<Repo[]>([]);
  const [isReposLoading, setIsReposLoading] = useState<boolean>(false);
  const [reposError, setReposError] = useState<string | null>(null);

  const loadHealth = async () => {
    try {
      setIsHealthLoading(true);
      setHealthError(null);
      const data = await fetchHealth();
      setHealthStatus(data.status ?? 'unknown');
    } catch (error) {
      setHealthError('Unable to reach backend');
      setHealthStatus('unreachable');
      console.error(error);
    } finally {
      setIsHealthLoading(false);
    }
  };

  useEffect(() => {
    loadHealth();
  }, []);

  const handleSearch = async (value: string) => {
    if (!value.trim()) {
      setRepos([]);
      setReposError('Please enter a GitHub username.');
      return;
    }

    try {
      setUsername(value.trim());
      setIsReposLoading(true);
      setReposError(null);
      const data = await fetchRepos(value.trim());
      setRepos(data);
    } catch (error) {
      setRepos([]);
      setReposError('Failed to load repositories.');
      console.error(error);
    } finally {
      setIsReposLoading(false);
    }
  };

  return (
    <div className="page">
      <header className="page__header">
        <div>
          <p className="eyebrow">GitHub Dashboard</p>
          <h1>Production-ready repository insights</h1>
          <p className="lede">
            Query GitHub in real time through the FastAPI backend. Enter a username to see their public repositories.
          </p>
        </div>
        <div className="badge">Frontend · React · Vite</div>
      </header>

      <main className="page__content">
        <section className="card">
          <div className="section-header">
            <div>
              <p className="eyebrow">Backend</p>
              <h2>Health status</h2>
            </div>
            <button className="ghost" onClick={loadHealth} disabled={isHealthLoading}>
              {isHealthLoading ? 'Checking…' : 'Refresh'}
            </button>
          </div>
          <HealthStatus status={healthStatus} isLoading={isHealthLoading} error={healthError} />
        </section>

        <section className="card">
          <div className="section-header">
            <div>
              <p className="eyebrow">GitHub</p>
              <h2>Repositories</h2>
            </div>
          </div>
          <RepoSearch defaultValue={username} onSearch={handleSearch} isLoading={isReposLoading} />
          <RepoList repos={repos} isLoading={isReposLoading} error={reposError} />
        </section>
      </main>
    </div>
  );
}

export default App;

