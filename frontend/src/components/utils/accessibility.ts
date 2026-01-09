/**
 * Accessibility utilities for the todo application
 */

// Focus management utilities
export const focusFirstElement = (container: HTMLElement | null) => {
  if (!container) return;

  const focusableElements = container.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  ) as NodeListOf<HTMLElement>;

  if (focusableElements.length > 0) {
    focusableElements[0].focus();
  }
};

export const trapFocus = (container: HTMLElement | null, event: KeyboardEvent) => {
  if (!container || event.key !== 'Tab') return;

  const focusableElements = container.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  ) as NodeListOf<HTMLElement>;

  if (focusableElements.length === 0) return;

  const firstElement = focusableElements[0];
  const lastElement = focusableElements[focusableElements.length - 1];

  if (event.shiftKey && document.activeElement === firstElement) {
    lastElement.focus();
    event.preventDefault();
  } else if (!event.shiftKey && document.activeElement === lastElement) {
    firstElement.focus();
    event.preventDefault();
  }
};

// ARIA utilities
export const toggleAriaExpanded = (element: HTMLElement | null, expanded: boolean) => {
  if (element) {
    element.setAttribute('aria-expanded', expanded.toString());
  }
};

export const setAriaLabel = (element: HTMLElement | null, label: string) => {
  if (element) {
    element.setAttribute('aria-label', label);
  }
};

export const setAriaDescribedBy = (element: HTMLElement | null, id: string) => {
  if (element) {
    element.setAttribute('aria-describedby', id);
  }
};

// Keyboard navigation utilities
export const handleArrowKeys = (
  currentIndex: number,
  maxIndex: number,
  callback: (newIndex: number) => void,
  event: React.KeyboardEvent
) => {
  switch (event.key) {
    case 'ArrowUp':
      event.preventDefault();
      const newIndexUp = currentIndex > 0 ? currentIndex - 1 : maxIndex;
      callback(newIndexUp);
      break;
    case 'ArrowDown':
      event.preventDefault();
      const newIndexDown = currentIndex < maxIndex ? currentIndex + 1 : 0;
      callback(newIndexDown);
      break;
    default:
      break;
  }
};

// Screen reader announcements
export const announceToScreenReader = (message: string) => {
  const announcement = document.createElement('div');
  announcement.setAttribute('aria-live', 'polite');
  announcement.setAttribute('aria-atomic', 'true');
  announcement.className = 'sr-only';
  announcement.textContent = message;

  document.body.appendChild(announcement);

  setTimeout(() => {
    document.body.removeChild(announcement);
  }, 1000);
};

// Utility to add screen reader only class
export const srOnlyStyle = {
  position: 'absolute',
  width: '1px',
  height: '1px',
  padding: '0',
  margin: '-1px',
  overflow: 'hidden',
  clip: 'rect(0, 0, 0, 0)',
  whiteSpace: 'nowrap',
  borderWidth: '0',
} as const;