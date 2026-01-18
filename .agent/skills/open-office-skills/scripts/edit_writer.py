#!/usr/bin/env python3
"""
Simple example script to edit Open Office Writer documents.
Requires LibreOffice with UNO Python bindings.
For portability: Works on Linux/macOS/Windows with LibreOffice installed.
"""

import sys
import uno
from com.sun.star.beans import PropertyValue
from com.sun.star.uno import Exception as UnoException

def edit_writer_document(input_file, output_file, replace_text=None):
    """Edit a Writer document by replacing text."""
    try:
        # Connect to LibreOffice (assumes soffice is running)
        local_context = uno.getComponentContext()
        resolver = local_context.ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", local_context)
        ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
        smgr = ctx.ServiceManager

        # Load document
        desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        url = uno.systemPathToFileUrl(input_file)
        doc = desktop.loadComponentFromURL(url, "_blank", 0, ())

        if not doc:
            raise Exception("Could not load document")

        # Get text
        text = doc.Text

        if replace_text:
            # Simple text replacement (for demo)
            old_text, new_text = replace_text.split(':', 1)
            text.String = text.String.replace(old_text, new_text)

        # Save document
        output_url = uno.systemPathToFileUrl(output_file)
        doc.storeToURL(output_url, ())

        # Close document
        doc.close(True)

        return f"Successfully edited {input_file} and saved to {output_file}"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python edit_writer.py input.odt output.odt --replace 'old:new'")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    replace_text = None

    if len(sys.argv) > 4 and sys.argv[3] == "--replace":
        replace_text = sys.argv[4]

    result = edit_writer_document(input_file, output_file, replace_text)
    print(result)