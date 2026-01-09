import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import TaskForm from '@/components/Task/TaskForm';
import { TaskFormData } from '@/types/Task';

describe('TaskForm', () => {
  const mockOnSubmit = jest.fn();
  const mockOnCancel = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('renders form fields correctly', () => {
    render(
      <TaskForm
        onSubmit={mockOnSubmit}
        onCancel={mockOnCancel}
      />
    );

    expect(screen.getByLabelText('Task Title *')).toBeInTheDocument();
    expect(screen.getByLabelText('Description')).toBeInTheDocument();
    expect(screen.getByLabelText('Priority *')).toBeInTheDocument();
    expect(screen.getByText('Add Task')).toBeInTheDocument();
  });

  it('allows user to input task details', () => {
    render(
      <TaskForm
        onSubmit={mockOnSubmit}
        onCancel={mockOnCancel}
      />
    );

    const titleInput = screen.getByLabelText('Task Title *');
    const descriptionTextarea = screen.getByLabelText('Description');
    const prioritySelect = screen.getByLabelText('Priority *');

    fireEvent.change(titleInput, { target: { value: 'New Task' } });
    fireEvent.change(descriptionTextarea, { target: { value: 'Task description' } });
    fireEvent.change(prioritySelect, { target: { value: 'high' } });

    expect(titleInput).toHaveValue('New Task');
    expect(descriptionTextarea).toHaveValue('Task description');
    expect(prioritySelect).toHaveValue('high');
  });

  it('submits form with correct data', async () => {
    render(
      <TaskForm
        onSubmit={mockOnSubmit}
        onCancel={mockOnCancel}
      />
    );

    const titleInput = screen.getByLabelText('Task Title *');
    const descriptionTextarea = screen.getByLabelText('Description');
    const prioritySelect = screen.getByLabelText('Priority *');
    const submitButton = screen.getByText('Add Task');

    fireEvent.change(titleInput, { target: { value: 'New Task' } });
    fireEvent.change(descriptionTextarea, { target: { value: 'Task description' } });
    fireEvent.change(prioritySelect, { target: { value: 'high' } });
    fireEvent.click(submitButton);

    await waitFor(() => {
      expect(mockOnSubmit).toHaveBeenCalledWith({
        title: 'New Task',
        description: 'Task description',
        priority: 'high'
      } as TaskFormData);
    });
  });

  it('validates required fields', async () => {
    render(
      <TaskForm
        onSubmit={mockOnSubmit}
        onCancel={mockOnCancel}
      />
    );

    const submitButton = screen.getByText('Add Task');
    fireEvent.click(submitButton);

    await waitFor(() => {
      expect(screen.getByText('Title is required')).toBeInTheDocument();
    });
  });

  it('shows cancel button when onCancel is provided', () => {
    render(
      <TaskForm
        onSubmit={mockOnSubmit}
        onCancel={mockOnCancel}
      />
    );

    expect(screen.getByText('Cancel')).toBeInTheDocument();
  });

  it('does not show cancel button when onCancel is not provided', () => {
    render(
      <TaskForm
        onSubmit={mockOnSubmit}
      />
    );

    expect(screen.queryByText('Cancel')).not.toBeInTheDocument();
  });
});