# Open Office Skills Reference

## Supported File Formats

- **Writer (.odt)**: Text documents
- **Calc (.ods)**: Spreadsheets
- **Impress (.odp)**: Presentations
- **Draw (.odg)**: Vector graphics

## Portability Considerations

### Cross-Platform Implementation
- Uses LibreOffice UNO API (Universal Network Objects)
- Works on Windows, macOS, Linux
- Requires LibreOffice installation
- Python 3.7+ recommended

### Installation Requirements
```bash
# Install LibreOffice
# Windows: Download from libreoffice.org
# macOS: brew install --cask libreoffice
# Linux: sudo apt install libreoffice

# Python UNO bindings are included with LibreOffice
# Add to PATH or use full path to python in LibreOffice
```

### Alternative Approaches
- **Windows**: COM interfaces via `comtypes`
- **macOS/Linux**: UNO preferred
- **Fallback**: Command-line conversions using `soffice --convert-to`

## API Usage Examples

### Starting LibreOffice in listening mode
```bash
# Start LibreOffice in background
soffice --accept="socket,host=localhost,port=2002;urp;StarOffice.ServiceManager" &
```

### Converting files
```bash
soffice --convert-to pdf input.odt
soffice --convert-to xlsx input.ods
```

## Error Handling

- Check if LibreOffice is running
- Handle file not found errors
- Validate output file creation
- Close documents properly to free resources

## Performance Tips

- Process files sequentially rather than parallel
- Use temporary directories for intermediate files
- Batch operations when possible
- Monitor memory usage for large documents