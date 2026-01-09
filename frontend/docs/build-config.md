# Build Configuration

This document outlines the build configuration for the Todo Management Frontend application.

## Environment Configuration

### Development Environment
- **Environment Variable**: `NEXT_PUBLIC_APP_ENV=development`
- **API Base URL**: `http://localhost:3500`
- **DAPR Port**: 3500
- **Hot Reloading**: Enabled
- **Source Maps**: Enabled
- **Minification**: Disabled

### Staging Environment
- **Environment Variable**: `NEXT_PUBLIC_APP_ENV=staging`
- **API Base URL**: `https://staging-api.todoapp.com`
- **DAPR Port**: 3500
- **Hot Reloading**: Disabled
- **Source Maps**: Enabled
- **Minification**: Enabled
- **Compression**: Enabled

### Production Environment
- **Environment Variable**: `NEXT_PUBLIC_APP_ENV=production`
- **API Base URL**: `https://api.todoapp.com`
- **DAPR Port**: 3500
- **Hot Reloading**: Disabled
- **Source Maps**: Disabled
- **Minification**: Enabled
- **Compression**: Enabled
- **Bundle Analyzer**: Disabled

## Build Process

### Dependencies
- Node.js 18.x or higher
- npm 8.x or higher
- Dapr runtime (for local development)

### Build Steps
1. Install dependencies: `npm install`
2. Run build command: `npm run build`
3. Start production server: `npm run start`

### Output
- Production build output is located in the `.next/` directory
- Static assets are optimized and compressed
- Bundle sizes are analyzed and reported
- Code splitting is applied to optimize loading

## Performance Optimization

### Bundle Size Targets
- Main bundle: < 200KB
- Vendor bundle: < 300KB
- Individual page chunks: < 100KB

### Performance Metrics
- Initial page load: < 2 seconds
- Time to interactive: < 3 seconds
- Largest Contentful Paint: < 2.5 seconds
- First Input Delay: < 100ms

## Security Configuration

### Content Security Policy (CSP)
- Script sources: 'self' only
- Style sources: 'self' and inline styles
- Image sources: 'self' and data: URLs
- Connect sources: API endpoints only

### Environment Variables
- Sensitive information stored in environment variables
- No secrets in source code
- Environment-specific configurations

## Deployment Configuration

### Docker Configuration
- Multi-stage build process
- Base image: node:18-alpine
- Production build in separate stage
- Minimal final image size

### CDN Configuration
- Static assets served from CDN
- Cache headers set appropriately
- Versioned asset URLs to prevent caching issues