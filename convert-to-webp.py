#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to convert JPG/PNG images to WebP
Requirements: pip install Pillow
"""

import os
import sys
import io
from pathlib import Path
from PIL import Image

# Fix encoding for Windows console
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def convert_to_webp(input_path, output_path, quality=85):
    """Convert images to WebP"""
    try:
        img = Image.open(input_path)
        # Convert to RGB if RGBA (to avoid errors with some images)
        if img.mode in ('RGBA', 'LA', 'P'):
            # Create white background for images with alpha
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        img.save(output_path, 'WEBP', quality=quality, method=6)
        return True
    except Exception as e:
        print(f"✗ Error converting {input_path}: {e}")
        return False

def main():
    print("Converting images to WebP...")
    print("=" * 50)
    
    image_path = Path("images")
    quality = 85
    
    if not image_path.exists():
        print(f"❌ Directory not found: {image_path}")
        sys.exit(1)
    
    # Get all image files
    image_extensions = ['.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG']
    images = []
    for ext in image_extensions:
        images.extend(image_path.rglob(f'*{ext}'))
    
    if not images:
        print("❌ No image files found!")
        sys.exit(1)
    
    print(f"Found {len(images)} image files\n")
    
    converted = 0
    skipped = 0
    errors = 0
    
    for img_path in images:
        webp_path = img_path.with_suffix('.webp')
        
        # Skip if WebP file already exists
        if webp_path.exists():
            print(f"⏭  Already exists: {img_path.name} -> {webp_path.name}")
            skipped += 1
            continue
        
        print(f"🔄 Converting: {img_path.name}...", end=' ')
        
        if convert_to_webp(img_path, webp_path, quality):
            # Calculate file sizes
            original_size = img_path.stat().st_size / (1024 * 1024)  # MB
            webp_size = webp_path.stat().st_size / (1024 * 1024)  # MB
            reduction = (1 - webp_size / original_size) * 100
            
            print(f"✓ ({original_size:.2f}MB -> {webp_size:.2f}MB, reduced {reduction:.1f}%)")
            converted += 1
        else:
            errors += 1
    
    print("\n" + "=" * 50)
    print(f"✅ Completed!")
    print(f"   - Converted: {converted} files")
    print(f"   - Skipped: {skipped} files")
    if errors > 0:
        print(f"   - Errors: {errors} files")

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("❌ The Pillow library is missing!")
        print("Install using the command: pip install Pillow")
        sys.exit(1)
