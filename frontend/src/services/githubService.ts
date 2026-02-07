import { apiClient } from './apiClient';
import { Repo } from '../types/github';

export async function fetchRepos(username: string): Promise<Repo[]> {
  return apiClient.get<Repo[]>('/github/repos', {
    query: { username },
  });
}

