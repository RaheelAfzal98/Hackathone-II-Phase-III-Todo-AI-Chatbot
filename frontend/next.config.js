/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'http',
        hostname: 'localhost',
      },
      {
        protocol: 'http',
        hostname: '127.0.0.1',
      },
    ],
  },
  env: {
    NEXT_PUBLIC_API_BASE_URL: process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000',
    NEXT_PUBLIC_DAPR_HTTP_PORT: process.env.NEXT_PUBLIC_DAPR_HTTP_PORT || '3500',
    NEXT_PUBLIC_DAPR_GRPC_PORT: process.env.NEXT_PUBLIC_DAPR_GRPC_PORT || '50001',
    NEXT_PUBLIC_BETTER_AUTH_URL: process.env.NEXT_PUBLIC_BETTER_AUTH_URL || 'http://localhost:8000',
  },
};

module.exports = nextConfig;