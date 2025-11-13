#!/usr/bin/env python3
"""
Vuno Text Editor v0.0.2a - Simple launcher script
Run with: python run.py [filename]
"""

import sys

def main():
    """Main entry point."""
    from vuno import Editor, __version__
    
    # Show version if requested
    if len(sys.argv) > 1 and sys.argv[1] in ['--version', '-v']:
        print(f"Vuno Text Editor v{__version__}")
        sys.exit(0)
    
    if len(sys.argv) > 1 and sys.argv[1] in ['--help', '-h']:
        print(f"Vuno Text Editor v{__version__}")
        print("\nUsage: python run.py [filename]")
        print("\nKeyboard Shortcuts:")
        print("  Ctrl+X  - Exit")
        print("  Ctrl+O  - Save")
        print("  Ctrl+W  - Search")
        print("  Ctrl+N  - Find Next")
        print("  Ctrl+Z  - Undo")
        print("  Ctrl+Y  - Redo")
        print("  Ctrl+K  - Cut Line")
        print("  Ctrl+U  - Paste")
        print("  Ctrl+T  - Go to Line")
        print("  Ctrl+L  - Toggle Line Numbers")
        print("  Ctrl+S  - Show Statistics")
        print("  Ctrl+G  - Help")
        sys.exit(0)
    
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    
    try:
        editor = Editor(filename)
        editor.run()
    except KeyboardInterrupt:
        print("\nExited.")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()