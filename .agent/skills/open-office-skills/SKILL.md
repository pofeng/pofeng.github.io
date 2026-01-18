---
name: open-office-skills
description: Process Open Office files including Writer (.odt), Calc (.ods), Impress (.odp), and Draw (.odg) documents. Use when working with LibreOffice or Apache OpenOffice files, creating, editing, converting, or analyzing Open Office documents. Supports cross-platform operations with Python and LibreOffice.
---

# Open Office Skills

This skill enables processing of Open Office suite files (LibreOffice/Apache OpenOffice) including text documents, spreadsheets, presentations, and drawings. It uses Python with the LibreOffice UNO API for cross-platform compatibility.

## Quick start

To edit a Writer document:
```
python scripts/edit_writer.py input.odt --output output.odt --text "Add this text"
```

## Instructions

1. **Identify file type**: Check the file extension (.odt for Writer, .ods for Calc, .odp for Impress, .odg for Draw)

2. **Use appropriate script**:
   - For text documents: `edit_writer.py`
   - For spreadsheets: `process_calc.py`
   - For presentations: `modify_impress.py`
   - For drawings: `handle_draw.py`

3. **Handle conversion**: Use `convert.py` to convert between formats or to PDF

4. **Validate output**: Always verify the generated files open correctly in LibreOffice

## Examples

### Edit a Writer document
```bash
python scripts/edit_writer.py document.odt --replace "old text:new text"
```

### Process a Calc spreadsheet
```bash
python scripts/process_calc.py spreadsheet.ods --sum-column A --output results.json
```

### Convert to PDF
```bash
python scripts/convert.py presentation.odp --format pdf --output presentation.pdf
```

## Best practices

- Always backup original files before processing
- Test conversions on small files first
- Use absolute paths for file operations
- Handle encoding properly for international text
- Close LibreOffice processes after operations

## Requirements

- Python 3.7+
- LibreOffice installed (cross-platform)
- Required packages: `pip install uno` (if using UNO bindings)
- Alternative: Use `pyoo` or `comtypes` for Windows, but prioritize UNO for portability

## Advanced usage

For complex operations, see [reference.md](reference.md).

## Implementation notes

This skill prioritizes portability by using the LibreOffice UNO API, which works on Windows, macOS, and Linux. For Windows-specific operations, it falls back to COM interfaces if needed, but the primary implementation is cross-platform.