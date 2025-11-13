#!/usr/bin/env python3
"""
Nano Text Editor - Python Implementation (Cross-Platform)
Entry point for the application.
"""

import sys
from vuno import Editor, __version__


def main():
    """Main function to run the editor."""
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    
    try:
        editor = Editor(filename)
        editor.run()
    except KeyboardInterrupt:
        print("\nExited.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()