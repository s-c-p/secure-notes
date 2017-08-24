import json
import hashlib
import contextlib

@contextlib.contextmanager
def documentDB(file_path, expected_null="{}"):
	if not os.path.isfile(file_path):
		with open(file_path, mode='wt') as _:
			_.write(expected_null)
	with open(file_path, mode='rt') as fp:
		con = json.load(fp)
	yield con
	with open(file_path, mode='wt') as fp:
		json.dump(con, fp)
	return

def calc_hash(file_path, algo="sha256"):
	hasher = getattr(hashlib, algo)()
	with open(file_path, mode='rb') as fp:
		for a_chunk in iter(lambda: fp.read(1024), b""):
			hasher.update(a_chunk)
	return hasher.hexdigest()

