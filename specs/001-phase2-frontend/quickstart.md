# Quickstart Guide: Phase 2 Frontend - Todo Management UI

## Prerequisites

- Node.js 18.x or higher
- npm or yarn package manager
- Git version control
- Access to backend services via Dapr

## Setup Instructions

### 1. Clone the Repository
```bash
git clone [repository-url]
cd [repository-directory]
```

### 2. Navigate to Frontend Directory
```bash
cd frontend
```

### 3. Install Dependencies
```bash
npm install
# or
yarn install
```

### 4. Environment Configuration
Create a `.env.local` file in the frontend directory:
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:3500
NEXT_PUBLIC_DAPR_HTTP_PORT=3500
NEXT_PUBLIC_DAPR_GRPC_PORT=50001
```

### 5. Run Development Server
```bash
npm run dev
# or
yarn dev
```

The application will be available at `http://localhost:3000`

## Key Scripts

- `npm run dev` - Start development server with hot reloading
- `npm run build` - Build the application for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint to check for code issues
- `npm run test` - Run unit tests
- `npm run test:e2e` - Run end-to-end tests

## Project Structure Overview

```
frontend/
├── src/
│   ├── components/     # Reusable React components
│   │   ├── Task/       # Task-specific components
│   │   ├── Layout/     # Layout components
│   │   ├── UI/         # Base UI components
│   │   ├── hooks/      # Custom React hooks
│   │   └── utils/      # Utility functions
│   ├── pages/          # Next.js pages
│   ├── services/       # API and service clients
│   ├── styles/         # Global and component styles
│   └── types/          # TypeScript type definitions
├── public/             # Static assets
├── tests/              # Test files
└── package.json        # Project configuration
```

## Development Workflow

### Creating a New Component
1. Create component file in `src/components/[Category]/ComponentName.tsx`
2. Export component with proper TypeScript typing
3. Add unit tests in `tests/unit/components/`
4. Import and use in parent components

### Adding a New Page
1. Create page file in `src/pages/` following Next.js routing conventions
2. Implement page component with proper TypeScript typing
3. Add integration tests in `tests/integration/pages/`

### Connecting to Backend Services
1. Add API endpoint in `src/services/apiClient.ts`
2. Create custom hook in `src/components/hooks/` for data fetching
3. Connect hook to components as needed

## Environment Variables

- `NEXT_PUBLIC_API_BASE_URL`: Base URL for backend API
- `NEXT_PUBLIC_DAPR_HTTP_PORT`: Port for Dapr HTTP communication
- `NEXT_PUBLIC_DAPR_GRPC_PORT`: Port for Dapr gRPC communication
- `NEXT_PUBLIC_APP_ENV`: Application environment (development/staging/production)

## Common Tasks

### Running Tests
```bash
# Run all tests
npm run test

# Run tests in watch mode
npm run test -- --watch

# Run E2E tests
npm run test:e2e
```

### Building for Production
```bash
npm run build
npm run start
```

### Linting and Formatting
```bash
# Check for linting issues
npm run lint

# Fix linting issues automatically
npm run lint -- --fix

# Format code with Prettier
npm run format
```

## Dapr Integration

### Starting Dapr Locally
```bash
dapr run --app-id frontend --app-port 3000 --dapr-http-port 3500 npm run dev
```

### Calling Backend Services
The frontend uses Dapr service invocation to communicate with backend services. All API calls go through the centralized `apiClient.ts` service which handles Dapr-specific headers and error handling.

## Troubleshooting

### Common Issues
- **Port conflicts**: Change port in package.json or terminate conflicting processes
- **Dapr not connecting**: Ensure Dapr runtime is installed and running
- **API calls failing**: Check backend service is running and Dapr sidecar is connected

### Debugging Tips
- Enable Dapr logs: `dapr run --log-level debug ...`
- Check browser developer tools for network errors
- Use `console.log` statements in development (removed in production)