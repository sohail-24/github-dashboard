import { FormEvent, useState } from 'react';

interface Props {
  defaultValue?: string;
  isLoading: boolean;
  onSearch: (username: string) => void;
}

export default function RepoSearch({ defaultValue = '', isLoading, onSearch }: Props) {
  const [value, setValue] = useState<string>(defaultValue);

  const handleSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    onSearch(value);
  };

  return (
    <form className="search" onSubmit={handleSubmit}>
      <div className="input-group">
        <label htmlFor="username">GitHub username</label>
        <div className="input-row">
          <input
            id="username"
            name="username"
            type="text"
            placeholder="e.g. sohail-24"
            value={value}
            onChange={(e) => setValue(e.target.value)}
            autoComplete="off"
          />
          <button type="submit" disabled={isLoading}>
            {isLoading ? 'Loading…' : 'Fetch repos'}
          </button>
        </div>
      </div>
      <p className="muted small">Data is served via `/github/repos?username=` on the backend.</p>
    </form>
  );
}

