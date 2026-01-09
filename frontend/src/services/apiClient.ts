import { Task, TaskFormData } from '@/types/Task';
import { ApiResponse, ErrorResponse } from '@/types/ApiResponse';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000/api';

class ApiClient {
  private baseUrl: string;

  constructor() {
    this.baseUrl = API_BASE_URL;
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<ApiResponse<T>> {
    const url = `${this.baseUrl}${endpoint}`;

    const defaultHeaders = {
      'Content-Type': 'application/json',
    };

    const config: RequestInit = {
      ...options,
      headers: {
        ...defaultHeaders,
        ...options.headers,
      },
    };

    // Add JWT token if available
    const token = typeof window !== 'undefined' ? localStorage.getItem('jwt_token') : null;
    if (token && config.headers) {
      (config.headers as Record<string, string>)['Authorization'] = `Bearer ${token}`;
    }

    try {
      const response = await fetch(url, config);

      if (!response.ok) {
        // Handle different status codes appropriately
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.message || `API request failed with status ${response.status}`);
      }

      const data = await response.json();

      return {
        success: true,
        data,
        message: data.message,
      };
    } catch (error) {
      console.error('API request error:', error);
      return {
        success: false,
        message: error instanceof Error ? error.message : 'Unknown error occurred',
      };
    }
  }

  async getAllTasks(): Promise<ApiResponse<Task[]>> {
    // Get user ID from localStorage or session
    const userId = typeof window !== 'undefined' ? localStorage.getItem('user_id') : null;
    if (!userId) {
      return {
        success: false,
        message: 'User not authenticated'
      };
    }
    return this.request<Task[]>(`/${userId}`, { method: 'GET' });
  }

  async createTask(taskData: TaskFormData): Promise<ApiResponse<Task>> {
    const userId = typeof window !== 'undefined' ? localStorage.getItem('user_id') : null;
    if (!userId) {
      return {
        success: false,
        message: 'User not authenticated'
      };
    }
    return this.request<Task>(`/${userId}`, {
      method: 'POST',
      body: JSON.stringify({
        title: taskData.title,
        description: taskData.description,
        completed: taskData.completed || false
      }),
    });
  }

  async updateTask(id: string, taskData: Partial<Task>): Promise<ApiResponse<Task>> {
    const userId = typeof window !== 'undefined' ? localStorage.getItem('user_id') : null;
    if (!userId) {
      return {
        success: false,
        message: 'User not authenticated'
      };
    }
    return this.request<Task>(`/${userId}/${id}`, {
      method: 'PUT',
      body: JSON.stringify(taskData),
    });
  }

  async toggleTaskCompletion(id: string): Promise<ApiResponse<{ id: string; completed: boolean }>> {
    const userId = typeof window !== 'undefined' ? localStorage.getItem('user_id') : null;
    if (!userId) {
      return {
        success: false,
        message: 'User not authenticated'
      };
    }
    return this.request<{ id: string; completed: boolean }>(`/${userId}/${id}/toggle`, {
      method: 'PATCH',
    });
  }

  async deleteTask(id: string): Promise<ApiResponse<void>> {
    const userId = typeof window !== 'undefined' ? localStorage.getItem('user_id') : null;
    if (!userId) {
      return {
        success: false,
        message: 'User not authenticated'
      };
    }
    return this.request<void>(`/${userId}/${id}`, { method: 'DELETE' });
  }

  async filterTasks(
    status?: 'all' | 'active' | 'completed',
    priority?: 'all' | 'low' | 'medium' | 'high',
    search?: string
  ): Promise<ApiResponse<Task[]>> {
    const userId = typeof window !== 'undefined' ? localStorage.getItem('user_id') : null;
    if (!userId) {
      return {
        success: false,
        message: 'User not authenticated'
      };
    }

    // Build query parameters
    const queryParams = new URLSearchParams();
    if (status && status !== 'all') queryParams.append('status', status);
    if (priority && priority !== 'all') queryParams.append('priority', priority);
    if (search) queryParams.append('search', search);

    const queryString = queryParams.toString();
    const endpoint = queryString ? `/${userId}?${queryString}` : `/${userId}`;

    return this.request<Task[]>(endpoint, { method: 'GET' });
  }
}

export const apiClient = new ApiClient();