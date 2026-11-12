# AI Chatbot (Python + Flask + HTML/CSS/JS)

A simple AI chatbot with a chat-box web page. The frontend is plain HTML, CSS and JavaScript.
The backend is a small Flask server that calls the Claude API, so your API key stays safe on the server.

## Project Structure

```
ai-chatbot/
├── app.py            # Flask backend (calls the AI API)
├── index.html        # Frontend (chat box UI)
├── requirements.txt  # Python packages
└── README.md
```

## Requirements

- Python 3.8 or newer
- An Anthropic API key (get one at https://console.anthropic.com)

## Setup and Run

1. Open a terminal inside the `ai-chatbot` folder.

2. (Optional but recommended) create a virtual environment:

   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac / Linux
   ```

3. Install the packages:

   ```
   pip install -r requirements.txt
   ```

4. Set your API key:

   - Windows (Command Prompt): `set ANTHROPIC_API_KEY=your_key_here`
   - Windows (PowerShell): `$env:ANTHROPIC_API_KEY="your_key_here"`
   - Mac / Linux: `export ANTHROPIC_API_KEY=your_key_here`

5. Start the server:

   ```
   python app.py
   ```

6. Open your browser and go to: http://127.0.0.1:5000

## How It Works

1. You type a message in the chat box.
2. JavaScript sends the full conversation to the Flask `/chat` route.
3. Flask sends it to the AI model using the API.
4. The reply comes back and is shown in the chat box.
5. The `history` list in `index.html` keeps the conversation, so the bot remembers earlier messages.

## Customize

- Change the bot's personality: edit the `system=` line in `app.py`.
- Change the look: edit the `<style>` section in `index.html`.
- Change reply length: edit `max_tokens` in `app.py`.

## Troubleshooting

- **"Error: ... api_key ..."**: the API key is not set. Set it again in the same terminal and run `python app.py`.
- **"ModuleNotFoundError"**: run `pip install -r requirements.txt`.
- **Model not found error**: check the current model names in the Anthropic docs and update `model=` in `app.py`.
- **Quota or billing error**: check your usage and credits in the Anthropic console.

