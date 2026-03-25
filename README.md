# Nova Bot

Nova Bot is a Markov chain text generator seeded from the vocabulary and cadence of William S. Burroughs' *Naked Lunch*. Enter a start word and the app generates a stream of associative text, walking a probabilistic path through the novel's language.

## How It Works

1. A vocabulary list (`hoard.txt`) filters which words are valid
2. Word-to-word transitions are built from `naked_lunch.txt` at startup
3. Given a start word, the app randomly walks the transition map to generate text
4. A Flask web interface lets users enter a start word and generate output on demand

## Getting Started

**Requirements:** Python 3.12+

```bash
# Clone the repo
git clone git@github.com:mstanisi/novabot.git
cd novabot

# Create and activate a virtual environment
python3 -m venv jupyter-env
source jupyter-env/bin/activate

# Install dependencies
pip install flask

# Run the app
python nova_bot.py
```

Then open `http://127.0.0.1:5000` in your browser.

> **Note:** You will need to supply your own copies of `hoard.txt` and `naked_lunch.txt` — these are not included in the repository.

## Project Structure

```
novabot/
├── nova_bot.py          # Flask app and Markov chain logic
├── 2. nova-bot.ipynb    # Development notebook
├── 1. data transform.ipynb  # Data exploration notebook
└── README.md
```

## Roadmap

- [ ] Improve text coherence and output formatting
- [ ] Add controls for output length
- [ ] Explore transformer-based refinement of Markov output
- [ ] Better handling of unknown start words (fuzzy matching)
- [ ] Deployment

## License

TBD

