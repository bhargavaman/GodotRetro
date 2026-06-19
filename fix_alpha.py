import os
import re

directory = 'addons/godot_retro/shaders/compute'
files_to_fix = [
    'blur.glsl',
    'color_correction.glsl',
    'crt_basic.glsl',
    'crt_complex.glsl',
    'dithering.glsl',
    'grain_complex.glsl',
    'monochrome.glsl',
    'posterization_complex.glsl',
    'posterization_simple.glsl',
    'vhs.glsl'
]

for filename in files_to_fix:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r') as f:
        content = f.read()

    # Find the imageStore line with 1.0
    pattern = r'imageStore\(color_image,\s*pixel,\s*vec4\(([^,]+),\s*1\.0\)\);'
    
    if re.search(pattern, content):
        replacement = r'float alpha = texelFetch(color_texture, pixel, 0).a;\n\timageStore(color_image, pixel, vec4(\1, alpha));'
        new_content = re.sub(pattern, replacement, content)
        
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed {filename}")
    else:
        print(f"Pattern not found in {filename}")
