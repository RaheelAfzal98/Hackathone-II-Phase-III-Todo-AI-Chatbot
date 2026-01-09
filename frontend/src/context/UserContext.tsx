'use client';

import React, { createContext, useContext, useEffect, useState, ReactNode } from 'react';
import { User } from '@/types/User';
import { authService } from '@/services/authService';

interface UserContextType {
  user: User | null;
  loading: boolean;
  login: (email: string, password: string) => Promise<{ success: boolean; message?: string }>;
  logout: () => Promise<{ success: boolean; message?: string }>;
  register: (name: string, email: string, password: string) => Promise<{ success: boolean; message?: string }>;
}

const UserContext = createContext<UserContextType | undefined>(undefined);

interface UserProviderProps {
  children: ReactNode;
}

export const UserProvider: React.FC<UserProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if user is already logged in from previous session
    const currentUser = authService.getCurrentUser();
    setUser(currentUser);
    setLoading(false);

    // Set up event listeners or other initialization if needed
  }, []);

  const login = async (email: string, password: string) => {
    try {
      const result = await authService.login({ email, password });
      if (result.success && result.user) {
        setUser(result.user);
      }
      return result;
    } catch (error) {
      console.error('Login error:', error);
      return { success: false, message: 'An unexpected error occurred during login' };
    }
  };

  const logout = async () => {
    try {
      const result = await authService.logout();
      if (result.success) {
        setUser(null);
      }
      return result;
    } catch (error) {
      console.error('Logout error:', error);
      return { success: false, message: 'An unexpected error occurred during logout' };
    }
  };

  const register = async (name: string, email: string, password: string) => {
    try {
      const result = await authService.register({ name, email, password });
      if (result.success && result.user) {
        setUser(result.user);
      }
      return result;
    } catch (error) {
      console.error('Registration error:', error);
      return { success: false, message: 'An unexpected error occurred during registration' };
    }
  };

  const value = {
    user,
    loading,
    login,
    logout,
    register,
  };

  return <UserContext.Provider value={value}>{children}</UserContext.Provider>;
};

export const useUser = () => {
  const context = useContext(UserContext);
  if (context === undefined) {
    throw new Error('useUser must be used within a UserProvider');
  }
  return context;
};