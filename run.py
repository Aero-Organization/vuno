#!/usr/bin/env python3
"""
Vuno Text Editor v0.0.2b - Simple launcher script
Run with: python run.py [filename]
"""

import sys

def main():
    """Main entry point."""
    from vuno import Editor, __version__, __description__
    
    # Show version if requested
    if len(sys.argv) > 1 and sys.argv[1] in ['--version', '-v']:
        print(f"Vuno Text Editor v{__version__}")
        print(__description__)
        sys.exit(0)
    
    if len(sys.argv) > 1 and sys.argv[1] in ['--help', '-h']:
        print(f"Vuno Text Editor v{__version__}")
        print(__description__)
        print("\nUsage: python run.py [filename]")
        print("\nKeyboard Shortcuts:")
        print("\n  File Operations:")
        print("    Ctrl+X  - Exit editor")
        print("    Ctrl+O  - Save file")
        print("    Ctrl+S  - Save as (new filename)")
        print("\n  Edit Operations:")
        print("    Ctrl+Z  - Undo")
        print("    Ctrl+Y  - Redo")
        print("    Ctrl+K  - Cut Line")
        print("    Ctrl+C  - Copy line")
        print("    Ctrl+U  - Paste from clipboard")
        print("\n  Search & Navigation:")
        print("    Ctrl+W  - Search for text")
        print("    Ctrl+N  - Find next occurrence")
        print("    Ctrl+T  - Go to line numbers")
        print("\n  View:")
        print("    Ctrl+L  - Toggle line numbers")
        print("    Ctrl+I  - Show file statistics")
        print("    Ctrl+G  - Show help")
        print("\nExamples:")
        print("  python run.py              # Start with empty file")
        print("  python run.py myfile.txt   # Open existing file")
        print("  python run.py --version    # Show version")
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