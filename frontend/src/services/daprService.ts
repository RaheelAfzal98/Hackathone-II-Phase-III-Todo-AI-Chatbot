import { DaprClient, DaprClientOptions, client, daprOptions } from './mockDaprClient';
import { ErrorResponse } from '@/types/ApiResponse';

// Initialize Dapr client with environment variables
const daprAppId = process.env.NEXT_PUBLIC_DAPR_APP_ID || 'backend';

/**
 * Generic Dapr service wrapper for common operations
 */
class DaprService {
  /**
   * Invoke a service using Dapr service invocation
   */
  async invokeService(
    appId: string,
    methodName: string,
    httpVerb: 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE',
    body?: any
  ): Promise<any> {
    try {
      const response = await client.invoker.invoke(
        appId,
        methodName,
        httpVerb,
        body ? JSON.stringify(body) : undefined
      );

      return JSON.parse(response.toString());
    } catch (error: any) {
      console.error(`Error invoking service ${appId}/${methodName}:`, error);
      throw error;
    }
  }

  /**
   * Get state from Dapr state store
   */
  async getState(storeName: string, key: string): Promise<any> {
    try {
      const response = await client.state.get(storeName, key);
      return response;
    } catch (error: any) {
      console.error(`Error getting state for key ${key}:`, error);
      throw error;
    }
  }

  /**
   * Save state to Dapr state store
   */
  async saveState(storeName: string, key: string, value: any): Promise<void> {
    try {
      await client.state.save(storeName, [{ key, value }]);
    } catch (error: any) {
      console.error(`Error saving state for key ${key}:`, error);
      throw error;
    }
  }

  /**
   * Delete state from Dapr state store
   */
  async deleteState(storeName: string, key: string): Promise<void> {
    try {
      await client.state.delete(storeName, key);
    } catch (error: any) {
      console.error(`Error deleting state for key ${key}:`, error);
      throw error;
    }
  }

  /**
   * Publish an event to Dapr pub/sub
   */
  async publishEvent(pubSubName: string, topicName: string, data: any): Promise<void> {
    try {
      await client.pubsub.publish(pubSubName, topicName, data);
    } catch (error: any) {
      console.error(`Error publishing event to ${pubSubName}/${topicName}:`, error);
      throw error;
    }
  }

  /**
   * Get secret from Dapr secret store
   */
  async getSecret(storeName: string, key: string): Promise<any> {
    try {
      const response = await client.secret.get(storeName, key);
      return response?.[key] || null;
    } catch (error: any) {
      console.error(`Error getting secret ${key} from store ${storeName}:`, error);
      throw error;
    }
  }

  /**
   * Get the configured Dapr client
   */
  getClient(): any {
    return client;
  }

  /**
   * Get the configured Dapr options
   */
  getOptions(): DaprClientOptions {
    return daprOptions;
  }
}

export default new DaprService();