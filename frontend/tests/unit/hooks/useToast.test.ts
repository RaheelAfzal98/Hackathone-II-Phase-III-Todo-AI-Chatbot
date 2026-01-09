import { renderHook, act } from '@testing-library/react';
import useToast from '@/components/hooks/useToast';

describe('useToast', () => {
  it('should initialize with default state', () => {
    const { result } = renderHook(() => useToast());

    expect(result.current.toast.show).toBe(false);
    expect(result.current.toast.message).toBe('');
    expect(result.current.toast.type).toBe('info');
    expect(result.current.toast.duration).toBe(5000);
  });

  it('should show toast with custom message and type', () => {
    const { result } = renderHook(() => useToast());

    act(() => {
      result.current.showToast('Test message', 'success', 3000);
    });

    expect(result.current.toast.show).toBe(true);
    expect(result.current.toast.message).toBe('Test message');
    expect(result.current.toast.type).toBe('success');
    expect(result.current.toast.duration).toBe(3000);
  });

  it('should show success toast', () => {
    const { result } = renderHook(() => useToast());

    act(() => {
      result.current.success('Success message');
    });

    expect(result.current.toast.show).toBe(true);
    expect(result.current.toast.message).toBe('Success message');
    expect(result.current.toast.type).toBe('success');
  });

  it('should show error toast', () => {
    const { result } = renderHook(() => useToast());

    act(() => {
      result.current.error('Error message');
    });

    expect(result.current.toast.show).toBe(true);
    expect(result.current.toast.message).toBe('Error message');
    expect(result.current.toast.type).toBe('error');
  });

  it('should hide toast', () => {
    const { result } = renderHook(() => useToast());

    // First show a toast
    act(() => {
      result.current.showToast('Test message');
    });

    expect(result.current.toast.show).toBe(true);

    // Then hide it
    act(() => {
      result.current.hideToast();
    });

    expect(result.current.toast.show).toBe(false);
  });

  it('should update toast with different convenience methods', () => {
    const { result } = renderHook(() => useToast());

    // Test info
    act(() => {
      result.current.info('Info message');
    });
    expect(result.current.toast.message).toBe('Info message');
    expect(result.current.toast.type).toBe('info');

    // Test warning
    act(() => {
      result.current.warning('Warning message');
    });
    expect(result.current.toast.message).toBe('Warning message');
    expect(result.current.toast.type).toBe('warning');
  });
});