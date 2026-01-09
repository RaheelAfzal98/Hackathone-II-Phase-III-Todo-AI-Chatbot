import { useState, useEffect } from 'react';
import { Task, TaskFormData } from '@/types/Task';
import { apiClient } from '@/services/apiClient';
import useToast from './useToast';

const useTasks = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const { success, error: showError } = useToast();

  // Fetch tasks
  const fetchTasks = async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await apiClient.getAllTasks();

      if (response.success) {
        setTasks(response.data || []);
      } else {
        setError(response.error?.message || 'Failed to fetch tasks');
        showError(response.error?.message || 'Failed to fetch tasks');
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unexpected error occurred');
      showError('Failed to fetch tasks');
    } finally {
      setLoading(false);
    }
  };

  // Create a new task
  const createTask = async (taskData: TaskFormData) => {
    try {
      setLoading(true);
      const response = await apiClient.createTask(taskData);

      if (response.success && response.data) {
        setTasks(prev => [response.data!, ...prev]);
        success('Task created successfully');
        return response.data;
      } else {
        showError(response.error?.message || 'Failed to create task');
        return null;
      }
    } catch (err) {
      showError('Failed to create task');
      return null;
    } finally {
      setLoading(false);
    }
  };

  // Update a task
  const updateTask = async (id: string, taskData: Partial<Task>) => {
    try {
      setLoading(true);
      const response = await apiClient.updateTask(id, taskData);

      if (response.success && response.data) {
        setTasks(prev => prev.map(task => task.id === id ? response.data! : task));
        success('Task updated successfully');
        return response.data;
      } else {
        showError(response.error?.message || 'Failed to update task');
        return null;
      }
    } catch (err) {
      showError('Failed to update task');
      return null;
    } finally {
      setLoading(false);
    }
  };

  // Toggle task completion
  const toggleTaskCompletion = async (id: string) => {
    try {
      setLoading(true);
      const response = await apiClient.toggleTaskCompletion(id);

      if (response.success && response.data) {
        setTasks(prev => prev.map(task =>
          task.id === id ? { ...task, completed: response.data!.completed } : task
        ));
        success(response.data.completed ? 'Task marked as complete' : 'Task marked as incomplete');
        return response.data;
      } else {
        showError(response.error?.message || 'Failed to toggle task completion');
        return null;
      }
    } catch (err) {
      showError('Failed to toggle task completion');
      return null;
    } finally {
      setLoading(false);
    }
  };

  // Delete a task
  const deleteTask = async (id: string) => {
    try {
      setLoading(true);
      const response = await apiClient.deleteTask(id);

      if (response.success) {
        setTasks(prev => prev.filter(task => task.id !== id));
        success('Task deleted successfully');
      } else {
        showError(response.error?.message || 'Failed to delete task');
      }
    } catch (err) {
      showError('Failed to delete task');
    } finally {
      setLoading(false);
    }
  };

  // Filter tasks locally
  const filterTasks = (status: 'all' | 'active' | 'completed', priority: 'all' | 'low' | 'medium' | 'high', search?: string) => {
    return tasks.filter(task => {
      const statusMatch = status === 'all' ||
        (status === 'active' && !task.completed) ||
        (status === 'completed' && task.completed);

      const priorityMatch = priority === 'all' || task.priority === priority;

      const searchMatch = !search || search === '' ||
        task.title.toLowerCase().includes(search.toLowerCase()) ||
        (task.description && task.description.toLowerCase().includes(search.toLowerCase()));

      return statusMatch && priorityMatch && searchMatch;
    });
  };

  // Initialize tasks on mount
  useEffect(() => {
    fetchTasks();
  }, []);

  return {
    tasks,
    loading,
    error,
    fetchTasks,
    createTask,
    updateTask,
    toggleTaskCompletion,
    deleteTask,
    filterTasks,
  };
};

export default useTasks;