## ChatGPT Getting Started (Python)

### REQUIREMENTS

- Python3

### OPENAI API KEY

In order to run this example you will need an API key from OpenAI. If you don't have one, head over to
[OpenAI Platform](https://platform.openai.com) and sign in (or sign up), then under your account menu,
select "View API keys" and click on "Create new secret key." Make sure to copy the key somewhere safe,
since it won't be shown again.

Once you have an API key, copy the `.env.sample` file to `.env` and set the `OPEN_AI_KEY` value:

    OPEN_AI_KEY=sk-XyZetc

### SET UP

To set up the virtual environment for this example, run the `set-up.sh` script and then activate the virtual environment:

    ./set-up.sh
    source .venv/bin/activate

### RUNNING

To run the example, just run the `src/main.py` script:

    python3 src/main.py
