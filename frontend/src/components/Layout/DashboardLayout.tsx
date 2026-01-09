import React, { ReactNode } from 'react';
import Header from './Header';

interface DashboardLayoutProps {
  children: ReactNode;
  title?: string;
}

const DashboardLayout: React.FC<DashboardLayoutProps> = ({ children, title }) => {
  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main>
        <div className="mx-auto max-w-7xl py-6 sm:px-6 lg:px-8">
          {title && (
            <div className="mb-6">
              <h2 className="text-2xl font-semibold text-gray-800">{title}</h2>
            </div>
          )}
          <div className="px-4 py-6 sm:px-0">
            <div className="h-full rounded-lg border-4 border-dashed border-gray-200">
              {children}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default DashboardLayout;