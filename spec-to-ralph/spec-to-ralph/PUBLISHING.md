# Publishing spec-to-ralph

## Option 1: Create Your Own Marketplace

If you want full control, host your own marketplace:

### 1. Create a GitHub repo for the marketplace

```bash
# Create marketplace repo
mkdir switchfin-plugins
cd switchfin-plugins
git init

# Create marketplace structure
mkdir -p .claude-plugin plugins
```

### 2. Add marketplace.json

Create `.claude-plugin/marketplace.json`:

```json
{
  "name": "switchfin-plugins",
  "description": "Switchfin's Claude Code plugins for AI-native development",
  "version": "1.0.0",
  "plugins": [
    {
      "name": "spec-to-ralph",
      "description": "Bridge GitHub Spec Kit to Ralph Wiggum autonomous loops. Convert spec-driven development artifacts into optimized prompts for overnight autonomous coding.",
      "version": "1.0.0",
      "author": {
        "name": "Doug / Switchfin",
        "url": "https://github.com/switchfin"
      },
      "source": "./plugins/spec-to-ralph",
      "category": "development",
      "keywords": ["spec-kit", "ralph-wiggum", "autonomous", "sdd"]
    }
  ]
}
```

### 3. Copy the plugin

```bash
# Copy spec-to-ralph into plugins/
cp -r /path/to/spec-to-ralph plugins/
```

### 4. Push to GitHub

```bash
git add .
git commit -m "Initial marketplace with spec-to-ralph"
git remote add origin https://github.com/switchfin/switchfin-plugins.git
git push -u origin main
```

### 5. Users can install with:

```bash
# Add your marketplace
/plugin marketplace add switchfin/switchfin-plugins

# Install the plugin
/plugin install spec-to-ralph@switchfin-plugins
```

---

## Option 2: Submit to Community Marketplace

Several community marketplaces accept plugin submissions:

### Dan Ávila's Marketplace
- Repo: https://github.com/davila7/claude-code-plugins
- Submit via PR

### Seth Hobson's Marketplace  
- Repo: https://github.com/wshobson/claude-code-workflows
- Submit via PR

### claude-plugins.dev Registry
- Site: https://claude-plugins.dev
- Submit via their process

### Submission PR Template

```markdown
## New Plugin: spec-to-ralph

### Description
Bridge GitHub Spec Kit to Ralph Wiggum autonomous loops. Converts spec-driven development artifacts (constitution, spec, plan, tasks) into optimized prompts for autonomous overnight coding.

### Commands
- `/spec-to-ralph:status` - Check project readiness
- `/spec-to-ralph:generate` - Generate PROMPT.md
- `/spec-to-ralph:start` - Generate + start Ralph

### Dependencies
- `ralph-wiggum@claude-plugins-official`

### Use Case
Developers using GitHub Spec Kit for planning who want to execute their specs autonomously with Ralph Wiggum. Eliminates manual prompt engineering between spec completion and autonomous execution.

### Author
Doug / Switchfin
https://github.com/switchfin
```

---

## Option 3: Submit to Anthropic's Official Marketplace

For inclusion in `claude-plugins-official`:

### Requirements
- High quality, well-tested
- Clear documentation
- Follows plugin structure conventions
- Provides real value to users

### Process
1. Fork https://github.com/anthropics/claude-plugins-official
2. Add plugin to `plugins/` directory
3. Update `.claude-plugin/marketplace.json`
4. Submit PR with detailed description
5. Wait for review

### Entry for marketplace.json

Add to the `plugins` array:

```json
{
  "name": "spec-to-ralph",
  "description": "Bridge GitHub Spec Kit to Ralph Wiggum autonomous loops. Convert spec-driven development artifacts into optimized prompts for overnight autonomous coding.",
  "version": "1.0.0",
  "author": {
    "name": "Switchfin",
    "url": "https://github.com/switchfin"
  },
  "source": "./plugins/spec-to-ralph",
  "category": "development"
}
```

---

## Local Testing Before Publishing

```bash
# Create a local marketplace for testing
mkdir -p ~/local-marketplace/.claude-plugin
mkdir -p ~/local-marketplace/plugins

# Copy plugin
cp -r spec-to-ralph ~/local-marketplace/plugins/

# Create minimal marketplace.json
cat > ~/local-marketplace/.claude-plugin/marketplace.json << 'EOF'
{
  "name": "local-test",
  "plugins": [
    {
      "name": "spec-to-ralph",
      "source": "./plugins/spec-to-ralph"
    }
  ]
}
EOF

# In Claude Code:
/plugin marketplace add ~/local-marketplace
/plugin install spec-to-ralph@local-test

# Test the commands
/spec-to-ralph:status
```

---

## Promotion Ideas

Once published:

1. **Tweet/post** about bridging Spec Kit + Ralph (two hot topics)
2. **Add to Awesome Claude Code** list
3. **Write a blog post** showing the workflow
4. **Submit to Hacker News** with example use case
5. **Add to Switchfin's portfolio** as developer tooling credibility

The positioning: "First to bridge spec-driven development with autonomous execution"
