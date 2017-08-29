import pytest

import utils
import queue

def crypto(file_name, direction):
    queue.push({
        "file_acted_upon": file_name,
        "action": direction,
        "old_hash": old_hash,
        "new_hash": utils.calc_hash(file_name)
    }, "crypto")
    return