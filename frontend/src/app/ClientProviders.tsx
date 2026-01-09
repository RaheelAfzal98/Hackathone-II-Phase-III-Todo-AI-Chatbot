'use client';

import { UserProvider } from '@/context/UserContext';
import { AuthProvider } from 'better-auth/react';
import React, { ReactNode } from 'react';

export default function ClientProviders({ children }: { children: ReactNode }) {
  return (
    <AuthProvider>
      <UserProvider>
        {children}
      </UserProvider>
    </AuthProvider>
  );
}