import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import { SWRConfig } from 'swr';
import Dashboard from '@/src/pages/index'; // Adjust import based on your setup

// Mock the useTasks hook
jest.mock('@/components/hooks/useTasks', () => ({
  __esModule: true,
  default: () => ({
    tasks: [
      {
        id: '1',
        title: 'Test Task',
        description: 'Test Description',
        completed: false,
        priority: 'medium',
        createdAt: '2023-01-01T00:00:00Z',
        updatedAt: '2023-01-01T00:00:00Z',
      }
    ],
    loading: false,
    error: null,
    createTask: jest.fn(),
    toggleTaskCompletion: jest.fn(),
    deleteTask: jest.fn(),
    fetchTasks: jest.fn(),
  })
}));

describe('Dashboard Integration', () => {
  it('renders task list with tasks', async () => {
    render(
      <SWRConfig value={{ provider: () => new Map() }}>
        <Dashboard />
      </SWRConfig>
    );

    await waitFor(() => {
      expect(screen.getByText('Test Task')).toBeInTheDocument();
      expect(screen.getByText('Test Description')).toBeInTheDocument();
    });
  });

  it('displays loading state when tasks are loading', () => {
    // Re-mock with loading state
    jest.mock('@/components/hooks/useTasks', () => ({
      __esModule: true,
      default: () => ({
        tasks: [],
        loading: true,
        error: null,
        createTask: jest.fn(),
        toggleTaskCompletion: jest.fn(),
        deleteTask: jest.fn(),
        fetchTasks: jest.fn(),
      })
    }));

    render(
      <SWRConfig value={{ provider: () => new Map() }}>
        <Dashboard />
      </SWRConfig>
    );

    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });

  it('displays error message when there is an error', () => {
    // Re-mock with error state
    jest.mock('@/components/hooks/useTasks', () => ({
      __esModule: true,
      default: () => ({
        tasks: [],
        loading: false,
        error: 'Failed to fetch tasks',
        createTask: jest.fn(),
        toggleTaskCompletion: jest.fn(),
        deleteTask: jest.fn(),
        fetchTasks: jest.fn(),
      })
    }));

    render(
      <SWRConfig value={{ provider: () => new Map() }}>
        <Dashboard />
      </SWRConfig>
    );

    expect(screen.getByText('Failed to fetch tasks')).toBeInTheDocument();
  });

  it('renders the add new task button', () => {
    render(
      <SWRConfig value={{ provider: () => new Map() }}>
        <Dashboard />
      </SWRConfig>
    );

    expect(screen.getByText('Add New Task')).toBeInTheDocument();
  });

  it('renders the task filters component', () => {
    render(
      <SWRConfig value={{ provider: () => new Map() }}>
        <Dashboard />
      </SWRConfig>
    );

    expect(screen.getByText('Status')).toBeInTheDocument();
    expect(screen.getByText('Priority')).toBeInTheDocument();
    expect(screen.getByPlaceholderText('Search tasks...')).toBeInTheDocument();
  });
});