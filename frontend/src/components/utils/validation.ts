export interface ValidationErrors {
  [key: string]: string;
}

export const validateTask = (title: string, description?: string, priority?: string): ValidationErrors => {
  const errors: ValidationErrors = {};

  // Validate title
  if (!title || title.trim().length === 0) {
    errors.title = 'Title is required';
  } else if (title.length > 255) {
    errors.title = 'Title must be 255 characters or less';
  } else if (title.trim().length < 1) {
    errors.title = 'Title must be at least 1 character';
  }

  // Validate description
  if (description && description.length > 1000) {
    errors.description = 'Description must be 1000 characters or less';
  }

  // Validate priority
  if (priority && !['low', 'medium', 'high'].includes(priority)) {
    errors.priority = 'Priority must be low, medium, or high';
  }

  return errors;
};

export const validateTitle = (title: string): string | null => {
  if (!title || title.trim().length === 0) {
    return 'Title is required';
  }
  if (title.length > 255) {
    return 'Title must be 255 characters or less';
  }
  if (title.trim().length < 1) {
    return 'Title must be at least 1 character';
  }
  return null;
};

export const validateEmail = (email: string): string | null => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!email) {
    return 'Email is required';
  }
  if (!emailRegex.test(email)) {
    return 'Please enter a valid email address';
  }
  return null;
};

export const validateRequired = (value: string, fieldName: string): string | null => {
  if (!value || value.trim().length === 0) {
    return `${fieldName} is required`;
  }
  return null;
};