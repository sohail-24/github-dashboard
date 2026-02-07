export interface Repo {
  name: string;
  stars?: number;
  language?: string | null;
  url: string;
  description?: string | null;
  forks?: number;
}

export interface HealthResponse {
  status: string;
}

