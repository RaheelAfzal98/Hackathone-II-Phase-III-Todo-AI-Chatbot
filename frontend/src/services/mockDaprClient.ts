/**
 * Mock Dapr Client for development without actual Dapr infrastructure
 * This simulates the Dapr client functionality for frontend development
 */

// Define the same interfaces as the real Dapr client
export interface DaprClientOptions {
  daprHost: string;
  daprPort: number;
  communicationProtocol: 'http' | 'grpc';
  clientToken?: string;
}

export interface MockDaprClient {
  invoker: {
    invoke: (
      appId: string,
      methodName: string,
      httpVerb: 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE',
      body?: string
    ) => Promise<any>;
  };
  state: {
    get: (storeName: string, key: string) => Promise<any>;
    save: (storeName: string, stateObjects: Array<{ key: string; value: any }>) => Promise<void>;
    delete: (storeName: string, key: string) => Promise<void>;
  };
  pubsub: {
    publish: (pubSubName: string, topicName: string, data: any) => Promise<void>;
  };
  secret: {
    get: (storeName: string, key: string) => Promise<any>;
  };
}

// Mock implementation
class MockDaprClientImpl implements MockDaprClient {
  invoker = {
    invoke: async (
      appId: string,
      methodName: string,
      httpVerb: 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE',
      body?: string
    ) => {
      console.log(`Mock Dapr invoke: ${httpVerb} ${appId}/${methodName}`);

      // Simulate API responses based on the method
      if (methodName.includes('tasks')) {
        switch (httpVerb) {
          case 'GET':
            if (methodName.includes('/filter')) {
              // Simulate filtered tasks
              return {
                toString: () => JSON.stringify({
                  data: [],
                  message: 'Filtered tasks retrieved successfully'
                })
              };
            } else if (methodName.includes('/:id') || methodName.includes('toggle-complete')) {
              // Simulate single task response
              return {
                toString: () => JSON.stringify({
                  data: { id: '1', title: 'Sample Task', completed: false, priority: 'medium', createdAt: new Date().toISOString() },
                  message: 'Task retrieved successfully'
                })
              };
            } else {
              // Simulate all tasks
              return {
                toString: () => JSON.stringify({
                  data: [
                    { id: '1', title: 'Sample Task 1', completed: false, priority: 'medium', createdAt: new Date().toISOString() },
                    { id: '2', title: 'Sample Task 2', completed: true, priority: 'high', createdAt: new Date().toISOString() }
                  ],
                  message: 'Tasks retrieved successfully'
                })
              };
            }
          case 'POST':
            return {
              toString: () => JSON.stringify({
                data: {
                  id: Math.random().toString(36).substr(2, 9),
                  ...JSON.parse(body || '{}'),
                  completed: false,
                  createdAt: new Date().toISOString()
                },
                message: 'Task created successfully'
              })
            };
          case 'PUT':
            return {
              toString: () => JSON.stringify({
                data: {
                  id: methodName.split('/')[2], // Extract ID from URL
                  ...JSON.parse(body || '{}'),
                  createdAt: new Date().toISOString()
                },
                message: 'Task updated successfully'
              })
            };
          case 'PATCH':
            return {
              toString: () => JSON.stringify({
                data: {
                  id: methodName.split('/')[2], // Extract ID from URL
                  completed: true
                },
                message: 'Task completion status updated'
              })
            };
          case 'DELETE':
            return {
              toString: () => JSON.stringify({
                message: 'Task deleted successfully'
              })
            };
        }
      }

      // Default response
      return {
        toString: () => JSON.stringify({ data: null, message: 'Operation successful' })
      };
    }
  };

  state = {
    get: async (storeName: string, key: string) => {
      console.log(`Mock Dapr state get: ${storeName}/${key}`);
      // Return mock state based on key
      return localStorage.getItem(`${storeName}:${key}`) || null;
    },
    save: async (storeName: string, stateObjects: Array<{ key: string; value: any }>) => {
      console.log(`Mock Dapr state save: ${storeName}`);
      stateObjects.forEach(obj => {
        localStorage.setItem(`${storeName}:${obj.key}`, JSON.stringify(obj.value));
      });
    },
    delete: async (storeName: string, key: string) => {
      console.log(`Mock Dapr state delete: ${storeName}/${key}`);
      localStorage.removeItem(`${storeName}:${key}`);
    }
  };

  pubsub = {
    publish: async (pubSubName: string, topicName: string, data: any) => {
      console.log(`Mock Dapr pubsub publish: ${pubSubName}/${topicName}`, data);
    }
  };

  secret = {
    get: async (storeName: string, key: string) => {
      console.log(`Mock Dapr secret get: ${storeName}/${key}`);
      // In a real implementation, this would fetch from a secure store
      return null;
    }
  };
}

// Initialize Dapr client with environment variables
const daprAppId = process.env.NEXT_PUBLIC_DAPR_APP_ID || 'backend';
const daprHttpPort = parseInt(process.env.NEXT_PUBLIC_DAPR_HTTP_PORT || '3500', 10);
const daprGrpcPort = parseInt(process.env.NEXT_PUBLIC_DAPR_GRPC_PORT || '50001', 10);

export const daprOptions: DaprClientOptions = {
  daprHost: process.env.NEXT_PUBLIC_DAPR_HOST || 'localhost',
  daprPort: daprHttpPort,
  communicationProtocol: 'http' as const,
  clientToken: process.env.NEXT_PUBLIC_DAPR_TOKEN,
};

// Export the mock client
export const DaprClient = MockDaprClientImpl;
export const client = new MockDaprClientImpl();