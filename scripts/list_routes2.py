import importlib.util
import os

app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', 'app.py'))
spec = importlib.util.spec_from_file_location('backend_app', app_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
app = getattr(mod, 'app')
for rule in app.url_map.iter_rules():
    print(f"{rule.endpoint}: {rule}")
