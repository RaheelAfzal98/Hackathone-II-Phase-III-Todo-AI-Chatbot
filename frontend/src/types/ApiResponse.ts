export interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  message?: string;
  error?: {
    code: string;
    message: string;
    details?: Record<string, any>;
  };
}

export interface ErrorDetails {
  code: string;
  message: string;
  details?: Record<string, any>;
}

export interface ErrorResponse {
  success: boolean;
  error: ErrorDetails;
}