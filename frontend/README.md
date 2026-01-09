# Todo Management Frontend

A responsive todo management application built with Next.js, TypeScript, and Tailwind CSS.

## Features

- Create, read, update, and delete tasks
- Filter tasks by status and priority
- Mark tasks as complete/incomplete
- Responsive design for desktop and mobile
- Authentication and user management
- Real-time feedback with toast notifications
- Accessibility features (WCAG 2.1 AA compliant)

## Prerequisites

- Node.js 18.x or higher
- npm or yarn package manager

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

3. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

4. Create a `.env.local` file in the frontend directory with the following content:
   ```env
   NEXT_PUBLIC_API_BASE_URL=http://localhost:3500
   NEXT_PUBLIC_DAPR_HTTP_PORT=3500
   NEXT_PUBLIC_DAPR_GRPC_PORT=50001
   ```

5. Run the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

The application will be available at [http://localhost:3000](http://localhost:3000).

## Environment Variables

- `NEXT_PUBLIC_API_BASE_URL`: Base URL for backend API
- `NEXT_PUBLIC_DAPR_HTTP_PORT`: Port for Dapr HTTP communication
- `NEXT_PUBLIC_DAPR_GRPC_PORT`: Port for Dapr gRPC communication

## Available Scripts

- `npm run dev` - Start development server with hot reloading
- `npm run build` - Build the application for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint to check for code issues
- `npm run test` - Run unit tests
- `npm run test:e2e` - Run end-to-end tests

## Project Structure

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

## API Documentation

The frontend communicates with the backend via REST API endpoints. The API contract is defined in `specs/001-phase2-frontend/contracts/task-api-contract.md`.

## Testing

To run the tests:
```bash
npm run test
```

To run tests in watch mode:
```bash
npm run test -- --watch
```

## Deployment

To build the application for production:
```bash
npm run build
npm run start
```

## Dapr Integration

This application uses Dapr for service-to-service communication. To run with Dapr:

```bash
dapr run --app-id frontend --app-port 3000 --dapr-http-port 3500 npm run dev
```