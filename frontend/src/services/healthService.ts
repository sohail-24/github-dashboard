import { apiClient } from './apiClient';
import { HealthResponse } from '../types/github';

export async function fetchHealth(): Promise<HealthResponse> {
  return apiClient.get<HealthResponse>('/health');
}

