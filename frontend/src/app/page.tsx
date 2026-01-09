'use client';

import React, { useState } from 'react';
import Head from 'next/head';
import DashboardLayout from '@/components/Layout/DashboardLayout';
import TaskList from '@/components/Task/TaskList';
import TaskForm from '@/components/Task/TaskForm';
import TaskFilters from '@/components/Task/TaskFilters';
import Button from '@/components/UI/Button';
import useTasks from '@/components/hooks/useTasks';
import Toast from '@/components/UI/Toast';
import { TaskFormData, FilterState } from '@/types/Task';

const Dashboard: React.FC = () => {
  const { tasks, loading, error, createTask, toggleTaskCompletion, deleteTask, fetchTasks } = useTasks();
  const [showForm, setShowForm] = useState(false);
  const [filterState, setFilterState] = useState<FilterState>({
    statusFilter: 'all',
    priorityFilter: 'all',
    searchQuery: '',
  });
  const [toast, setToast] = useState({
    show: false,
    message: '',
    type: 'success' as 'success' | 'error' | 'info' | 'warning',
  });

  const handleCreateTask = async (taskData: TaskFormData) => {
    const result = await createTask(taskData);
    if (result) {
      setShowForm(false);
      setToast({
        show: true,
        message: 'Task created successfully!',
        type: 'success',
      });
    }
  };

  const handleToggleComplete = async (id: string) => {
    await toggleTaskCompletion(id);
  };

  const handleDeleteTask = async (id: string) => {
    await deleteTask(id);
  };

  const handleEditTask = (task: any) => {
    // For now, we'll just show the form to create a new task
    // In a real implementation, we would populate the form with the task data
    console.log('Edit task:', task);
  };

  const handleFilterChange = (filters: Partial<FilterState>) => {
    setFilterState(prev => ({
      ...prev,
      ...filters
    }));
  };

  const handleClearFilters = () => {
    setFilterState({
      statusFilter: 'all',
      priorityFilter: 'all',
      searchQuery: '',
    });
  };

  const handleToastClose = () => {
    setToast({ ...toast, show: false });
  };

  return (
    <div>
      <Head>
        <title>Todo Dashboard</title>
        <meta name="description" content="Manage your tasks efficiently" />
      </Head>

      <DashboardLayout title="Task Dashboard">
        <div className="mb-6">
          <Button
            variant="primary"
            onClick={() => setShowForm(!showForm)}
          >
            {showForm ? 'Cancel' : 'Add New Task'}
          </Button>
        </div>

        {showForm && (
          <div className="mb-8 bg-white p-6 rounded-lg shadow-md">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Create New Task</h3>
            <TaskForm
              onSubmit={handleCreateTask}
              onCancel={() => setShowForm(false)}
              submitText="Create Task"
            />
          </div>
        )}

        <TaskFilters
          filterState={filterState}
          onFilterChange={handleFilterChange}
          onClearFilters={handleClearFilters}
        />

        <div className="bg-white shadow rounded-lg p-6">
          <h2 className="text-xl font-semibold text-gray-800 mb-4">Your Tasks</h2>

          {error && (
            <div className="mb-4 p-4 bg-red-50 text-red-700 rounded-md">
              {error}
            </div>
          )}

          <TaskList
            tasks={tasks}
            loading={loading}
            emptyMessage="No tasks yet. Create your first task!"
            statusFilter={filterState.statusFilter}
            priorityFilter={filterState.priorityFilter}
            searchQuery={filterState.searchQuery}
            onToggleComplete={handleToggleComplete}
            onDelete={handleDeleteTask}
            onEdit={handleEditTask}
          />
        </div>
      </DashboardLayout>

      <Toast
        show={toast.show}
        message={toast.message}
        type={toast.type}
        onClose={handleToastClose}
      />
    </div>
  );
};

export default Dashboard;