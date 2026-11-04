"""Procedural recipe for phw_sorter; execute through Blender MCP."""
from pathlib import Path
import importlib.util
helper=Path(__file__).with_name('common.py')
spec=importlib.util.spec_from_file_location('phw_common',helper)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
module.build('phw_sorter')
