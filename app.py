import queue

def crypto(file_name, direction):
    queue.push("crypto", {
        "file_acted_upon": file_name
    })
    return