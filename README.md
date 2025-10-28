# Both Are True Blog

Hugo blog using the PaperMod theme.

## YAML Front Matter Validation

To prevent YAML syntax errors in blog posts (which cause Netlify builds to fail), this repo includes automatic validation.

### Setup Pre-commit Hook (One-time)

The pre-commit hook is already in place in `.git/hooks/pre-commit` and will automatically check any staged markdown files when you commit.

**Requirements:**
```bash
pip3 install pyyaml
```

### Manual Validation

Check a single file:
```bash
python3 validate-frontmatter.py content/posts/my-post.md
```

Check all posts:
```bash
python3 validate-frontmatter.py --check-all
```

Auto-fix YAML errors:
```bash
python3 validate-frontmatter.py --fix content/posts/my-post.md
```

### Common YAML Issues

The validator catches and fixes:

1. **Nested quotes** - Converts `""text""` to proper YAML format
2. **Unescaped special characters** - Properly escapes colons, quotes, etc.
3. **Invalid YAML syntax** - Validates structure before commit

### Bypassing Validation

If you need to commit without validation (not recommended):
```bash
git commit --no-verify
```

## Development

Start local Hugo server:
```bash
hugo server --buildDrafts
```

Build for production:
```bash
hugo --gc --minify
```

## Deployment

Pushes to `master` automatically deploy to Netlify.
