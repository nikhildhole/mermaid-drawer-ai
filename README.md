# Mermaid Drawer AI

A FastAPI backend service that leverages LangGraph and LangChain with Google's Gemini AI to generate, validate, and manage Mermaid diagrams in real-time.

## Features

- **AI-Powered Diagram Generation**: Uses Google's Gemini 2.5 Flash model to create Mermaid diagrams from natural language descriptions
- **Real-Time Collaboration**: WebSocket support for live updates and multi-user diagram editing
- **Streaming Responses**: Server-Sent Events (SSE) for real-time workflow progress updates
- **User-Specific Storage**: Isolated diagram storage per user
- **Modular Agent Architecture**: LangGraph workflow with specialized agents for requirements gathering, generation, validation, and summarization
- **Comprehensive Logging**: Structured logging with console and file outputs
- **Health Check Endpoint**: Built-in service monitoring

## Architecture

The application uses a multi-agent LangGraph workflow:

1. **Requirements Gatherer**: Analyzes user queries to determine if they're Mermaid-related and gathers necessary context
2. **Mermaid Generator**: Creates or modifies Mermaid syntax using AI tools
3. **Mermaid Validator**: Validates the generated diagram syntax
4. **Summary Generator**: Provides a concise summary of the changes made

## Installation

### Prerequisites

- Python 3.10+
- Google AI API key (for Gemini model access)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd mermaid-drawer-ai
```

2. Install dependencies:
```bash
pip install -e .
```

3. Set up environment variables:
Create a `.env` file in the root directory:
```
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage

### Running the Server

#### Development Mode
```bash
python -m fastapi_lang_graph.cli dev
```

#### Production Mode
```bash
python -m fastapi_lang_graph.cli prod
```

The server will start on `http://localhost:8000` (configurable).

### API Endpoints

#### Health Check
- **GET** `/`
- Returns service status

#### Generate Diagram (Streaming)
- **POST** `/ask`
- Body: `{"query": "Create a flowchart for user login", "user_id": "user123"}`
- Returns: Server-Sent Events stream with real-time updates

#### WebSocket Diagram Management
- **WebSocket** `/mermaid`
- Messages:
  - Update: `{"type": "update", "user_id": "user123", "content": "graph TD\nA-->B"}`
  - Get: `{"type": "get", "user_id": "user123"}`

## Project Structure

```
fastapi_lang_graph/
├── api/v1/routers/          # API route handlers
│   ├── graph.py            # Streaming graph execution endpoint
│   ├── mermaid.py          # WebSocket diagram management
│   └── working_test.py     # Health check
├── core/
│   └── logging.py          # Logging configuration
├── graph/
│   ├── state.py            # LangGraph state definitions
│   ├── workflow.py         # Main agent workflow
│   ├── agents/             # AI agent implementations
│   ├── nodes/              # LangGraph node wrappers
│   └── models/             # AI model configurations
└── services/
    └── code.py             # User code storage service
```

## Dependencies

- **FastAPI**: Modern web framework
- **LangGraph**: Agent orchestration framework
- **LangChain**: LLM integration library
- **Google GenAI**: Gemini model access
- **Uvicorn**: ASGI server
- **Pydantic**: Data validation
- **WebSockets**: Real-time communication

## Development

### Running Tests
```bash
pytest
```

### Code Quality
- Uses structured logging for debugging
- Modular agent design for easy extension
- Type hints throughout the codebase

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Nikhil Dhole - nikhildadaddhole@gmail.com