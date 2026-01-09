'use client';

import React, { useState, useEffect } from 'react';
import { Task, TaskFormData } from '@/types/Task';
import { validateTask } from '../utils/validation';
import Input from '../UI/Input';
import Button from '../UI/Button';

interface TaskFormProps {
  initialData?: Partial<Task> | TaskFormData;
  onSubmit: (taskData: TaskFormData) => void;
  onCancel?: () => void;
  submitText?: string;
}

const TaskForm: React.FC<TaskFormProps> = ({
  initialData = { title: '', description: '', priority: 'medium' },
  onSubmit,
  onCancel,
  submitText = 'Add Task'
}) => {
  const [formData, setFormData] = useState<TaskFormData>({
    title: initialData?.title || '',
    description: initialData?.description || '',
    priority: initialData?.priority || 'medium'
  });
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  useEffect(() => {
    setFormData({
      title: initialData?.title || '',
      description: initialData?.description || '',
      priority: initialData?.priority || 'medium'
    });
    setErrors({});
  }, [initialData]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));

    // Clear error when user starts typing
    if (errors[name]) {
      setErrors(prev => {
        const newErrors = { ...prev };
        delete newErrors[name];
        return newErrors;
      });
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Validate form
    const validationErrors = validateTask(formData.title, formData.description, formData.priority);
    setErrors(validationErrors);

    if (Object.keys(validationErrors).length === 0) {
      setIsSubmitting(true);
      try {
        await onSubmit(formData);
        // Reset form after successful submission
        if (!(initialData as any)?.id) { // Only reset for new tasks, not updates
          setFormData({ title: '', description: '', priority: 'medium' });
        }
      } catch (error) {
        console.error('Error submitting task:', error);
      } finally {
        setIsSubmitting(false);
      }
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <Input
          id="title"
          name="title"
          label="Task Title *"
          value={formData.title}
          onChange={handleChange}
          required
          error={errors.title}
          placeholder="Enter task title"
        />
      </div>

      <div>
        <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-1">
          Description
        </label>
        <textarea
          id="description"
          name="description"
          value={formData.description}
          onChange={handleChange}
          rows={3}
          className="block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500 sm:text-sm"
          placeholder="Enter task description (optional)"
        />
        {errors.description && <p className="mt-1 text-sm text-red-600">{errors.description}</p>}
      </div>

      <div>
        <label htmlFor="priority" className="block text-sm font-medium text-gray-700 mb-1">
          Priority *
        </label>
        <select
          id="priority"
          name="priority"
          value={formData.priority}
          onChange={handleChange}
          className="block w-full rounded-md border-gray-300 shadow-sm focus:border-primary-500 focus:ring-primary-500 sm:text-sm"
          required
        >
          <option value="low">Low</option>
          <option value="medium">Medium</option>
          <option value="high">High</option>
        </select>
        {errors.priority && <p className="mt-1 text-sm text-red-600">{errors.priority}</p>}
      </div>

      <div className="flex space-x-3 pt-2">
        <Button
          type="submit"
          isLoading={isSubmitting}
          disabled={isSubmitting}
        >
          {submitText}
        </Button>

        {onCancel && (
          <Button
            type="button"
            variant="secondary"
            onClick={onCancel}
            disabled={isSubmitting}
          >
            Cancel
          </Button>
        )}
      </div>
    </form>
  );
};

export default TaskForm;