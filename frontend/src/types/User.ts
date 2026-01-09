export interface User {
  id: string;
  email: string;
  name?: string;
  isLoggedIn: boolean;
  jwtToken?: string;
  refreshToken?: string;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface RegisterCredentials {
  email: string;
  password: string;
  name?: string;
}