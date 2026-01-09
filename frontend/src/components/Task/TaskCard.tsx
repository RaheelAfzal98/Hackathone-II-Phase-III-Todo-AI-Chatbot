'use client';

import React, { useState } from 'react';
import { Task } from '@/types/Task';
import Button from '../UI/Button';
import Modal from '../UI/Modal';

interface TaskCardProps {
  task: Task;
  onToggleComplete: (id: string) => void;
  onDelete: (id: string) => void;
  onEdit: (task: Task) => void;
}

const TaskCard: React.FC<TaskCardProps> = ({ task, onToggleComplete, onDelete, onEdit }) => {
  const [showConfirmDialog, setShowConfirmDialog] = useState(false);

  const handleToggleComplete = () => {
    onToggleComplete(task.id);
  };

  const handleDeleteClick = () => {
    setShowConfirmDialog(true);
  };

  const handleConfirmDelete = () => {
    onDelete(task.id);
    setShowConfirmDialog(false);
  };

  const handleCancelDelete = () => {
    setShowConfirmDialog(false);
  };

  const handleEdit = () => {
    onEdit(task);
  };

  // Determine priority color
  const priorityColors = {
    low: 'border-l-green-500',
    medium: 'border-l-yellow-500',
    high: 'border-l-red-500',
  };

  return (
    <>
      <div
        className={`relative bg-white rounded-lg shadow-md p-4 mb-3 border-l-4 ${priorityColors[task.priority]} transition-all duration-300 ${
          task.completed ? 'opacity-70 bg-gray-50' : 'opacity-100'
        }`}
      >
        <div className="flex items-start">
          <input
            type="checkbox"
            checked={task.completed}
            onChange={handleToggleComplete}
            className="mt-1 h-5 w-5 rounded border-gray-300 text-primary-600 focus:ring-primary-500"
            aria-label={`Mark task "${task.title}" as ${task.completed ? 'incomplete' : 'complete'}`}
          />
          <div className="ml-3 flex-1 min-w-0">
            <h3
              className={`text-lg font-medium ${
                task.completed ? 'line-through text-gray-500' : 'text-gray-900'
              }`}
            >
              {task.title}
            </h3>
            {task.description && (
              <p className={`mt-1 text-sm ${
                task.completed ? 'line-through text-gray-400' : 'text-gray-500'
              }`}>
                {task.description}
              </p>
            )}
            <div className="mt-2 flex items-center">
              <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium ${
                task.priority === 'high'
                  ? 'bg-red-100 text-red-800'
                  : task.priority === 'medium'
                    ? 'bg-yellow-100 text-yellow-800'
                    : 'bg-green-100 text-green-800'
              }`}>
                {task.priority.charAt(0).toUpperCase() + task.priority.slice(1)} priority
              </span>
              <span className="ml-2 text-xs text-gray-500">
                {new Date(task.createdAt).toLocaleDateString()}
              </span>
            </div>
          </div>
          <div className="ml-4 flex space-x-2">
            <Button
              variant="ghost"
              size="sm"
              onClick={handleEdit}
              aria-label={`Edit task "${task.title}"`}
            >
              <svg className="h-5 w-5 text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
              </svg>
            </Button>
            <Button
              variant="danger"
              size="sm"
              onClick={handleDeleteClick}
              aria-label={`Delete task "${task.title}"`}
            >
              <svg className="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
            </Button>
          </div>
        </div>
      </div>

      {/* Confirmation Dialog */}
      <Modal
        isOpen={showConfirmDialog}
        onClose={handleCancelDelete}
        title="Confirm Deletion"
      >
        <div className="mt-2">
          <p className="text-gray-700">
            Are you sure you want to delete the task <strong>"{task.title}"</strong>?
          </p>
          <p className="text-gray-500 mt-2">
            This action cannot be undone.
          </p>
        </div>

        <div className="mt-6 flex justify-end space-x-3">
          <Button
            variant="secondary"
            onClick={handleCancelDelete}
          >
            Cancel
          </Button>
          <Button
            variant="danger"
            onClick={handleConfirmDelete}
          >
            Delete
          </Button>
        </div>
      </Modal>
    </>
  );
};

export default TaskCard;