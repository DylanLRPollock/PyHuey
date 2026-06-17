# PyHuey Model Registry Audit

## Scope

This audit records the current PyHuey model registry stored at:

`src/pygpt_net/data/config/models.json`

The active runtime copy is normally stored in the user workdir as:

`L:\PyHuey\workdir\models.json`

PyHuey loads the workdir copy during normal runtime after the initial install/copy step.

## Current registry summary

- Total model entries: 105
- Unique base model IDs: 92
- Providers:
  - OpenAI
  - Anthropic
  - Google
  - xAI
  - Perplexity
  - DeepSeek API
  - Ollama
  - HuggingFace Router
- No `active` or `disabled` field exists in the model schema.
- Models are available when present in `items` and when their `mode` matches the active UI mode.
- All registry entries are currently `imported: false`.

## Required modern entries

The registry must include at least:

- `gpt-5.2-low`
- `gpt-5.2-medium`
- `gpt-5.2-high`
- `claude-opus-4-5`
- `claude-sonnet-4-5`
- `grok-4-1-fast-reasoning`
- `grok-4-1-fast-non-reasoning`
- `gpt-image-1.5`
- `gpt-realtime`

## Default-model note

The current registry contains multiple entries marked `"default": true`.

This is tolerated for now because the upstream PyGPT model schema supports a per-model `default` flag. However, a future cleanup pass should define a clearer PyHuey default policy, likely one default per major mode:

- Chat/text
- Image
- Audio/realtime
- Research, if needed

## Runtime note

Updating the repository default model registry does not automatically overwrite an existing workdir registry.

For an existing PyHuey installation, update both:

- `src/pygpt_net/data/config/models.json`
- `L:\PyHuey\workdir\models.json`

Then restart PyHuey and confirm the terminal shows:

`[Models] L:\PyHuey\workdir\models.json`
