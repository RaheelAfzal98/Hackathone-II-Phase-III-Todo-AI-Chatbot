import React, { useState, useRef, useEffect } from 'react';
import './ChatInterface.css';
import chatAPI from '../services/chat_api.js';

const ChatInterface = ({ userId }) => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  // Function to scroll to bottom of messages
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Function to handle sending a message
  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    // Add user message to the chat
    const userMessage = {
      id: Date.now(),
      sender: 'user',
      content: inputValue,
      timestamp: new Date().toISOString()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Call the chat API using the service
      const data = await chatAPI.sendMessage(userId, inputValue, localStorage.getItem(`conversation_id_${userId}`));

      // Store conversation ID in local storage for continuity
      if (data.conversation_id) {
        localStorage.setItem(`conversation_id_${userId}`, data.conversation_id);
      }

      // Add AI response to the chat
      const aiMessage = {
        id: Date.now() + 1,
        sender: 'assistant',
        content: data.response,
        timestamp: new Date().toISOString(),
        tool_calls: data.tool_calls,
        tool_responses: data.tool_responses
      };

      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error('Error sending message:', error);

      // Add error message to the chat
      const errorMessage = {
        id: Date.now() + 1,
        sender: 'system',
        content: 'Sorry, I encountered an error processing your request. Please try again.',
        timestamp: new Date().toISOString()
      };

      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  // Format timestamp for display
  const formatTime = (timestamp) => {
    return new Date(timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <div className="chat-interface">
      <div className="chat-header">
        <h2>AI Task Assistant</h2>
        <p>Manage your tasks with natural language</p>
      </div>

      <div className="chat-messages">
        {messages.length === 0 ? (
          <div className="welcome-message">
            <h3>Hello! I'm your AI task assistant.</h3>
            <p>You can ask me to:</p>
            <ul>
              <li>Add tasks: "Add a task to buy groceries"</li>
              <li>List tasks: "Show my tasks"</li>
              <li>Complete tasks: "Mark task 3 as complete"</li>
              <li>Update tasks: "Change the title of task 1"</li>
              <li>Delete tasks: "Delete task 2"</li>
            </ul>
          </div>
        ) : (
          messages.map((message) => (
            <div
              key={message.id}
              className={`message ${message.sender}-message`}
            >
              <div className="message-content">
                <span className="message-text">{message.content}</span>
                <span className="message-time">{formatTime(message.timestamp)}</span>
              </div>
              {message.tool_calls && message.tool_calls.length > 0 && (
                <div className="tool-calls">
                  <small>Used tools: {message.tool_calls.map(tc => tc.name).join(', ')}</small>
                </div>
              )}
            </div>
          ))
        )}
        {isLoading && (
          <div className="message assistant-message">
            <div className="message-content">
              <span className="message-text">Thinking...</span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSendMessage} className="chat-input-form">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Type your task request here..."
          disabled={isLoading}
        />
        <button type="submit" disabled={isLoading || !inputValue.trim()}>
          Send
        </button>
      </form>
    </div>
  );
};

export default ChatInterface;