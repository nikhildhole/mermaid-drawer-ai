# Mermaid Drawer AI

A FastAPI backend service that leverages LangGraph and LangChain with Google's Gemini AI to generate, validate, and manage Mermaid diagrams in real-time.

## Frontend

For the frontend application that interacts with this backend, refer to: [mermaid-visualizer](https://github.com/nikhildhole/mermaid-visualizer)

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
## Screenshots

![Mermaid Visualizer Interface](screenshot.png)

*Screenshot of the Mermaid Visualizer showing the three-panel layout with editor, diagram viewer, and chat sidebar.*
## Installation

### Prerequisites

- Python 3.10+
- Google AI API key (for Gemini model access)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/nikhildhole/mermaid-drawer-ai
cd mermaid-drawer-ai
```

2. Install dependencies:
```bash
uv pip install -e .
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
uv run dev
```

#### Production Mode
```bash
uv run prod
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
uv run pytest
```

### Code Quality
- Uses structured logging for debugging
- Modular agent design for easy extension
- Type hints throughout the codebase

## Customization

The application is highly modular and customizable. You can modify various components to suit your needs:

### Agent Prompts and Tools
- **Requirements Gatherer** (`fastapi_lang_graph/graph/agents/requirements_gatherer.py`): Modify the `PROMPT` variable and add/remove tools like the DuckDuckGo search tool
- **Mermaid Generator** (`fastapi_lang_graph/graph/agents/mermaid_generator.py`): Customize the generation prompt and tools (get_current_code, write_to_current_code)
- **Mermaid Validator** (`fastapi_lang_graph/graph/agents/mermaid_validator.py`): Adjust validation prompts and tools
- **Summary Generator** (`fastapi_lang_graph/graph/agents/summary_generator.py`): Modify summary generation logic

### Workflow Graph
- **Main Workflow** (`fastapi_lang_graph/graph/workflow.py`): Modify the LangGraph workflow by adding/removing nodes, changing edges, or adjusting routing logic
- **State Definition** (`fastapi_lang_graph/graph/state.py`): Extend the `MessagesState` TypedDict to include additional fields

### Language Models
- **Gemini Model** (`fastapi_lang_graph/graph/models/gemini.py`): Currently uses Google Gemini 2.5 Flash. Modify to use different Gemini models
- **Alternative LLMs**: Create new model files (e.g., `openai.py`) following the same pattern and update agent imports to use OpenAI models instead

### Commands
- Use `uv run dev` for development with auto-reload
- Use `uv sync` to sync dependencies after modifying `pyproject.toml`

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