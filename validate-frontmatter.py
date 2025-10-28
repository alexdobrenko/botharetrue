#!/usr/bin/env python3
"""
Validate and fix YAML front matter in Hugo blog posts.
Can be used standalone or as a pre-commit hook.
"""

import sys
import re
from pathlib import Path
import yaml


def extract_frontmatter(content):
    """Extract YAML front matter from markdown content."""
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        return match.group(1), match.end()
    return None, 0


def fix_yaml_string(value):
    """
    Properly escape a string value for YAML.
    Uses single quotes and escapes internal single quotes.
    """
    if not isinstance(value, str):
        return value

    # If the string contains special characters, use single quotes
    # and escape any internal single quotes
    if any(char in value for char in ['"', "'", ':', '#', '\n']):
        return "'" + value.replace("'", "''") + "'"

    return value


def validate_and_fix_frontmatter(file_path, fix=False):
    """
    Validate YAML front matter in a markdown file.
    If fix=True, attempt to fix common issues.
    Returns (is_valid, error_message, fixed_content)
    """
    try:
        content = Path(file_path).read_text(encoding='utf-8')
    except Exception as e:
        return False, f"Error reading file: {e}", None

    frontmatter_text, end_pos = extract_frontmatter(content)

    if frontmatter_text is None:
        return False, "No front matter found", None

    # Try to parse the YAML
    try:
        data = yaml.safe_load(frontmatter_text)
        return True, "Valid YAML", None
    except yaml.YAMLError as e:
        if not fix:
            return False, f"YAML error: {e}", None

        # Try to fix by properly escaping the title and other string fields
        try:
            # Attempt to parse line by line and reconstruct
            lines = frontmatter_text.split('\n')
            fixed_data = {}

            for line in lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    value = value.strip()

                    # Remove existing quotes if present
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    elif value.startswith("'") and value.endswith("'"):
                        value = value[1:-1].replace("''", "'")

                    # Try to parse as different types
                    if value.lower() in ['true', 'false']:
                        fixed_data[key] = value.lower() == 'true'
                    elif value.isdigit():
                        fixed_data[key] = int(value)
                    elif re.match(r'^\d{4}-\d{2}-\d{2}', value):
                        fixed_data[key] = value
                    else:
                        fixed_data[key] = value

            # Generate properly formatted YAML
            fixed_yaml_lines = ['---']
            for key, value in fixed_data.items():
                if isinstance(value, str) and any(char in value for char in ['"', "'", ':', '#', '\n']):
                    # Use single quotes and escape internal single quotes
                    escaped_value = "'" + value.replace("'", "''") + "'"
                    fixed_yaml_lines.append(f'{key}: {escaped_value}')
                elif isinstance(value, bool):
                    fixed_yaml_lines.append(f'{key}: {str(value).lower()}')
                else:
                    fixed_yaml_lines.append(f'{key}: {value}')
            fixed_yaml_lines.append('---')

            # Validate the fixed YAML
            fixed_frontmatter = '\n'.join(fixed_yaml_lines[1:-1])
            yaml.safe_load(fixed_frontmatter)

            # Reconstruct the full content
            body = content[end_pos:]
            fixed_content = '\n'.join(fixed_yaml_lines) + '\n' + body

            return True, "Fixed YAML errors", fixed_content

        except Exception as fix_error:
            return False, f"Could not fix YAML: {fix_error}", None


def main():
    """Main function for CLI usage."""
    import argparse

    parser = argparse.ArgumentParser(description='Validate and fix Hugo front matter')
    parser.add_argument('files', nargs='*', help='Markdown files to check')
    parser.add_argument('--fix', action='store_true', help='Automatically fix issues')
    parser.add_argument('--check-all', action='store_true', help='Check all posts in content/posts/')

    args = parser.parse_args()

    if args.check_all:
        blog_dir = Path(__file__).parent / 'content' / 'posts'
        files_to_check = list(blog_dir.glob('*.md'))
    else:
        if not args.files:
            parser.error("Please provide files to check or use --check-all")
        files_to_check = args.files

    errors_found = False

    for file_path in files_to_check:
        file_path = Path(file_path)

        if not file_path.exists():
            print(f"❌ {file_path}: File not found")
            errors_found = True
            continue

        is_valid, message, fixed_content = validate_and_fix_frontmatter(file_path, fix=args.fix)

        if is_valid:
            if fixed_content:
                if args.fix:
                    file_path.write_text(fixed_content, encoding='utf-8')
                    print(f"✅ {file_path}: {message} (fixed)")
                else:
                    print(f"⚠️  {file_path}: {message} (use --fix to repair)")
                    errors_found = True
            else:
                print(f"✅ {file_path}: {message}")
        else:
            print(f"❌ {file_path}: {message}")
            errors_found = True

    sys.exit(1 if errors_found else 0)


if __name__ == '__main__':
    main()
