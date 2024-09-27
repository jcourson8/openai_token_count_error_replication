# openai_token_count_error_replication
**Issue:** Encountering openai.RateLimitError due to exceeding token limits when using the text-embedding-3-large model, despite pre-calculating tokens with tiktoken.

**Cause:** Discrepancies in token calculation between tiktoken and OpenAI API's internal processing, leading to requests larger than the 1,000,000 TPM limit.

## Usage
Ensure you have the openai and tiktoken packages installed:

```python3 -m pip install openai tiktoken```

Run the script with your OpenAI API key set as an environment variable:

```OPENAI_API_KEY=<your_api_key> python3 replication.py```