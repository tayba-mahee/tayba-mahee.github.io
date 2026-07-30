#!/usr/bin/env python3
"""
Cat Photos Organizer with HEIC Conversion
Renames, converts HEIC to JPG, and updates markdown references
"""

import os
import shutil
from pathlib import Path
import re

try:
    from PIL import Image
    from pillow_heif import register_heif_opener
    register_heif_opener()
    HEIC_SUPPORT = True
except ImportError:
    HEIC_SUPPORT = False
    print("⚠ Warning: pillow-heif not installed. HEIC files will be skipped.")
    print("Install with: pip3 install pillow pillow-heif")

# Configuration
CATS_DIR = "/Users/maheetayba/Developer/copilot-resume-site/assets/Cats"
MD_FILES = [
    "/Users/maheetayba/Developer/copilot-resume-site/cats.md",
    "/Users/maheetayba/Developer/copilot-resume-site/_tabs/hobbies.md"
]

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.heic', '.JPG', '.JPEG', '.PNG', '.GIF', '.HEIC'}

def create_backup():
    """Create backup of Cats directory"""
    print("Creating backup...")
    backup_dir = CATS_DIR + "_backup"
    if os.path.exists(backup_dir):
        shutil.rmtree(backup_dir)
    shutil.copytree(CATS_DIR, backup_dir)
    print(f"✓ Backed up to {backup_dir}\n")

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

def convert_image_to_jpg(input_path, output_path):
    """Convert any image format to JPG"""
    try:
        img = Image.open(input_path)
        # Convert RGBA to RGB if needed
        if img.mode in ('RGBA', 'LA', 'P'):
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
            img = rgb_img
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        img.save(output_path, 'JPEG', quality=90)
        return True
    except Exception as e:
        print(f"  ✗ Conversion error: {e}")
        return False

def process_images():
    """Process all images in Cats directory"""
    path_mapping = {}
    stats = {'renamed': 0, 'converted': 0, 'skipped': 0, 'errors': 0}
    
    print("Processing images...")
    print("-" * 60)
    
    for root, dirs, files in os.walk(CATS_DIR):
        if '_backup' in root:
            continue
        
        folder_name = os.path.basename(root)
        image_files = [f for f in files if any(f.endswith(ext) for ext in IMAGE_EXTENSIONS)]
        
        if not image_files:
            continue
        
        image_files.sort()
        print(f"\n📁 {folder_name} ({len(image_files)} images)")
        
        for idx, filename in enumerate(image_files, 1):
            old_path = os.path.join(root, filename)
            old_ext = os.path.splitext(filename)[1].lower()
            
            # Generate new filename
            new_filename = f"{slugify(folder_name)}-{idx:02d}.jpg"
            new_path = os.path.join(root, new_filename)
            
            # Check if conversion needed
            needs_conversion = old_ext in ['.heic', '.png'] or old_ext.upper() in ['.HEIC', '.PNG']
            
            try:
                if needs_conversion:
                    # Convert to JPG
                    if old_ext.lower() == '.heic' and not HEIC_SUPPORT:
                        print(f"  ⚠ Skipping HEIC (no support): {filename}")
                        stats['skipped'] += 1
                        continue
                    
                    if convert_image_to_jpg(old_path, new_path):
                        os.remove(old_path)  # Remove original
                        print(f"  🔄 Converted: {filename} -> {new_filename}")
                        stats['converted'] += 1
                    else:
                        stats['errors'] += 1
                        continue
                else:
                    # Just rename
                    if old_path != new_path:
                        # Handle duplicates
                        if os.path.exists(new_path):
                            base, ext = os.path.splitext(new_filename)
                            counter = 1
                            while os.path.exists(new_path):
                                new_filename = f"{base}-dup{counter}{ext}"
                                new_path = os.path.join(root, new_filename)
                                counter += 1
                        
                        os.rename(old_path, new_path)
                        print(f"  ✓ Renamed: {filename} -> {new_filename}")
                        stats['renamed'] += 1
                    else:
                        print(f"  ✓ Already correct: {filename}")
                
                # Store mapping for markdown updates
                old_rel = old_path.replace("/Users/maheetayba/Developer/copilot-resume-site/assets/", "/assets/")
                new_rel = new_path.replace("/Users/maheetayba/Developer/copilot-resume-site/assets/", "/assets/")
                path_mapping[old_rel] = new_rel
                
            except Exception as e:
                print(f"  ✗ Error processing {filename}: {e}")
                stats['errors'] += 1
    
    print()
    print("-" * 60)
    print(f"📊 Summary:")
    print(f"  Renamed: {stats['renamed']}")
    print(f"  Converted: {stats['converted']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Errors: {stats['errors']}")
    print()
    
    return path_mapping

def update_markdown_files(path_mapping):
    """Update image paths in markdown files"""
    if not path_mapping:
        print("No path changes to update")
        return
    
    print("Updating markdown files...")
    print("-" * 60)
    
    for md_file in MD_FILES:
        if not os.path.exists(md_file):
            continue
        
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        updates = 0
        
        for old_path, new_path in path_mapping.items():
            if old_path in content:
                content = content.replace(old_path, new_path)
                updates += 1
        
        if content != original:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated {os.path.basename(md_file)} ({updates} paths)")
        else:
            print(f"  No changes in {os.path.basename(md_file)}")
    
    print()

def main():
    """Main execution"""
    print("=" * 60)
    print("🐱 CAT PHOTOS ORGANIZER (with HEIC Conversion)")
    print("=" * 60)
    print()
    
    if not HEIC_SUPPORT:
        print("⚠ HEIC conversion NOT available")
        print()
    else:
        print("✓ HEIC conversion available")
        print()
    
    print(f"This will:")
    print(f"  1. Rename all images to: folder-name-01.jpg, folder-name-02.jpg, ...")
    print(f"  2. Convert HEIC/PNG files to JPG")
    print(f"  3. Update references in markdown files")
    print(f"  4. Create backup before changes")
    print()
    print(f"Directory: {CATS_DIR}")
    print()
    
    response = input("Continue? (yes/no): ").strip().lower()
    if response not in ['yes', 'y']:
        print("Cancelled.")
        return
    
    print()
    create_backup()
    path_mapping = process_images()
    update_markdown_files(path_mapping)
    
    print("=" * 60)
    print("✅ DONE!")
    print("=" * 60)
    print()
    print("To restore from backup if needed:")
    print(f"  rm -rf '{CATS_DIR}'")
    print(f"  mv '{CATS_DIR}_backup' '{CATS_DIR}'")
    print()

if __name__ == "__main__":
    main()
