'use client';

import React, { useEffect, useState } from 'react';
import { useUser } from '@/context/UserContext';
import ChatInterface from '@/components/ChatInterface';
import DashboardLayout from '@/components/Layout/DashboardLayout';
import { useRouter } from 'next/navigation';

const ChatPage: React.FC = () => {
  const { user, loading: userLoading } = useUser();
  const router = useRouter();

  // Redirect to login if not authenticated
  useEffect(() => {
    if (!userLoading && !user) {
      router.push('/login');
    }
  }, [user, userLoading, router]);

  if (userLoading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading...</p>
        </div>
      </div>
    );
  }

  if (!user) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50 flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">Please log in to access the AI Chatbot</h2>
          <p className="text-gray-600">Redirecting to login...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-50">
      <DashboardLayout title="AI Task Assistant">
        <div className="max-w-4xl mx-auto p-6">
          <div className="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
            <div className="p-6 border-b border-gray-200 bg-gradient-to-r from-indigo-50 to-blue-50">
              <h1 className="text-2xl font-bold text-gray-900 flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 mr-3 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
                AI Task Assistant
              </h1>
              <p className="text-gray-600 mt-2">Manage your tasks with natural language commands</p>
            </div>
            <div className="p-4 h-[calc(100vh-280px)] flex flex-col">
              <ChatInterface userId={user.id} />
            </div>
          </div>

          <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="bg-white p-6 rounded-xl shadow-md border border-gray-200">
              <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2 text-green-500" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                Examples
              </h3>
              <ul className="text-sm text-gray-600 space-y-2">
                <li className="flex items-start">
                  <span className="text-indigo-500 mr-2">•</span>
                  "Add a task to buy groceries"
                </li>
                <li className="flex items-start">
                  <span className="text-indigo-500 mr-2">•</span>
                  "Show me all my tasks"
                </li>
                <li className="flex items-start">
                  <span className="text-indigo-500 mr-2">•</span>
                  "Mark task 3 as complete"
                </li>
              </ul>
            </div>

            <div className="bg-white p-6 rounded-xl shadow-md border border-gray-200">
              <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2 text-blue-500" viewBox="0 0 20 20" fill="currentColor">
                  <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                </svg>
                Commands
              </h3>
              <ul className="text-sm text-gray-600 space-y-2">
                <li className="flex items-start">
                  <span className="text-indigo-500 mr-2">•</span>
                  "List pending tasks"
                </li>
                <li className="flex items-start">
                  <span className="text-indigo-500 mr-2">•</span>
                  "Update task 1 to 'Call mom'"
                </li>
                <li className="flex items-start">
                  <span className="text-indigo-500 mr-2">•</span>
                  "Delete the meeting task"
                </li>
              </ul>
            </div>

            <div className="bg-white p-6 rounded-xl shadow-md border border-gray-200">
              <h3 className="font-semibold text-gray-800 mb-3 flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2 text-purple-500" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
                </svg>
                Tips
              </h3>
              <ul className="text-sm text-gray-600 space-y-2">
                <li className="flex items-start">
                  <span className="text-indigo-500 mr-2">•</span>
                  Be specific with task IDs
                </li>
                <li className="flex items-start">
                  <span className="text-indigo-500 mr-2">•</span>
                  Use clear language
                </li>
                <li className="flex items-start">
                  <span className="text-indigo-500 mr-2">•</span>
                  Ask for help anytime
                </li>
              </ul>
            </div>
          </div>
        </div>
      </DashboardLayout>
    </div>
  );
};

export default ChatPage;