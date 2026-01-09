import { User, LoginCredentials, RegisterCredentials } from '@/types/User';
import { signIn, signOut, signUp, getSession } from '@better-auth/client';

class AuthService {
  private user: User | null = null;

  constructor() {
    // Check if user is already logged in from previous session
    const storedUser = typeof window !== 'undefined' ? localStorage.getItem('user') : null;
    if (storedUser) {
      this.user = JSON.parse(storedUser);
    }
  }

  async login(credentials: LoginCredentials): Promise<{ success: boolean; user?: User; message?: string }> {
    try {
      // Call Better Auth login API
      const response = await signIn.email({
        email: credentials.email,
        password: credentials.password,
        redirect: false,
      });

      if (response?.error) {
        return {
          success: false,
          message: response.error.message || 'Login failed'
        };
      }

      // Get the current user after successful login
      const currentUser = await getSession();

      if (currentUser) {
        const betterUser = currentUser.user;

        // Create our User object
        const user: User = {
          id: betterUser.id,
          email: betterUser.email,
          name: betterUser.name || betterUser.email.split('@')[0],
          isLoggedIn: true,
          jwtToken: currentUser.accessToken || '',
          refreshToken: currentUser.refreshToken || ''
        };

        // Store user and token in localStorage
        if (typeof window !== 'undefined') {
          localStorage.setItem('user', JSON.stringify(user));
          localStorage.setItem('user_id', user.id); // Store user ID for API calls
          localStorage.setItem('jwt_token', user.jwtToken || '');
        }

        this.user = user;

        return {
          success: true,
          user: user,
          message: 'Login successful'
        };
      } else {
        return {
          success: false,
          message: 'Login failed - unable to retrieve user session'
        };
      }
    } catch (error) {
      console.error('Login error:', error);
      return {
        success: false,
        message: 'Login failed. Please check your credentials.'
      };
    }
  }

  async register(credentials: RegisterCredentials): Promise<{ success: boolean; user?: User; message?: string }> {
    try {
      // Call Better Auth register API
      const response = await signUp.email({
        email: credentials.email,
        password: credentials.password,
        name: credentials.name,
      });

      if (response?.error) {
        return {
          success: false,
          message: response.error.message || 'Registration failed'
        };
      }

      // Get the current user after successful registration
      const currentUser = await getSession();

      if (currentUser) {
        const betterUser = currentUser.user;

        // Create our User object
        const user: User = {
          id: betterUser.id,
          email: betterUser.email,
          name: betterUser.name || betterUser.email.split('@')[0],
          isLoggedIn: true,
          jwtToken: currentUser.accessToken || '',
          refreshToken: currentUser.refreshToken || ''
        };

        // Store user and token in localStorage
        if (typeof window !== 'undefined') {
          localStorage.setItem('user', JSON.stringify(user));
          localStorage.setItem('user_id', user.id); // Store user ID for API calls
          localStorage.setItem('jwt_token', user.jwtToken || '');
        }

        this.user = user;

        return {
          success: true,
          user: user,
          message: 'Registration successful'
        };
      } else {
        return {
          success: false,
          message: 'Registration failed - unable to retrieve user session'
        };
      }
    } catch (error) {
      console.error('Registration error:', error);
      return {
        success: false,
        message: 'Registration failed. Please try again.'
      };
    }
  }

  async logout(): Promise<{ success: boolean; message?: string }> {
    try {
      // Call Better Auth logout API
      await signOut({ redirect: false });

      // Clear user data from localStorage
      if (typeof window !== 'undefined') {
        localStorage.removeItem('user');
        localStorage.removeItem('user_id');
        localStorage.removeItem('jwt_token');
      }

      this.user = null;

      return {
        success: true,
        message: 'Logged out successfully'
      };
    } catch (error) {
      console.error('Logout error:', error);
      return {
        success: false,
        message: 'Logout failed'
      };
    }
  }

  getCurrentUser(): User | null {
    return this.user;
  }

  isAuthenticated(): boolean {
    return this.user?.isLoggedIn ?? false;
  }

  // Method to refresh token if needed
  async refreshToken(): Promise<boolean> {
    try {
      const refreshedSession = await getSession();
      if (refreshedSession) {
        const betterUser = refreshedSession.user;
        const user: User = {
          id: betterUser.id,
          email: betterUser.email,
          name: betterUser.name || betterUser.email.split('@')[0],
          isLoggedIn: true,
          jwtToken: refreshedSession.accessToken || '',
          refreshToken: refreshedSession.refreshToken || ''
        };

        // Update stored user
        if (typeof window !== 'undefined') {
          localStorage.setItem('user', JSON.stringify(user));
          localStorage.setItem('user_id', user.id);
          localStorage.setItem('jwt_token', user.jwtToken || '');
        }

        this.user = user;
        return true;
      }
      return false;
    } catch (error) {
      console.error('Token refresh error:', error);
      return false;
    }
  }
}

export const authService = new AuthService();