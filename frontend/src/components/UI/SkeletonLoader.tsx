import React from 'react';

interface SkeletonLoaderProps {
  className?: string;
  count?: number;
}

const SkeletonLoader: React.FC<SkeletonLoaderProps> = ({ className = '', count = 1 }) => {
  const skeletons = Array.from({ length: count }, (_, index) => (
    <div
      key={index}
      className={`animate-pulse bg-gray-200 rounded-md ${className}`}
    />
  ));

  return <>{skeletons}</>;
};

export default SkeletonLoader;