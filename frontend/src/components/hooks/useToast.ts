import { useState, useCallback } from 'react';
import { ToastState } from '@/types/Task';

const useToast = () => {
  const [toast, setToast] = useState<ToastState>({
    show: false,
    message: '',
    type: 'info',
    duration: 5000,
  });

  const showToast = useCallback((message: string, type: ToastState['type'] = 'info', duration: number = 5000) => {
    setToast({
      show: true,
      message,
      type,
      duration,
    });
  }, []);

  const hideToast = useCallback(() => {
    setToast(prev => ({
      ...prev,
      show: false,
    }));
  }, []);

  const success = useCallback((message: string, duration?: number) => {
    showToast(message, 'success', duration);
  }, [showToast]);

  const error = useCallback((message: string, duration?: number) => {
    showToast(message, 'error', duration);
  }, [showToast]);

  const info = useCallback((message: string, duration?: number) => {
    showToast(message, 'info', duration);
  }, [showToast]);

  const warning = useCallback((message: string, duration?: number) => {
    showToast(message, 'warning', duration);
  }, [showToast]);

  return {
    toast,
    showToast,
    hideToast,
    success,
    error,
    info,
    warning,
  };
};

export default useToast;