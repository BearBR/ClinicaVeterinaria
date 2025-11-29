import importlib, sys
sys.path.append(r".")
app_mod = importlib.import_module("backend.app")
client = app_mod.app.test_client()
resp = client.post("/api/login", json={"username":"admin","password":"admin123"})
print("STATUS::", resp.status_code)
print("BODY::", resp.get_data(as_text=True))
