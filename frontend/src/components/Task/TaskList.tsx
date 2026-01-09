import React from 'react';
import { Task } from '@/types/Task';
import TaskCard from './TaskCard';
import SkeletonLoader from '../UI/SkeletonLoader';

interface TaskListProps {
  tasks: Task[];
  loading?: boolean;
  emptyMessage?: string;
  statusFilter?: 'all' | 'active' | 'completed';
  priorityFilter?: 'all' | 'low' | 'medium' | 'high';
  searchQuery?: string;
  onToggleComplete: (id: string) => void;
  onDelete: (id: string) => void;
  onEdit: (task: Task) => void;
}

const TaskList: React.FC<TaskListProps> = ({
  tasks,
  loading = false,
  emptyMessage = 'No tasks found',
  statusFilter = 'all',
  priorityFilter = 'all',
  searchQuery = '',
  onToggleComplete,
  onDelete,
  onEdit
}) => {
  // Apply filters
  const filteredTasks = tasks.filter(task => {
    const statusMatch = statusFilter === 'all' ||
      (statusFilter === 'active' && !task.completed) ||
      (statusFilter === 'completed' && task.completed);

    const priorityMatch = priorityFilter === 'all' || task.priority === priorityFilter;

    const searchMatch = !searchQuery || searchQuery === '' ||
      task.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      (task.description && task.description.toLowerCase().includes(searchQuery.toLowerCase()));

    return statusMatch && priorityMatch && searchMatch;
  });

  if (loading) {
    return (
      <div className="space-y-4">
        {[...Array(3)].map((_, index) => (
          <SkeletonLoader key={index} className="h-20 w-full" />
        ))}
      </div>
    );
  }

  if (filteredTasks.length === 0) {
    return (
      <div className="text-center py-12">
        <svg
          className="mx-auto h-12 w-12 text-gray-400"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          aria-hidden="true"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
          />
        </svg>
        <h3 className="mt-2 text-sm font-medium text-gray-900">{emptyMessage}</h3>
        <p className="mt-1 text-sm text-gray-500">
          Get started by creating a new task.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {filteredTasks.map(task => (
        <div
          key={task.id}
          className="animate-fadeInSlideIn"
        >
          <TaskCard
            task={task}
            onToggleComplete={onToggleComplete}
            onDelete={onDelete}
            onEdit={onEdit}
          />
        </div>
      ))}
    </div>
  );
};

export default TaskList;