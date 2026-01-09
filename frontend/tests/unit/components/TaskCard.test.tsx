import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import TaskCard from '@/components/Task/TaskCard';
import { Task } from '@/types/Task';

describe('TaskCard', () => {
  const mockTask: Task = {
    id: '1',
    title: 'Test Task',
    description: 'Test Description',
    completed: false,
    priority: 'medium',
    createdAt: '2023-01-01T00:00:00Z',
    updatedAt: '2023-01-01T00:00:00Z',
  };

  const mockOnToggleComplete = jest.fn();
  const mockOnDelete = jest.fn();
  const mockOnEdit = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
  });

  it('renders task title and description', () => {
    render(
      <TaskCard
        task={mockTask}
        onToggleComplete={mockOnToggleComplete}
        onDelete={mockOnDelete}
        onEdit={mockOnEdit}
      />
    );

    expect(screen.getByText('Test Task')).toBeInTheDocument();
    expect(screen.getByText('Test Description')).toBeInTheDocument();
  });

  it('displays priority badge with correct color', () => {
    const { container } = render(
      <TaskCard
        task={mockTask}
        onToggleComplete={mockOnToggleComplete}
        onDelete={mockOnDelete}
        onEdit={mockOnEdit}
      />
    );

    const priorityBadge = container.querySelector('.bg-yellow-100');
    expect(priorityBadge).toBeInTheDocument();
    expect(priorityBadge).toHaveTextContent('Medium priority');
  });

  it('calls onToggleComplete when checkbox is clicked', () => {
    render(
      <TaskCard
        task={mockTask}
        onToggleComplete={mockOnToggleComplete}
        onDelete={mockOnDelete}
        onEdit={mockOnEdit}
      />
    );

    const checkbox = screen.getByRole('checkbox');
    fireEvent.click(checkbox);

    expect(mockOnToggleComplete).toHaveBeenCalledWith('1');
  });

  it('shows confirmation dialog when delete button is clicked', () => {
    render(
      <TaskCard
        task={mockTask}
        onToggleComplete={mockOnToggleComplete}
        onDelete={mockOnDelete}
        onEdit={mockOnEdit}
      />
    );

    const deleteButton = screen.getByLabelText('Delete task "Test Task"');
    fireEvent.click(deleteButton);

    expect(screen.getByText('Confirm Deletion')).toBeInTheDocument();
    expect(screen.getByText('Are you sure you want to delete the task "Test Task"?')).toBeInTheDocument();
  });

  it('completes task styling when completed is true', () => {
    const completedTask = { ...mockTask, completed: true };
    const { container } = render(
      <TaskCard
        task={completedTask}
        onToggleComplete={mockOnToggleComplete}
        onDelete={mockOnDelete}
        onEdit={mockOnEdit}
      />
    );

    const title = screen.getByText('Test Task');
    expect(title).toHaveClass('line-through');
    expect(container.firstChild).toHaveClass('opacity-70');
  });
});