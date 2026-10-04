# Clay Table Setup for Claygent Testing

How to set up a Clay table that works with the Claygent Builder's test-iterate loop.

## Step 1: Create a Webhook-Sourced Table

1. In Clay, click **+ New Table**
2. Select **Webhook** as the data source
3. Clay generates a unique webhook URL: copy this URL
4. Paste the URL into Claude Code when prompted

## Step 2: Required Columns

The webhook payload creates columns automatically on first POST. Your table will have:

| Column | Type | Source |
|--------|------|--------|
| `domain` | Text | Webhook input: the company website to analyze |
| `prompt` | Text | Webhook input: the full Claygent prompt |
| `prompt_version` | Text | Webhook input: version tracking (v1, v2, v3) |
| `callback_url` | Text | Webhook input: where Clay sends results back |
| `json_schema` | Text | Webhook input: the JSON schema for structured output |

## Step 3: Add Claygent Column

1. Click **+ Add Column**, then **Claygent** (under AI)
2. Configure:
   - **System Prompt:** Paste from the deliverable's "System Prompt" section
   - **Prompt:** Use `/domain` as the input variable (references the domain column)
   - **Click JSON Schema:** Paste from the deliverable's "JSON Schema" section
   - **Model:** Match the model recommendation from the deliverable
3. The Claygent column runs automatically when new rows arrive via webhook

## Step 4: Add HTTP Request Column (Callback)

This column sends Claygent results back to Claude Code's listener.

1. Click **+ Add Column**, then **HTTP Request** (under Integrations)
2. Configure:
   - **Method:** POST
   - **URL:** Use `/callback_url` (references the callback_url column from webhook)
   - **Body:** JSON with the Claygent output fields:
     ```json
     {
       "row_id": "/domain",
       "claygent_output": "/claygent_column_name",
       "prompt_version": "/prompt_version"
     }
     ```
   - Replace `/claygent_column_name` with the actual name of your Claygent column

## Step 5: Test the Setup

Before running the full test batch:

1. Send a single test row via webhook:
   ```bash
   curl -X POST "YOUR_WEBHOOK_URL" \
     -H "Content-Type: application/json" \
     -d '{"domain": "slack.com", "prompt": "Test prompt", "prompt_version": "test", "callback_url": "YOUR_NGROK_URL/results"}'
   ```
2. Verify the row appears in Clay
3. Verify the Claygent column runs
4. Verify the HTTP Request column sends results back
5. Check `./clay-results/` for the received JSON

## Architecture

```
+-------------+     curl POST (test rows)      +--------------+
| Claude Code | -----------------------------> |  Clay table  |
|   (Bash)    |                                |  (webhook)   |
|             | <----------------------------- |  + Claygent  |
+-------------+   HTTP callback (results +     +--------------+
                   agent steps + reasoning)
```

## Troubleshooting

- **Webhook URL not working:** Check that the table is active (not paused). Webhook URLs expire if the table is deleted.
- **Claygent not running:** Ensure the system prompt and JSON schema are pasted into the Claygent column config, not just sent via webhook.
- **Callback not received:** Check that ngrok is running and the tunnel URL matches what was sent in `callback_url`. Check `./clay-results/` directory exists.
- **JSON schema rejected:** Validate against the 10 Clay/OpenAI Structured Outputs rules in the SKILL.md. Most common issue: missing `additionalProperties: false`.
